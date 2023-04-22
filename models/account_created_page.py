from .common_page import CommonPage


class AccountCreatedPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "account_created"

    def proceed(self):
        self.page.get_by_role("link", name="Continue").click()
