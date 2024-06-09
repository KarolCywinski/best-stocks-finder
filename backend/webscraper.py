import requests
from bs4 import BeautifulSoup 

def fetch_possible_time_frames() -> tuple:
    return ('5 min', '15 min', '1 hour', '1 day')

def fetch_best_stocks(short_sell: bool, time_frame: str) -> list:
    # check if time frame is valid
    time_frames = fetch_possible_time_frames()
    if(time_frame not in time_frames):
        return []
    
    # make a GET request
    response = requests.get('https://www.investing.com/technical/stocks-technical-summary');

    # check if response is successful
    if(response.status_code == 200):
        html = BeautifulSoup(response.content, 'html.parser')
        technical_table = html.find('div', id='technical_summary_container').find('tbody')

        # list of all stocks information
        stocks_list = []
        stock_info = {}

        # find all <tr> tags with attribute "data-row-type" equal to "movingAverages" or "summary"
        for row in technical_table.findAll('tr', {'data-row-type' : ['movingAverages', 'summary']}):
            # if all single stock info collected - go to the next stock
            if time_frames[-1] in stock_info.keys():
                stock_info = {}

            if(row['data-row-type'] == 'movingAverages'):
                stock_info['name'] = row.find('a').text
                # remove thousands separator
                stock_info['price'] = float(row.find('p').text.replace(',', ''))
            else:
                for idx, cell in enumerate(row.findAll('td')):
                    if(idx > 0):
                        stock_info[time_frames[idx - 1]] = cell.text

            # if all single stock info collected - add it to the list
            if(time_frames[-1] in stock_info.keys()):
                if((short_sell and 'Strong Sell' == stock_info[time_frame]) or (not short_sell and 'Strong Buy' == stock_info[time_frame])):
                    stocks_list.append(stock_info)

    return sorted(stocks_list, key=lambda x: x['price'])

        
    