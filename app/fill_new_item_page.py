from app import driver


def fill_new_item_page(tender_way):
    if tender_way == 1:
        # 新增一個品項
        # 品項名稱
        driver.find_element_by_xpath('//*[@id="tpamTenderItemToList[0].itemName"]').send_keys('測試品項')
        # 預估數量
        driver.find_element_by_xpath('//*[@id="tpamTenderItemToList[0].itemQty"]').send_keys('1')
        # 單位
        driver.find_element_by_xpath('//*[@id="tpamTenderItemToList[0].itemUnit"]').send_keys('1')
        # 預算金額
        driver.find_element_by_xpath('//*[@id="itemAmount_0"]').send_keys('5000')

        # 下一頁
        driver.find_element_by_xpath('//*[@id="Next_page"]').click()