from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

# from threading import Timer

import time
import progressbar
import pytz
import datetime

# baseURL = 'https://mcourse.mfac.or.kr/lecture/llist/index/'

options = webdriver.FirefoxOptions()
options.headless = True


def checkingmapo():
    list_URL = [
        'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00266/I000001',
        'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00267/I000031',
        'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00263/I000001',
        'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00264/I000031',
        # 'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00804/I000718'
    ]

    print('\nswim 11A\nswim 1B\nswim 10A\nswim 10B\ngolf 13A\n')

    # # swim 11A
    # URL = 'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00266/I000001'

    # # swim 11B
    # URL = 'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00267/I000031'

    # # swim 10A
    # URL = 'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00263/I000001'

    # # swim 10B
    # URL = 'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00264/I000031'

    # # golf 13A
    # URL = 'https://mcourse.mfac.or.kr/lecture/detail/index/MAPOARTCENTER/2001/00804/I000718'

    for elem in list_URL:
        driver = webdriver.Firefox(options=options)
        driver.get(elem)

        # lecture_category = driver.find_element(
        #     By.CLASS_NAME, 'ctgcd'
        # )

        remaining_spot = driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[3]')

        res = remaining_spot.text

        LOCAL_TIMEZONE = datetime.datetime.now(
            datetime.timezone.utc).astimezone().tzinfo
        seoulKoreaTz = pytz.timezone("Asia/Seoul")

        print(
            f'Checking...{datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")} {remaining_spot.text}')

        driver.delete_all_cookies()
        driver.quit()


res = ''

while res != '마감':
    # t = Timer(10.0, checkingmapo)
    # t.start()
    checkingmapo()
    time.sleep(900)

    # bar = progressbar.ProgressBar(maxval=20,
    #                               widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    # bar.start()
    # for i in range(10):
    #     print(f'Running...{i} times')
    #     # bar.update(i+1)
    #     t = Timer(8.0, checkingmapo)
    #     t.start()
    # bar.finish()
