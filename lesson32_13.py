import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fill_form(self, link):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("tt")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("pp")
        browser.find_element(By.CSS_SELECTOR, ".third_class .third").send_keys(
            "11@11.com"
        )

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)

        self.assertEqual(
            "Congratulations! You have successfully registered!", registration_result
        )

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fill_form(link)

        self.assertEqual(
            "Congratulations! You have successfully registered!", registration_result
        )


if __name__ == "__main__":
    unittest.main()
