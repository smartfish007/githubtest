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
        self.assertTemplateUsed(respose,'home.html')#检测响应是用哪个模板渲染的
    def test_can_save_a_POST_request(self):#测试post请求响应,是否返回文本框的数据
        response=self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response, 'home.html')  # 检测响应是否同一个模板渲染的
# Create your tests here.
