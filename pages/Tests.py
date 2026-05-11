# Run all shopping tests
pytest tests/test_shopping_flow.py -v

# Run only smoke tests
pytest tests/test_shopping_flow.py -m smoke

# Run specific test
pytest tests/test_shopping_flow.py::TestShoppingFlow::test_complete_shopping_flow

# Run with Firefox
pytest tests/test_shopping_flow.py --browser=firefox