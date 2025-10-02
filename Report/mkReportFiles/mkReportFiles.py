from enum import Enum
import logging
import os


logging.basicConfig(
    level=logging.INFO,
    filename='MK_KNOU_REPORT.log',
    filemode='w',
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)
        

class AssignmentType(Enum):
    MIDTERM = "중간과제물",
    OFFLINE_CLASS = "출석수업과제물"

class ReportType(Enum):
    COMMON = "공통형",
    SPECIFIC = "지정형"

YEAR = "YEAR"  # 학년도
SEMESTER = "SEMESTER"  # 학기
GRADE = "GRADE"  # 학년
ASSIGNMENTS = "ASSIGNMENTS"  # 과제 유형: 중간과제물/출석수업과제물/...
TITLE = "TITLE"  # 교과목명
REPORT_TYPE = "REPORT_TYPE"  # 과제 유형: 공통형/지정형
STUD_NUM = "STUDENT_NUMBER"
STUD_NAME = "STUDENT_NAME"
TEL_NUM = "TELEPHONE_NUMBER"

# 과제 및 학생 정보 사전
report_info = {
    STUD_NUM: "202334-153914",  # 학번
    STUD_NAME: "강민주",  # 이름
    TEL_NUM: "010-8733-8662",  # 전화번호
    YEAR: "2025",  # 학년도
    GRADE: "1",  # 학년
    SEMESTER: "2",  # 학기
    ASSIGNMENTS: AssignmentType.MIDTERM.value[0],  # 중간과제물/출석수업과제물
    TITLE: "",  # 강의 제목
    REPORT_TYPE: ""  # 과제 유형: 공통형/지정형
}


ARTICLE_TITLE_LIST = []  # 과제 과목명 리스트
REPORT_TYPE_LIST = []  # 과제 과제유형 리스트

knou_path = f"C:/Users/UserK/Minjukang727/github/KNOU"  # 기본 경로
fName = f"{report_info[YEAR]}_{report_info[GRADE]}y_{report_info[SEMESTER]}s"  # 폴더명: 학년도_학년y_학기s
folder_name = report_info[ASSIGNMENTS]  # 폴더명: 중간과제물 or 출석수업과제물


path = f"{knou_path}/Report/{fName}/{report_info[ASSIGNMENTS]}"  # 레포트 저장할 경로
os.makedirs(path, exist_ok=True)  # 폴더 생성
path


reports_file = "reports.txt"  # 과제 유형 받을 텍스트 파일
f_path = f"{path}/{reports_file}"  # 텍스트 파일 생성할 경로
note_path = f"{knou_path}/{report_info[YEAR]}_{report_info[GRADE]}_{report_info[SEMESTER]}"  # 현재 수강중인 과목명을 가져오기 위한 강의 노트 폴더가 저장된 폴더 경로
article_folder_list = os.listdir(note_path)  # note_path에 저장된 폴더명 리스트

# 강의 소개 md 파일에서 현재 수강중인 과제명 가져오기
# note_path 경로에서 강의명/강의명.md 경로로 강의 소개 md 파일 저장되어 있음
# 강의 소개 md 파일에서 첫번째 줄이 '# 강의 제목'
for article_folder in article_folder_list:
    with open(f"{note_path}/{article_folder}/{article_folder}.md", 'r', encoding='utf-8') as f:
        article_title = f.readline().strip()[2:]  # 한 줄씩 읽어 첫째줄 가져옴. 문장 처음의 '# '을 슬라이싱
        ARTICLE_TITLE_LIST.append(article_title)


# 과목명\n과제유형을 담은 txt 파일 작성
if not os.path.exists(reports_file):
    with open(f_path, 'w', encoding='utf-8') as f:
        for article_title in ARTICLE_TITLE_LIST:
            f.write(f"{article_title}\n{ReportType.COMMON.value[0]}\n")

input(f"과제물 과목명 및 유형 파일 [reports.txt]를 모두 수정하였습니까?")

# 과제 유형 가져오기
with open(f_path, 'r', encoding='utf-8') as f:
    report_info_list = f.read().strip().split("\n")
    ARTICLE_TITLE_LIST = report_info_list[::2]
    REPORT_TYPE_LIST = report_info_list[1::2]


# 레포트 커버 양식 가져오기
form_path = f"{knou_path}/Report/Cover/Report_form.md"
report_form = ""
with open(form_path, 'r', encoding='utf-8') as f:
    report_form = f.read()


for title, report_type in zip(ARTICLE_TITLE_LIST, REPORT_TYPE_LIST):
    report_info[TITLE] = title
    report_info[REPORT_TYPE] = report_type
    content = report_form

    for key, value in report_info.items():
        content = content.replace(key, value)

    report_name = f"{report_info[ASSIGNMENTS]}_{title}_{report_info[STUD_NUM]}.md"
    report_path = f"{path}/{report_name}"
    if not os.path.exists(report_name):
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)

try:
    os.remove(f_path)
except FileNotFoundError:
    logging.warning("삭제할 파일이 존재하지 않습니다.")
except Exception as e:
    logging.error(f"파일 삭제 중 예외 발생: {e}")