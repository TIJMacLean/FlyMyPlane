from django.test import TestCase
from ..models import Owner

# Create your tests here.
class OwnerTest(TestCase):
    """ Test module for Owner model """

    def setUp(self):
        Owner.objects.create(
            name='Test Person', email_address="test@test.com", phone_number="01234567890")
        Owner.objects.create(
            name='Test Person 2', email_address="test2@test.com", phone_number="09876543210")

    def test_owner_welcomer(self):
        test_person = Owner.objects.get(name='Test Person')
        test_person2 = Owner.objects.get(email_address='test2@test.com')
        self.assertEqual(
            test_person.welcomer(), "Welcome back, Test Person!")
        self.assertEqual(
            test_person2.welcomer(), "Welcome back, Test Person 2!")