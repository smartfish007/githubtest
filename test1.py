from selenium import webdriver
import unittest
class Myunittest(unittest.TestCase):
   def setUp(self):#测试开始前运行
      self.browser=webdriver.Firefox()
   def tearDown(self):#测试开始后运行
      self.browser.quit()
   def test_can_start_a_list_and_retrieve_it_later(self):#测试的主要方法
      self.browser.get("http://127.0.0.1:8000/save_data")
      self.assertIn("数据库操作",self.browser.title)#断言
      self.fail("Finish test")#提前结束测试
if __name__=='__main__':
   unittest.main(warnings='ignore')#启动unittest测试程序

