import os
import requests
import logging
from enum import Enum

class ArticleType(Enum):
    NORMAL = "일반"
    CODE = "코드"
    LECTURE = "주차별 강의"


# ====================================================================
# Article클래스 : 강의 클래스
# ====================================================================
class Article:

    def __init__(self, title_kor, title_eng, article_type: ArticleType, ttxt):
        # level: DEBUG/INFO/WARNING/ERROR/CRITICAL
        logging.basicConfig(
            level=logging.INFO,
            filename='KNOU.log',
            filemode='w',
            format='[%(asctime)s] [%(levelname)s] %(message)s'
        )
        
        self.title_kor = title_kor.strip()  # 강의 제목(한글)
        self.title_eng = title_eng.strip()  # 강의 제목(영문)

        self.article_type = article_type
        self.ttxt = ttxt

        thisSemester = "2025_Freshman_2ndSem_"
        self.PATH =  f"C:/Users/UserK/Minjukang727/github/KNOU/{thisSemester}/{self.title_eng}"  # 강의 저장할 경로 설정

        self.lec_list = []   # 강의 인스턴스 리스트

        self.TITLE_KOR = "TITLE_KOR"
        self.LEC_BASIC_INFO = "LECTURE_BASIC_INFO"
        self.LEC_WEEKS = "LECTURE_WEEKS"
        self.LEC_BODY_INFO = "LECTURE_BODY_INFO"
        self.LEC_BODY_PD = "LECTURE_BODY_PRODUCER"
        self.PROF_INFO = "PROFESSOR_INFO"
        self.BOOK_INFO = "BOOK_INFO"
        self.LEC_LIST = "LECTURE_LIST"


        # 노트 작성을 위한 replace 사전
        self.intro_rdict = {
            self.TITLE_KOR: self.title_kor,
            self.LEC_BASIC_INFO: "",
            self.LEC_WEEKS: "",
            self.LEC_BODY_INFO: "",
            self.LEC_BODY_PD: "",
            self.PROF_INFO: "",
            self.BOOK_INFO: "",
            self.LEC_LIST: ""
        }

    # 강의 폴더 만들기
    def mkFolder(self, intro):
        print(f"'{self.title_kor}'의 강의 폴더 만들기를 시작합니다.")
        
        IMG_FOLDER = "IMGs"
        HOMEWORK_FOLDER = "HW"
        
        # 경로를 현재 강의 폴더로 수정
        fNames = [IMG_FOLDER, HOMEWORK_FOLDER]

        for fName in fNames:
            os.makedirs(f"{self.PATH}/{fName}", exist_ok=True)
            
        # 강의 소개 마크다운 파일 만들기
        self.mkFile(self.title_eng, intro)


    # 파일 생성 메서드
    def mkFile(self, title, content, lec_order=0):
        path = self.PATH

        if self.article_type == ArticleType.CODE:
            if lec_order != 0:
                path = f"{path}/LECTURE{lec_order:02d}"
            CODE_FOLDER = "Code"
            IMGs_FOLDER = "IMGs"
            dirs = [CODE_FOLDER, IMGs_FOLDER]
            
            for dir in dirs:
                os.makedirs(f"{path}/{dir}", exist_ok=True)
                
        f_name = f"{title}.md"  # 파일명
        f_path = f"{path}/{f_name}"  # 파일 경로

        if not os.path.exists(f_name):
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            logging.warning(f"이미 '{title}' 파일이 존재합니다.")
    
    # 노트 내용 rdict 참조하여 수정한 파일 생성
    def mkFileWithRDict(self, title, content, rdict, lec_order=0):
        for key, value in rdict.items():
                content = content.replace(key, value)
        
        self.mkFile(title, content, lec_order)


    # intro replace 사전 작성
    def setRDict(self, key, value):
        self.intro_rdict[key] = value       

    # set 주차 강의 목차 리스트
    def setLecList(self, lec_list_kor, note) : 
        lec_titles_path = f"{self.PATH}/lec_titles.txt"
        f_info = "주차별 강의 제목 파일 [lec_titles.txt]"
        lec_list_eng = self.ttxt.titlesKor2Eng(lec_list_kor, lec_titles_path, f_info, ArticleType.LECTURE)  

        rdict_lec_list = []

        for i, (title_kor, title_eng) in enumerate(zip(lec_list_kor, lec_list_eng)):
            # 주차 강의 인스턴스 생성
            lec_note = Note(self, title_kor, title_eng, i + 1)
            self.lec_list.append(lec_note)
            pre_lec = self.lec_list[i - 1]

            if i == 0:
                self.setPreOf1stLec()
            elif i:
                pre_lec.setNextLec(lec_note)

            if i > 0:
                self.mkFileWithRDict(pre_lec.title_eng, note, pre_lec.rdict, pre_lec.lec_order)
                rdict_lec_list.append(self.getMDLecPath(pre_lec))

            if i == len(lec_list_kor) - 1:
                self.mkFileWithRDict(lec_note.title_eng, note, lec_note.rdict, lec_note.lec_order)
                rdict_lec_list.append(self.getMDLecPath(lec_note))
            
        self.setRDict(self.LEC_LIST, "".join(rdict_lec_list))


    # 주차별 강의 상대 경로 가져오기
    def getMDLecPath(self, lec):
        rel_path = ""

        if self.article_type == ArticleType.CODE:
            rel_path = f"[{lec.title_kor}](./LECTURE{lec.lec_order:02d}/{lec.title_eng}.md)  \n"
        elif self.article_type == ArticleType.NORMAL:
            rel_path = f"[{lec.title_kor}](./{lec.title_eng}.md)  \n"
        
        return rel_path

    def downloadBookIMG(self, image_url):
        # 이미지 저장 경로
        IMG_PATH = f"{self.PATH}/IMGs/book_cover.png"
        RELATIVE_IMG_PATH = IMG_PATH.replace(self.PATH, '.')  # 상대 경로

        # requests로 이미지 데이터를 가져옴
        response = requests.get(image_url)

        # 'wb' 모드로 파일을 열어 바이너리 데이터를 그대로 씁니다.
        with open(IMG_PATH, "wb") as f:
            f.write(response.content)

        logging.info("책 표지 사진 다운로드 및 저장 완료.")
        return RELATIVE_IMG_PATH

    def setPreOf1stLec(self):
        lec = self.lec_list[0]
        if self.article_type == ArticleType.NORMAL:
            lec.rdict[lec.PRE_LEC_INFO] = f"[{self.title_kor}](./{self.title_eng}.md)"
        elif self.article_type == ArticleType.CODE:
            lec.rdict[lec.PRE_LEC_INFO] = f"[{self.title_kor}](../{self.title_eng}.md)"


