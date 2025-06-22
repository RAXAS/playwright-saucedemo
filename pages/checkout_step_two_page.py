from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    CHECKOUT_FINISH_SELECTOR = "#finish"

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = "checkout-step-two.html"

    def finish_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_FINISH_SELECTOR)
        self.assert_text_present_on_page("Thank you for your order!")
