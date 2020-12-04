from app import driver


def login(username, ext, password):
    driver.find_element_by_id('orgUserId').send_keys(username)
    driver.find_element_by_id('orgUserIdExt').send_keys(ext)
    driver.find_element_by_id('orgPassword').send_keys(password)
    driver.find_element_by_xpath('//*[@id="orgAccountMode"]/table/tbody/tr[4]/td/table/tbody/tr/td[1]/a/div').click()
