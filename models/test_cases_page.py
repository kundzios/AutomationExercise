from .common_page import CommonPage


class TestCasesPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "test_cases"
