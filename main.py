import time

# Импортируем WebDriver для управления браузером
from selenium import webdriver

# Для настройки запуска Chrome (установка драйвера)
from selenium.webdriver.chrome.service import Service as ChromeService

# Для поиска элементов по типам (By.ID и т.д.)
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

# Автоматическая загрузка драйвера Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запуск браузера в фоновом режиме (без графического интерфейса)
#options.add_argument("--headless")

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
valid_username = "performance_glitch_user"
valid_password = "secret_sauce"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Вводим логин
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys(valid_username)
print("Input login")

# Ждём, выделяем и удаляем логин
time.sleep(2)
username.send_keys(Keys.CONTROL + "a")
print("Highlight login")
time.sleep(1)
username.send_keys(Keys.BACKSPACE)
print("Login deleted")

# Ввод пароля
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(valid_password)
print("Input password")

# Ждём, выделяем и удаляем пароль
time.sleep(2)
password.send_keys(Keys.CONTROL + "a")
print("Highlight password")
time.sleep(1)
password.send_keys(Keys.BACKSPACE)
print("Password deleted")

# нажимаем Enter для отправки формы
password.send_keys(Keys.ENTER)

# Ждем и обновляем страницу, для сбрасывания состояния
time.sleep(5)
driver.refresh()
print("Page refreshed")

# Выход из браузера
driver.quit()