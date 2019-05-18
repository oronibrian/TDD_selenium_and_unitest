from django.test import TestCase
from django.urls import reverse,resolve
from post.views import PostList,PostDetail


class TestUrls(TestCase):


	def test_post_list_url_resolver(self):
		url=reverse('home')
		self.assertEquals(resolve(url).func.view_class,PostList)