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
   def test_can_start_a_list_and_retrieve_it_later(self):#测试的主要方法
      self.browser.get(self.live_server_url)
      self.assertIn("To-Do lists",self.browser.title)#断言
      header_text=self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Hello World',header_text)
      input=self.browser.find_element_by_id("id_new_item")
      self.assertEqual(
         input.get_attribute('placeholder'),#获取属性里的值
         'Enter a to-do item'
      )
      input.send_keys('Buy1')#填入文本框
      input.send_keys(Keys.ENTER)#回车
      self.wait_for_row_in_list_table('1:Buy1')
      input = self.browser.find_element_by_id("id_new_item")
      input.send_keys('Buy2')  # 填入文本框
      input.send_keys(Keys.ENTER)  # 回车
      self.wait_for_row_in_list_table('2:Buy2')
   def  wait_for_row_in_list_table(self,row_text):
      start_time=time.time()
      max_wait=5
      while True:
         try:#第一个出口测试成功
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])
            return
         except(AssertionError,WebDriverException) as e:
            if time.time()-start_time>max_wait:#第二个出口测试失败，返回失败原因
               raise e
            time.sleep(0.5)
         #AssertionError找到表格没有找到想要的行
         #WebDriverException页面未加载或者没有找到表格


