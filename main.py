import os # module for interaction with your operation system

from selenium import webdriver # general modul for selenium
from selenium.webdriver.support.select import Select # for handling select drop down
from selenium.webdriver.support.wait import WebDriverWait # selenium modul for waiting response browser
from selenium.webdriver.support import expected_conditions as EC # modul selenium for condition
from selenium.webdriver.common.by import By # modul selenium handle after wait for search element

Wait_time = 60  # time for waiting process

# personal data

first_name = 'Muhammad'
last_name = 'Yasa'
mobile_phone_number = '080989999'
password = 'NeverSurrender123'

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver')) # handling file chromedriver
driver.get('https://www.facebook.com/') # getting url from facebook
driver.find_element_by_id('u_0_2').click() # function click by id

element = WebDriverWait(driver, Wait_time).until( # waiting process time
    EC.element_to_be_clickable((By.ID, 'u_1_b')) # search element from id
) # method for waiting process until element is clickable
element.send_keys(first_name) # input for first name

driver.find_element_by_id('u_1_d').send_keys(last_name) # input last name from search element id
driver.find_element_by_id('u_1_g').send_keys(mobile_phone_number) # input mobile phone from search element id
driver.find_element_by_id('password_step_input').send_keys(password) # input password from search element id

# handling date ( drop down )
day = Select(driver.find_element_by_id('day')) # use select method for drop down condition
day.select_by_visible_text('24') # with value method

month = Select(driver.find_element_by_id('month')) # use select method for drop down condition
month.select_by_visible_text('Agu') # with value method

year = Select(driver.find_element_by_id('year')) # use select method for drop down condition
year.select_by_visible_text('2000') # with value method

# handling sex ( radio button )
driver.find_element_by_css_selector("input[type='radio'][value='2']").click() # use selector for handling radio button, and use value

# ending for button complete register
driver.find_element_by_id('u_1_s').click()