from .common_page import CommonPage


class LoginPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "login"

    def login(self, email, password):
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def sign_up_simple(self, name, email):
        self.page.get_by_placeholder("Name").fill(name)
        self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_role("button", name="Signup").click()