# ====================================================================
# Note클래스 : 주차별 강의 정보를 담은 클래스
# ====================================================================
class Note:
    def __init__(self, article, title_kor, title_eng, lec_order):
        self.article = article
        self.article_type = article.article_type

        self.title_kor = title_kor.strip()
        self.title_eng = title_eng.strip()
        self.lec_order = lec_order

        self.PATH = f"{self.article.PATH}/lecture{lec_order:02d}"

        self.pre_lec = None
        self.next_lec = None
        
        self.LEC_TITLE_KOR = "LECTURE_TITLE_KOR"
        self.LEC_TITLE_ENG = "LECTURE_TITLE_ENG"
        self.PRE_LEC_INFO = "PREVIOUS_LECTURE_INFO"
        self.NEXT_LEC_INFO = "NEXT_LECTURE_INFO"    
        self.LEC_ORDER = "LECTURE_ORDER"
        self.END_NEXT = "완강 (END)"
        
        # 노트 내용 입력용 replace 사전
        self.rdict = {
            self.PRE_LEC_INFO: "",
            self.LEC_TITLE_KOR: title_kor,
            self.NEXT_LEC_INFO: self.END_NEXT
        }
            
            

    # 이전 강의 설정
    # def setPreLec(self, pre_lec):
    #     self.pre_lec = pre_lec

    #     if self.article_type == ArticleType.NORMAL:
    #         self.rdict[self.PRE_LEC_INFO] = f"[{pre_lec.title_kor}](./{pre_lec.title_eng}.md)"
    #     elif self.article_type == ArticleType.CODE:
    #         self.rdict[self.PRE_LEC_INFO] = f"[{pre_lec.title_kor}](../lecture{self.lec_order - 1:02d}/{pre_lec.title_eng}.md)"
            
    


    # 다음 강의 설정
    def setNextLec(self, next_lec):
        self.next_lec = next_lec
        next_lec.pre_lec = self

        if self.article_type == ArticleType.NORMAL:
            self.rdict[self.NEXT_LEC_INFO] = f"[{next_lec.title_kor}](./{next_lec.title_eng}.md)"
            next_lec.rdict[self.PRE_LEC_INFO] = f"[{self.title_kor}](./{self.title_eng}.md)"
        elif self.article_type == ArticleType.CODE:
            self.rdict[self.NEXT_LEC_INFO] = f"[{next_lec.title_kor}](../lecture{self.lec_order + 1:02d}/{next_lec.title_eng}.md)"
            next_lec.rdict[self.PRE_LEC_INFO] = f"[{self.title_kor}](../lecture{self.lec_order:02d}/{self.title_eng}.md)"

    
    # def mkFileWithRDict(self, title, content, rdict):
    #     for key, value in rdict.items():
    #             content = content.replace(key, value)
        
    #     self.mkFile(title, content, self.PATH)