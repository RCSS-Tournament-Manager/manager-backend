from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import CustomUser, RegistrationInvite


class CustomUserModelTest(TestCase):
    def test_user_email_phone_unique(self):
        # Creating a user with unique email and phone number should work
        user1 = CustomUser.objects.create_user(
            "user1", email="user1@example.com", phone_number="+1234567890"
        )
        user1.full_clean()  # This will raise a ValidationError if the user is not valid

        # Creating a user with a duplicate email should raise a ValidationError
        with self.assertRaises(ValidationError):
            user2 = CustomUser.objects.create_user(
                "user2", email="user1@example.com", phone_number="+0987654321"
            )
            user2.full_clean()

        # Creating a user with a duplicate phone number should raise a ValidationError
        with self.assertRaises(ValidationError):
            user3 = CustomUser.objects.create_user(
                "user3", email="user3@example.com", phone_number="+1234567890"
            )
            user3.full_clean()


class RegistrationInviteModelTest(TestCase):
    def test_registration_invite_email_or_phone(self):
        # create test invite key
        invite_key = "key"

        # Creating an invite with only an email should work
        invite1 = RegistrationInvite.objects.create(
            email="invite1@example.com", key="key1"
        )
        invite1.full_clean()

        # Creating an invite with only a phone number should work
        invite2 = RegistrationInvite.objects.create(
            phone_number="+1234567890", key="key2"
        )
        invite2.full_clean()

        # Creating an invite with neither an email nor a phone number should raise a ValidationError
        with self.assertRaises(ValidationError):
            invite3 = RegistrationInvite.objects.create(key="key3")
            invite3.full_clean()

        # Creating an invite with both an email and a phone number should work
        invite4 = RegistrationInvite.objects.create(
            email="invite4@example.com", phone_number="+0987654321", key="key4"
        )
        invite4.full_clean()

        # Creating an invite with a duplicate email should raise a ValidationError
        with self.assertRaises(ValidationError):
            invite5 = RegistrationInvite.objects.create(
                email="invite1@example.com", key="key5"
            )
            invite5.full_clean()

        # Creating an invite with a duplicate phone number should raise a ValidationError
        with self.assertRaises(ValidationError):
            invite6 = RegistrationInvite.objects.create(
                phone_number="+1234567890", key="key6"
            )
            invite6.full_clean()
