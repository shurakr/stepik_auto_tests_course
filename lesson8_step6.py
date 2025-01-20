from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value").text
y = calc(x_element)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

i1 = browser.find_element(By.ID, "answer")
i1.send_keys(y)
i2 = browser.find_element(By.ID, "robotCheckbox")
i2.click()
i3 = browser.find_element(By.ID, "robotsRule")
i3.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
