from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.implicitly_wait(5)

driver.get("http://books.toscrape.com")
wait = WebDriverWait(driver, 10)

all_info = []
page_count = 1
while True:
    try:
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod")))
        books = driver.find_elements(By.CLASS_NAME, "product_pod")

        for index, book in enumerate(books, 1):
            try:
                title = book.find_element(By.XPATH, ".//h3/a").get_attribute("title")


                price_text = book.find_element(By.CLASS_NAME, "price_color").text
                price = float (price_text.replace('£',''))


                rating_element = book.find_element(By.XPATH, ".//p[contains(@class, 'star-rating')]")
                ratting_class = rating_element.get_attribute("class")
                rating_text = ratting_class.split()[-1]
                rating_map = {'One':'1','Two' : '2', 'Three':'3','Four' : '4', 'Five' : '5'}

                rating = rating_map.get(rating_text, 0)



                availability = book.find_element(By.XPATH, ".//p[contains(@class, 'instock')]").text.strip()
            
            
                books_data = {
                    "Book title" : title,
                    "Book price" : price,
                    "Book rating" : rating,
                    "Book in stock" : availability
                }

                all_info.append(books_data)

            except Exception as e:

                continue
                

        try:
            next_page = driver.find_element(By.XPATH, "//a[text()='next']")

            next_page.click()
            print(f"Moving to next page {page_count + 1}....")


            time.sleep(1)

            page_count += 1
        
        except:
            print(f"No more page to scrap. check last page number :{page_count} ")
            break

    except Exception as e:
        print(f"\n Reached last page! Total page: {page_count}")
        break

driver.quit()

        # print(title, " ", price, " " , rating, " " , availability)
        


df = pd.DataFrame(all_info)
df.to_csv("Book_scrap_data.csv", index=False )


