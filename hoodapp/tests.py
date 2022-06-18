from django import test
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'maureen', email = 'ndiemam@gmail.com', password = 'passwadd')
        self.user.save()
        self.maureen = Profile(bio = 'A Fullstack Programmer', user = self.user)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.maureen,Profile))

    def test_save(self):
        Profile.objects.create()
        self.maureen.save_user_profile(self.user)
        users = Profile.objects.all()
        self.assertTrue(len(users)>0)

class HoodTest(TestCase):
    def setUp(self):
        self.user = User(username='maureen', email='ndiemam@gmail.com', password='passwadd')
        self.user.save()
        self.maureen = Profile(bio='A fullstack Programmer', user=self.user)
        self.NeighbourHood = NeighbourHood(name = '',bio = "",admin = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.NeighbourHood.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,NeighbourHood))

    def test_save(self):
        self.NeighbourHood.save_hood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) == 1)



class PostTest(TestCase):
    def setUp(self):
        self.user = User(username='maureen', email='maureen@gmail.com', password='passwadd')
        self.user.save()
        self.maureen = Profile(bio='A fullstack Programmer', user=self.user)
        self.NeighbourHood = NeighbourHood(name='Muthaiga', bio="kitusuru", admin=self.user)
        self.business = Business(name="saniamo", owner = self.user, business_description= 'eucabeth',
                                 locale = self.hood,business_number = 4322323)
        self.post = Post(title='Postings',post = 'This is the post',
                         hood = self.hood, poster = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.NeighbourHood.delete()
        self.business.delete()
        self.post.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 1)
