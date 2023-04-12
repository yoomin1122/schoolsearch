#사용되고 있는 것들이 뭔지 모르겠지만 일단은 다 넣어놓고 오픈 직전에 정리 할 예정
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver



# 학교 이름, 책 이름 변수 값 설정
schoolname = "학교 이름"
booksname = "책 이름"

#크롬 드라이버 실행(그대신 개인정보 보안을 위해 시크릿탭을 이용하여 접속)
chrome_options = webdriver.ChromeOptions() #옵션 설정
chrome_options.add_argument("--incognito") #시크릿탭 설정
driver = webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options) #크롬 드라이버 실행
driver.get("https://reading.edus.or.kr/r/newReading/search/schoolListForm.jsp") #사이트 서치
assert "우리학교자료검색 | 독서교육종합시스템입니다." in driver.title #타이틀이 맞는지 확인

#input칸 id를 이용하여 찾고, 학교 이름 검색 후 enter키 입력
schnamesearchinput = driver.find_element(By.ID, 'schoolSearch') 
schnamesearchinput.send_keys(schoolname)
schnamesearchinput.send_keys(Keys.RETURN)

#문제가 생길 수도 있으니 time.sleep을 이용하여 텀 가지기
time.sleep(3)

#id가 없어서 xpath를 이용하여 해당 경로 click
a = driver.find_element(By.XPATH, '//*[@id="schoolData"]/div[3]/section/div[3]/ul/li[2]/div/div[2]/a').click()


#문제가 생길 수도 있으니 time.sleep을 이용하여 텀 가지기
time.sleep(3)

#input칸을 xpath로 찾고 해당 input칸에 bookname 변수값을 넣어준뒤 enter키를 이용하여 실행
booksnameinput = driver.find_element(By.XPATH, '//*[@id="searchCon2"]')
booksnameinput.send_keys(booksname)
booksnameinput.send_keys(Keys.RETURN)

#실행이 완료되어도 크롬 드라이버가 꺼지지 않게 true pass해놓음.
while(True):
    	pass
