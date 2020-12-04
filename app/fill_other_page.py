from app import driver


# 其他頁籤填資料
def fill_other_page(tender_way, file_name):
    if tender_way == 12:
        # 履約期限
        driver.find_element_by_id('fdts').send_keys('5')
        # 是否依據採購法第11條之1，成立採購工作及審查小組
        driver.find_element_by_xpath('//*[@id="isLaw111_radio"]/div[2]/label').click()

        # 本案採購契約是否採用主管機關訂定之範本 => 是
        # 本案採購契約是否採用主管機關訂定之最新版範本 => 否
        driver.find_element_by_xpath('//*[@id="DirectForm"]/table/tbody/tr[9]/td[2]/div[1]/div[1]/label').click()
        driver.find_element_by_xpath('//*[@id="tr_isUsePccNewSample"]/td[2]/div[2]/div[2]/label').click()
        driver.find_element_by_id('notNewSampleReason').send_keys('測試 \n 測試 \n 測試')

        driver.find_element_by_xpath('//*[@id="tr_isReconstruct"]/td[2]/div[1]/div[2]/label').click()

        # 廠商資格摘要
        driver.find_element_by_id('isVendorDescs').click()
        driver.find_element_by_xpath('//*[@id="venderDesc_checkbox"]/input[1]').click()
        driver.find_element_by_xpath('//*[@id="venderDesc_checkbox"]/input[2]').click()
        driver.find_element_by_xpath('//*[@id="isVendorDescQua"]').click()
        driver.find_element_by_xpath('//*[@id="isVendorDescConInd_checkbox"]').click()

        driver.find_element_by_xpath('//*[@id="vendorTax"]').click()
        driver.find_element_by_xpath('//*[@id="vendorIndustry"]').click()

        driver.find_element_by_xpath(
            '//*[@id="DirectForm"]/table/tbody/tr[13]/td[2]/div[1]/table/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_xpath(
            '//*[@id="DirectForm"]/table/tbody/tr[13]/td[2]/div[1]/table/tbody/tr[2]/td[3]/textarea').clear()
        driver.find_element_by_xpath(
            '//*[@id="DirectForm"]/table/tbody/tr[13]/td[2]/div[1]/table/tbody/tr[2]/td[3]/textarea').send_keys(
            'AAA \n AAA \n AAA')
        driver.find_element_by_id('descn').send_keys('BBB \n BBB \n BBB')
        driver.find_element_by_xpath('//*[@id="Next_page"]').click()
        driver.implicitly_wait(1)

        # 文件上傳區塊通通跳過
        # 廠商說明書
        driver.find_element_by_xpath('//*[@id="VendorStatement"]/div[3]/a[2]').click()
        driver.implicitly_wait(1)

        # 標價清單
        # 預設填一項資料
        driver.find_element_by_xpath('//*[@id="tr_iteminfo_0"]/td[1]/input[3]').send_keys('1')
        driver.find_element_by_xpath('//*[@id="tr_iteminfo_0"]/td[2]/textarea').send_keys('123')
        driver.find_element_by_xpath('//*[@id="tr_iteminfo_0"]/td[3]/input').send_keys('1')
        driver.find_element_by_xpath('//*[@id="tr_iteminfo_0"]/td[4]/input').send_keys('1')
        driver.find_element_by_xpath('//*[@id="VendorStatement"]/div[2]/a[2]').click()
        driver.implicitly_wait(1)

        # 三用文件
        driver.find_element_by_xpath('//*[@id="VendorStatement"]/div/a[2]').click()
        driver.implicitly_wait(1)

        # 招標資料上傳
        driver.find_element_by_xpath('//*[@id="Next_page"]').click()
        driver.implicitly_wait(1)
    elif tender_way == 1:
        # 是否依據採購法第99條
        # 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[1]/td[2]/div[1]/div/div/div[3]/label').click()
        # 是 => 目的事業主管機關核准文號輸入
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[1]/td[2]/div[1]/div/div/div[1]/label').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[1]/td[2]/div[1]/div/div/div[2]/input').send_keys('機關名稱109年12月01日001字第1234567890號')

        # 履約期限
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[9]/td[2]/div[1]/input').send_keys('12345')

        # 是否依據採購法第11條之1，成立採購工作及審查小組
        # 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[2]/label').click()
        # 是 => 後續全選是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/label').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/div/div[1]/div[1]/label').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/div/div[1]/div[1]/span[2]/label[1]').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/div/div[2]/div[1]/label').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/div/div[3]/div[1]/label').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/div/div[3]/div[1]/span[2]/label[1]').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[11]/td[2]/div[1]/div/div[1]/div/div[4]/div[1]/label').click()

        # 本案採購契約是否採用主管機關訂定之範本
        # 是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[12]/td[2]/div[1]/div[1]/label').click()
        # 本案採購契約是否採用主管機關訂定之最新版範本
        # 是
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[13]/td[2]/div[2]/div[1]/label').click()
        # 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[13]/td[2]/div[2]/div[2]/label').click()
        # 本案採購契約未採用主管機關訂定之最新版範本之理由 (限填1000個中文字)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[13]/td[2]/div[2]/div[3]/textarea').send_keys('測試測試\n測試測試\n測試測試')

        # 本案採購契約是否採用主管機關訂定之範本
        # # 否
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[12]/td[2]/div[1]/div[2]/label').click()
        # # 不採用主管機關訂定之範本之理由 (限填100個中文字)
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[12]/td[2]/div[1]/div[3]/textarea').send_keys('測試測試\n測試測試\n測試測試')

        # 採購監辦 => 第一項: 依政府採購法第12條規定，報請上級機關派員監辦
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[14]/td[2]/div[1]/div[1]/label').click()

        # 是否屬災區重建工程 => 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[15]/td[2]/div[1]/div[2]/label').click()

        # 廠商資格摘要
        # 廠商登記或設立之證明
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/input').click()
        # 具公司登記
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/input[1]').click()
        # 具商業登記
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/input[2]').click()
        # 且須符合以下任一資格(可複選)：
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/div[2]/input').click()
        # 為營造業(以下可複選)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/div[2]/div/div[2]/input').click()
        # 土木包工業
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/div[2]/div/div[2]/div/input[1]').click()
        # 綜合營造業
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/div[2]/div/div[2]/div/input[2]').click()
        # 丙等(含以上)
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/div[2]/div/div[2]/div/span[1]/label[3]').click()

        # 廠商納稅之證明。如營業稅或所得稅
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[2]/input').click()

        # 廠商依工業團體法或商業團體法加入工業或商業團體之證明
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[3]/input').click()

        # 是否訂有與履約能力有關之基本資格
        # 廠商具有製造、供應或承做能力之證明 => 輸入框先清空後輸入
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/table/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/table/tbody/tr[2]/td[3]/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/table/tbody/tr[2]/td[3]/textarea').send_keys('測試測試\n測試測試\n測試測試')

        # 廠商具有如期履約能力之證明 => 輸入框先清空後輸入
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/table/tbody/tr[3]/td[1]/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/table/tbody/tr[3]/td[3]/textarea').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/table/tbody/tr[3]/td[3]/textarea').send_keys('測試測試\n測試測試\n測試測試')

        # 是否訂有與履約能力有關之特定資格
        # 否 => 不訂定特定資格之理由 (限填200個中文字)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[3]/label').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[4]/textarea').send_keys('AAA\nBBB\nCCC')
        # 是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[1]/label').click()
        # 廠商應附具之特定資格證明文件 (可複選)
        # 具有相當經驗或實績
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[2]/input[1]').click()
        # 具有相當人力
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[2]/input[2]').click()
        # 具有相當財力
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[2]/input[3]').click()
        # 具有相當設備
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[2]/input[4]').click()
        # 具有符合國際或國家品質管理之驗證文件
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div[2]/input[5]').click()

        # 附加說明(限填2000個中文字)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[20]/td[2]/div/textarea').send_keys('測試測試\n測試測試\n測試測試')

        # 是否刊登英文公告 => 預設選是
        # 機關地址(英)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[21]/td[2]/div[1]/div/div[2]/div[2]/div[2]/input').send_keys('somewhere street some number lane nowhere district, Taipei City')
        # 標案名稱(英)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[21]/td[2]/div[1]/div/div[2]/div[3]/div[2]/input').send_keys(file_name)
        # 聯絡人(英)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[21]/td[2]/div[1]/div/div[2]/div[4]/div[2]/input').send_keys('Kevin Tung')
        # 聯絡電話(英)
        driver.find_element_by_xpath('//*[@id="engTelCountryCode"]').send_keys('886')
        driver.find_element_by_xpath('//*[@id="engTelArea"]').send_keys('02')
        driver.find_element_by_xpath('//*[@id="engTelNo"]').send_keys('12345678')
        driver.find_element_by_xpath('//*[@id="engTelExt"]').send_keys('1234')

        # 傳真號碼(英)
        driver.find_element_by_xpath('//*[@id="engFaxCountryCode"]').send_keys('886')
        driver.find_element_by_xpath('//*[@id="engFaxArea"]').send_keys('02')
        driver.find_element_by_xpath('//*[@id="engFaxNo"]').send_keys('12345678')

        # 招標文件售價及付款方式(英)
        driver.find_element_by_xpath('//*[@id="engPay"]').send_keys('1.Price for selling on-site : cash only NT$*****   2.Price for selling via mail order : postal money order NT$***** , made payable to XXXXX        3.Price for acquiring electronic tender documentation on the internet (URL: web.pcc.gov.tw): electronic payment NT$***** ')

        # 領標地點(英)
        driver.find_element_by_xpath('//*[@id="engPickPlace"]').send_keys('some place in Taipei City...')

        # 附加說明(英)
        driver.find_element_by_xpath('//*[@id="engDesc"]').send_keys('some test comment\njust some more test comment\nanother chunk of test comment')

        # 申訴受理單位(英)
        # driver.find_element_by_xpath('//*[@id="engImpeachDept2"]').send_keys('some chunk of test comments\nmore chunk of test comments\nand yet more chunk of test comments...')

        # 申訴受理單位
        # driver.find_element_by_xpath('//*[@id="impeachDept2"]').send_keys('測試測試\n測試測試\n測試測試')

        # 下一頁
        driver.find_element_by_xpath('//*[@id="Next_page"]').click()