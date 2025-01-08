from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



class amazonProduct():
    def __init__(self, url, name, price) -> None:
        self.url = url
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f"name:{self.name}\nprice: {self.price}\nURL: {self.url}\n------------ "


def searchForItem(item: str) -> None:
    searchBox = driver.find_element(By.ID, "twotabsearchtextbox")
    searchButton = driver.find_element(By.ID, "nav-search-submit-button")
    searchBox.send_keys(item)
    searchButton.click()
    driver.implicitly_wait(5)

def findItemsOnePage(item:str) -> None:
    searchForItem(item)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item")]'))
    )

    products = driver.find_elements(By.XPATH, '//div[contains(@class, "s-result-item")]')
    for prod in products:
        try:
            element = prod.find_elements(By.XPATH, './/a[contains(@class, "a-link-normal")]')
            
            if element and len(element) > 0:
                url = element[0].get_attribute("href")
                name = prod.find_elements(By.XPATH, './/a[contains(@class, "a-link-normal")]/h2/span')[0].text
             
                price = str(prod.find_elements(By.CSS_SELECTOR, ".a-price-whole")[0].text) + "." + str(prod.find_elements(By.CSS_SELECTOR, ".a-price-fraction")[0].text)
                
                product: amazonProduct = amazonProduct(url, name, price)
                print(product)
            else:
                print("No link found for this product.")
        except Exception as e:
            print(f"Error finding URL: {e}")
       

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com")
product = input("Please give me the product you want more information about on Amazon: ")
findItemsOnePage(product)

driver.quit()




    
