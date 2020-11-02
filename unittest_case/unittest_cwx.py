# coding=utf-8

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class C_wanxue_cn(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.driver.get('https://c.wanxue.cn')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()

    def test_a_login(self, user='wx98', password='abc123'):
        '''使用wx98登录'''
        self.driver.find_element_by_xpath('/html/body/div[6]/p/a').click()
        self.driver.find_element_by_xpath('//*[@id="categorylistLogout"]/div[1]/div/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(user)
        self.driver.find_element_by_xpath('//*[@id="slsLoginPwd"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginfrom"]/div[5]/input[1]').click()
        time.sleep(1)
        flag = self.driver.find_element_by_xpath('//*[@id="person"]/a').text
        print(flag)
        self.assertIn('wx98', flag, msg='wx98登录失败')

    def test_b_intellect_study(self):

        ''' 智能课程学习 '''
        # 进入数学三
        self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[2]/div[4]/div[4]/div[7]/dl/dd/a').click()
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

    def test_c_feitongkao(self):
        '''非统考视频'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[2]/div[4]/div[5]/div[7]/dl/dd/a').click()
        self.driver.find_element_by_xpath('//*[@id="regionName_1"]/div[9]/div[1]/dl/dd/a').click()
        time.sleep(2)
        try:# //*[@id="replaybtn"]
            self.feitongkao_xunhuan('/html/body/div[4]/div[3]/div[1]/div/ul[1]/li[1]/a[1]')


        except:
            print('非统考失败')

    def feitongkao_xunhuan(self, xpathName):
        '''非统考视频播放操作'''
        self.driver.find_element_by_xpath(xpathName).click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="replaybtn"]').click()
        time.sleep(5)
        self.driver.back()
        time.sleep(2)

    def test_d_xiaobenkecheng(self):

        '''校本课程'''
        self.driver.get('https://c.wanxue.cn/sls/jwcoursemodule/getCourseList')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="c_type"]/li[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="c_type"]/li[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="c_type"]/li[4]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="c_type_first"]').click()
        ####未完####

    def test_e_live_class(self):

        '''直播课堂'''
        self.driver.get('https://c.wanxue.cn/sls/liveVideoView/queryLivePublicLesson')
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
        time.sleep(2)

    # 直播课堂--直播课
    def zhiboke(self):
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/h2/p/a[2]').click()
        self.driver.find_element_by_link_text('2021届考研数学基础阶段课程-高数上（二期）').click()

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

    # 职业规划 ??????
    def test_f_zhiyeguihua(self):
        '''职业规划'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/ul/li[4]/a[2]').click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])

        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        time.sleep(2)

    # 科研转化
    def test_g_keyanzhuanhua(self):

        '''科研转化'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/ul/li[5]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[2]/a/img').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/ul/li[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/p/a').click()
        time.sleep(2)

    # 求职招聘
    def test_h_qiuzhizhaopin(self):

        '''求职招聘'''
        self.driver.get('https://c.wanxue.cn/sls/category/gourl?begin=findjob&end=findjob-hunter')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[2]/a').click()
        time.sleep(2)

    # 创业实训
    def test_i_chuangyeshixun(self):

        '''创业实训'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/ul/li[7]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/a').click()
        time.sleep(2)

    # 创业活动
    def test_j_chuangyehuodong(self):

        '''创业活动'''
        self.driver.get('https://c.wanxue.cn/sls/informacationCommon/index?beginurl=information&endurl=indexCyhd')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="chuangyehd"]/ul[1]/li[2]/a/img').click()

        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])

        self.driver.find_element_by_xpath('//*[@id="d_btn"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[5]/input[2]').click()
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        time.sleep(2)

    # 创客矩阵   ?
    def test_k_chuangkejuzhen(self):

        '''创客矩阵'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/ul/li[9]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[4]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[7]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/ul[7]/li[3]/a/img').click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 创业项目  ?
    def test_l_chuangyexiangmu(self):

        '''创业项目'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/ul/li[10]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/ul/li/a/img').click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/ul/li[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/ul/li[3]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/p/a').click()
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        time.sleep(2)

        # 创业资讯
    def test_m_chuangyezixun(self):

        '''创业资讯'''
        self.driver.get('https://c.wanxue.cn/sls/informationCyzx/index')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="cyzx"]').send_keys('双创')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/span/span/a').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('切实让“双创”政策落地生根').click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        time.sleep(2)

    # 创业知识
    def test_n_chuangyezhishi(self):

        '''创业知识'''
        self.driver.get('https://c.wanxue.cn/sls/informationCyzs/index')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="cyzs"]').send_keys('创造')
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/span/span/a').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('创新并不意味着新潮，而在于创造').click()
        all_hand = self.driver.window_handles
        self.driver.switch_to_window(all_hand[1])
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window(all_hand[0])
        time.sleep(2)

    # 创业书库
    def test_o_Super_book(self):

        '''创业书库'''
        self.driver.get('https://c.wanxue.cn/sls/superbook/getHtml')
        time.sleep(2)
        self.in_book('//*[@id="cy"]/div[1]/dl[2]/dd[1]')

    # 重复进入书籍内
    def in_book(self, book_element):
        self.driver.find_element_by_xpath(book_element).click()
        self.driver.find_element_by_xpath('//*[@id="next_page_button"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="prev_page_button"]').click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    # 创业大数据
    def test_p_chuangyedashuju(self):

        '''创业大数据'''
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/ul/li[14]/a[2]').click()

        time.sleep(2)

        self.dashuju('/html/body/div[2]/div/div[2]/div[1]/ul/li[2]/a')
        time.sleep(1)
        self.dashuju('/html/body/div[2]/div/div[2]/div[2]/ul/li[3]/a')

        self.dashuju('/html/body/div[2]/div/div[2]/div[3]/ul/li[2]/a')

        self.dashuju('/html/body/div[2]/div/div[2]/div[3]/ul/li[6]/a')

        time.sleep(2)
        self.driver.get('https://c.wanxue.cn/sls/category/queryList')

    def dashuju(self, element):
        self.driver.find_element_by_xpath(element).click()

