from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # ── Locators ────────────────────────────────────────────
    CART_ITEMS = (By.CSS_SELECTOR, "div[data-name='Active Items'] .sc-list-item")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, ".sc-product-title")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, ".sc-product-price")
    CART_SUBTOTAL = (By.ID, "sc-subtotal-amount-activecart")
    CART_QUANTITY = (By.CSS_SELECTOR, "span.sc-quantity-textfield")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".sc-empty-cart-header")
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, "proceedToRetailCheckout")
    DELETE_ITEM_BUTTON = (By.CSS_SELECTOR, "input[data-action='delete']")

    # ── URL ─────────────────────────────────────────────────
    CART_URL = "https://www.amazon.com/gp/cart/view.html"

    # ── Actions ─────────────────────────────────────────────
    def open_cart(self):
        """Navigate directly to cart page."""
        self.open(self.CART_URL)

    def get_cart_item_count(self) -> int:
        """Return number of items in cart."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.CART_ITEMS)
            )
            items = self.driver.find_elements(*self.CART_ITEMS)
            return len(items)
        except:
            return 0

    def get_first_item_title(self) -> str:
        """Get the title of first item in cart."""
        return self.get_text(self.CART_ITEM_TITLE)

    def get_cart_subtotal(self) -> str:
        """Get cart subtotal amount."""
        return self.get_text(self.CART_SUBTOTAL)

    def delete_first_item(self):
        """Remove first item from cart."""
        self.click(self.DELETE_ITEM_BUTTON)

    # ── Verifications ───────────────────────────────────────
    def is_cart_empty(self) -> bool:
        """Check if cart is empty."""
        return self.is_visible(self.EMPTY_CART_MESSAGE, timeout=5)

    def is_cart_page_loaded(self) -> bool:
        """Verify cart page loaded."""
        return "cart" in self.get_current_url().lower()

    def is_item_in_cart(self, product_name: str) -> bool:
        """Check if specific product is in cart."""
        item_title = self.get_first_item_title()
        return product_name.lower() in item_title.lower()