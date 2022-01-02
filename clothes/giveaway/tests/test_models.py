from django.test import TestCase
from giveaway.models import Category, Institution, Donation
from django.contrib.auth.models import User


class CategoryModelTestCase(TestCase):
    @classmethod
    def setUpData(cls):
        cls.category = Category.objects.create(name="category 1")

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.category.name, str)
        self.assertIsInstance(self.category.description, str)

    def test_first_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)


class InstitutionModelTestCase(TestCase):
    @classmethod
    def setUpData(cls):
        cls.institution = Institution.objects.create(name="institution 1", description="content")

    def test_name_label(self):
        institution = Institution.objects.get(id=1)
        field_label = institution._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        institution = Institution.objects.get(id=1)
        field_label = institution._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        institution = Institution.objects.get(id=1)
        max_length = institution._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

