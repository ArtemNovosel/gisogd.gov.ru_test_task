# описываем страницу на которой будем работать

# импортируем локатор
from selenium.webdriver.common.by import By
# подключаем базовую страницу
from base_page import BasePage


class Locators:  # прописываем нужные для теста локаторы со страницы РНТД
    LOKATOR_SEARCH_DOC = (By.XPATH, '//*[@placeholder="Введите наименование или номер"]')
    LOKATOR_SEARCH_BUTTON = (By.XPATH, '//*[@class="g-btn g-btn--primary g-a11y-btn--primary"]')
    LOKATOR_MESSAGE_LIST_DOC = (By.XPATH, '//*[@class="ba-mb-2 ba-text-sm ba-font-semibold"]')
    LOCATOR_LIST_DOC = (By.XPATH, '//*[@id="__layout"]//article[1]/a/p')


class SearchHelper(BasePage):  # класс который осуществляет поиск
    def enter_word(self, word):  # передаем слово в поле
        search_field = self.find_element(Locators.LOKATOR_SEARCH_DOC, time=5)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_button(self):  # клик на кнопку Найти
        return self.find_element(Locators.LOKATOR_SEARCH_BUTTON, time=5).click()

    def message_list_doc(self):  # забираем сообщение с колличеством документов
        return self.find_element(Locators.LOKATOR_MESSAGE_LIST_DOC, time=5).text

    def click_doc(self):  # нажимаем на первый документ в списке найденных
        return self.find_element(Locators.LOCATOR_LIST_DOC, time=10).click()
