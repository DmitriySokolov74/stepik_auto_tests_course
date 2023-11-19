# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def first_function(url, link):
    try:
        driver = webdriver.Chrome()
        time.sleep(5)
        # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        driver.get(url)
        time.sleep(5)

        # Найдем кнопку, которая отправляет введенное решение
        submit_button = driver.find_element(By.LINK_TEXT, link)

        # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
        submit_button.click()
        time.sleep(5)
    finally:
        # После выполнения всех действий мы должны не забыть закрыть окно браузера
        driver.quit()


def fill_form(browser):
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def search_by_full_link(url):
    try:
        hidden_url_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
        browser = webdriver.Chrome()
        browser.get(url)
        link_element = browser.find_element(By.LINK_TEXT, hidden_url_text)
        link_element.click()
        fill_form(browser)
    finally:
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def search_several_elements(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        input_elements = browser.find_elements(By.TAG_NAME, "input")
        for element in input_elements:
            element.send_keys("Мой ответ")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    finally:
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def search_by_xpath(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//form/div[6]/button[contains(text(), 'Submit')]")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_reg(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        required_label_texts = ["First name*", "Last name*", "Email*"]
        for label in required_label_texts:
            label_selector_text = f"//label[contains(text(), '{label}')]"
            input_selector_text = label_selector_text + "/following::input[@required]"
            input_element = browser.find_element(By.XPATH, input_selector_text)
            input_element.send_keys("test text")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def test_checkbox_and_radiobutton(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(5)
        x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
        x = x_element.text
        calc_value = calc(x)
        text_field = browser.find_element(By.XPATH, "//input[@type='text']")
        text_field.send_keys(calc_value)
        robot_checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
        robot_checkbox.click()
        radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
        radiobutton.click()
        submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        submit.click()
    finally:
        time.sleep(20)
        browser.quit()


def test_get_attribute(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(4)
        element = browser.find_element(By.XPATH, "//img[@id='treasure']")
        x = element.get_attribute("valuex")
        calc_value = calc(x)
        text_field = browser.find_element(By.XPATH, "//input[@type='text']")
        text_field.send_keys(calc_value)
        robot_checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
        robot_checkbox.click()
        radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
        radiobutton.click()
        submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        submit.click()
    finally:
        time.sleep(20)
        browser.quit()


def select_value(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(3)
        first_num_element = browser.find_element(By.ID, "num1")
        second_num_element = browser.find_element(By.ID, "num2")
        sum_nums = int(first_num_element.text) + int(second_num_element.text)
        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(sum_nums))
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
    finally:
        time.sleep(10)
        browser.quit()


def execute_js():
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")
    time.sleep(10)


def scroll_page(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(0)
        button = browser.find_element(By.TAG_NAME, "button")
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        calc_value = calc(x)
        input_element = browser.find_element(By.ID, "answer")
        input_element.send_keys(calc_value)
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        #browser.execute_script("window.scrollBy(0, 100);")

        check_element = browser.find_element(By.ID, "robotCheckbox")
        check_element.click()
        radio_element = browser.find_element(By.ID, "robotsRule")
        radio_element.click()
        button.click()
    finally:
        time.sleep(10)
        browser.quit()


def send_file():
    try:
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "files", "test_file.txt")
        url = "https://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(1)
        first_name_field = browser.find_element(By.XPATH, "//input[@name='firstname']")
        first_name_field.send_keys("Ivan")
        last_name_field = browser.find_element(By.XPATH, "//input[@name='lastname']")
        last_name_field.send_keys("Ivanov")
        email_field = browser.find_element(By.XPATH, "//input[@name='email']")
        email_field.send_keys("sok@s.ru")
        button_file = browser.find_element(By.ID, "file")
        button_file.send_keys(file_path)
        button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_submit.click()
    finally:
        time.sleep(20)
        browser.quit()


def accept_confirm():
    try:
        url = "http://suninjuly.github.io/alert_accept.html"
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(1)
        button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_submit.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        captcha_result = calc(x)
        text_field = browser.find_element(By.ID, "answer")
        text_field.send_keys(captcha_result)
        button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_submit.click()
    finally:
        time.sleep(20)
        browser.quit()


def switch_to_window():
    try:
        url = "http://suninjuly.github.io/redirect_accept.html"
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(1)
        button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_submit.click()
        names = browser.window_handles
        new_window = names[1]
        browser.switch_to.window(new_window)
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        captcha_result = calc(x)
        text_field = browser.find_element(By.ID, "answer")
        text_field.send_keys(captcha_result)
        button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_submit.click()
    finally:
        time.sleep(20)
        browser.quit()


class GetExceptionType:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print(str(exc_type))
            return True


def check_exception_type():
    with GetExceptionType("http://suninjuly.github.io/cats.html") as g:
        browser = webdriver.Chrome()
        browser.get(g.url)
        element = browser.find_element(By.ID, "button")


def wait_element():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        price_element = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
        book_button = browser.find_element(By.ID, "book")
        book_button.click()
        value_element_text = browser.find_element(By.ID, "input_value").text
        value = calc(value_element_text)
        text_field = browser.find_element(By.ID, "answer")
        text_field.send_keys(value)
        submit_button = browser.find_element(By.ID, "solve")
        submit_button.click()
    finally:
        time.sleep(10)
        browser.quit()

# Press the green button in the gutter to run the script.
wait_element()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
