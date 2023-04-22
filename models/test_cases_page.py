from .common_page import CommonPage


class TestCasesPage(CommonPage):
    __test__ = False

    def __init__(self, page):
        super().__init__(page)
        self.url += "test_cases"
