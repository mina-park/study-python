'''
	참고 : http://yumere.tistory.com/75
			 http://selenium-python.readthedocs.io/api.html
			 http://selenium-python.readthedocs.io/waits.html
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

#driver.maximize_window()
driver.set_window_size(1000, 800)

driver.get("http://www.naver.com")

# 네이버 오른쪽 중앙 "투데이" 항목이 뜰 때까지 대기
elem = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, 'ws_tsq'))
		)

assert "NAVER" in driver.title


# 네이버 로그인 시도
elem_login = driver.find_element_by_name("id")
elem_login.clear()
elem_login.send_keys("user_id")
elem_login = driver.find_element_by_name("pw")
elem_login.clear()
elem_login.send_keys("user_pw")
elem_login.send_keys(Keys.RETURN)

driver.implicitly_wait(5)


# 네이버 검색창 하단의 자동검색어 3개 클릭
driver.get("http://www.naver.com")
for idx in range(1, 4):
	elem_xpath = '//*[@id="qu_txt"]/span[%d]/a' %idx
	driver.find_element_by_xpath(elem_xpath).click()
	time.sleep(5)
	driver.back()

# 네이버에 검색어 입력하여 검색
elem_search = driver.find_element_by_id("query")
elem_search.clear()
elem_search.send_keys("촛불집회")
#elem_search.send_keys(Keys.RETURN)
driver.find_element_by_id("search_btn").click()

assert "네이버 통합검색" in driver.title

# 검색 결과 화면캡쳐
driver.get_screenshot_as_file("./naver.jpg")

# 검색 결과의 첫번째 뉴스 클릭
driver.find_element_by_xpath('//*[@id="sp_nws_all1"]/dl/dt/a').click()
assert "촛불집회" in driver.title
time.sleep(5)

driver.quit()

