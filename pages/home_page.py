from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    #---Locators----------------------------------------
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, "h2.a-size-mini")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] h2 a")

    #---URL---------------------------------------------
    HOME_URL = "https://www.amazon.com"

    #---Actions-----------------------------------------
    def open_home_page(self):
        """Navigate to homepage."""
        self.open(self.HOME_URL)

    def enter_search_term(self, search_term: str):
        """Type search query into search box."""
        self.type(self.SEARCH_BOX, search_term)

    def click_search_button(self):
        """Click the search button."""
        self.click(self.SEARCH_BUTTON)

    def search_product(self, product_name: str):
        """Complete search flow in one action."""
        self.enter_search_term(product_name)
        self.click_search_button()

    def click_first_product(self):
        """Click the first product in search results."""
        self.click(self.FIRST_PRODUCT)

        # ── Verifications ───────────────────────────────────────

    def is_search_results_displayed(self) -> bool:
        """Check if search results appear."""
        return self.is_visible(self.SEARCH_RESULTS_HEADER, timeout=10)

    def get_search_results_text(self) -> str:
        """Get the search results header text."""
        return self.get_text(self.SEARCH_RESULTS_HEADER)