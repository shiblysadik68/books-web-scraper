from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


driver = webdriver.Chrome()
driver.get("http://books.toscrape.com")
time.sleep(3)

all_info = []
page_count = 1
while True:
    books = driver.find_elements(By.XPATH, "//article[@class ='product_pod']")

    for book in books:
        title = book.find_element(By.XPATH, ".//h3/a").get_attribute("title")
        price = book.find_element(By.XPATH, ".//p[@class='price_color']").text
        rating = book.find_element(By.XPATH, ".//p[contains(@class, 'star-rating')]").get_attribute("class")
        availability = book.find_element(By.XPATH, ".//p[contains(@class, 'instock')]").text
        
        
        books_data = {
            "Book title" : title,
            "Book price" : price,
            "Book rating" : rating,
            "Book in stock" : availability
        }

        all_info.append(books_data)
        time.sleep(5)

    try:
        next_page = driver.find_element(By.XPATH, "//a[text()='next']")
        print("Found the next text, Now clicking button")
        next_page.click()
        time.sleep(3)
        page_count +=1
    
    except:
        print(f"No more page to scrap. check last page number :{page_count} ")
        break

driver.quit()

        # print(title, " ", price, " " , rating, " " , availability)
        


df = pd.DataFrame(all_info)
df.to_csv("Book_scrap_data.csv", index=False )


