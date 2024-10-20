import time

from appium import webdriver

from appium.options.common import AppiumOptions

from selenium.webdriver import ActionChains

from selenium.webdriver.common.actions import interaction

from selenium.webdriver.common.actions.action_builder import ActionBuilder

from selenium.webdriver.common.actions.pointer_input import PointerInput

import subprocess

import re

import os

# starting appium webdriver

caps={}

caps["platformName"]="iOS"

caps["deviceName"]=""

caps['udid']=''

caps['automationName']='XCUITest'

driver = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(caps)) # load driver

actions = ActionChains(driver)

actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

# ------------------------------
while not os.path.exists('response'):
    pass

result = subprocess.run(['./xykscpp', 'response'], stdout=subprocess.PIPE)

pattern = r"\[\"[<>]+\"\]" # regex pattern matching

with open('response.json', 'w') as f:
    f.write(result.stdout.decode('utf-8'))

with open('response.json', 'r') as f:
    text = f.read()
    matches = re.findall(pattern, text)

# ------------------------------

# output the answers

print('waiting...')

for i in range(13):
    time.sleep(1)
    print(i+1)

# thanks to delay of the app

print('Starting...')

start = time.time()

for i in range(len(matches)):
    actions.w3c_actions.pointer_action.move_to_location(200, 500)
    actions.w3c_actions.pointer_action.pause(0)
    actions.w3c_actions.pointer_action.click_and_hold()
    if matches[i][2] == '>' :
        actions.w3c_actions.pointer_action.move_to_location(240, 540)
        actions.w3c_actions.pointer_action.move_to_location(200, 580)
    else :
        actions.w3c_actions.pointer_action.move_to_location(160, 540)
        actions.w3c_actions.pointer_action.move_to_location(200, 580)
    
    actions.w3c_actions.pointer_action.release()
    actions.perform()

# ------------------------------

end = time.time()

print('Time taken: ', end-start)

# cleaning up, which is compulsory

os.rename('response.json', 'response.json.old')

os.rename('response', 'response.old')

driver.quit()