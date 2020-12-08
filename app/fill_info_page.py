from app import driver
from app.helper import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


# 招標頁籤填資料
def fill_info_page(tender_way):
    if tender_way == 12:
        click(by_xpath('//*[@id="DirectForm"]/table/tbody/tr[9]/td[2]/div[1]/div[2]/label'))

        # 是否訂有底價 => 否 => 採購法第47條第1項第1款
        click(by_xpath('//*[@id="DirectForm"]/table/tbody/tr[9]/td[2]/div[1]/div[2]/label'))
        click(by_xpath('//*[@id="div_isGovernmentEstimate"]/div[1]/label'))

        click(by_xpath('//*[@id="DirectForm"]/table/tbody/tr[18]/td[2]/div[1]/div[2]/label'))

        # 下一頁
        click(by_xpath('/html/body/div[2]/div/div[5]/div/form/div[3]/a[3]'))

    elif tender_way == 2:
        # 是否訂有底價 => 否 => 第一項
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[9]/td[2]/div[1]/div[2]/label'))
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[9]/td[2]/div[1]/div[2]/div/div[1]/label'))

        # 是否屬特殊採購
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[17]/td[2]/div[1]/div/div[2]/label'))

        # 是否屬統包
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[19]/td[2]/div[3]/div/div[1]/label'))
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[19]/td[2]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[2]/input[1]'))
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[19]/td[2]/div[3]/div/div[1]/div/table/tbody/tr[2]/td[2]/input[1]'))

        # 本案完成後所應達到之功能、效益、標準、品質或特性(填列摘要情形，限填500個中文字)
        send_keys(
            by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[23]/td[2]/div[1]/textarea'),
            'AAA\nBBB\nCCC\nDDD'
        )

        # 是否屬二以上機關之聯合採購(不適用共同供應契約規定)
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[25]/td[2]/div[1]/div[2]/label'))

        # 是否屬國際競圖之採購 => 是 => 是 => 是
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[27]/td[2]/div[1]/div[1]/label'))
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[27]/td[2]/div[1]/div[1]/div/div/table/tbody/tr[1]/td[2]/input[1]'))
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[27]/td[2]/div[1]/div[1]/div/div/table/tbody/tr[2]/td[2]/input[1]'))

        # 是否採行協商措施
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[28]/td[2]/div[1]/div/div[1]/label'))

        # 是否適用採購法第104條或105條或招標期限標準第10條或第4條之1
        # 是 => select選1
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[29]/td[2]/div[1]/div[1]/label'))
        select = Select(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/table/tbody/tr[29]/td[2]/div[1]/div[2]/select'))
        select.select_by_value('6')

        # 下一頁
        click(by_xpath('/html/body/div[2]/div/div[5]/div[3]/form/div[3]/a[2]'))

    elif tender_way == 1:
        # 是否訂有底價
        # 是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[9]/td[2]/div[1]/div[1]/label').click()
        # # 否 => 選第一項: 採購法第47條第1項第1款
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[9]/td[2]/div[1]/div[2]/label').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[9]/td[2]/div[1]/div[3]/p[1]/label').click()

        # 是否屬特殊採購
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[17]/td[2]/div[1]/div/div[1]/label').click()

        # 是否已辦理公開閱覽, 預設: 否
        # 選select
        # select = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[18]/td[2]/div[1]/div[3]/div[2]/select'))
        # select.select_by_value('政府採購法第22條第1項第3款')

        # 是否屬統包
        # 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div/div[4]/label').click()
        # # 是, 1. 2. 都選是
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div/div[2]/label').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div/div[3]/div[2]/div[2]/label[1]').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[19]/td[2]/div[1]/div/div[3]/div[2]/div[4]/label[1]').click()
        # 本案完成後所應達到之功能、效益、標準、品質或特性 (填列摘要情形，限填500個中文字)
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[23]/td[2]/div[1]/textarea').send_keys('測試測試\n測試測試\n測試測試')

        # 是否屬二以上機關之聯合採購(不適用共同供應契約規定)
        # 是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[25]/td[2]/div[1]/div[1]/label').click()
        # 否
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[25]/td[2]/div[1]/div[2]/label').click()

        # 是否屬國際競圖之採購
        # 否
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[27]/td[2]/div[1]/div[3]/label').click()
        # # 是, 1. 2. 都選是
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[27]/td[2]/div[1]/div[1]/label').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[27]/td[2]/div[1]/div[2]/div[2]/div[2]/label[1]').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[27]/td[2]/div[1]/div[2]/div[2]/div[4]/label[1]').click()

        # 是否採行協商措施 => 是
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[28]/td[2]/div[1]/div/div[1]/label').click()

        # 是否適用採購法第104條或105條或招標期限標準第10條或第4條之1
        # 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[29]/td[2]/div[1]/div[3]/label').click()
        # # 是 => 2. 公營事業為商業性轉售或用於製造產品、提供服務以供轉售目的所為之採購，基於採購案件之特性或實際需要，有縮短等標期之必要者
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[29]/td[2]/div[1]/div[1]/label').click()
        # select = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[29]/td[2]/div[1]/div[2]/select'))
        # select.select_by_value('2')

        # 是否依據採購法第106條第1項第1款辦理
        # 否
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[30]/td[2]/div[1]/div/div[3]/label').click()
        # 是
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[30]/td[2]/div[1]/div/div[1]/label').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/table/tbody/tr[30]/td[2]/div[1]/div/div[2]/div[1]/input').send_keys('9.99')
        # 駐在地國別
        # driver.find_element_by_xpath('//*[@id="fkForeignNation_chosen"]').click()
        # driver.find_element_by_xpath('//*[@id="fkForeignNation_chosen"]/a/span').text = '美國(United States of America)' # .send_keys('美國(United States of America)')
        # driver.find_elements_by_tag_name('body').send_keys(Keys.ENTER)

        # 下一頁
        driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/form/div[2]/a[2]').click()



