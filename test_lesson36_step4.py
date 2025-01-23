from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import pytest
import time
import math
import json


def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open("config.json", "r") as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    options = Options()
    options.page_load_strategy = "eager"
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()


@pytest.mark.parametrize(
    "number",
    ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"],
)
def test_hardmode(browser, number):
    cfg = load_config()
    login = cfg["login_stepik"]
    password = cfg["password_stepik"]
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    # Ждем пока не появится кнопка реги и нажимаем кнопку реги
    button1 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    button1.click()
    # Вводим логин и пароль
    input1 = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    input1.send_keys(login)
    input2 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    input2.send_keys(password)
    # Отправляем заполненную форму
    button2 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
    )
    button2.click()

    try:
        # Если кнопка "Решить снова" присутствует
        button3 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        )
        button3.click()
        print('Кнопка "Решить снова" обнаружена, поле textarea неактивное')
        # Если кнопки "Решить снова" не оказалось
    except TimeoutException:
        print('Кнопка "Решить снова" не обнаружена, поле textarea активное')

    finally:
        # Ждем пока поле textarea не очистится и станет активным(пропадет атрибут "disabled"),
        # при этом не используем time.sleep!
        WebDriverWait(browser, 10).until_not(
            EC.element_attribute_to_include(
                (By.CSS_SELECTOR, "textarea.ember-text-area"), "disabled"
            )
        )
        answer = math.log(int(time.time()))
        input3 = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "textarea.ember-text-area")
            )
        )
        input3.send_keys(answer)
        # Нажимаем кнопку "Отправить"
        button4 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button4.click()
        # Ждем пока не появится фидбек, что ответ верный
        feedback = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )
        # Сравниваем, что фидбек полностью совпадает с "Correct!"
        assert feedback.text == "Correct!", f"{feedback.text}"


if __name__ == "__main__":
    pytest.main()
