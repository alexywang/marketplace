from django.test import TestCase
from .models import UserProfile
from .views import *
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.http import Http404

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="I_Fxjcaoie",email="test@gmail.com",password="weather1!")
        user.is_active = True
        user.save()
                
        profile = UserProfile.objects.create(phone="123",user=user)
        
        
        self.user=user
        self.user.UserProfile=profile
        self.factory = RequestFactory()
    
    
    def test_get_user_profile(self):
        request = self.factory.get('profile?username=I_Fxjcaoie')
        request.user=self.user
        
        response = get_user(request)
        self.assertEquals(response.status_code,200)
        
        body_response= response.content.decode('utf8')
        correct_name= 'I_Fxjcaoie' in body_response
        
        self.assertEqual(True,correct_name)
    
    


    def test_raise_404(self):
        request = self.factory.get('profile?username=FAIL')
        request.user=self.user
        triggered404=False
        try:
             response = get_user(request)
        except Http404:   
             triggered404=True
        
        self.assertEquals(triggered404,True)
        
        
        