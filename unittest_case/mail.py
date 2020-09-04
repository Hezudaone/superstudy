# coding=utf-8
import os
import yagmail
import datetime

sender = '1244783557@qq.com'
password = 'nlxtygnxkpwogjdb'
res = '1244783557@qq.com'
yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', smtp_ssl=True)


root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
report_dir = root_dir + '/report'
now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(now)
#str1 = report_dir+'/'+filename+'.html'
str1 = report_dir+'/'+'2020-08-04 10_17_47.html'



#contents = ['这是一个测试邮件', str1, os.path.join(os.path.dirname(__file__), 'report/测试报告2020-08-04 10_17_47.html')]
yag.send(to=res, subject='测试发邮件', contents=str1)
print('发送成功')
