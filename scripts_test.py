import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver=webdriver.Chrome()
url='http://localhost/admin.php?m=mgr/admin.login'
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_name('username').click()
driver.find_element_by_name('username').send_keys('admin')

driver.find_element_by_name('password').click()
driver.find_element_by_name('password').send_keys('admin')

driver.find_element_by_xpath('//*[@id="loginFrm"]/input').click()

driver.find_element_by_xpath('//*[@id="header"]/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="side-menu"]/div[3]/ul/li[2]/a').click()

ele=driver.find_element_by_id('mainframe')
driver.switch_to.frame(ele)
driver.find_element_by_xpath('/html/body/div[2]/h3/a[2]/span').click()

driver.find_element_by_xpath('//*[@id="username"]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('001')

driver.find_element_by_xpath('//*[@id="realname"]').click()
driver.find_element_by_xpath('//*[@id="realname"]').send_keys('陈老师')

driver.find_element_by_xpath('//*[@id="password"]').click()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')

from selenium.webdriver.support.ui import Select

ele=driver.find_element_by_name('roleid')
Select(ele).select_by_value('6')

ele2=driver.find_element_by_name('orid1')
Select(ele2).select_by_value('24')

driver.find_element_by_xpath('//*[@id="email"]').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys('16024760@qq.com')

driver.find_element_by_xpath('//*[@id="phone"]').click()
driver.find_element_by_xpath('//*[@id="phone"]').send_keys('17677788888')

ele3=driver.find_element_by_name('location_p')
Select(ele3).select_by_value('内蒙古自治区')

ele4=driver.find_element_by_name('location_c')
Select(ele4).select_by_value('鄂尔多斯市')

ele5=driver.find_element_by_name('location_a')
Select(ele5).select_by_value('鄂托克旗')

driver.find_element_by_xpath('//*[@id="address"]').click()
driver.find_element_by_xpath('//*[@id="address"]').send_keys('wu')

driver.find_element_by_xpath('//*[@id="introduce"]').click()
driver.find_element_by_xpath('//*[@id="introduce"]').send_keys('wu')

driver.find_element_by_xpath('//*[@id="btn_sub"]/span').click()
time.sleep(5)

driver.switch_to.alert.accept()

driver.find_element_by_xpath('/html/body/div[2]/h3/a/span').click()
