from django.test import TestCase
from django.urls import resolve
from note.views import  home_page
from note.models import Name,Item
class liveViewTest(TestCase):
    def test_first_returns_correct_html(self):#测试首页模板
        respose = self.client.get('/')
        self.assertTemplateUsed(respose, 'home.html')  # 检测响应是用哪个模板渲染的

    def test_can_Skip_a_POST_request(self):  # 测试首页post请求响应是否跳转到相应界面
        response = self.client.post('/', data={'name_text': 'cmy'})
        self.assertRedirects(response, '/note/cmy')  # 测试重定向

    def test_can_saved_first_post(self):#测试首页填的数据是否正确填入数据库
        response = self.client.post('/', data={'name_text': 'cmy'})
        new_name=Name.objects.first()
        self.assertEqual(new_name.name,'cmy')
        response = self.client.post('/', data={'name_text': 'cmy'})#测试输入同样的名字会不会保存到数据库
        name_list=Name.objects.all()
        self.assertEqual(name_list.count(),1)

    def test_note_returns_correct_html(self):#测试note模板
        Name.objects.create(name='cmy')
        respose = self.client.get('/note/cmy')
        self.assertTemplateUsed(respose, 'node.html')  # 检测响应是用哪个模板渲染的

    def test_second_returns_correct_html(self):  # 测试url参数是否传入视图模板,以及正确反应
        Name.objects.create(name='cmy')
        respose = self.client.get('/note/cmy')#访问创建好名字的node模板
        self.assertIn('cmy', respose.content.decode())
        respose = self.client.get('/note/cmy1')  # 访问没有创建好名字的node模板
        self.assertNotIn('cmy1', respose.content.decode())
        self.assertRedirects(respose, '/')

    def test_second_saved_post(self):#测试note页端的存储情况
        Name.objects.create(name='cmy')
        response = self.client.post('/note/cmy', data={'list_text': 'test1'})
        self.assertEqual(Item.objects.count(), 1)  # 测试在前端填写的有没有正确的填入数据库
        new_item = Item.objects.first()
        self.assertEqual('test1', new_item.text)

    def test_Item_display_correct(self):#测试访问item是否正常显示
        Name.objects.create(name='cmy')
        respose = self.client.get('/note/cmy')#没有存储事例前访问
        self.assertNotIn('1:test1', respose.content.decode())
        response = self.client.post('/note/cmy', data={'list_text': 'test1'})
        self.assertIn('1:test1', response.content.decode())#存储完,POST请求
        respose = self.client.get('/note/cmy')#存储完 GET请求
        self.assertIn('1:test1', respose.content.decode())

    class TestModel(TestCase):  # 测试数据库
        def test_saving_and_retrieving_items(self):  # 测试数据库是否正常存储
            input_name='cmy'
            saved_Name = Name.objects.create(name=input_name)
            Item.objects.create(name=saved_Name,text='test1')
            Item.objects.create(name=saved_Name, text='test2')
            item=saved_Name.item_set.all
            first_saved=item[0]
            second_saved=item[2]
            self.assertEqual(first_saved.text, 'test1')  # 测试Item保存数据是否成功
            self.assertEqual(second_saved.text, 'test2')
            saved_Name_list = Name.objects.first()#测试Name表第一个保存的数据是否成功
            self.assertEqual(saved_Name, saved_Name_list)
# Create your tests here.
