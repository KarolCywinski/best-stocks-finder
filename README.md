# Best Stocks Finder :bar_chart:
## What is it 🧐
This is a website application designed for finding "the best" deals :moneybag: in the stock market.

Users can select their preferred trading strategy (either buying :chart_with_upwards_trend: or selling :chart_with_downwards_trend:) and specify a time frame. 
The application then presents a table populated with various stocks and their current prices. 
The stocks displayed come from the technical summary section of the https://www.investing.com website and their information are extracted using web scraping :razor: techniques.

This application is made for fun :clown_face: so **don't look for a financial advice here!**
## Tech stack :hammer_and_wrench:
- Backend :gear:
  - Python :snake:
    - FastAPI 
    - BeautifulSoup
- Frontend :crayon:
  - Vue.js (CDN)
  - Bootstrap (CDN)
  - Axios (CDN)
## How to run it :man_technologist:
1. Verify your internet connectivity, as the application uses Content Delivery Network (CDN) on the frontend and web scraping techniques on the backend :globe_with_meridians:
2. Navigate to the *backend* directory where all the python files are kept and where your *venv* folder should be, assuming you're working with virtual environments: `cd ./backend`
3. Install all the required python packages before the first run: `pip install -r requirements.txt`
4. Run the backend server: `uvicorn api:app --reload`
5. Open: http://127.0.0.1:8000/best-stocks-finder
