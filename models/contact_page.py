from .common_page import CommonPage


class ContactPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "contact_us"
