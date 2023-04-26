from .common_page import CommonPage


class AccountCreatedPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "account_created"
        self.locator_header = page.get_by_text("Account Created!")

    def proceed_to_homepage(self):
        self.page.get_by_role("link", name="Continue").click()
