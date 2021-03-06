# -*- coding: utf-8 -*-

import sys
import time
import dns.resolver
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 한글 사용을 위해 기본 인코딩을 utf-8로 바꿈.
reload(sys)
sys.setdefaultencoding('utf-8')

f = open("./log/SKT_Login_Test_{}.txt".format(time.ctime()), "w")

for i in range(1, 3):
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 로그인 페이지 열기
    driver.get("https://www.jobplanet.co.kr/users/sign_in")

    page_loading_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user_email')))

    try:
        # 로그인
        user_email_login_id = driver.find_element_by_id("user_email")
        user_email_login_id.clear()
        user_email_login_id.send_keys("test053@intween.net")
        user_email_login_pw = driver.find_element_by_id("user_password")
        user_email_login_pw.clear()
        user_email_login_pw.send_keys("qa123123")
        driver.find_element_by_name("commit").click()

        assert "함께 만드는 프리미엄 기업정보 | 잡플래닛" in driver.title

        # 연결된 DNS 주소를 파일에 출력
        myResolver = dns.resolver.Resolver()
        fdata = "%s : %s \n" %(time.ctime(), myResolver.nameservers)
        f.write(fdata)

    except:
        myResolver = dns.resolver.Resolver()
        fdata = "%s : %s, 로그인 실패 \n" % (time.ctime(), myResolver.nameservers)
        f.write(fdata)
        continue

    # 로그아웃
    driver.find_element_by_link_text("마이페이지").click()
    driver.find_element_by_link_text("로그아웃").click()

    time.sleep(10)

    driver.quit()

f.close()

