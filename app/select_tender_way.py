from app import driver
from selenium.webdriver.support.select import Select


def select_tender_way_12():
    select = Select(driver.find_element_by_id('fkPmsTenderWay'))
    select.select_by_value('12')
    driver.find_element_by_id('sbt_New').click()


def select_tender_way_1():
    select = Select(driver.find_element_by_id('fkPmsTenderWay'))
    select.select_by_value('1')
    driver.find_element_by_xpath('//*[@id="span_AwardWay_radio"]/label[1]').click()
    driver.find_element_by_xpath('//*[@id="span_isMultipleAward_radio"]/label[1]').click()
    driver.find_element_by_id('sbt_New').click()
    driver.find_element_by_xpath('//*[@id="yes"]').click()
