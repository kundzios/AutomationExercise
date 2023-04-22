from .common_page import CommonPage


class SignupPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "signup"

    def sign_up_full(self, customer):
        if (customer.title == "Mr.") | (customer.title == "Mrs."):
            self.page.get_by_label(customer.title).check()
        self.page.get_by_label("Password *").fill(customer.password)
        self.page.locator("#days").select_option(str(customer.birth_day))
        self.page.locator("#months").select_option(str(customer.birth_month))
        self.page.locator("#years").select_option(str(customer.birth_year))
        if customer.wants_newsletter:
            self.page.get_by_label("Sign up for our newsletter!").check()
        if customer.wants_offers:
            self.page.get_by_label("Receive special offers from our partners!").check()
        self.page.get_by_label("First name *").fill(customer.name)
        self.page.get_by_label("Last name *").fill(customer.last_name)
        self.page.get_by_label("Company", exact=True).fill(customer.company)
        self.page.get_by_label("Address * (Street address, P.O. Box, Company name, etc.)").fill(customer.address)
        self.page.get_by_label("Address 2").fill(customer.address2)
        self.page.get_by_role("combobox", name="Country *").select_option(customer.country)
        self.page.get_by_label("State *").fill(customer.state)
        self.page.get_by_label("City *").fill(customer.city)
        self.page.locator("#zipcode").fill(customer.zip_code)
        self.page.get_by_label("Mobile Number *").fill(customer.phone_number)
        self.page.get_by_role("button", name="Create Account").click()
