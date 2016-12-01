'''
	참고 URL : http://selenium-python.readthedocs.io/getting-started.html
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys	# RETURN, F1, ALT 등과 같은 키보드의 특수키 동작 제공

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver = webdriver.Ie()

driver.get("http://www.python.org")	# 웹드라이버는 페이지가 모두 로드될때까지 기다림.(예외: AJAX)
assert "Python" in driver.title		# title에 "Python" 단어가 있음을 확인. 없으면 AssertionError 발생
elem = driver.find_element_by_name("q") # name="q"인 요소 찾기
elem.clear() # input field에 혹시 있을지 모를 기존 text 삭제
elem.send_keys("pycon") # input field에 "pycon" 입력
elem.send_keys(Keys.RETURN) # Keys 클래스를 사용하여 Return 키값 보내기
assert "No results found." not in driver.page_source # page_source가 없지 않음을 확인.
driver.close() #close() : browser window 닫기. 탭이 여러개라면 해당 탭만 닫기. 탭이 한개라면 브라우저 닫기.
# 탭 수와 상관없이 브라우저를 닫고 싶다면 quit() 사용.
