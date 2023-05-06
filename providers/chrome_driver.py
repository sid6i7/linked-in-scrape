from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc
# from config import *
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = uc.Chrome()
    return driver




