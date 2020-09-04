# coding=utf-8
import random

from selenium import webdriver
import time


driver = webdriver.Chrome()
# 打开s.wanxue.cn
driver.get("https://s.wanxue.cn")
#登录
driver.find_element_by_xpath("//*[@id='categorylistLogout']/div[1]/div/ul/li[4]/a").click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys("15230215418")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="slsLoginPwd"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="loginfrom"]/div[5]/input[1]').click()
time.sleep(2)
#选择atst课程
driver.find_element_by_xpath('/html/body/div[10]/div[3]/div[2]/div[4]/div[5]/div/dl/dd/a').click()
time.sleep(2)


f = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[3]')
kf = f.find_elements_by_tag_name('div')
#循环点击课程
for k in kf:
    time.sleep(3)
    k.click()


    w = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[1]/ul')
    x = w.find_elements_by_tag_name('li')
    print(x)
    #   循环目录
    for b, num in zip(x, range(1, len(x))):

        b.click()

        try:
            Wei = driver.find_element_by_xpath('//*[@id="' + str(num) + '"]/div[1]/div[1]/div/h3[1]/span')
        except:
            Wei = driver.find_element_by_xpath('//*[@id="' + str(num) + '"]/div[1]/div[1]/div/h3/span')

        #  判断目录下的章节是否是已学习状态
        print(Wei.text)
        if Wei.text == '未完成':
            f = driver.find_element_by_xpath('//*[@id="1"]/div[1]/div[1]/div')
            z = f.find_elements_by_tag_name('li')

            #  状态为“未完成”则循环点击学习该章节下的内容
            for xz in z:
                xz.click()
                #   切换窗口
                nowhandle = driver.current_window_handle  # 获取当前窗口
                handles = driver.window_handles  # 获取所有窗口
                for handle in handles:  # 切换窗口
                    if handle != driver.current_window_handle:
                        print('switch to ', handle)
                        driver.switch_to.window(handle)
                        print(driver.current_window_handle)  # 输出当前窗口句柄


    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/a[1]/img').click()



