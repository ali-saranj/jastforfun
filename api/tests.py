from django.test import TestCase

from .models import Post, User


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="test", description="destest", image="", )

    def title_title_content(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.title, "test")


class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(username='test',name="test",password="test",phone="09136978682")

    def name_name_content(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.name, "test")
                
                
