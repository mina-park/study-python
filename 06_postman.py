''' Postman > Basic Auth
	(첨부된 이미지 파일 참조 : 00_Postman_BasicAuth.JPG)
'''
import requests

s = requests.Session()
s.auth = ('postman', 'password')

r = s.get("https://echo.getpostman.com/basic-auth")
print(r.text)

