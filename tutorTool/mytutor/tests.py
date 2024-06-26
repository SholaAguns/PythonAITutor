from django.contrib.auth import get_user_model
from django.test import TestCase
User = get_user_model()
from .models import Response
import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tutorproject.settings'

class ResponseTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="unittestuser", email="unittestuser@test.com", password="Asecurepassword1")
        person = "Naruto"
        input = f"Give me some tough love motivation to study as posing as {person}. Provide your response in html friendly format"
        request = "Motivation from " + person
        text = "Listen up here datebayo..."
        created_at = datetime.datetime.now()
        test_response = Response.objects.create(user=user, input=input, request=request, text=text, created_dt=created_at )

    def test_one_user_response_is_returned(self):
        test_user = User.objects.get(username="unittestuser")
        users_responses = Response.objects.filter(user=test_user)
        self.assertEqual(users_responses.count(), 1)


