from .common_page import CommonPage


class LoginPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "login"
        self.locator_login_header = page.get_by_role("heading", name="Login to your account")
        self.locator_signup_header = page.get_by_role("heading", name="New User Signup!")
        self.locator_wrong_credentials_error = page.get_by_text("Your email or password is incorrect!")
        self.locator_already_registered_error = page.get_by_text("Email Address already exist!")

    def login(self, email, password):
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def sign_up_simple(self, name, email):
        self.page.get_by_placeholder("Name").fill(name)
        self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_role("button", name="Signup").click()
