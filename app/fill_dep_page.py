from app import driver


# 機關頁籤資訊
def fill_dep_page():
    driver.find_element_by_xpath('//*[@id="telExt"]').clear()
    driver.find_element_by_xpath('//*[@id="telExt"]').send_keys('1234')
    driver.find_element_by_xpath('//*[@id="faxCountry"]').clear()
    driver.find_element_by_xpath('//*[@id="faxCountry"]').send_keys('886')
    driver.find_element_by_xpath('//*[@id="faxNo"]').clear()
    driver.find_element_by_xpath('//*[@id="faxNo"]').send_keys('87899033')
    driver.find_element_by_xpath('//*[@id="DirectForm"]/div[3]/a').click()