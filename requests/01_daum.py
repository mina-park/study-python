import urllib.request

if __name__ == "__main__":
	print("Hello World")
	req = urllib.request.Request("http://www.daum.net") # urllib.request.Request : URL 요청과 관련한 정보를 담고 있는 추상화된 클래스. 헤더값 설정, 컨텐츠 타입 설정 등을 할 수 있음.
	data = urllib.request.urlopen(req).read() # urllib.request.urlopen : URL을 입력 받거나 Request 객체를 입력 받음.

	print(data)

	f = open("./01_daum_response.txt", "w")
	f.write(str(data))
	f.close()
