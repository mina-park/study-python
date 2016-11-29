''' 게시판에서 이미지 있는 게시물 URL을 정대경로로 만들기 - ioi 김소혜 갤러리
	http://hurderella.tistory.com/108 
	http://hurderella.tistory.com/113
	http://hurderella.tistory.com/117
	http://hurderella.tistory.com/123
'''

import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
	print("Hello World")
	req = urllib.request.Request("http://gall.dcinside.com/board/lists/?id=kimsohye");
	data = urllib.request.urlopen(req).read()

#	print(data)

#	with open("./04_ioi_basic_response.html", "wb") as f:
#		f.write(data)

soup = BeautifulSoup(data, 'html.parser')
link = soup.find_all('a')
idx = 0
for s in link:
	try:
		prop = s.get('class')
		if prop != None and prop[0] == "icon_pic_n":
			url_info = s.get('href')
			if url_info[:4] != "http":
				url_info = "http://gall.dcinside.com" + url_info
			print("%s : %s" %(url_info, s.get_text()))

	except UnicodeEncodeError:
		print("Error : %d" %idx)
	
	finally:
		idx +=1

