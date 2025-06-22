from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CARD_SELECTOR = ".inventory_item >> text='Add to cart'"
    SHOPPING_CART_LINK_SELECTOR = "[data-test='shopping-cart-link']"
    SHOPPING_CART_BADGE = "[data-test='shopping-cart-badge']"

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = "inventory.html"

    def add_first_item_to_card(self):
        self.wait_for_selector_and_click(self.ADD_TO_CARD_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def get_count_cart_item(self):
        return self.wait_for_badge_count_and_get(self.SHOPPING_CART_BADGE)
