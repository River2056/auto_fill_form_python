from app import driver


def fill_upload_file_page(tender_way):
    if tender_way == 1:
        # 目前先跳過
        driver.find_element_by_xpath('//*[@id="Next_page"]').click()