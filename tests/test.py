import time

import pytest

from rntd_page import SearchHelper


# Поиск валидного документа по номеру
def test_search(browser):
    rntd_page = SearchHelper(browser)  # Открываем браузер
    rntd_page.open_site('/rntd')  # с нужной страницей
    koll_one = rntd_page.message_list_doc()  # получаем сообщение о колличестве найденных документов
    rntd_page.enter_word("871н")  # вводим номер документа
    rntd_page.click_button()  # нажимаем найти
    time.sleep(2)  # ожидание прогрузки результата поиска
    koll_two = rntd_page.message_list_doc()  # получаем повторное сообщение о колличестве найденных документов
    assert koll_one != koll_two  # проверяем что результат поиска изменился


# Открытие страницы документа из списка найденных
def test_doc(browser):
    rntd_page = SearchHelper(browser)  # Открываем браузер
    rntd_page.open_site('/rntd')  # с нужной страницей
    rntd_page.click_button()  # нажимаем найти
    rntd_page.click_doc()  # нажимаем на первый документ в списке
    assert "https://gisogd.gov.ru/rntd" != browser.current_url  # проверяем переход на страницу документа по url
