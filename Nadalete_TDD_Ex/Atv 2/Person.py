from typing import List, Optional
from Email import Email

class Person:
    def __init__(self, id: int, name: str, age: int, emails: Optional[List[Email]] = None):
        self.id = id
        self.name = name
        self.age = age
        self.emails: List[Email] = list(emails) if emails is not None else []

    def add_email(self, email: Email) -> None:
        self.emails.append(email)