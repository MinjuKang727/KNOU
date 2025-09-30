from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from article import *
from Ttxt import Ttxt
import time
import os
import logging

# level: DEBUG/INFO/WARNING/ERROR/CRITICAL
logging.basicConfig(
    level=logging.INFO,
    filename='KNOU.log',
    filemode='w',
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)

# 번역 인스턴스 생성
ttxt = Ttxt()

# 노트 양식 문자열
intro = ""
note = ""
path = "C:/Users/UserK/Minjukang727/github/KNOU/mkLecNote"

with open(f'{path}/lec_intro.txt', 'r', encoding='utf-8') as f:
    intro = f.read()  # 강의 소개 양식

with open(f'{path}/lec_note.txt', 'r', encoding='utf-8') as f:
    note = f.read()  # 강의 노트 양식

# 크롬 웹 드라이버 실행
driver = webdriver.Chrome()
driver.get("https://ucampus.knou.ac.kr/")

# '더보기' 버튼 찾기
# 버튼의 XPath, ID, 클래스명 등으로 요소를 식별
# WebDriverWait는 페이지가 로드될 때까지 기다리는 역할을 함
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-login"))
    )

    # 로딩 오버레이가 사라질 때까지 최대 10초 동안 기다림
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "data-loading"))
    )
    
    # 버튼 클릭
    login_button.click()

    # 4. 아이디와 비밀번호 입력 필드 찾기
    # 웹페이지의 HTML 구조를 분석하여 input 박스의 name, id, class 등을 확인해야 합니다.
    # WebDriverWait는 요소가 로드될 때까지 최대 10초까지 기다립니다.
    wait = WebDriverWait(driver, 10)
    id_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    pw_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

    # 환경변수 설정한 아이디, 비밀번호 가져오기
    KNOU_ID = os.environ.get('KNOU_ID', 'U-KNOU ID')
    KNOU_PW = os.environ.get('KNOU_PW', 'U-KNOU PW')

    # 5. 아이디와 비밀번호 입력
    id_input.send_keys(KNOU_ID)
    pw_input.send_keys(KNOU_PW)
    pw_input.send_keys(Keys.ENTER)
    logging.info("KNOU 로그인 완료")

    # 강의명이 담긴 a태그가 로드 될 때까지 대기
    article_titles_kor = []
    article_titles_eng = []
    article_type_list = []
    article_total = 1
    i = 0
     
    while i < article_total:
        articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".lecture-progress-item")))
        article = articles[i].find_element(By.CSS_SELECTOR, ".lecture-info h3 a")

        if i == 0:
            article_total = len(articles)
            article_titles_kor = [article.find_element(By.CSS_SELECTOR, ".lecture-info h3 a").text for article in articles]
            article_titles_path = f"{path}/article_titles.txt"
            f_info = "강의 제목 파일 [article_titles.txt]"
            article_titles_eng, article_type_list = ttxt.titlesKor2Eng(article_titles_kor, 
                                                    article_titles_path, 
                                                    f_info,
                                                    ArticleType.NORMAL)
            # with open(f"{path}/article_titles.txt", 'r', encoding='utf-8') as f:
            #     title_list = f.read().strip().split("\n")
            #     article_titles_kor = title_list[::2]
            #     article_titles_eng = title_list[1::2]
            
            i = 6
            continue
        
        logging.info(f"[{article_titles_kor[i]}] 강의 크롤링 시작")
        
        # 강의 객체 생성
        cur_article = Article(article_titles_kor[i], article_titles_eng[i], ArticleType[article_type_list[i]], ttxt)
        # 강의 폴더 생성
        cur_article.mkFolder(intro)

        # 현재 강의 클릭
        article.click()

        # 강의 홈 버튼 로드 될 때까지 대기
        time.sleep(10)
        home_button = articles[i].find_element(By.CSS_SELECTOR, '.btns2 button')
        home_button.click()

        logging.info(f"[{article_titles_kor[i]}] 강의 소개 크롤링 시작")
        # 강의 기초 정보 가져오기
        lecture_basic_infos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".lecture-basic-info-body p")))
        # 강의 기초 정보 RDict에 적용
        cur_article.setRDict(cur_article.LEC_BASIC_INFO, lecture_basic_infos[0].text)
        cur_article.setRDict(cur_article.LEC_WEEKS, lecture_basic_infos[1].text)
        
        # 강의 개요 정보 가져오기
        content_block_bodys = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.content-block-body")))[1:4]
        lecture_body_info = content_block_bodys[0].find_elements(By.TAG_NAME, 'p')
        # 강의 개요 정보 RDict에 적용
        cur_article.setRDict(cur_article.LEC_BODY_INFO, lecture_body_info[0].text.replace("\n", "<br>"))
        
        if len(lecture_body_info) == 2:
            cur_article.setRDict(cur_article.LEC_BODY_PD, lecture_body_info[1].text)
        

        # 교수 소개 정보 가져오기
        professors = content_block_bodys[1].find_elements(By.CSS_SELECTOR, ".profile-info")
        prof_info_li = []

        for profile_info in professors:
            p_tags = profile_info.find_elements(By.TAG_NAME, 'p')
            p_name = p_tags[0].find_element(By.TAG_NAME, 'span').text
            prof_info_li.append(f"### {p_name}  \n> {p_tags[1].text}")

        professor_info = "<br><br>".join(prof_info_li)
        
        cur_article.setRDict(cur_article.PROF_INFO, "<br>\n> ".join(prof_info_li))

        # 교재 정보 추가
        # book_info_dict 키
        try:
            BOOK_IMG_SRC = "BOOK_IMG_SRC"
            BOOK_TITLE = "BOOK_TITLE"
            BOOK_INFO = "BOOK_INFO"
            BOOK_PRICE = "BOOK_PRICE"

            book_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".book-item")))
            book_info_form = f'<tr><td><img src="{BOOK_IMG_SRC}" alt="{BOOK_TITLE} 사진" style="width:80px;" /></td><td><h3>{BOOK_TITLE}</h3><p>{BOOK_INFO}</p><br><p>{BOOK_PRICE}</p></td></tr>'
            book_info_li = []

            for book in book_items:
                book_buy_info = book.find_element(By.CSS_SELECTOR, ".book-buy")
                book_buy_button = book_buy_info.find_element(By.CSS_SELECTOR, ".btn")

                book_cover_url = book.find_element(By.TAG_NAME, 'img').get_attribute('src')
                book_info_dict = {
                    BOOK_IMG_SRC: cur_article.downloadBookIMG(book_cover_url),
                    BOOK_TITLE: book.find_element(By.TAG_NAME, 'h3').text,
                    BOOK_INFO: book.find_element(By.CSS_SELECTOR, ".book-info p").text,
                    BOOK_PRICE: book_buy_info.text.replace(book_buy_button.text, "")
                }
                
                book_info = book_info_form
                for key, value in book_info_dict.items():
                    book_info = book_info.replace(key, value)
                book_info_li.append(book_info)

            cur_article.setRDict(cur_article.BOOK_INFO, "".join(book_info_li))
        except Exception as e:
            print(f"오류가 발생했습니다: {e}. 교재가 존재하지 않는 것으로 보고 다음으로 넘어갑니다.")
            cur_article.setRDict(cur_article.BOOK_INFO, "교재 없음")

        # 강의 목차 버튼 클릭
        lec_list_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-menu li:nth-child(2) a')))
        lec_list_button.click()
        logging.info(f"[{article_titles_kor[i]}] 강의 목차 크롤링 시작")

        # 강의 목차 리스트 정보 가져오기
        lecture_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3.lecture-title')))
        
        # 주차별 강의명 수집 및 노트 생성
        lec_title_list = []

        for t in lecture_list:
            lec_title_list.append(t.text)
        
        cur_article.setLecList(lec_title_list, note)
        cur_article.mkFileWithRDict(cur_article.title_eng, intro, cur_article.intro_rdict)
        logging.info(f"[{article_titles_kor[i]}] 강의 노트 작성 완료")

        myPage_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#gnb_top7')))
        myPage_button.click()
        i += 1
    
finally:
    # 작업 완료 후 브라우저 종료
    driver.quit()