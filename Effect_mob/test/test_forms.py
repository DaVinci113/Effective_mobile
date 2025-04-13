# from unicodedata import category
#
# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.urls import reverse
# from ads.models import Ad, Category
#
#
# class FormTestCase(TestCase):
#     def setUp(self):
#         User.objects.create_user(username='user1', email='user1@user1.com', password='user1')
#         User.objects.create_user(username='user2', email='user2@user2.com', password='user2')
#         self.client.login(username='user1', password='user1')
#
#     def test_ad_form(self):
#         form_data = {
#             'title': 'title112233',
#             'description': 'description1',
#             'image_url': 'https://yandex.ru/images/search?source.jpg',
#             'condition': 'NEW',
#             'created_at': '2025-04-12 21:43:11.864522'
#         }
#         response = self.client.post(reverse('ads:ad-create'), data=form_data)
#         print(response.text)
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(Ad.objects.filter(title='title112233'))