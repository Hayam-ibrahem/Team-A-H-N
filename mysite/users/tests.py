from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from users.models import User
from users.models import Company

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

    def test_login_validation(self):
        response = self.client.get('/login_validation/TestUser/TestPassword')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response_content, '{"user_ID": 1}')

        response = self.client.get('/login_validation/TestUser/WrongPassword')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response_content, 'User not Found')

        response = self.client.get('/login_validation/WrongUser/TestPassword')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response_content, 'User not Found')


class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(
            company_name="TestCompanyName",
            company_password="TestPassword",
            name="TestName",
            location="TestLocation",
            nOfEmployees="200",
            email="Test@email.com",
            company_interests="Interests")

    def test_company_is_in_database(self):
        self.assertIsNotNone(Company.objects.get(company_name="TestCompanyName"))

    def test_company_fields(self):
        company = Company.objects.get(company_name="TestCompanyName")
        self.assertEqual(company.company_name, "TestCompanyName")
        self.assertEqual(company.company_password, "TestPassword")
        self.assertEqual(company.name, "TestName")
        self.assertEqual(company.location, "TestLocation")
        self.assertEqual(company.nOfEmployees, "200")
        self.assertEqual(company.email, "Test@email.com")
        self.assertEqual(company.company_interests, "Interests")

    def test_login_validation(self):
        response = self.client.get('/companyValidateLogin/TestCompanyName/TestPassword')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response_content, '{"company_name": "TestCompanyName"}')

        response = self.client.get('/companyValidateLogin/TestCompanyName/WrongPassword')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response_content, 'Company not Found')

        response = self.client.get('/companyValidateLogin/WrongCompany/TestPassword')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response_content, 'Company not Found')