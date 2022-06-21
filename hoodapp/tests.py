from django.test import TestCase
from .models import *
# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='maureen',email="ndiemam@gmail.com", password='1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='maureen',email="ndiemam@gmail.com")
        self.NeighbourHood = NeighbourHood(name='Ngong', bio="Milimani", admin=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
        
    def test_save_post(self):
        self.post.save()
        
    def test_delete_post(self):
        self.post.save()



class HoodTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username='maureen',email="ndiemam@gmail.com")
        self.NeighbourHood = NeighbourHood(name = 'Ngong',bio = "Milimani",admin = self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, NeighbourHood))
        
    def test_save_post(self):
        self.hood.save()
        
    def test_delete_post(self):
        self.hood.save()
    