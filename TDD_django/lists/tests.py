from django.test import TestCase
from django.urls import resolve
from lists.views import  home_page
from django.template.loader import render_to_string
class HomepageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # 测试网站url（这里是网站跟路径）的关系是否如愿
        self.assertEqual(found.url_name, 'home')
        self.assertEqual(found.func, home_page)  # 看看是否能找到名为home_page的函数
    def test_home_page_returns_correct_html(self):
        respose=self.client.get('/')
        html=respose.content.decode('utf8')
        self.assertTemplateNotUsed(respose,'home.html')#检测响应是用哪个模板渲染的
# Create your tests here.
