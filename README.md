<h1 align="center"> Web Scraping API with Selenium</h1>

![Python](https://img.shields.io/badge/python-v3.10-green) ![Flask](https://img.shields.io/badge/flask-v2.2-blue) ![BeautifulSoup](https://img.shields.io/badge/beautifulsoup-v4.11-blue) ![Selenium](https://img.shields.io/badge/selenium-v4.6-blue) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white) 

This project is a web scraping API to extract information about videos on youtube for a specific channel.

This API have only one endpoint (home /), where you can vary the paramaters to change the behaviour of this API. The paramaters are those:
- name_channel: This paramater is the name of the channel to be scraped (without the @ being used recently)
- jumps: Decides the number of jumps given in the page (this jumps are used to load more videos). Default is 0
- wait_time: Time between each jump in seconds, depends on your internet to load the page, so the slower the internet, the bigger need to be this wait_time. Default is 3 seconds
- popular: Order by popularity if true, orders by popularity. Default is false (valid values, <b>true</b> and <b>false</b>)