import allure
import pytest
from conftest import browser
from pages.login_page import LoginPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage

@allure.feature("Тесты работы с ордерами")
class TestOrders:
    @allure.story("Проверка создания заказа")
    def test_create_order(self, browser):
        page = browser.new_page()
        login_page = LoginPage(page)
        checkout_step_one_page = CheckoutStepOnePage(page)
        checkout_step_two_page = CheckoutStepTwoPage(page)
        inventory_page = InventoryPage(page)

        with allure.step("Авторизация пользователя"):
            login_page.login("standard_user", "secret_sauce")
            assert page.url.endswith("/inventory.html"), "Не удалось авторизоваться"

        with allure.step("Добавление товара в корзину"):
            inventory_page.add_first_item_to_card()
            assert inventory_page.get_count_cart_item() == 1, "Товар не добавлен в корзину"

        with allure.step("Переход к оформлению заказа"):
            checkout_step_one_page.start_checkout()
            assert page.url.endswith("/checkout-step-one.html"), "Ошибка перехода на страницу оформления заказа"

        with allure.step("Заполнение данных для доставки"):
            checkout_step_one_page.fill_checkout_form("John", "Doe", "12345")
            checkout_step_one_page.continue_checkout()
            assert page.url.endswith("/checkout-step-two.html"), "Ошибка перехода подтверждения заказа"

        with allure.step("Завершение оформления заказа"):
            checkout_step_two_page.finish_checkout()
            assert page.url.endswith("/checkout-complete.html"), "Заказ не был завершен"


