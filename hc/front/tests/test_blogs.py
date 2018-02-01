<<<<<<< HEAD
# from hc.test import BaseTestCase
# from hc.front.models import Blog_post, Category
# from django.shortcuts import reverse


# class BlogTest(BaseTestCase):
#     def setUp(self):
#         self.client.login(username="alice@example.org", password="password")

#         self.test_category = Category.objects.create(
#             name='Tech Category'
#         )
#         self.test_post = Blog_post.objects.create(
#             title='Python Blog',
#             content='This is a blog on python.',
#             category=self.test_category
#         )

#     def test_landing_page_returns_all_posts(self):
#         response = self.client.get(reverse('hc-blog'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'front/blog_posts.html')
    
#     def test_view_one_blog(self):
#         response = self.client.get(reverse('hc-read_blog'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'front/read_blog.html')
        
#     def test_create_blog(self):
#         response = self.client.get(reverse('hc-create_blog'))        
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'front/create_blog.html')
#         form = {
#             'title':'Html Blog',
#             'content':'This is a blog on html.',
#             'category':self.test_category
#         }
#         response_one = self.client.post(reverse('hc-create_blog'), form)
#         self.assertEqual(response_one.status_code, 200)
=======
from hc.test import BaseTestCase
from hc.front.models import Blog_post, Category
from django.shortcuts import reverse
from django.utils import timezone

class BlogTest(BaseTestCase):
    def setUp(self):
        super(BlogTest, self).setUp()
        self.client.login(username="alice@example.org", password="password")
        self.category = Category(name='Tech')
        self.category.save()
        self.blog = Blog_post(title='Python',content='This is a blog on python', 
                             category = self.category, published=timezone.now())
        self.blog.save()
   

    def test_create_category(self):
        """Test to check if categories are created"""
        url = reverse('hc-create_blog')
        data = {'category': ['Design'], 'new_category': ['']}
        response = self.client.post(url, data)
        query_category = Category.objects.get(name="Design")
        self.assertEqual('Design', query_category.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'front/create_blog.html')


    def test_create_blog(self):
        """Test to check if blogs are created"""
        url = reverse('hc-create_blog')
        data = {'category_name': ['Tech'], 'title': ['Html'], 'content': ['This is a blog on html'], 'create_blog': ['']}
        response = self.client.post(url, data)
        query_blog = Blog_post.objects.get(title="Html")
        self.assertEqual('Html', query_blog.title)
        self.assertEqual(response.status_code, 302)


    def test_home_page_returns_all_blogs(self):
        """Test to check if home page returns all blogs"""
        response = self.client.get(reverse('hc-blog', kwargs={'filter_by':0}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'front/blog_posts.html')

>>>>>>> [Fix:#153727855]Improved UI and added edit and delete feature to blog posts
