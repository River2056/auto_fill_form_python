from app import fill_dep_page as dep
from app import fill_buy_info_page as buy_info
from app import fill_info_page as info
from app import fill_var_page as var
from app import fill_other_page as other
from app import fill_new_item_page as new_item
from app import fill_upload_file_page as upload_file


# 完整跑完一次 公開取得電子報價單
def run_tender_way_12(file_name):
    # 機關資料頁籤
    dep.fill_dep_page()
    # 採購資料頁籤填資料
    buy_info.fill_buy_info_page(12, file_name)
    # 招標資料頁籤填料
    info.fill_info_page(12)
    # 領投開標頁籤資料
    var.fill_var_page(12)
    # 其他頁籤資料
    other.fill_other_page(12, file_name)


# 完整跑完一次 公開取得報價單與企劃書
def run_tender_way_2(file_name):
    # 機關資料頁籤
    dep.fill_dep_page()
    # 採購資料頁籤填資料
    buy_info.fill_buy_info_page(2, file_name)
    # 招標資料頁籤填料
    info.fill_info_page(2)
    # 領投開標頁籤資料
    var.fill_var_page(2)
    # 其他頁籤資料
    other.fill_other_page(2, file_name)
    # 招標品項
    new_item.fill_new_item_page(1)
    # 文件上傳
    upload_file.fill_upload_file_page(1)


# 完整跑完一次 公開招標
def run_tender_way_1(file_name):
    # 機關頁籤
    dep.fill_dep_page()
    # 採購頁籤
    buy_info.fill_buy_info_page(1, file_name)
    # 招標頁籤
    info.fill_info_page(1)
    # 領投開標頁籤
    var.fill_var_page(1)
    # 其他頁籤
    other.fill_other_page(1, file_name)
    # 招標品項
    new_item.fill_new_item_page(1)
    # 文件上傳
    upload_file.fill_upload_file_page(1)
