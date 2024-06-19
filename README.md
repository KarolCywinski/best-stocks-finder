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
### Using Python virtual environment :snake: :desert_island:
1. Install Python and verify your internet connectivity, as the application uses Content Delivery Network (CDN) on the frontend :earth_asia:
2. Navigate to the *backend* directory where all the python files are kept: `cd ./backend`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment from the console or if you are using VS Code, select the proper Python interpreter from the created *venv* directory :rocket:
5. Install all the required python packages before the first run: `pip install -r requirements.txt`
6. Run the backend server: `uvicorn api:app --reload`
7. Open: http://127.0.0.1:8000/best-stocks-finder
### Using Docker :whale2: :ocean:
1. Install Docker and verify your internet connectivity, as the application uses Content Delivery Network (CDN) on the frontend :earth_americas:
2. Build the image and run the container defined in the *docker-compose.yml* file: `docker-compose up`
3. Open: http://127.0.0.1:8000/best-stocks-finder
