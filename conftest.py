import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    # инициализируем драйвер
    driver = webdriver.Firefox(executable_path="./firefoxdriver")
    # выполняем тест
    yield driver
    # закрываем сессию
    driver.quit()
