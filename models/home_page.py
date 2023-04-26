from .common_page import CommonPage


class HomePage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.title = "Automation Exercise"
        self.locator_main_slider = page.locator("#slider")
