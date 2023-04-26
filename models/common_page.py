import re


class CommonPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com/"
        self.locator_logged_in_as = page.get_by_text(re.compile("Logged in as *"))

    def navigate(self):
        self.page.goto(self.url)
        return self

    def go_to_home_page(self):
        self.page.get_by_role("link", name=" Home").click()

    def go_to_products_page(self):
        self.page.get_by_role("link", name=" Products").click()

    def go_to_cart_page(self):
        self.page.get_by_role("link", name=" Cart").click()

    def go_to_login_page(self):
        self.page.get_by_role("link", name=" Signup / Login").click()

    def go_to_test_cases_page(self):
        self.page.get_by_role("link", name=" Test Cases").click()

    def go_to_contact_page(self):
        self.page.get_by_role("link", name=" Contact us").click()

    def log_out(self):
        self.page.get_by_role("link", name=" Logout").click()

    def delete_account(self):
        self.page.get_by_role("link", name=" Delete Account").click()

    def subscribe_for_newsletter(self, email):
        self.page.get_by_placeholder("Your email address").fill(email)
        self.page.get_by_role("button", name="").click()
        return self
