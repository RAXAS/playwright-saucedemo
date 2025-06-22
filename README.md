# Автоматизация QA тестов для SauceDemo

## Описание

Набор автоматизированных тестов на Python с использованием Playwright и pytest для демо-сайта
Saucedemo (https://www.saucedemo.com). Структура проекта следует паттерну Page Object Model, реализуя страницы и тесты с
подробными шагами.

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL репозитория>
   cd <папка репозитория>

2. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate     # Windows

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Установите браузеры для Playwright:
   ```bash
   playwright install

### Запуск тестов
   ```bash
   pytest --alluredir=allure-results

### Отчет Allure
После запуска тестов сформируется папка allure-results. Для просмотра отчета:
   ```bash
   allure serve allure-results
