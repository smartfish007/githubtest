from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time
import unittest
class Myunittest(unittest.TestCase):
   def setUp(self):#测试开始前运行
      self.browser=webdriver.Firefox()
   def tearDown(self):#测试开始后运行
      self.browser.quit()
   def test_can_start_a_list_and_retrieve_it_later(self):#测试的主要方法
      self.browser.get("http://127.0.0.1:8000")
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
      time.sleep(1)
      input = self.browser.find_element_by_id("id_new_item")
      input.send_keys('Buy2')  # 填入文本框
      input.send_keys(Keys.ENTER)  # 回车
      time.sleep(1)
      table=self.browser.find_element_by_id('id_list_table')
      rows=table.find_elements_by_tag_name('tr')
      self.assertIn('16:Buy1',[row.text for row in rows])
      self.assertIn('17:Buy2', [row.text for row in rows])
      self.fail("Finish test")#提前结束测试
if __name__=='__main__':
   unittest.main(warnings='ignore')#启动unittest测试程序

