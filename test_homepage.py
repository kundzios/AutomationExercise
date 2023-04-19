import re
from playwright.sync_api import Page, expect


def test_homepage(page: Page):
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))
