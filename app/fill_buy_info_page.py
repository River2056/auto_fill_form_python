from app import driver
from app.helper import *
from selenium.webdriver.support.select import Select


# 採購資料頁籤填資料
def fill_buy_info_page(tender_way, file_name):
    if tender_way == 12:
        send_keys(get_by_id('tenderName'), file_name)
        send_keys(get_by_id('fkDmsProctrgCode'), '5111')
        click(get_by_tag_name('body'))
        send_keys(get_by_id('planNo'), '12345')
        # driver.find_element_by_id('tenderName').send_keys(file_name)
        # driver.find_element_by_id('fkDmsProctrgCode').send_keys('5111')
        # driver.find_element_by_tag_name('body').click()
        # driver.find_element_by_id('planNo').send_keys('12345')

        # 本採購案是否屬於建築工程
        click(get_by_xpath('//*[@id="IsBuild"]/td[2]/div[1]/div[1]/label'))
        select = Select(get_by_id('fkTpamProperty'))
        select.select_by_value('1')
        send_keys(get_by_id('procurementAmount1'), '100000')
        wait(2)
        # driver.find_element_by_xpath('//*[@id="IsBuild"]/td[2]/div[1]/div[1]/label').click()
        # select = Select(driver.find_element_by_id('fkTpamProperty'))
        # select.select_by_value('1')
        # driver.find_element_by_id('procurementAmount1').send_keys('100000')
        # driver.implicitly_wait(2)

        driver.find_element_by_xpath("//*[@id='DirectForm']/table/tbody/tr[10]/td[2]/div[1]/div[1]/label").click()
        driver.find_element_by_xpath('//*[@id="tr_isSensitive"]/td[2]/div[1]/div[1]/label').click()
        driver.find_element_by_xpath('//*[@id="tr_isAffectSec"]/td[2]/div[1]/div[1]/label').click()
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[15]/td[2]/div[1]/div[1]/div/div[1]/input').send_keys(
            '100000')
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="tr_budgetIsPdt"]/td[2]/div[1]/div[1]/label').click()
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[17]/td[2]/div[1]/div[1]/div/div[1]/input').send_keys(
            '100000')
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="tr_estimatedProcIsPdt"]/td[2]/div[1]/div[1]/label').click()
        driver.find_element_by_xpath('//*[@id="tr_fuRite"]/td[2]/div[1]/label[2]').click()
        driver.implicitly_wait(1)
        driver.find_element_by_id('fuRiteComment').send_keys('abc \n def \n ghi')
        driver.find_element_by_xpath('//*[@id="tr_isGrant"]/td[2]/div[1]/div[1]/label').click()
        driver.implicitly_wait(1)
        driver.find_element_by_id('input_orgId_0').send_keys('3')
        driver.find_element_by_id('tpamOrgAidMoney_0').send_keys('500')
        driver.find_element_by_xpath('//*[@id="tr_isExTender"]/td[2]/div[1]/div[2]/label').click()
        # click(get_by_xpath('//*[@id="DirectForm"]/div[2]/a[2]'))
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/div[3]/a[2]').click()
    elif tender_way == 1:
        try:
            # 標案名稱
            send_keys(get_by_id('tenderName'), file_name)
            # 標的分類
            send_keys(get_by_id('fkDmsProctrgCode'), '5111')
            click(get_by_tag_name('body'))
            wait(2)

            # 工程計畫編號
            send_keys(get_by_id('planNo'), '12345')

            # 以下根據狀況comment
            # case 1
            # 本採購案是否屬於建築工程 => 第一項
            click(get_by_xpath('//*[@id="IsBuild"]/td[2]/div[1]/label[1]'))

            # # case 2
            # # 本採購案是否屬於建築工程 => 第二項 => 輸入金額5百萬 => 是 => 否 => 是 => 是
            # click(get_by_xpath('//*[@id="IsBuild"]/td[2]/div[1]/label[2]'))
            # # 輸入金額5百萬
            # send_keys(
            #     get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]/span/div/div[1]/input'),
            #     '5000000'
            # )
            # # 是
            # click(
            #     get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/div[1]/table/tbody/tr[3]/td/div/div/div[1]/label')
            # )
            # # 否
            # click(
            #     get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/div[1]/table/tbody/tr[4]/td/div/div[2]/div[2]/label')
            # )
            # # 是
            # click(
            #     get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/div[1]/table/tbody/tr[5]/td/div/div[2]/div[1]/label')
            # )
            # # 是
            # click(
            #     get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/div[1]/table/tbody/tr[6]/td/div/div[2]/div[1]/label')
            # )

            # # case 3
            # # 本採購案是否屬於建築工程 => 第三項 => 輸入金額5百萬
            # click(get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/input[3]'))
            # # 輸入5百萬
            # send_keys(
            #     get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/span/div/div[1]/input'),
            #     '5000000'
            # )

            # # case 4
            # # 本採購案是否屬於建築工程
            # click(get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/label[3]'))

            # # case 5
            # # 本採購案是否屬於建築工程
            # click(get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[5]/td[2]/div[1]/label[4]'))

            # 財物採購性質
            select = Select(get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[7]/td[2]/div[1]/select'))
            select.select_by_value('1')

            # 採購金額 => 輸入5億
            send_keys(
                get_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[8]/td[2]/div[1]/div/div/div[1]/input'),
                '500000000'
            )

            # 根據狀況comment
            # # 有無已簽准預期使用情形及效益目標 => 有

            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[10]/td[2]/div[1]/div[1]/label').click()

            # 有無已簽准預期使用情形及效益目標 => 無 => 第一項
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[10]/td[2]/div[1]/div[2]/label').click()
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[10]/td[2]/div[1]/span[2]/input[1]').click()

            # 辦理方式
            # 自辦(會loading, 設等待秒數)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[11]/td[2]/div[1]/div[1]/label').click()
            driver.implicitly_wait(3)
            # # 代辦 => 輸入機關
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[11]/td[2]/div[1]/div[2]/label').click()
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[11]/td[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/input').send_keys('9.99')
            # driver.find_element_by_tag_name('body').click()
            # driver.implicitly_wait(2)

            # 依據法條
            select = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[12]/td[2]/div[1]/select'))
            select.select_by_value('4') # 採購法第18條、第19條

            # 是否適用條約或協定之採購 WTO
            # 是否適用WTO政府採購協定(GPA)
            # driver.find_element_by_xpath('//*[@id="radio_GPA2_isApplied"]').click()
            # 是否適用臺紐經濟合作協定(ANZTEC)
            # driver.find_element_by_xpath('//*[@id="radio_ANZTEC_isApplied"]').click()
            # 是否適用臺星經濟夥伴協定(ASTEP)
            # driver.find_element_by_xpath('//*[@id="radio_ASTEP_isApplied"]').click()

            # 是否採用電子競價
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[14]/td[2]/div[1]/div[2]/label').click()

            # 本採購是否屬「具敏感性或國安(含資安)疑慮之業務範疇」採購 => 是
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[16]/td[2]/div[2]/div[1]/label').click()

            # 本採購是否屬「涉及國家安全」採購 => 是
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[17]/td[2]/div[2]/div[1]/label').click()

            # 預算金額
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[18]/td[2]/div[1]/div[1]/div/div[1]/input').send_keys('500000000')

            # 預算金額是否公開
            # 是
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[19]/td[2]/div[1]/div[1]/label').click()
            # # 否 => 轉售或供製造、加工後轉售之採購 or 預算金額涉及商業機密 or 機關認為不宜公開
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[19]/td[2]/div[1]/div[2]/label').click()
            # select = Select(driver.find_element_by_id('budgetNopubReason'))
            # select.select_by_value('轉售或供製造、加工後轉售之採購')
            # # select.select_by_value('預算金額涉及商業機密')
            # # select.select_by_value('機關認為不宜公開')

            # 預計金額 => 輸入5億
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[20]/td[2]/div[1]/div/div/div[1]/input').send_keys('500000000')

            # 預計金額是否公開 => 是
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[21]/td[2]/div[1]/div[1]/label').click()

            # 後續擴充
            # 否
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[22]/td[2]/div[1]/div[1]/label').click()
            # 是 => 輸入說明
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[22]/td[2]/div[1]/div[2]/label').click()
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[22]/td[2]/div[1]/div[3]/textarea').send_keys('測試測試\n測試測試\n測試測試')

            # 是否受機關補助
            # 否
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[23]/td[2]/div[1]/div[3]/label').click()
            # 是 => 新增一筆
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[23]/td[2]/div[1]/div[1]/label').click()
            # driver.find_element_by_id('input_orgId_0').send_keys('3')
            # driver.find_element_by_tag_name('body').click()
            # driver.find_element_by_id('tpamOrgAidMoney_0').send_keys('50000')
            # driver.find_element_by_tag_name('body').click()
            # driver.implicitly_wait(2)

            # 本案是否曾以不同案號辦理招標公告且已傳輸其無法決標公告，目前仍未決標
            # 否
            driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[24]/td[2]/div[1]/div[2]/label').click()
            # # 是
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[24]/td[2]/div[1]/div[1]/label').click()
            # # 前案採購資訊
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[25]/td[2]/div/div[1]/div/div[1]/input').send_keys('9.99') # 前案機關代碼
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/form/table/tbody/tr[25]/td[2]/div/div[2]/input[1]').send_keys('12345') # 前案標案案號

            # 下一頁
            driver.find_element_by_xpath('//*[@id="DirectForm"]/div[3]/a[2]').click()
        except Exception:
            # 中間有錯, 跳過, 直接下一頁
            driver.find_element_by_xpath('//*[@id="DirectForm"]/div[3]/a[2]').click()