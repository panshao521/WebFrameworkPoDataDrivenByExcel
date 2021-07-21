# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:45
Author:   panyuangao@foxmail.com
File:     main.py
Describe: 通过excel数据驱动，执行测试用例
"""
from Util import Excel
from Util.DateStr import *
from Conf.ProjVar import *
from Action.test_steps import *
from Util.TakePic import  take_pic
import traceback
import time

excel = Excel.ExcelUtil(test_data_file_path_126)
print(excel.get_file_path())
# print(excel.get_sheet_names())
excel.set_sheet_by_index(0) # 设定为第一个sheet，获取登录账号信息
login_data = excel.get_sheet_all_cell_values() # 获取第一个sheet所有单元格内容
# print(login_data)
for row in login_data:
    test_data_flag = True # 默认这个用例的结果为True,如果出现任何报错则为False
    if row[login_data_valid_col_no].lower() == 'y': # 是否执行列为y的数据行，才会执行
        username = row[login_username_col_no] # 获取用户名
        passwd = row[login_passwd_col_no] # 获取密码

        try:
            driver = login(username,passwd)
        except:
            traceback.print_exc()
            test_data_flag = False
            quit()
            continue
        print(test_data_flag)

        test_data_sheet_name = row[test_data_sheet_name_col_no] # 获取数据表的名称
        excel.set_sheet_by_name(test_data_sheet_name)
        contact_data = excel.get_sheet_all_cell_values() # 获取所有联系人的sheet中的所有数据
        #设定测试结果sheet作为当前操作sheet
        excel.set_sheet_by_name("测试结果")
        excel.write_a_line_in_sheet(contact_data[0],fgcolor='FF9D6F') # 在测试结果页sheet，写入联系人sheet页表头

        for contact_row in contact_data[1:]: # 从联系人的sheet中读取数据行
            contact_data_flag = True
            if contact_row[contact_data_valid_col_no].lower() == 'y':
                name = contact_row[contact_name_col_no]
                email = contact_row[contact_email_col_no]
                phone = contact_row[contact_phone_col_no]
                other_info = contact_row[contact_info_col_no]
                assert_word = contact_row[assert_word_col_no]
                try:
                    addContact(name,email,phone,other_info,assert_word)
                except Exception as e:
                    traceback.print_exc()
                    pic_file_path = take_pic(driver)
                    contact_row[pic_path_col_no] = pic_file_path
                    contact_data_flag = False
                    test_data_flag = False
            contact_row[test_end_time_col_no] = get_chinese_current_datetime()  # 联系人结果行，写入执行时间

            # 联系人结果行，写入测试结果
            if contact_row[contact_data_valid_col_no].lower() != 'y':
                contact_row[test_result_col_no] = "不执行"
            elif contact_data_flag:
                contact_row[test_result_col_no] = "成功"
            else:
                contact_row[test_result_col_no] = "失败"

            if contact_row[test_result_col_no] == "失败":
                excel.write_a_line_in_sheet(contact_row, font_color="red")
            else:
                excel.write_a_line_in_sheet(contact_row)

        row[login_end_time_col_no] = get_chinese_current_datetime() # 登录结果行，写入执行时间

        # 登录结果行，写入测试结果
        if test_data_flag:
            row[login_test_result_col_no] = "成功"
        else:
            row[login_test_result_col_no] = "失败"

        excel.write_a_line_in_sheet(login_data[0], fgcolor="40E0D0") #在测试结果页sheet，写入登录sheet页表头
        if row[login_test_result_col_no] == "失败":
            excel.write_a_line_in_sheet(row, font_color="red")
        else:
            excel.write_a_line_in_sheet(row)

        time.sleep(3)
        quit()

