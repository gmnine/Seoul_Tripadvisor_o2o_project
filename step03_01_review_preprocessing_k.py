#---------------/ 라이브러리 설치, 패키지 불러오기 /---------------
import time

import pandas as pd
import re
import kss
from pykospacing import Spacing
from hanspell import spell_checker
from soynlp.normalizer import *
from tqdm import tqdm

# 우분투 환경에서도 돌아가게 하기 위함
spacing = Spacing()

punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-",
                 "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity',
                 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi',
                 '\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': '',}

#-----------------------/ def 함수 /--------------------------
#------------------- 파일 업데이트 및 저장하기 --------------------
# def update_file_processed_review(processed_review):
#     # file_clean_review_csv.write(' '.join(processed_review))
#     # file_clean_review_csv.write("\n")
#     print("update_file_processed_review")

def sentence_strip(lines):
    sentence_tokenized_text = []
    # for i, line in enumerate(lines):
    #     if i > 5:     # 전체 wikipedia 문서는 사이즈가 크므로, 일부만 테스트.
    #         break

    line = lines.strip()
    for sent in kss.split_sentences(line):
        sentence_tokenized_text.append(sent.strip())

    return sentence_tokenized_text

def clean_punc(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])

    for p in punct:
        text = text.replace(p, f' {p} ')

    # specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    # for s in specials:
    #     text = text.replace(s, specials[s])
    #print('clean_punc')

    return text.strip()

def clean_text(texts):
    corpus = []
    for i in range(0, len(texts)):
        review = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '',str(texts[i])) #remove punctuation
        review = re.sub(r'\d+','', review)# remove number
        review = review.lower() #lower case
        review = re.sub(r'\s+', ' ', review) #remove extra space
        review = re.sub(r'<[^>]+>','',review) #remove Html tags
        review = re.sub(r'\s+', ' ', review) #remove spaces
        review = re.sub(r"^\s+", '', review) #remove space from start
        review = re.sub(r'\s+$', '', review) #remove space from the end
        corpus.append(review)
    return corpus

# ------------------------ 외래어 사용시 주석 해제 ---------------------------
def spell_check_text(texts):
    corpus = []
    for sent in texts:
        spacing_text = spacing(sent)
        spelling_text = spell_checker.check(spacing_text)
        checked_spelling = spelling_text.checked
        normalized_sent = repeat_normalize(checked_spelling)
        for lownword in lownword_map:
            normalized_sent = normalized_sent.replace(lownword, lownword_map[lownword])
        corpus.append(normalized_sent)
    return corpus

def rm_emoji(data):
    return data.encode('euc-kr','ignore').decode('euc-kr')

#-------------------/ 호출 및 코드 실행 /-------------------
# file_clean_review_csv = open("/pythonProject/step03_data_travel_processed_review.csv", "a", encoding="utf-8")

#----------------- Basic PreProcessing -----------------
# data = open("/Users/gmnine/Pycharm_Projects/pythonProject/step02_02_data_travel_review_k_sample.csv", "r", encoding="utf-8")
# total_lines = data.readlines()

#data = pd.read_csv("/Users/gmnine/Pycharm_Projects/pythonProject/step02_02_data_travel_review_k.csv", index_col=0)

#------------------------------- 위의 경로의 데이터를 4개의 파일로 데이터 분산처리 -------------------------------
# file_src = "/Users/gmnine/Pycharm_Projects/pythonProject/step02_02_data_travel_review_k1.csv"
# file_dst = "/Users/gmnine/Pycharm_Projects/pythonProject/step02_02_data_travel_review_k1_ppc.csv"

# file_src = "/Users/gmnine/Pycharm_Projects/pythonProject/step02_02_data_travel_review_k2.csv"
# file_dst = "/Users/gmnine/Pycharm_Projects/pythonProject/step02_02_data_travel_review_k2_ppc.csv"

file_src = "/pythonProject/csv_file/step02_02_data_travel_review_k3.csv"
file_dst = "/pythonProject/csv_file/step02_02_data_travel_review_k3_ppc.csv"

data = pd.read_csv(file_src, index_col=0)
# print(data)
# data2= data['review']
# print(data2[2])
reviews = data['review']
index = 0
temp = []

for review in tqdm(reviews, desc="전처리 진행 상황 "):
    # time.sleep(0.1)
    # print(review)

    # if index == 5:
    #     break

    index = index + 1
