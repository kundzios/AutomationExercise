from .common_page import CommonPage


class SignupPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "signup"
