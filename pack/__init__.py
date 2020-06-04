from selenium.webdriver.common.by import By

"""
    +号
"""
jia = (By.XPATH,"//android.widget.ImageButton[@resource-id='com.android.contacts:id/floating_action_button']")
name = (By.XPATH,"//*[contains(@text,'姓名')]")
tel = (By.XPATH,"//*[contains(@text,'电话')]")
re_keys = (By.XPATH,"//android.widget.ImageButton[@content-desc='向上导航']")