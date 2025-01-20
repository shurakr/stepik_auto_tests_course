from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element(By.ID, "num1").text)
num2 = int(browser.find_element(By.ID, "num2").text)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(num1 + num2))  # ищем элемент с текстом "Python"


button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
