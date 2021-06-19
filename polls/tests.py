from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import apiviews
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model



# Create your tests here.
class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create(username='text', email='test@gmail.com', password='test')


    def test_list(self):
        request = self.factory.get(self.uri, HTTP_AUTHENTICATION = 'Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200, 'Expected response code 200, Received {0}, instead.'
                         .format(response.status_code))
