from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

new_window = browser.window_handles[-1]
browser.switch_to.window(new_window)
first_window = browser.window_handles[0]

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
i1 = browser.find_element(By.ID, "answer")
i1.send_keys(y)


button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

# успеваем скопировать код за 30 секунд
# time.sleep(30)

alert_text = browser.switch_to.alert.text
print(alert_text.split(": ")[-1])
browser.switch_to.alert.accept()

# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
