from app import driver
from app import login
from app import select_tender_way as select
from app import run_tender_way as run
import random


def main():
    url = 'http://127.0.0.1:8080/tps'
    driver.get(url)
    driver.implicitly_wait(6)

    # 登入
    login.login('3.13.20.2', '0', 'abc123')
    driver.implicitly_wait(6)
    url = 'http://127.0.0.1:8080/tps/TenderManagement/showTenderTmp'
    driver.get(url)

    # 產生隨機標案案號
    random_num = random.randint(100000000000, 999999999999)
    file_name = f'test_{random_num}'
    driver.find_element_by_id('tenderCaseNo').send_keys(file_name)

    # 公開取得電子報價單
    select.select_tender_way_12()
    run.run_tender_way_12(file_name)

    # 公開招標
    # select.select_tender_way_1()
    # run.run_tender_way_1(file_name)


if __name__ == '__main__':
    main()
