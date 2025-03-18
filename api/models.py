from django.db import models

# Create your models here.

class User:
    def __init__(self, id, username, password, email, credit_card_number):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.credit_card_number = credit_card_number