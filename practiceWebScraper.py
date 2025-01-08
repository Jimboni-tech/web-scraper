
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

class item():
    def __init__(self, url, image, name, price, brand) -> None:
        self.url = url
        self.image = image
        self.name = name
        self.price = price
        self.brand = brand
    def __str__(self) -> str:
        return f"URL: {self.url}\nimage:{self.image}\nname:{self.name}\nprice:{self.price}\nbrand:{self.brand}\n------------ "



def scraper(driver, prod) -> None:

    driver.get(f"https://www.etsy.com/search?q={prod}")

    products = driver.find_elements(By.CSS_SELECTOR, "wt-list-unstyled")
    for prod in products:
        name = prod.find_element(By.CSS_SELECTOR, ".wt-grid__item-xs-12").text
        price = prod.find_element(By.CSS_SELECTOR, ".lc-price").text
        img = prod.find_element(By.CSS_SELECTOR, ".wt-image").get_attribute("src")
        url = prod.find_element(By.CSS_SELECTOR, ".listing-link").get_attribute("href")
        brand = prod.fin_element(By.CSS_SELECTOR, ".jujjegt76").text
        product: item = item(url, img, name, price, brand)
        print(product)



options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options = options)
product = input("Please enter the product that you would like to scrape for: ")
scraper(driver, product)
driver.quit()



    
