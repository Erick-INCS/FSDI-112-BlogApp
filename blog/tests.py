from django.contrib.auth import  get_user_model
from django.test import  TestCase
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):
    """
    docstring
    """
    def setUp(self):
        """
        docstring
        """
        self.user = get_user_model().objects.create_user(
            username='user',email='mail.conm', password='...'
        )

        self.post = Post.objects.create(
            title="title",body='nice body', author=self.user
        )

    def test_string_representation(self):
        """
        docstring
        """
        post = Post(title='title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        """
        docstring
        """
        self.assertEqual(f'{self.post.title}', 'title')
        self.assertEqual(f'{self.post.author}', 'user')
        self.assertEqual(f'{self.post.body}', 'nice body')


    def test_post_list_view(self):
        """
        docstring
        """
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "post_detail.html")



        