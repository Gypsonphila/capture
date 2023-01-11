from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

from capture.models import ShangHaiFutures, ZhengZhouFutures, DaLianFutures


URL = 'https://futures.cngold.org/hangqing/'
DB_FIELD_LIST = ["bourse_name", "code", "name", "newest_price", "amount_increase_price", "amount_increase", "opening_price", "top_price", "bottom_price", "yesterday_price", "update_time"]


def create_browser_client():
    browser = webdriver.Chrome()
    return browser


def capture_handler():
    browser = create_browser_client()
    try:
        browser.get(URL)
        browser.maximize_window()
        browser.implicitly_wait(60)

        target_box = browser.find_element(By.XPATH, "/html/body/div[3]/div[3]")
        tabs = target_box.find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, 'li')

        for li in tabs:
            li.click()
            handles = browser.window_handles
            browser.switch_to.window(handles[-1])

            target_table_box = browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]")
            title = target_table_box.find_element(By.CLASS_NAME, "fl").text
            dl_list = target_table_box.find_element(By.CLASS_NAME, "dl_list").find_elements(By.CLASS_NAME, "clearfix")

            insert_dict = {DB_FIELD_LIST[0]: title}
            for i, dl in enumerate(dl_list):
                if i != 0:
                    dd_list = dl.find_elements(By.TAG_NAME, "dd")

                    for dd_idx, dd in enumerate(dd_list):
                        dd_text = dd.text
                        insert_idx = dd_idx + 1
                        insert_dict[DB_FIELD_LIST[insert_idx]] = dd_text

                    if title == '上海期货交易所':
                        ShangHaiFutures.objects.update_or_create(insert_dict, code=insert_dict[DB_FIELD_LIST[1]])
                    elif title == '郑州商品交易所':
                        ZhengZhouFutures.objects.update_or_create(insert_dict, code=insert_dict[DB_FIELD_LIST[1]])
                    elif title == '大连商品交易所':
                        DaLianFutures.objects.update_or_create(insert_dict, code=insert_dict[DB_FIELD_LIST[1]])

            browser.close()
            browser.switch_to.window(handles[0])

    except Exception as error:
        print(f'爬取失败-----{error}')
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_img = browser.get_screenshot_as_file(f'{date_time}.png')
        print(error_img)
    finally:
        browser.quit()
        print('爬取结束！')


def run():
    capture_handler()
