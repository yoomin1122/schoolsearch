import os
from flask import Flask, render_template, redirect, url_for
from flask import request
import socket
from requests import get
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from datetime import datetime
from selenium import webdriver

schoolname = "송악고등학교"
app = Flask(__name__, template_folder='templates', static_folder='static')

if not os.path.isdir('./{}'.format("log")):

	os.mkdir('./{}'.format("log"))
	# current_dateTime = datetime.now(pytz.timezone('Asia/Seoul'))
current_dateTime = datetime.today().strftime('%Y-%m-%d %H-%M-%S')
f = open(f"./log/{current_dateTime}.txt", 'a')
print("version 1.0.0")

chrome_options = webdriver.ChromeOptions() #옵션 설정
chrome_options.add_argument("--incognito") #시크릿탭 설정
# chrome_options.add_argument("headless") #백그라운드에서 실행
driver = webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options) #크롬 드라이버 실행
driver.implicitly_wait(3)
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

@app.route('/', methods=['GET','POST'])
def wow():
    hostname = socket.gethostname()
    user_ip = socket.gethostbyname(hostname)
    return render_template('index.html')     



@app.route('/portfolio')
def readme():
    return redirect("https://www.yoomin.xyz")

@app.route('/inside',methods=['GET','POST'] )
def ing(methods=['GET','POST']):
    if request.method == 'POST':
          postbookname = request.form.get('searchhtml')
          #input칸을 xpath로 찾고 해당 input칸에 bookname 변수값을 넣어준뒤 enter키를 이용하여 실행
          booksnameinput = driver.find_element(By.XPATH, '//*[@id="searchCon2"]')
          booksnameinput.send_keys(postbookname)
          booksnameinput.send_keys(Keys.RETURN)

          bookslist = driver.find_element(By.XPATH, '//*[@id="searchData"]/div/div[3]/div/div[2]/div/p/span')
          bookslist = int(bookslist.text)
          
          if bookslist == 1: #책이 한 개만 검색이 되었을때 가장 마지막에 만들 예정
               print("책이 한개 검색되었습니다")
               print("=============================================================")
               f.write(f"책이 한개 검색되었습니다 \n")
               f.write("============================================================= \n")
          elif 0 >= bookslist: #책이 하나도 없을때
               print(f"{postbookname}라는 책을 찾을 수 없습니다. 다시 검색 해주시기 바랍니다")
               f.write(f"{postbookname}라는 책을 찾을 수 없습니다. 다시 검색 해주시기 바랍니다 \n")
               f.close()
               driver.quit()
               exit()
          else: #책이 2개 이상 검색이 되었을때
               print(f"{bookslist}만큼 검색되었습니다")
               f.write(f"{bookslist}만큼 검색되었습니다 \n")
               f.write("============================================================= \n")
               print("=============================================================")

               j = 0
 
               bookname = []
               bookmake = []
               bookPublisher = []
               bookNumber = []
               bookloan = []
               time.sleep(2)
               for i in range(1, bookslist+1):
                    try:
                         print(i)
                         #책 이름
                         
                         bookname.append(driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[2]/a/span').get_attribute("innerHTML"))
                         print("책 이름 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[2]/a/span').get_attribute("innerHTML"))
                         f.write("책 이름 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[2]/a/span').get_attribute("innerHTML") + "\n")

                         #책 저자
                         
                         bookmake.append(driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[1]/span[2]').text)
                         print("저자  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[1]/span[2]').text)
                         f.write("저자  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[1]/span[2]').text + "\n")

                         #책 출판사
                         
                         bookPublisher.append(driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[2]/span[2]').text)
                         print("출판사  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[2]/span[2]').text)
                         f.write("출판사  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[2]/span[2]').text + "\n")

                         #책 청구기호
                         
                         bookNumber.append(driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[3]/span[2]').text)
                         print("책 번호  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[3]/span[2]').text)
                         f.write("책 번호  : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[3]/div[3]/span[2]').text + "\n")

                         #대출 가능 여부(대출가능일때)\
                         
                         bookloan.append(driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/div').get_attribute("innerHTML"))
                         print("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/div').get_attribute("innerHTML"))
                         f.write("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/div').get_attribute("innerHTML") + "\n")
                         print("=============================================================")
                         f.write("============================================================= \n")
                    except:


                         #대출 가능 여부(대출중일때)

                         bookloan.append(driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/p').text)
                         f.write("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/p').text + "\n")
                         f.write("=============================================================\n")
                         print("대출 가능 여부 : " + driver.find_element(By.XPATH, f'//*[@id="searchData"]/div/div[3]/div/div[4]/ul[{i}]/li/div[4]/div/p').text)
                         print("=============================================================")



                    

               f.close()
               print(bookname)
               print(bookmake)
               print(bookPublisher)
               print(bookNumber)
               print(bookloan)   
          return render_template('search.html', postbookname = postbookname, bookslist = int(bookslist), bookname = bookname, bookmake = bookmake, bookPublisher = bookPublisher, bookNumber = bookNumber, bookloan=bookloan)
    else:
          return render_template('search.html')

@app.route('/read',methods=['GET','POST'] )
def soundgood(methods=['GET','POST']):


    return render_template('readme.html')

@app.route('/privacy',methods=['GET','POST'] )
def ohmygod(methods=['GET','POST']):

    return render_template('privacy.html')

# app name
@app.errorhandler(404)
def not_found(e):
  
  return render_template("404.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1234))
    (app.run(host='0.0.0.0', port=port, debug=True))
