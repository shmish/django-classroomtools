from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError
from django import forms

class RandomizerAccountAdapter(DefaultAccountAdapter):

    def clean_email(self, email):
        """
        Validates an email value. You can hook into this if you want to
        (dynamically) restrict what email addresses can be chosen.
        """
        print(email)
        domain = email.split('@')
        domain = "@" + domain[1]
        
        if domain == "@dryfly.ca":
            print("OK")
            return email
        else:
            print("Fail")
            raise ValidationError("You must use a VSB email address")
              
        return email

