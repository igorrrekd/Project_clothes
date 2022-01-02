from django.test import SimpleTestCase
from django.urls import reverse, resolve
from giveaway.views import LandingPageView, AddDonationView, LoginView, LogoutView, RegisterView, UserProfileView


class TestUrls(SimpleTestCase):

    def test_urls_landing(self):
        url = reverse('landing-page')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LandingPageView)

    def test_urls_donate(self):
        url = reverse('donate')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddDonationView)

    def test_urls_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_urls_logout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_urls_register(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterView)

    # def test_urls_profile(self):
    #     url = reverse('profile')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, UserProfileView)
