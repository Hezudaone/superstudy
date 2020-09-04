# coding=utf-8

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys


class S_wanxue_cn(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://s.wanxue.cn')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()

    def test_a_login(self, user='wx98', password='abc123'):
        '''使用wx98登录''' #
        self.driver.find_element_by_xpath('//*[@id="categorylistLogout"]/div[1]/div/ul/li[4]/a').click()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(user)
        self.driver.find_element_by_xpath('//*[@id="slsLoginPwd"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginfrom"]/div[5]/input[1]').click()
        time.sleep(1)
        flag = self.driver.find_element_by_xpath('//*[@id="person"]/a').text
        print(flag)
        self.assertIn('wx98', flag, msg='wx98登录失败')

    #
    def test_b_intellect_study(self):
        '''智能课程学习'''
        # 进入政治课程
        # self.driver.find_element_by_xpath('/html/body/div[10]/div[3]/div[2]/div[4]/div[6]/div[2]/dl/dd/a').click()
        # 进入数学1
        self.driver.find_element_by_xpath('/html/body/div[10]/div[3]/div[2]/div[4]/div[6]/div[5]/dl/dd/a').click()
        # 开始学习
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[1]/h4[2]').click()  # 进度管控
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/h4[3]').click()  # 学习报告
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[1]/h4[4]').click()  # 动态学习规划
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/h4[5]').click()  # 错题通练
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/h4[6]').click()  # 题目收藏夹
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/h4[1]').click()  # 课程学习
        # 阶段选择
        self.jieduan_for()


    # 阶段选择
    def jieduan_for(self):
        inex = 1
        for i in range(7):  #
            self.driver.find_element_by_xpath('//*[@id="stageIndex' + str(inex) + '"]/a').click()
            # 判断该阶段是 已完成 或者 未完成
            try:
                stast_element = self.driver.find_element_by_link_text('超级智能学习 > 开始')
                stast_element.click()
                # 智能课程循环
                flag = self.coures_for()
                if flag:
                    continue
                break
            except:
                # 该阶段学完,另外选阶段
                inex += 1

    # 智能课程学习循环
    def coures_for(self):
        for x in range(22):

            try:
                time.sleep(3)

                tub_element = self.driver.find_element_by_xpath('//*[@id="nextName"]/span[1]').text

            except:

                # 习题组页面无法获取到下一步按钮元素,报错后答题提交   #之后写成随机答题
                element = self.driver.find_element_by_tag_name("body")
                element.send_keys(Keys.ALT, 's')
                try:
                    self.driver.find_element_by_xpath('//*[@id="submietStemDisable"]').click()
                except:
                    self.driver.find_element_by_link_text('返回学习导图').click()
                    return True
                continue

            # 教材
            if '课程' in tub_element:
                # 下一页
                self.driver.find_element_by_xpath('//*[@id="next_page_button"]').click()
                # 下一步
                self.driver.find_element_by_xpath('//*[@id="nextName"]/span[1]').click()
            # 视频
            elif '习题组' in tub_element:
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="replaybtn"]').click()
                time.sleep(4)
                # 下一步
                self.driver.find_element_by_xpath('//*[@id="nextName"]/span[1]').click()
            # 解析
            elif '学习任务包' in tub_element:
                try:
                    # 获取解析标识
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[3]')
                    time.sleep(3)
                    # 下一步
                    self.driver.find_element_by_xpath('//*[@id="nextName"]/span[1]').click()
                    #
                    self.driver.find_element_by_link_text('立即开始').click()
                except:
                    # 人工指导
                    self.driver.find_element_by_xpath('//*[@id="nextName"]/span[1]').click()
                    self.driver.find_element_by_xpath('/html/body/div[6]/div/a[1]').click()

    def test_c_feitongkao_av(self):
        '''全国非统考专业课'''
        self.driver.get('https://s.wanxue.cn/sls/notUnifiedExam/getContent')
        self.driver.find_element_by_xpath('//*[@id="regionName_1"]/div[2]/div[2]/dl/dd/a').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/div/ul[2]/li[1]/a[1]').click()

        self.driver.find_element_by_xpath('//*[@id="replaybtn"]').click()
        time.sleep(3)
        self.driver.back()
        flag = self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/h2/span').text
        self.assertIn('列表', flag, msg='全国非统考专业课,视频播放失败')

    def test_d_liankao(self):
        '''资料中心-联考/非联考'''
        self.driver.get('https://s.wanxue.cn/sls/nonDownload/queryRegionAll')
        self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[1]/div[2]/div[1]/a/div/p').click()

        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        self.driver.find_element_by_xpath('//*[@id="type57"]/dl[1]/dd[1]/a').click()
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        # 非联考
        self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div/div[2]/div[3]/div/ul/li[8]/ul/li[2]/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="projectName"]').send_keys('力学')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="proName105"]/li[1]/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="proName105"]/li[2]/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="proName105"]/li[3]/ul/li/a').click()


        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="type57"]/dl[5]/dd[1]/a').click()

        flag = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/ul/li[3]/a').text
        self.assertIn('订单', flag, msg='资料中心异常')
        time.sleep(4)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])


    def test_e_chaojishuk(self):
        '''超级书库'''
        self.driver.get('https://s.wanxue.cn/sls/superbook/getHtml')
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('//*[@id="yyy"]/div[1]/dl[1]').click()

        all_hand = self.driver.window_handles
        time.sleep(1)
        self.driver.switch_to_window(all_hand[-1])

        self.driver.find_element_by_xpath('//*[@id="next_page_button"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="prev_page_button"]').click()
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])

    def test_f_zonghezixun(self):
        '''综合资讯'''
        self.driver.get('https://s.wanxue.cn/sls/information/index')
        self.driver.find_element_by_xpath('//*[@id="t1"]/tbody/tr[1]/td[2]/a').click()
        time.sleep(2)
        self.all_hand = self.driver.window_handles
        time.sleep(2)
        self.driver.switch_to_window(self.all_hand[-1])

        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(self.all_hand[0])

    def test_g_wodekecheng(self):
        '''我的课程'''
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/ul/li[6]/a[2]').click()
        time.sleep(2)
        self.my_course_for('//*[@id="ul_12"]/li[2]/a/img')

        # 最近学习
        self.driver.find_element_by_xpath('//*[@id="coursePage-study"]').click()
        self.driver.find_element_by_xpath('//*[@id="courseRecordstudy"]/tr[1]/td[4]/a').click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(4)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        # 激活学习项目
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="activePage"]').click()
        time.sleep(2)
        # 修改密码
        self.driver.find_element_by_xpath('//*[@id="pwdPage"]').click()
        self.up_pwd('abc123', 'wanxue456', 'wx98')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[2]/ul/li[6]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pwdPage"]').click()
        self.up_pwd('wanxue456', 'abc123', 'wx98')

    # 我的课程-修改密码
    def up_pwd(self, oldPwd, newPwd, username):
        self.driver.find_element_by_xpath('//*[@id="oldPwd"]').send_keys(oldPwd)
        self.driver.find_element_by_xpath('//*[@id="newPwd"]').send_keys(newPwd)
        self.driver.find_element_by_xpath('//*[@id="reNewPwd"]').send_keys(newPwd)
        self.driver.find_element_by_xpath('//*[@id="use3"]/div/p[5]/input').click()  #
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        self.test_a_login(username, newPwd)

    # 我的课程-循环课程
    def my_course_for(self, element):

        time.sleep(2)
        self.driver.find_element_by_xpath(element).click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        time.sleep(2)

    #
    def test_h_zhiboke(self):
        '''直播课堂'''
        self.driver.get('https://s.wanxue.cn/sls/liveVideoView/queryLivePublicLesson')
        #self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[2]/ul/li[7]/a[2]').click()
        self.gongkaike()
        time.sleep(2)
        try:
            self.zhiboke()
        except:
            pass

