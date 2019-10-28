from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
class Myunittest(LiveServerTestCase):
   def setUp(self):#测试开始前运行
      self.browser=webdriver.Firefox()
   def tearDown(self):#测试开始后运行
      self.browser.quit()
   def test_correct_satrt_correct_return(self):#测试首页输入后跳转，增加事例，不同用户操作是否正常
       #测试首页提交post后的提交是否正常
       self.browser.get(self.live_server_url)
       self.assertIn("Notepad Rigister", self.browser.title)  # 断言
       header_text = self.browser.find_element_by_tag_name('h1').text
       self.assertIn('User Notepad', header_text)
       input = self.browser.find_element_by_id("id_input_name")
       self.assertEqual(
           input.get_attribute('placeholder'),  # 获取属性里的值
           'Enter name'
       )
       input.send_keys('cmy1')  # 填入文本框
       input.send_keys(Keys.ENTER)  # 回车
       time.sleep(10)
       self.wait_for_first_to_second('cmy1')
       women_lists_url = self.browser.current_url#测试重定向后的url
       self.assertRegex(women_lists_url, "/note/cmy1")
       #self.fail("Finish test1")  # 提前结束测试,测试首页跳转成功

       #测试存储事例是否成功
       input = self.browser.find_element_by_id("id_input_item")
       self.assertEqual(
           input.get_attribute('placeholder'),  # 获取属性里的值
           'Enter a new item'
       )
       input.send_keys('women')  # 填入文本框
       input.send_keys(Keys.ENTER)  # 回车
       self.wait_for_row_in_list_table('1:women')
       #self.fail("Finish test2")  # 提前结束测试,测试用户增加事例成功

       #测试第二个用户访问有没有第一个用户留下的痕迹
       self.browser.quit()
       self.browser = webdriver.Firefox()
       self.browser.get(self.live_server_url)
       input = self.browser.find_element_by_id("id_input_name")
       self.assertEqual(
           input.get_attribute('placeholder'),  # 获取属性里的值
           'Enter name'
       )
       input.send_keys('cmy2')  # 填入文本框
       input.send_keys(Keys.ENTER)  # 回车
       self.wait_for_first_to_second('cmy2')
       page_text = self.browser.find_element_by_tag_name('body').text
       self.assertNotIn(page_text, 'women')#上一个用户的操作是否留下痕迹
       women_lists_url = self.browser.current_url  # 测试重定向后的url
       self.assertRegex(women_lists_url, "/note/cmy2")
       #self.fail("Finish test3")  # 提前结束测试,测试不同用户操作不同显示成功
   def wait_for_first_to_second(self, row_text):#等待首页跳转
       start_time = time.time()
       max_wait = 5
       while True:
           try:  # 第一个出口测试成功
               windows = self.browser.window_handles
               self.browser.switch_to.window(windows[-1]) # 获取窗口句柄
               name = self.browser.find_element_by_tag_name('h1').text
               self.assertEqual(row_text,name)
               return
           except(AssertionError, WebDriverException) as e:
               if time.time() - start_time > max_wait:  # 第二个出口测试失败，返回失败原因
                   raise e
               time.sleep(0.5)
   def wait_for_row_in_list_table(self, row_text):#等待添加事例
       start_time = time.time()
       max_wait = 5
       while True:
           try:  # 第一个出口测试成功
               table = self.browser.find_element_by_id('id_list_table')
               rows = table.find_elements_by_tag_name('tr')
               self.assertIn(row_text, [row.text for row in rows])
               return
           except(AssertionError, WebDriverException) as e:
               if time.time() - start_time > max_wait:  # 第二个出口测试失败，返回失败原因
                   raise e
               time.sleep(0.5)
