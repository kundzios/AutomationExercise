from .common_page import CommonPage


class CartPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "view_cart"
