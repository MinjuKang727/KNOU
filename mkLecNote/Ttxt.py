from deep_translator import GoogleTranslator
from pykospacing import Spacing
from article import ArticleType
import re
import logging
import os

class Ttxt:
    def __init__(self):
        # level: DEBUG/INFO/WARNING/ERROR/CRITICAL
        logging.basicConfig(
            level=logging.INFO,
            filename='KNOU.log',
            filemode='w',
            format='[%(asctime)s] [%(levelname)s] %(message)s'
        )

        # 띄어쓰기 복원기 초기화
        self.spacing = Spacing()
        # Translator 객체 생성
        self.translatorKo2En = GoogleTranslator(source='ko', target='en')
        self.translatorEn2Ko = GoogleTranslator(source='en', target='ko')
        

    # 번역 메서드: 한영
    def kor2eng(self, text) :
        corrected = self.spacing(text)
        return self.translatorKo2En.translate(corrected)
    
    # 번역 메서드: 영한
    def eng2kor(self, text):
        return self.translatorKo2En.translate(text)

    # '0강' -> '00강' 치환 메서드
    def replaceNum(self, match):
        str1 = match.group(1)
        str2 = match.group(2)
        if str1.isdigit():
            return f"{int(str1):02d} "
        elif str2.isdigit():
            return f"{str1}{int(str2):02d}"

    # 문자열 정리 메서드
    def arrangeNameKor2Eng(self, text):
        text = re.sub(r'C\+\+', 'Cpp', text)
        text = re.sub(r'(\d+)(강.)', self.replaceNum, text)
        text = re.sub(r'(\w+)\s*(?:\[(\d+)\]|\((\d+)\))', r'\1\2', text)
        text = re.sub(r'[^a-zA-Z0-9가-힣!?]+', ' ', text)
        text = re.sub(r'(Unit)\s+(\d+)', self.replaceNum, text)
        text = self.kor2eng(text)
        text = re.sub(r'Part\s+(I|II|III|IV|V)', r'Part\1', text)
        text = re.sub(r'\s+', '_', text)
        return text

    # 한글 문자열 정리 결과가 마음에 드는지 확인하기 위한 메서드
    def askIsOK(self, text, arranged, cnt=0):
        if cnt > 3:
            logging.info(f"3회 안에 결정하지 못하여 [{text}]를 반환합니다.")
            return text

        answer = input(f"[{text}]를 [{arranged}]로 바꿔도 괜찮으십니까? (y/n)\n").lower()
        
        if answer == 'y' or answer == '':
            return arranged
        elif answer == 'n':
            arranged = input(f"[{text}]를 어떻게 수정하고 싶으십니까?\n")
            return self.askIsOK(text, arranged, cnt + 1)
        else:
            return self.askIsOK(text, answer, cnt + 1)

    # 제목 한영 변환
    def titlesKor2Eng(self, title_list_kor, path, f_info, type: ArticleType):
        title_list_eng = []
        title_type_list = []

        with open(path, 'w', encoding='utf-8') as f:
            for title_kor in title_list_kor:
                title_eng = self.arrangeNameKor2Eng(title_kor)  # 강의 제목(영어)
                title_list_eng.append(title_eng)

                if type == ArticleType.LECTURE:
                    f.write(f"{title_kor}\n{title_eng}\n")
                else:
                    f.write(f"{title_kor}\n{title_eng}\n{type.name}\n")
        
        input(f"(임의의 문자가 입력될 때까지 대기 중...)\n'{f_info}' 수정을 완료하였습니까?")
      
        with open(f"{path}", 'r', encoding='utf-8') as f:
            content = f.read().strip().split("\n")
            
            if type == ArticleType.LECTURE:
                title_list_eng = content[1::2]
            else:
                title_list_eng = content[1::3]
                title_type_list = content[2::3]
        
        try:
            os.remove(path)
        except:
            logging.warning(f"'{path}' 파일이 존재하지 않습니다.")

        if type == ArticleType.LECTURE:
            return title_list_eng
        else:
            return title_list_eng, title_type_list