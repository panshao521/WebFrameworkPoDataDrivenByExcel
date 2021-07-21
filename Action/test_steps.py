# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:43
Author:   panyuangao@foxmail.com
File:     test_steps.py
Describe: 封装测试步骤，打开浏览器，登录，添加联系人，退出
"""
from PageObjects import IndexPage,HomePage,ContactPerson
from Conf.ProjVar import chrome_driver_path
from selenium import webdriver

driver = ""
def browser(browser_name):
    global driver
    if "chrome" in browser_name.lower():
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
    else:
        driver = webdriver.Safari()
    return driver

def login(username,passwd):
    global driver
    driver = browser('chrome')
    index_page = IndexPage.IndexPage(driver)
    index_page.login(username,passwd)
    import time
    time.sleep(5)
    assert '通讯录' in driver.page_source
    return driver

def addContact(name,email,phone,other_info,assert_keyword ):
    home_page = HomePage.HomePage(driver)
    home_page. click_address_link()
    contact_person = ContactPerson.ContactPerson(driver)
    contact_person.click_create_contact_person_button()
    contact_person.input_name(name)
    contact_person.input_email(email)
    contact_person.input_phone(phone)
    contact_person.input_other_info(other_info)
    contact_person.click_confirm_button()
    import time
    time.sleep(1)
    assert assert_keyword in driver.page_source

def quit():
    global dirver
    driver.quit()

if __name__ == '__main__':
    browser("chrome")
    login("youngboss2020", "Wy123456")
    addContact("王五","12234@qq.com","13838383388","我只是备注而已")
    quit()