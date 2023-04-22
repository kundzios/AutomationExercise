from dataclasses import dataclass


@dataclass
class Customer:
    email: str = "random@mail.com"
    password: str = "Passw0rd"
    name: str = "Bob"
    last_name: str = "Randomguy"
    title: str = "Mr."
    birth_day: int = 13
    birth_month: int = 7
    birth_year: int = 2000
    wants_newsletter: bool = True
    wants_offers: bool = True
    company: str = "Bobex"
    address: str = "13 Random St"
    address2: str = "entrance C"
    country: str = "United States"
    state: str = "Florida"
    city: str = "Miami"
    zip_code: str = "12345"
    phone_number: str = "1234567890"
