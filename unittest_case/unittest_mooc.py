# coding=utf-8
import time
import unittest
from selenium import webdriver


class Mooc_wanxue_cn(unittest.TestCase):



        @classmethod
        def setUpClass(self):
                self.driver = webdriver.Chrome()
                self.driver.get('https://mooc.wanxue.cn')
                self.driver.maximize_window()
                self.driver.implicitly_wait(2)

        @classmethod
        def tearDownClass(self):
                time.sleep(5)
                self.driver.close()

        # 登录
        def test_a_login(self, username='stu101', password='123456'):
                self.driver.find_element_by_xpath('/html/body/div[6]/p/a').click()
                self.driver.find_element_by_xpath('//*[@id="categorylistLogout"]/div[1]/div/ul/li[3]/a').click()
                self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
                self.driver.find_element_by_xpath('//*[@id="slsLoginPwd"]').send_keys(password)
                self.driver.find_element_by_xpath('//*[@id="loginfrom"]/div[3]/input[1]').click()

        # 学习中心
        def test_b_xuexizhongxin(self):
                self.driver.get('https://mooc.wanxue.cn/sls/jwcoursemodule/queryList')
                self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div/div[2]/div[2]/dl/dd/a').click()
                self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]/a').click()
                self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[3]/a').click()
                self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[4]/a').click()
                self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[1]/a').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="contentX"]/div[2]/div/ul[2]/li/a/span').click()
                self.driver.find_element_by_xpath('//*[@id="replaybtn"]').click()
                time.sleep(4)

                self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/a[2]').click()

                self.driver.find_element_by_xpath('//*[@id="contentX"]/div[1]/ul/li[2]/a').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[2]/div/a[1]').click()

        # 直播课堂
        def test_c_zhiboketang(self):
                self.driver.get('https://mooc.wanxue.cn/sls/liveVideoView/queryLivePublicLesson')
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/dl[4]/dd[1]/a').click()

                all_hand = self.driver.window_handles
                self.driver.switch_to_window(all_hand[1])
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="lessonState"]/tr/td[4]/a').click()
                time.sleep(4)
                all_hand = self.driver.window_handles
                time.sleep(1)
                self.driver.close()
                self.driver.switch_to_window(all_hand[2])
                self.driver.close()
                self.driver.switch_to_window(all_hand[0])
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/dl[1]/dd[1]/a').click()
                all_hand = self.driver.window_handles
                self.driver.switch_to_window(all_hand[1])
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to_window(all_hand[0])

        # 职业测评
        def test_d_zhiyeceping(self):
                self.driver.get('http://mbti-kds.wanxue.cn/toCreatePass.htm?name=stu101')
                time.sleep(2)

        # 创业资讯
        def test_e_chuangyezixun(self):
                self.driver.get('https://mooc.wanxue.cn/sls/informationCyzx/index')
                self.driver.find_element_by_xpath('//*[@id="cyzx"]').send_keys('武汉')
                self.driver.find_element_by_xpath(
                        '/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/span/span/a').click()
                self.driver.find_element_by_link_text('武汉大学把创新创业教育融入人才培养全过程').click()
                all_hand = self.driver.window_handles
                self.driver.switch_to_window(all_hand[1])
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to_window(all_hand[0])

        # 企业通识
        def test_f_qiyetongshi(self):
                self.driver.get('https://mooc.wanxue.cn/sls/informationCyzs/index')
                self.driver.find_element_by_xpath('//*[@id="cyzs"]').send_keys('总公司')
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/span/span/a').click()
                self.driver.find_element_by_link_text('总公司、分公司、母公司与子公司的联系与区别').click()
                all_hand = self.driver.window_handles
                self.driver.switch_to_window(all_hand[1])
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to_window(all_hand[0])

        # 精准求职
        def test_g_jingzhunqiuzhi(self):
                self.driver.get('https://mooc.wanxue.cn/sls/jwcoursemodule/moocRecruit')
                self.driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]').click()
                self.driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[3]').click()
                self.driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[1]').click()
                self.driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]').click()

if __name__ == '__main__':
    unittest.main()