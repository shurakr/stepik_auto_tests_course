from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
input3.send_keys("11@11.com")
input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .first")
input4.send_keys("Russia")
input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .second")
input5.send_keys("Moscow")

button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
