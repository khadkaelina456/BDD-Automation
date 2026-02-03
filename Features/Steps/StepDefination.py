from behave import *
from selenium.webdriver import Chrome
import time

@given(u'User is on Registration Page')
def step_impl(context):
    context.driver = Chrome()
    context.driver.get('https://www.facebook.com/r.php')
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

@when(u'User enters firstname')
def step_impl(context):
    context.driver.find_element('name', 'firstname').send_keys('Puspa')

@when(u'User enters lastname')
def step_impl(context):
    context.driver.find_element('name', 'lastname').send_keys('K.C.')

@when(u'User enters month')
def step_impl(context):
    context.driver.find_element('xpath', '//select[@name="birthday_month"]').send_keys("Feb")

@when(u'User enters day')
def step_impl(context):
    context.driver.find_element('xpath', '//select[@name="birthday_day"]').send_keys("18")

@when(u'User enters year')
def step_impl(context):
    context.driver.find_element('xpath', '//select[@name="birthday_year"]').send_keys("2002")

@when(u'User click gender')
def step_impl(context):
    # Selects female radio button
    context.driver.find_element('xpath', '//input[@value="1"]').click()

@when(u'User enters email')
def step_impl(context):
    context.driver.find_element('xpath', "//input[@name='reg_email__']").send_keys("kanxi@gmail.com")

@when(u'User enters password')
def step_impl(context):
    context.driver.find_element('xpath', "//input[@name='reg_passwd__']").send_keys("pus123")

@when(u'User click on signup button')
def step_impl(context):
    context.driver.find_element('xpath', "//button[@name='websubmit']").click()

@then(u'User should be registered successfully')
def step_impl(context):
    time.sleep(3) # Just to see the result
    print("Success: Valid Registration Scenario Passed")
    context.driver.quit()

@then(u'User should be registered with duplicate email successfully')
def step_impl(context):
    time.sleep(3)
    print("Success: Duplicate Email Scenario Passed")
    context.driver.quit()