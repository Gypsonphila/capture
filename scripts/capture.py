from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime


URL = 'https://futures.cngold.org/hangqing/'


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

        table_row_list = {}
        for li in tabs:
            li.click()
            handles = browser.window_handles
            browser.switch_to.window(handles[-1])

            target_table_box = browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]")
            title = target_table_box.find_element(By.CLASS_NAME, "fl").text
            dl_list = target_table_box.find_element(By.CLASS_NAME, "dl_list").find_elements(By.CLASS_NAME, "clearfix")

            table_row_list[title] = []

            for i, dl in enumerate(dl_list):
                if i != 0:
                    dd_list = dl.find_elements(By.TAG_NAME, "dd")

                    row_list = []
                    for dd in dd_list:
                        dd_text = dd.text
                        row_list.append(dd_text)
                    table_row_list[title].append(row_list)

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
