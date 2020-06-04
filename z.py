from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction



def z():
    desired_caps = {}
    # 系统 platformName
    desired_caps['platformName']= 'Android'
    # 版本 platformVersion
    desired_caps['platformVersion']= '5.1'
    # 设备号 deviceName
    desired_caps['deviceName']= '127.0.0.1:62001'
    # 包名 appPackage
    desired_caps['appPackage']= 'com.android.settings'
    # 启动名 appActivity
    desired_caps['appActivity']= '.Settings'

    # 声明手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    a = driver.find_element_by_xpath("//*[contains(@text,'蓝牙')]")
    b = driver.find_element_by_xpath("//*[contains(@text,'显示')]")


    TouchAction(driver).press(b).move_to(a).wait(1000).release().perform()

    driver.quit()