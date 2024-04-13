from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import Creator

class TestAboutForm(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = Creator(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_collaborate_form(self):
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)