#------------------- 라인별 텍스트 출력 --------------------
# for preprocessing in range(0, len(total_lines)):
#     total_lines[preprocessing]
    #---------------------- 문장 분리 -------------------------
    sentence_tokenized_text = sentence_strip(review)
    # print("sentence_tokenized_text =",sentence_tokenized_text)

    #------------------- 불 필요한 문자 치환 --------------------
    cleaned_corpus = []
    for review in sentence_tokenized_text:
        cleaned_corpus.append(clean_punc(review, punct, punct_mapping))

    # print("cleaned_corpus =",cleaned_corpus)

    # for i in range(0, 3):
    #     print(cleaned_corpus[i])

    basic_preprocessed_corpus = clean_text(cleaned_corpus)

    # for i in range(0, 3):
    #     print(basic_preprocessed_corpus[i])

    # print("basic_preprocessed_corpus =",basic_preprocessed_corpus)

    #------------------------ Spell check ------------------------
    #------- 띄어쓰기 검사 (from pykospacing import Spacing) --------
    #[예제]
    # spacing_text = spacing("김형호영화시장분석가는'1987'의네이버영화정보네티즌10점평에서언급된단어들을지난해12월27일부터올해1월10일까지통계프로그램R과KoNLP패키지로텍스트마이닝하여분석했다.")
    # spacing_text = spacing("내이름은구근모입니다.오투오에서교육받고있습니다")
    # print(spacing_text)

    #[적용]
    # spacing_text = []
    # for review in range(0, len(basic_preprocessed_corpus)):
    #     spacing_text.append(spacing(basic_preprocessed_corpus[review]))
    #
    # print("spacing_text =", spacing_text)

    #------- 맞춤법 검사 (from hanspell import spell_checker) --------
    #[예제]
    # sent = "대체 왜 않돼는지 설명을 해바"
    # spelled_sent = spell_checker.check(sent)      # 스펠 체크 동작 후 스펠 체크 결과를 리턴
    # checked_sent = spelled_sent.checked           # 스펠 체크 결과에서 스펠체크 하고 난 후 문장을 뽑아냄
    # print("checked_sent",checked_sent)

    #[적용]]
    # checked_spelling = []
    # for review in range(0, len(spacing_text)):
    #     spelling_text = spell_checker.check(spacing_text[review])
    #     checked_spelling.append(spelling_text.checked)
    #
    # print("checked_spelling =",checked_spelling)

    #------- 반복되는 이모티콘, 자모 정규화 Normalization (from soynlp.normalization) --------
    #[예제]
    # print(repeat_normalize('와하하하하하하하하하핫', num_repeats=2)) => num_repeats=2 : 반복되는 일정한 규칙을 2로 변형
    # print(repeat_normalize('구근근근근근근모', num_repeats=1))

    #[적용]
    # repeat_normalize_result = []
    # for review in range(0, len(checked_spelling)):
    #     normalize_text = repeat_normalize(checked_spelling[review], num_repeats=2)
    #     repeat_normalize_result.append(normalize_text)
    #
    # print("repeat_normalize =",repeat_normalize_result)

    #----------------- finished data PreProcessing -----------------
    # update_file_processed_review_info
    # processed_review = repeat_normalize_result
    # print("finished_data =",processed_review)

    # update_file_processed_review(processed_review)
    # preprocessed review 칼럼에 데이터를 넣는다.
    # 전처리완료후 csv의 새로운 파일을 만든다.

    #----------------- 외래어 ------------------
    # lownword_map = {}
    # lownword_data = open("/Users/gmnine/Pycharm_Projects/pythonProject/sample/sample_data_k.csv","r",encoding="utf-8")
    # lownword_line = lownword_data.readlines()

    lownword_map = {}
    lownword_data = open('/Users/gmnine/Pycharm_Projects/pythonProject/confused_loanwords.txt', 'r', encoding='utf-8')

    lines = lownword_data.readlines()

    for line in lines:
        line = line.strip()
        miss_spell = line.split('\t')[0]
        ori_word = line.split('\t')[1]
        lownword_map[miss_spell] = ori_word

    #------------------- 라인별 텍스트 출력 --------------------
    # for review in range(0, 3):
    #     print("line =",str(review),lownword_data[review])

    spell_preprocessed_corpus = spell_check_text(basic_preprocessed_corpus)
    # print("spell_preprocessed_corpus =",spell_preprocessed_corpus)

    # ------------------- emoji 이모티콘 제거 --------------------
    str_corpus = " ".join(spell_preprocessed_corpus)
    # print("str_corpus =", str_corpus)

    rm_emoji_text = rm_emoji(str_corpus)
    # print('rm_emoji_text =',rm_emoji_text)

    # finished_review_data = spell_preprocessed_corpus
    # temp.append(" ".join(rm_emoji_text))
    temp.append(rm_emoji_text)

# data.iloc[:,6] = temp
# print(data.iloc[:,6])

data['processed_review'] = temp
print(data['processed_review'])

#------------------ 새로운 csv에 저장하기 ------------------
data.to_csv('/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step03_01_data_travel_review_k_ppc.csv')
#------------------------------------------------------
# file_clean_review_csv.close()