*** Settings ***
Library       SeleniumLibrary
Resource        ../Common/CommonTask.robot
Test Setup    Opening Browser Setting
Test Teardown   Clearing and Closing Browser Setting 
*** Test Cases ***
Testing Log
    Open Browser        http://www.google.com     chrome