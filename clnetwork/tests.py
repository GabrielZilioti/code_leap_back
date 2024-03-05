from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import CLNetwork
from .serializers import CLNetworkSerializer
from lorem_text import lorem

paragraph = lorem.paragraph()

class CLNetworkModelTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.cl_network_data = {'username': 'test_user', 'title': 'Test Title', 'content': paragraph}
        self.cl_network = CLNetwork.objects.create(**self.cl_network_data)

    def test_model_can_create_cl_network(self):
        cl_network_count = CLNetwork.objects.count()
        self.assertEqual(cl_network_count, 1)


class CLNetworkViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.cl_network_data = {'username': 'test_user', 'title': 'Test Title', 'content': paragraph}
        self.response = self.client.post(
            reverse('clnetwork-list'),
            self.cl_network_data,
            format="json")

    def test_view_can_create_cl_network(self):
        self.assertEqual(self.response.status_code, 201)

    def test_view_can_retrieve_cl_network(self):
        cl_network = CLNetwork.objects.get()
        response = self.client.get(reverse('clnetwork-detail', kwargs={'pk': cl_network.id}), format="json")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, cl_network)

    def test_view_can_delete_cl_network(self):
        cl_network = CLNetwork.objects.get()
        response = self.client.delete(reverse('clnetwork-detail', kwargs={'pk': cl_network.id}), format="json")
        self.assertEqual(response.status_code, 204)

    def test_view_can_update_cl_network(self):
        change_cl_network = {'username': 'new_user', 'title': 'New Title', 'content': 'New Content'}
        cl_network = CLNetwork.objects.get()
        response = self.client.put(
            reverse('clnetwork-detail', kwargs={'pk': cl_network.id}),
            change_cl_network,
            format='json')
        self.assertEqual(response.status_code, 200)
