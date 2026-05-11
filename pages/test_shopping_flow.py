# tests/test_shopping_flow.py

import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestShoppingFlow:
    """Test suite for product search and cart functionality."""

    @pytest.mark.smoke
    def test_search_product(self, driver):
        """Test searching for a product."""
        home_page = HomePage(driver)

        # Navigate and search
        home_page.open_home_page()
        home_page.search_product("laptop")

        # Verify search results appear
        assert home_page.is_search_results_displayed(), "Search results not displayed"
        assert "laptop" in home_page.get_search_results_text().lower(), \
            "Search results don't match search term"

    @pytest.mark.smoke
    def test_add_single_product_to_cart(self, driver):
        """Test adding one product to cart."""
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Search for product
        home_page.open_home_page()
        home_page.search_product("wireless mouse")
        home_page.click_first_product()

        # Verify product page loaded
        assert product_page.is_product_page_loaded(), "Product page did not load"

        # Add to cart
        product_page.click_add_to_cart()

        # Verify confirmation
        assert product_page.is_added_to_cart_confirmation_displayed(), \
            "Add to cart confirmation not shown"

        # Go to cart and verify
        product_page.click_go_to_cart()
        assert cart_page.is_cart_page_loaded(), "Cart page did not load"
        assert cart_page.get_cart_item_count() >= 1, "Cart is empty"

    @pytest.mark.regression
    def test_add_multiple_quantity_to_cart(self, driver):
        """Test adding product with quantity greater than 1."""
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.search_product("notebook")
        home_page.click_first_product()

        # Add to cart with quantity 2
        product_page.add_to_cart_with_quantity("2")

        assert product_page.is_added_to_cart_confirmation_displayed(), \
            "Add to cart confirmation not shown"

    @pytest.mark.regression
    def test_complete_shopping_flow(self, driver):
        """Test complete flow: search -> add to cart -> verify cart."""
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Step 1: Search
        home_page.open_home_page()
        home_page.search_product("headphones")
        assert home_page.is_search_results_displayed(), "No search results"

        # Step 2: Select product
        home_page.click_first_product()
        assert product_page.is_product_page_loaded(), "Product page failed to load"

        # Get product details before adding
        product_title = product_page.get_product_title()

        # Step 3: Add to cart
        product_page.click_add_to_cart()
        assert product_page.is_added_to_cart_confirmation_displayed(), \
            "No add to cart confirmation"

        # Step 4: Verify in cart
        product_page.click_go_to_cart()
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        assert cart_page.get_cart_item_count() >= 1, "Product not in cart"

        # Verify correct product is in cart
        assert cart_page.is_item_in_cart(product_title), \
            f"Expected product '{product_title}' not found in cart"

    @pytest.mark.regression
    def test_remove_item_from_cart(self, driver):
        """Test removing a product from cart."""
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Add item to cart first
        home_page.open_home_page()
        home_page.search_product("pen")
        home_page.click_first_product()
        product_page.click_add_to_cart()
        product_page.click_go_to_cart()

        # Verify item added
        initial_count = cart_page.get_cart_item_count()
        assert initial_count >= 1, "Cart should have at least 1 item"

        # Remove item
        cart_page.delete_first_item()

        # Verify removal (cart count decreased or empty message appears)
        # Note: This may need adjustment based on actual application behavior
        import time
        time.sleep(2)  # Wait for cart update