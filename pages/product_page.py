from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # ── Locators ────────────────────────────────────────────
    PRODUCT_TITLE = (By.ID, "productTitle")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".a-price-whole")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_CONFIRMATION = (By.ID, "attach-added-to-cart-message")
    QUANTITY_DROPDOWN = (By.ID, "quantity")
    GO_TO_CART_BUTTON = (By.ID, "attach-view-cart-button-form")
    PROCEED_TO_CHECKOUT = (By.NAME, "proceedToRetailCheckout")

    # ── Actions ─────────────────────────────────────────────
    def get_product_title(self) -> str:
        """Return the product title."""
        return self.get_text(self.PRODUCT_TITLE)

    def get_product_price(self) -> str:
        """Return the product price."""
        return self.get_text(self.PRODUCT_PRICE)

    def click_add_to_cart(self):
        """Click add to cart button."""
        self.click(self.ADD_TO_CART_BUTTON)

    def select_quantity(self, quantity: str):
        """Select quantity from dropdown."""
        from selenium.webdriver.support.ui import Select
        dropdown_element = self.find(self.QUANTITY_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_value(quantity)

    def add_to_cart_with_quantity(self, quantity: str = "1"):
        """Add product to cart with specified quantity."""
        if quantity != "1":
            self.select_quantity(quantity)
        self.click_add_to_cart()

    def click_go_to_cart(self):
        """Navigate to cart after adding product."""
        self.click(self.GO_TO_CART_BUTTON)

    # ── Verifications ───────────────────────────────────────
    def is_added_to_cart_confirmation_displayed(self) -> bool:
        """Check if 'Added to Cart' message appears."""
        return self.is_visible(self.CART_CONFIRMATION, timeout=10)

    def is_product_page_loaded(self) -> bool:
        """Verify product page loaded by checking title exists."""
        return self.is_visible(self.PRODUCT_TITLE, timeout=10)