# реализации ожиданий элементов
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):  # инициализируем драйвер
        self.driver = driver
        self.base_url = "https://gisogd.gov.ru"  # прописываем базовый урл

    def open_site(self, page_address):  # открываем сайт
        return self.driver.get(self.base_url + page_address)

    def find_element(self, locator,
                     time=10):  # метод поиска элемента на странице, передаем локатор и время ожидания, выводит сообщение если не найден
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'не найден локатор{locator}')
