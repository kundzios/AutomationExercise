import pytest
from playwright.sync_api import Page, expect

from models.home_page import HomePage
from models.products_page import ProductPage
from models.cart_page import CartPage
from models.login_page import LoginPage
from models.signup_page import SignupPage
from models.test_cases_page import TestCasesPage
from models.contact_page import ContactPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    p = HomePage(page)
    p.navigate()
    p.go_to_products_page()
    # this triggers a one-time full-screen ad that otherwise breaks the tests
    yield
    print("afterEach")


def test_case1(page: Page):
    p = HomePage(page)
    p.navigate()
    expect(page).to_have_title("Automation Exercise")
