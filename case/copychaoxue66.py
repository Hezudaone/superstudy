# coding=utf-8

from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.by import By


class a(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get('https://s.wanxue.cn/sls/stemUser')
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)

    def test_copy(self):
        username=self.driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[1]/td[2]/span/span/input')
        password=self.driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/span/span/input')

        username.clear()
        username.send_keys('diyao')
        password.clear()
        password.send_keys('dy123456')
        #角色
        self.driver.find_element_by_xpath('//*[@id="roleID"]/span/span/span[2]/span').click()
        self.driver.find_element_by_xpath('//*[@id="15$cell$1"]/div/div/span[2]/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[4]/td/input').click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element_by_xpath('/html/body/div[4]/ul/li[22]/a').click()
        self.driver.find_element_by_xpath('//*[@id="key$text"]').send_keys('chaoxue66')
        chaxun=self.driver.find_element_by_xpath('//*[@id="center"]/div[2]/div/div/div[1]/div/div/div[2]/div/table/tbody/tr/td[2]/a/span')
        chaxun.click()
        # 勾选复选框
        time.sleep(3)
        #self.driver.findElement(By.xpath(".//label[@id='agree_to_terms_label']")).click()

        #element = self.driver.find_element_by_xpath('//*[@id="user"]/div/div[2]/div[4]/div[2]/div/table')
        #self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element_by_xpath('//*[@id="1$cell$1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="buttons"]/a[4]/span').click()
        time.sleep(3)
        frame1 = self.driver.find_element_by_xpath('//*[@id="mini-31"]/div/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(frame1)
        self.driver.find_element_by_xpath('//*[@id="targetUserNameS$text"]').send_keys('wx98')
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/a/span').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="mini-7$0"]').click()
        self.driver.find_element_by_xpath('//*[@id="copyButton"]/span').click()






    @classmethod
    def tearDownClass(self):
        time.sleep(50)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()