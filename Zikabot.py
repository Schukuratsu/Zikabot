from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import BotEngine

chromedriver_path = 'assets/chromedriver.exe' 
service = Service(chromedriver_path)
service.start()
webdriver = webdriver.Remote(service.service_url)

BotEngine.init(webdriver)
BotEngine.update(webdriver)

webdriver.close()