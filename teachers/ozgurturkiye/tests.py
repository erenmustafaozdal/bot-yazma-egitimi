import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import settings

# driver = webdriver.Chrome(settings.chrome_driver_path)
# driver.maximize_window()


class IstanbulAkademiIletisimForm(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(settings.chrome_driver_path)
        driver = self.driver
        driver.get("https://istanbulakademi.meb.gov.tr/iletisim.php")

    def test_get_sender_name_by_id(self):
        elem = self.driver.find_element_by_id("sender_name")
        self.assertEqual(elem.get_attribute("id"), "sender_name")

    def test_get_sender_name_by_name(self):
        elem = self.driver.find_element_by_name("sender_name")
        self.assertEqual(elem.get_attribute("name"), "sender_name")

    def test_get_sender_name_by_css_selector(self):
        elem = self.driver.find_element_by_css_selector("#sender_name")
        self.assertEqual(elem.get_attribute("id"), "sender_name")

    def test_set_sender_name_by_name(self):
        modal_button = self.driver.find_element_by_class_name("btn-warning")
        modal_button.click()
        elem = self.driver.find_element_by_name("sender_name")
        elem.send_keys("ozgur")
        self.assertEqual(elem.get_attribute("value"), "ozgur")

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

