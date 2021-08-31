import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestCase.locators import *

driver = webdriver.Chrome('chromedriver/chromedriver')
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 20)


# @pytest.mark.d2d
def test_day_to_day_health():
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, username))).send_keys("Admin")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, password))).send_keys("admin123")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, login))).click()


test_day_to_day_health()


# @pytest.mark.d2d
def test_add_leave():
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'menu_leave_viewLeaveModule'))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'menu_leave_Entitlements'))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'menu_leave_addLeaveEntitlement'))).click()

    # CLick add to multiple employee
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'entitlements_filters_bulk_assign'))).click()

    # Deselect
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'entitlements_filters_bulk_assign'))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, 'ac_input'))).send_keys("Aaliyah Haq")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//li[@class='ac_even ac_over']"))).click()

    leave_type = Select(driver.find_element_by_id('entitlements_leave_type'))
    leave_type.select_by_index(1)

    time.sleep(2)

    # leave_type = Select(wait.until(expected_conditions.visibility_of_element_located(
    #     (By.ID, 'entitlements_leave_type'))).click()

    # leave_type.select_by_visible_text('CAN - FMLA')
    # leave_type.select_by_id('7')
    # leave_type.select_by_index(2)

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='entitlements_entitlement']"))).send_keys("1")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'btnSave'))).click()

    # Accept the leave addition
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'dialogUpdateEntitlementConfirmBtn'))).click()

    time.sleep(2)


test_add_leave()


# @pytest.mark.d2d
def test_assign_leave():
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'menu_leave_assignLeave'))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'assignleave_txtEmployee_empName'))).send_keys("a")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "(//li[contains(@class,'ac_even ac_over')])[2]"))).click()

    assign_leave_type = Select(driver.find_element_by_id('assignleave_txtLeaveType'))
    assign_leave_type.select_by_index(2)
    time.sleep(2)

    # assign_leave_type = wait.until(expected_conditions.visibility_of_element_located(
    #     (By.ID, 'assignleave_txtLeaveType'))).click()

    # assign_leave_type.select_by_value('7')
    # assign_leave_type.select_by_visible_text('CAN - FMLA')
    # assign_leave_type.select_by_index(2)

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='assignleave_txtFromDate']"))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//a[normalize-space()='28']"))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='assignleave_txtToDate']"))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//a[normalize-space()='28']"))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//textarea[@id='assignleave_txtComment']"))).send_keys("Test")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='assignBtn']"))).click()

    time.sleep(2)


test_assign_leave()


# @pytest.mark.d2d
def test_leave_list():
    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'menu_leave_viewLeaveList'))).click()

    # If we need to invoke calendar

    # wait.until(expected_conditions.visibility_of_element_located(
    #     (By.XPATH, "//input[@id='calFromDate']"))).click()
    #
    # wait.until(expected_conditions.visibility_of_element_located(
    #     (By.XPATH, "//input[@id='calToDate']"))).click()

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='leaveList_txtEmployee_empName']"))).send_keys("Aaliyah Haq")

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'btnSearch'))).click()

    cancel_leave = Select(driver.find_element_by_id('select_leave_action_66'))
    cancel_leave.select_by_index(2)

    time.sleep(5)

    # cancel_leave = wait.until(expected_conditions.visibility_of_element_located(
    #     (By.ID, 'select_leave_action_66'))).click()

    # cancel_leave.select_by_value('92')
    # cancel_leave.select_by_index(2)
    # cancel_leave.select_by_visible_text('Cancel')

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, "//input[@id='btnSave']"))).click()


test_leave_list()

# driver.quit()