# 直播课堂---公开课 /html/body/div[11]/div/div[2]/ul/li[7]/a[2]
    def gongkaike(self):

        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/a/img').click()
        time.sleep(3)
        self.driver.back()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="101"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="publicUl2"]/li[5]/dl/dd[3]/a').click()
        time.sleep(6)
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(1)
        self.driver.switch_to_frame('video')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/div[1]/i').click()
        time.sleep(8)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])

    # 直播课堂--直播课  //*[@id="body"]/div[2]/div[2]/div/div[2]/div[1]/ul/li[2]/a/div[2]/div
    def zhiboke(self):
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/h2/p/a[2]').click()
        self.driver.find_element_by_link_text('2021届考研数学基础阶段课程-高数上（二期）').click()
        # self.driver.find_element_by_xpath('//*[@id="ll"]/dl[1]/dd[1]/a').click()#2021届考研数学基础阶段课程-线代(二期)
        time.sleep(2)
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="lessonState"]/tr[4]/td[4]/a').click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[2])
        time.sleep(8)

        self.driver.close()
        self.driver.switch_to_window(all_hand[1])
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])

    def test_i_fudaojuzhen(self):
        '''辅导矩阵'''
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/li[8]/a[2]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul[1]/li[3]/span[1]/img').click()
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul[1]/li[5]/span[1]/img').click()
        self.driver.back()

    def test_j_baokaojuece(self):
        '''报考决策'''
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/ul/li[9]/a[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="provinceid"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="collegeid"]/option[14]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/form/input').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/form/a/span').click()
        self.baokaoyixiang_edit('//*[@id="one2"]/a', '//*[@id="33"]/a', '//*[@id="two7"]/a')

    # 我的报考意向
    def baokaoyixiang_edit(self, a, b, c):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/a[1]/img').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(a).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(b).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(c).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dosubmit"]').click()
        time.sleep(2)

    def test_k_xianxia(self):
        '''线下解题'''
        self.driver.get('https://s.wanxue.cn/sls/category/queryList')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[2]/ul/li[5]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/ul/li[2]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/ul/li[1]/a/div/img').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/ul/li[4]/a/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right_content"]/div/div[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/a[1]/img').click()



if __name__ == '__main__':
    unittest.main()




