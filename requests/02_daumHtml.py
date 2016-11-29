import urllib.request

if __name__ == "__main__":
	print("Hello World")
	req = urllib.request.Request("http://www.daum.net")
	data = urllib.request.urlopen(req).read()

	print(data)

	f = open("./02_daum_response_basic.html", "wb") # 주의! [01_daum.py] 파일과 옵션이 달라졌음. w->wb, binary 저장 옵션으로 변경
	f.write(data) # write하는 데이터도 str로 변환하지 않고, bytes 타입으로 바로 전달.
	f.close()
