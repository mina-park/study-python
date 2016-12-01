'''
	참고 : http://yumere.tistory.com/75
	http://selenium-python.readthedocs.io/api.html
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

#driver.maximize_window()
driver.set_window_size(1000, 800)


# 네이버 로그인 시도
driver.get("http://www.naver.com")
elem = driver.find_element_by_name("id")
elem.clear()
elem.send_keys("user_id")
elem = driver.find_element_by_name("pw")
elem.clear()
elem.send_keys("user_pw")
elem.send_keys(Keys.RETURN)

#time.sleep(5)
driver.implicitly_wait(5)

# 네이버 검색
#driver.get("http://www.naver.com")
driver.back()
elem_search = driver.find_element_by_id("query")
elem_search.clear()
elem_search.send_keys("최순실 게이트")
#elem_search.send_keys(Keys.RETURN)
driver.find_element_by_id("search_btn").click()

#time.sleep(5)

driver.get_screenshot_as_file("./naver.jpg")

driver.close()

