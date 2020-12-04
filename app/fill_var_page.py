from app import driver
from app.helper import *
from selenium.webdriver.common.keys import Keys


# 領投開標填資料
def fill_var_page(tender_way):
    if tender_way == 12:
        clear(by_xpath('//*[@id="deptCharge1"]'))
        send_keys(by_xpath('//*[@id="deptCharge1"]'), '0')
        wait(1)
        # driver.find_element_by_id('docChargeExpRsn').send_keys('abc \n def \ ghi')
        # driver.find_element_by_id('dcIdstrName').send_keys('台灣中油股份有限公司')
        # driver.find_element_by_id('dcOidstrName').send_keys('採購處')
        # driver.find_element_by_id('bankAccountName').send_keys('台灣中油股份有限公司')

        click(by_xpath('//*[@id="div_isEsubmitY"]/div[1]/div/label[1]'))
        click(by_xpath('//*[@id="div_isEsubmitY"]/div[2]/div/label[1]'))

        # 截止投標日期
        send_keys(by_id('waitDay'), '7')
        click(by_tag_name('body'))

        date_value = by_id('label_spdtDate').get_attribute('innerHTML')
        send_keys(by_id('opdtDateInput'), date_value)
        click(by_tag_name('body'))

        # is_Deposite_Y
        click(by_xpath('//*[@id="DirectForm"]/table/tbody/tr[6]/td[2]/div[1]/div/div[3]/label'))
        # driver.find_element_by_id('tenderDepositeY').send_keys('1000')
        # 投標文字
        click(by_xpath('//*[@id="DirectForm"]/table/tbody/tr[7]/td[2]/div[1]/label[1]'))

        # 下一頁
        click(by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/div[3]/a[2]'))
    elif tender_way == 1:
        # 是否提供電子領標 => 預設都選是
        # 招標文件售價及付款方式
        driver.find_element_by_xpath('//*[@id="costPayPhyObtain"]').send_keys('現金')

        # 是否提供電子投標
        # 是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/table/tbody/tr[2]/td[2]/div[1]/div/div[1]/label').click()

        # 截止投標
        # 等待天數
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/table/tbody/tr[3]/td[2]/div[1]/div[1]/input[2]').send_keys('26')
        driver.find_element_by_tag_name('body').click()
        # label_spdtDate
        date_value = driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/table/tbody/tr[3]/td[2]/div[1]/div[1]/span/label').get_attribute('innerHTML')

        # 開標時間
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/table/tbody/tr[4]/td[2]/div[1]/div/div/div/div/input[1]').send_keys(date_value)
        driver.find_element_by_tag_name('body').click()

        # 是否須繳納押標金 => 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/table/tbody/tr[6]/td[2]/div[1]/div/div[3]/label').click()

        # 投標文字 => 正體中文
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/table/tbody/tr[7]/td[2]/div[1]/div[1]/label').click()

        # 下一頁
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[7]/form/div[2]/a[2]').click()
