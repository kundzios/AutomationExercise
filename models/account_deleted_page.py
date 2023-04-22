from .common_page import CommonPage


class AccountDeletedPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "delete_account"

    def proceed(self):
        self.page.get_by_role("link", name="Continue").click()
