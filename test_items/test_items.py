import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_should_see_add_to_basket_button(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(15)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )

    basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket, "Кнопка добавления в корзину не найдена"


if __name__ == "__main__":
    pytest.main(["test_items.py"])
