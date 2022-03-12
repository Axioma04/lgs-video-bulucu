
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import time

def find_suitable_videos(options: dict) -> bool:
    driverPath = os.path.dirname(os.path.realpath(__file__)) + '\chromedriver.exe'
    browser = webdriver.Chrome(driverPath)
    keyword, maxVideoCount, maxVideoLength, createPlaylist, startFrom = options.values()
    konular, sorular = int(int(maxVideoCount) / 2), int(int(maxVideoCount) / 2)
    startFrom = int(startFrom)
    search_query = keyword.replace(' ', '+')
    konu_videoları = get_videos(search_query, browser, '+konu+anlatımı', konular, bool(createPlaylist),int(startFrom))
    soru_videoları = get_videos(search_query, browser, '+soru+çözümü', sorular, bool(createPlaylist),int(startFrom))
    if os.path.isdir(os.path.dirname(os.path.realpath(__file__)) + '/outputs') == False: os.mkdir(os.path.dirname(os.path.realpath(__file__)) + '/outputs')
    with open(os.path.dirname(os.path.realpath(__file__)) + '/outputs/' + keyword + '.txt', 'w') as stdout:
        stdout.write(f'Bu kısım violence tarafından kodlandı. All right reserved \nIsim: {keyword}\n\nKonu Anlatimlari:\n\n')
        stdout.write("\n".join(konu_videoları))
        stdout.write('\n\nSoru Cozum Videolari:\n\n')
        stdout.write("\n".join(soru_videoları))
    pass

def get_videos(search_query: str, browser, secondQuery: str, sayi, playList=False, startFrom=0):
    base_url = 'https://www.youtube.com/results?search_query=' + search_query + secondQuery
    browser.get(base_url)
    time.sleep(2)
    videos = browser.find_elements_by_css_selector('ytd-video-renderer')[startFrom:sayi+startFrom]
    video_urls = []
    for video in videos:
        atag = video.find_element_by_css_selector('div ytd-thumbnail a')
        video_urls.append(atag.get_attribute('href'))
    return video_urls
    
