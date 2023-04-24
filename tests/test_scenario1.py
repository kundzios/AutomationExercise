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


def check_homepage_visibility(page):
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".carousel-inner").first).to_be_visible()


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    p = HomePage(page)
    p.navigate()
    p.go_to_products_page()
    # this triggers a one-time full-screen ad that otherwise breaks the tests
    yield
    print("afterEach")


def test_case1_register_user(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_login_page()
    login_page = LoginPage(page)
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()
    login_page.sign_up_simple(customer.name, customer.email)
    signup_page = SignupPage(page)
    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    expect(page.get_by_label("Name *", exact=True)).to_have_value(customer.name)
    expect(page.get_by_label("Email *")).to_have_value(customer.email)
    signup_page.sign_up_full(customer)
    expect(page.get_by_text("Account Created!")).to_be_visible()
    acc_created_page = AccountCreatedPage(page)
    acc_created_page.proceed_to_homepage()
    check_homepage_visibility(page)
    expect(page.get_by_text("Logged in as " + customer.name)).to_be_visible()
    # skipping the account deletion steps in order to reuse it in the next few test cases


def test_case4_logout_user(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_login_page()
    login_page = LoginPage(page)
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    login_page.login(customer.email, customer.password)
    check_homepage_visibility(page)
    expect(page.get_by_text("Logged in as " + customer.name)).to_be_visible()
    home_page.log_out()
    expect(page).to_have_url(login_page.url)


def test_case5_register_user_with_existing_email(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_login_page()
    login_page = LoginPage(page)
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()
    login_page.sign_up_simple(customer.name, customer.email)
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()


def test_case3_login_with_incorrect_credentials(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_login_page()
    login_page = LoginPage(page)
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    login_page.login("a" + customer.email, customer.password)
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()


def test_case2_login_with_correct_credentials(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_login_page()
    login_page = LoginPage(page)
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    login_page.login(customer.email, customer.password)
    check_homepage_visibility(page)
    expect(page.get_by_text("Logged in as " + customer.name)).to_be_visible()
    home_page.delete_account()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    acc_deleted_page = AccountDeletedPage(page)
    acc_deleted_page.proceed_to_homepage()
    check_homepage_visibility(page)
    expect(page.get_by_text("Logged in as " + customer.name)).not_to_be_visible()


def test_case6_contact_us_form(page: Page):
    filepath = 'tests/data/test_file.txt'
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_contact_page()
    contact_page = ContactPage(page)
    expect(page.get_by_role("heading", name="Get In Touch")).to_be_visible()
    contact_page.send_message_with_file(customer.name, customer.email, "A cool subject", "A cool message", filepath)
    expect(page.locator("#contact-page").get_by_text("Success! Your details have been submitted successfully.")).\
        to_be_visible()
    contact_page.proceed_to_homepage()
    check_homepage_visibility(page)


def test_case7_verify_test_cases_page(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    check_homepage_visibility(page)
    home_page.go_to_test_cases_page()
    test_cases_page = TestCasesPage(page)
    expect(page).to_have_url(test_cases_page.url)
