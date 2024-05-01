from rest_framework.test import APITestCase
from django.contrib.auth.models import Group

from django.urls import reverse
from rest_framework import status

from bulletion_board.models import Ad, Feedback
from users.models import User


class AdTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com', is_superuser=True
        )

        self.user1 = User.objects.create(
            email='test1@test1.com'
        )

        self.ad = Ad.objects.create(
            title='Test',
            price=10,
            description='Test'
        )

        self.feedback = Feedback.objects.create(
            text='Test1',
            owner=self.user1,
            ad=self.ad
        )

        moderator_group, created = Group.objects.get_or_create(name='moders')

        self.user = User.objects.create(email='test2@test2.com', is_superuser=True)
        self.user.groups.add(moderator_group)

    def test_get_list(self):
        """ Тест для получения списка объявлений """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('bulletion_board:list_ad')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_ad(self):
        """ Тест создания объявления """

        self.client.force_authenticate(user=self.user)

        data = {
            "title": self.ad.title,
            "price": self.ad.price,
            "owner": self.user.id,
            "description": self.ad.description
        }

        response = self.client.post(
            reverse('bulletion_board:create_ad'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Ad.objects.all().exists()
        )

        self.assertEqual(
            response.json()['title'],
            data['title']
        )

        self.assertEqual(
            response.json()['price'],
            data['price']
        )

        self.assertEqual(
            response.json()['description'],
            data['description']
        )

    def test_update_ad(self):
        """Тестирование изменения информации об объявлении"""

        self.client.force_authenticate(user=self.user)
        ad = Ad.objects.create(
            title='Test_ad',
            price=20,
            description='Test_ad',
            owner=self.user
        )

        response = self.client.patch(
            f'/app/update/{ad.id}/',
            {'title': 'Test_ad',
             'price': 20,
             'owner': self.user.id,
             'description': 'Test_ad'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_ad(self):
        """Тестирование удаления объявления"""

        self.client.force_authenticate(user=self.user)

        ad = Ad.objects.create(
            title='Test_ad',
            price=20,
            description='Test_ad',
            owner=self.user
        )

        response = self.client.delete(
            f'/app/delete/{ad.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_get_list_feedback(self):
        """ Тест для получения списка комментариев """

        self.client.force_authenticate(user=self.user1)

        response = self.client.get(
            reverse('bulletion_board:list_feedback')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_feedback(self):
        """ Тест создания комментария """

        self.client.force_authenticate(user=self.user1)

        data = {
            "text": self.feedback.text,
            "ad": self.ad.id,
            "owner": self.user1.id,
        }

        response = self.client.post(
            reverse('bulletion_board:create_feedback'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Feedback.objects.all().exists()
        )

        self.assertEqual(
            response.json()['text'],
            data['text']
        )

        self.assertEqual(
            response.json()['owner'],
            data['owner']
        )

        self.assertEqual(
            response.json()['ad'],
            data['ad']
        )

    def test_update_feedback(self):
        """Тестирование изменения информации о комментарии"""
        self.client.force_authenticate(user=self.user1)
        feedback = Feedback.objects.create(
            text='Test_feed',
            ad=self.ad,
            owner=self.user1
        )

        response = self.client.patch(
            f'/app/update/feedback/{feedback.id}/',
            {'text': 'Test_feed',
             'ad': self.ad.id,
             'owner': self.user1.id}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_feedback(self):
        """Тестирование удаления комментария"""

        self.client.force_authenticate(user=self.user1)

        feedback = Feedback.objects.create(
            text='Test_feed',
            ad=self.ad,
            owner=self.user1
        )

        response = self.client.delete(
            f'/app/delete/feedback/{feedback.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
