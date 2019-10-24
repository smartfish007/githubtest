from django.test import TestCase
from django.urls import resolve
from lists.views import  home_page
from lists.models import Item
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
        self.assertEqual(Item.objects.count(),1)#测试在前端填写的有没有正确的填入数据库
        new_item=Item.objects.first()
        self.assertEqual('A new list item',new_item.text)
        self.assertEqual(response.status_code, 302)
        #self.assertIn('A new list item',response.content.decode())
        #self.assertTemplateUsed(response, 'home.html')  # 检测响应是否同一个模板渲染的
    def test_displays_all_list_items(self):
        Item.objects.create(text='test1')
        Item.objects.create(text='test2')
        response = self.client.post('/')
        self.assertIn('test1', response.content.decode())
        self.assertIn('test2',response.content.decode())
class ItemModel(TestCase):#测试数据库
    def test_saving_and_retrieving_items(self):#测试数据库是否正常存储
        first_item=Item()
        first_item.text='first item'
        first_item.save()
        second_item=Item()
        second_item.text='second item'
        second_item.save()
        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)#测试保存数量
        first_saved=saved_items[0]
        second_saved=saved_items[1]
        self.assertEqual(first_saved.text,'first item')#测试保存的内容
        self.assertEqual(second_saved.text,'second item')
# Create your tests here.
