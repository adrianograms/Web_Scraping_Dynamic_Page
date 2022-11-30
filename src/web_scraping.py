from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re

def load_page_information(url, jumps, wait_time):
    """Load the dynamic page and return the html generated

    Args:
        url (string): Url of the site being scraped, in this case, a youtube channel
        jumps (int): Number of jumps given in the page to load more videos
        wait_time (int): Waited time between each jump

    Returns:
        object: Returns the html of the page
    """
    options = webdriver.FirefoxOptions()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    sleep(5) # Time to render all the dynamic componenets

    for _ in range(jumps):
        driver.execute_script("window.scrollTo(0, window.scrollY + 10000);")
        sleep(wait_time)

    html = driver.page_source
    driver.close()
    return html

def scrape_page(html):
    """Function to scrape information from the html of a youtube channel

    Args:
        html (object): html of the page being scraped

    Returns:
        array: Returns all the video informations scraped
    """
    cards_info = []

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('ytd-rich-grid-media', {'class': 'style-scope ytd-rich-item-renderer'}) 

    for card in cards:
        card_info = {}
        
        lenght_video = card.find('span', {'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).text
        card_info['lenght_video'] = re.findall('[0-9|:]+' ,lenght_video)[0]
        card_info['title_video'] = card.find('yt-formatted-string', {'id': 'video-title'}).text

        view_info = card.find('a', {'id': 'video-title-link'})['aria-label']
        card_info['views_video'] = int(re.findall('[0-9|,]+(?= views$)',view_info)[0].replace(',', ''))

        metadata_video = card.find_all('span', {'class': 'inline-metadata-item style-scope ytd-video-meta-block'})
        card_info['published_date_video'] = metadata_video[1].text

        cards_info.append(card_info)
        
    return cards_info

def get_video_infomations(url, jumps, wait_time):
    """Get informations about some videos of a specific channel on youtube

    Args:
        url (string): Url of the site, in short, is the url of the youtube channel
        jumps (int): Number of jumps given in the scraping (jump on the page to load more videos)
        wait_time (int): Wait time between each jump

    Returns:
        array: Returns a array with all the informations of the videos scraped
    """
    html = load_page_information(url, jumps, wait_time)
    return scrape_page(html)