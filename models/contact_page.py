from .common_page import CommonPage


class ContactPage(CommonPage):
    def __init__(self, page):
        super().__init__(page)
        self.url += "contact_us"
        self.locator_get_in_touch_header = page.get_by_role("heading", name="Get In Touch")
        self.locator_message_sent_successfully = page.locator("#contact-page")\
            .get_by_text("Success! Your details have been submitted successfully.")

    def send_message(self, name, email, subject, message):
        self.page.get_by_placeholder("Name").fill(name)
        self.page.get_by_placeholder("Email", exact=True).fill(email)
        self.page.get_by_placeholder("Subject").fill(subject)
        self.page.get_by_placeholder("Your Message Here").fill(message)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Submit").click()

    def send_message_with_file(self, name, email, subject, message, file):
        self.page.locator("input[name=\"upload_file\"]").set_input_files(file)
        self.send_message(name, email, subject, message)

    def proceed_to_homepage(self):
        self.page.get_by_role("link", name=" Home").click()
