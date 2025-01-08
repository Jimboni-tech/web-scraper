from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

class item():
    def __init__(self, url, image, name, price) -> None:
        self.url = url
        self.image = image
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f"URL: {self.url}\nimage:{self.image}\nname:{self.name}\nprice:{self.price}\n------------ "


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options = options)
driver.get("https://www.scrapingcourse.com/ecommerce/")
products = driver.find_elements(By.CSS_SELECTOR, ".product")
for prod in products:
    name = prod.find_element(By.CSS_SELECTOR, ".product-name").text
    price = prod.find_element(By.CSS_SELECTOR, ".price").text
    img = prod.find_element(By.CSS_SELECTOR, ".product-image").get_attribute("src")
    url = prod.find_element(By.CSS_SELECTOR, ".woocommerce-LoopProduct-link").get_attribute("href")
    product: item = item(url, img, name, price)
    print(product)

driver.quit()



    
