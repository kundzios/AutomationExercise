import pytest
from playwright.sync_api import Page, expect

from models.home_page import HomePage
from models.products_page import ProductPage
from models.cart_page import CartPage
from models.login_page import LoginPage
from models.signup_page import SignupPage
from models.test_cases_page import TestCasesPage
from models.contact_page import ContactPage
from models.account_created_page import AccountCreatedPage
from models.account_deleted_page import AccountDeletedPage
from helpers.customer import Customer

customer = Customer()


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    HomePage(page).navigate().go_to_products_page()
    # this triggers a one-time full-screen ad that otherwise breaks the tests
    yield
    print("afterEach")


def test_case0_home_page_visibility(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(page).to_have_title(home_page.title)
    expect(home_page.locator_main_slider).to_be_visible()


def test_case1_register_user(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_login_page()
    login_page = LoginPage(page)
    expect(login_page.locator_signup_header).to_be_visible()
    login_page.sign_up_simple(customer.name, customer.email)
    signup_page = SignupPage(page)
    expect(signup_page.locator_header).to_be_visible()
    expect(signup_page.locator_name_input).to_have_value(customer.name)
    expect(signup_page.locator_email_input).to_have_value(customer.email)
    signup_page.sign_up_full(customer)
    acc_created_page = AccountCreatedPage(page)
    expect(acc_created_page.locator_header).to_be_visible()
    acc_created_page.proceed_to_homepage()
    expect(page).to_have_url(home_page.url)
    expect(home_page.locator_logged_in_as).to_contain_text(customer.name)
    # skipping the account deletion steps in order to reuse it in the next few test cases


def test_case5_register_user_with_existing_email(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_login_page()
    login_page = LoginPage(page)
    login_page.sign_up_simple(customer.name, customer.email)
    expect(login_page.locator_already_registered_error).to_be_visible()


def test_case2_login_with_correct_credentials(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_login_page()
    login_page = LoginPage(page)
    expect(login_page.locator_login_header).to_be_visible()
    login_page.login(customer.email, customer.password)
    expect(page).to_have_url(home_page.url)
    expect(home_page.locator_logged_in_as).to_contain_text(customer.name)


def test_case3_login_with_incorrect_credentials(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_login_page()
    login_page = LoginPage(page)
    login_page.login("a" + customer.email, customer.password)
    expect(login_page.locator_wrong_credentials_error).to_be_visible()
    expect(login_page.locator_logged_in_as).not_to_be_visible()


def test_case4a_logout_user(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_login_page()
    login_page = LoginPage(page)
    login_page.login(customer.email, customer.password)
    expect(page).to_have_url(home_page.url)
    expect(home_page.locator_logged_in_as).to_contain_text(customer.name)
    home_page.log_out()
    expect(page).to_have_url(login_page.url)
    expect(home_page.locator_logged_in_as).not_to_be_visible()


def test_case4b_delete_account(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_login_page()
    login_page = LoginPage(page)
    login_page.login(customer.email, customer.password)
    expect(page).to_have_url(home_page.url)
    home_page.delete_account()
    acc_deleted_page = AccountDeletedPage(page)
    expect(acc_deleted_page.locator_header).to_be_visible()
    acc_deleted_page.proceed_to_homepage()
    expect(page).to_have_url(home_page.url)
    expect(home_page.locator_logged_in_as).not_to_be_visible()


def test_case6_contact_us_form(page: Page):
    filepath = 'tests/data/test_file.txt'
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_contact_page()
    contact_page = ContactPage(page)
    expect(contact_page.locator_get_in_touch_header).to_be_visible()
    contact_page.send_message_with_file(customer.name, customer.email, "A cool subject", "A cool message", filepath)
    expect(contact_page.locator_message_sent_successfully).to_be_visible()
    contact_page.proceed_to_homepage()
    expect(page).to_have_url(home_page.url)


def test_case7_verify_test_cases_page(page: Page):
    home_page = HomePage(page)
    home_page.navigate()\
             .go_to_test_cases_page()
    test_cases_page = TestCasesPage(page)
    expect(page).to_have_url(test_cases_page.url)
