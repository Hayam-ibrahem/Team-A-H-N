from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            user_name="TestUser",
            password="TestPassword",
            first_name="TestFirstName",
            last_name="TestLastName",
            email="Test@email.com",
            age="23",
            gender="Female",
            interests="Interests")

    def test_user_is_in_database(self):
        self.assertIsNotNone(User.objects.get(user_name="TestUser"))

    def test_user_fields(self):
        user = User.objects.get(user_name="TestUser")
        self.assertEqual(user.user_name, "TestUser")
        self.assertEqual(user.password, "TestPassword")
        self.assertEqual(user.first_name, "TestFirstName")
        self.assertEqual(user.last_name, "TestLastName")
        self.assertEqual(user.email, "Test@email.com")
        self.assertEqual(user.age, "23")
        self.assertEqual(user.gender, "Female")
        self.assertEqual(user.interests, "Interests")


class CompanyTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            user_name="TestUser",
            password="TestPassword",
            first_name="TestFirstName",
            last_name="TestLastName",
            email="Test@email.com",
            age="23",
            gender="Female",
            interests="Interests")

    def test_user_is_in_database(self):
        self.assertIsNotNone(User.objects.get(user_name="TestUser"))

    def test_user_fields(self):
        user = User.objects.get(user_name="TestUser")
        self.assertEqual(user.user_name, "TestUser")
        self.assertEqual(user.password, "TestPassword")
        self.assertEqual(user.first_name, "TestFirstName")
        self.assertEqual(user.last_name, "TestLastName")
        self.assertEqual(user.email, "Test@email.com")
        self.assertEqual(user.age, "23")
        self.assertEqual(user.gender, "Female")
        self.assertEqual(user.interests, "Interests")
