from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scraper(url):
  # Setup Chrome options
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--headless")  # Ensure GUI is off
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")

  # Choose Chrome Browser
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

  # Visit URL
  driver.get(url)  # replace with your URL

  # Get page source after JS has executed
  html = driver.page_source

  # Then you can continue with BeautifulSoup
  soup = BeautifulSoup(html, 'html.parser')
  return soup
