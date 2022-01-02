# from django.test import TestCase, Client
# from django.urls import reverse
# from giveaway.models import Category, Institution, Donation
# import json


# class TestViews(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.list_url = reverse('list')
#         self.detail_url = reverse('detail', args=['category1'])
#         self.project1 = Category.objects.create(name='category1', giveaway=10000)
#
#     def test_project_list_GET(self):
#         response = self.client.get(self.list_url)
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'giveaway/form.html')
#
#     def test_project_detail_GET(self):
#         response = self.client.get(self.detail_url)
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'giveaway/index.html')