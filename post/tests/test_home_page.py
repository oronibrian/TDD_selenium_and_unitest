from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from django.utils import timezone
from post.models import Post



class TestBlogPost(TestCase):

	def setUp(self):
		Post.objects.create(title="blog post title", content="Blog content", created_on=timezone.now())


	def test_text_content(self):
		post = Post.objects.get(id=1)
		expected_object_name = f'{post.title}'
		self.assertEquals(expected_object_name, 'blog post title')

	def test_post_list_view(self):
		response = self.client.get(reverse('post_detail',args=['blog_post_title']))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'blog post title')
		self.assertTemplateUsed(response, 'post_detail.html')



