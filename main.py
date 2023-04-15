#2023년 4월 15일 작동 하는지 잘 모름

#사용되고 있는 것들이 뭔지 모르겠지만 일단은 다 넣어놓고 오픈 직전에 정리 할 예정
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from selenium import webdriver
import pytz
import os

schoolname = "송악고등학교"
booksname = "파이썬"

def booksearcher():
	if not os.path.isdir('./{}'.format("log")):

		os.mkdir('./{}'.format("log"))
	# current_dateTime = datetime.now(pytz.timezone('Asia/Seoul'))
	current_dateTime = datetime.today().strftime('%Y-%m-%d %H-%M-%S')
	f = open(f"./log/{current_dateTime}.txt", 'a')
	print("version 1.0.0")

	# 학교 이름, 책 이름 변수 값 설정


	#크롬 드라이버 실행(그대신 개인정보 보안을 위해 시크릿탭을 이용하여 접속)
	chrome_options = webdriver.ChromeOptions() #옵션 설정
	chrome_options.add_argument("--incognito") #시크릿탭 설정
	chrome_options.add_argument("headless") #백그라운드에서 실행
	driver = webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options) #크롬 드라이버 실행
	driver.get("https://reading.edus.or.kr/r/newReading/search/schoolListForm.jsp") #사이트 서치
	assert "우리학교자료검색 | 독서교육종합시스템입니다." in driver.title #타이틀이 맞는지 확인

	#input칸 id를 이용하여 찾고, 학교 이름 검색 후 enter키 입력
	schnamesearchinput = driver.find_element(By.XPATH, '//*[@id="schoolSearch"]') 
	schnamesearchinput.send_keys(schoolname)
	schnamesearchinput.send_keys(Keys.RETURN)

	#문제가 생길 수도 있으니 time.sleep을 이용하여 텀 가지기
	time.sleep(2)

	#id가 없어서 xpath를 이용하여 해당 경로 click
	a = driver.find_element(By.XPATH, '//*[@id="schoolData"]/div[3]/section/div[3]/ul/li[2]/div/div[2]/a').click()

	#문제가 생길 수도 있으니 time.sleep을 이용하여 텀 가지기
	time.sleep(3)

	#input칸을 xpath로 찾고 해당 input칸에 bookname 변수값을 넣어준뒤 enter키를 이용하여 실행
	booksnameinput = driver.find_element(By.XPATH, '//*[@id="searchCon2"]')
	booksnameinput.send_keys(booksname)
	booksnameinput.send_keys(Keys.RETURN)

	#문제가 생길 수도 있으니 time.sleep을 이용하여 텀 가지기
	time.sleep(2)
	bookslist = driver.find_element(By.XPATH, '//*[@id="searchData"]/div/div[3]/div/div[2]/div/p/span')
	bookslist = int(bookslist.text)

	if bookslist == 1: #책이 한 개만 검색이 되었을때 가장 마지막에 만들 예정
		print("책이 한개 검색되었습니다")
		print("=============================================================")
		f.write(f"책이 한개 검색되었습니다 \n")
		f.write("============================================================= \n")
	elif 0 >= bookslist: #책이 하나도 없을때 
		print(f"{booksname}라는 책을 찾을 수 없습니다. 다시 검색 해주시기 바랍니다")
		f.write(f"{booksname}라는 책을 찾을 수 없습니다. 다시 검색 해주시기 바랍니다 \n")
		f.close()
		exit()
	else: #책이 2개 이상 검색이 되었을때
		print(f"{bookslist}만큼 검색되었습니다")
		f.write(f"{bookslist}만큼 검색되었습니다 \n")
		f.write("============================================================= \n")
		print("=============================================================")
		i = 1

		while bookslist >= i:
			try:
				#책 이름
				bookname = driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[2]/a/span').get_attribute("innerHTML")
				print("책 이름 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[2]/a/span').get_attribute("innerHTML"))
				f.write("책 이름 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[2]/a/span').get_attribute("innerHTML") + "\n")

				#책 저자
				bookmake = driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[1]/span[2]').text
				print("저자  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[1]/span[2]').text)
				f.write("저자  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[1]/span[2]').text + "\n")

				#책 출판사
				bookPublisher = driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[2]/span[2]').text
				print("출판사  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[2]/span[2]').text)
				f.write("출판사  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[2]/span[2]').text + "\n")

				#책 청구기호
				bookNumber = driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[3]/span[2]').text
				print("책 번호  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[3]/span[2]').text)
				f.write("책 번호  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[3]/span[2]').text + "\n")

				#대출 가능 여부(대출가능일때)
				bookloan = driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/div').get_attribute("innerHTML")
				print("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/div').get_attribute("innerHTML"))
				f.write("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/div').get_attribute("innerHTML") + "\n")
				print("=============================================================")
				f.write("============================================================= \n")
			except:
				

				#대출 가능 여부(대출중일때)
				bookloan = driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/p').text
				f.write("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/p').text + "\n")
				f.write("=============================================================\n")
				print("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/p').text)
				print("=============================================================")


			i += 1
		f.close()
		driver.quit()

