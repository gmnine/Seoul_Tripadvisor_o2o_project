#---------------/ 라이브러리 설치, 패키지 불러오기 /---------------
import pandas as pd
import re
import kss
import regex
from pykospacing import Spacing
from hanspell import spell_checker
from soynlp.normalizer import *
from khaiii import KhaiiiApi

# 우분투 환경에서도 돌아가게 하기 위함
spacing = Spacing()

punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-",
                 "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity',
                 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi',
                 '\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': '',}

#-----------------------/ def 함수 /--------------------------
#------------------- 파일 업데이트 및 저장하기 --------------------
def update_file_processed_review(processed_review):
    file_clean_review_csv.write(str(processed_review))
    file_clean_review_csv.write("\n")
    print("update_file_processed_review")
    pass

def sentence_strip(lines):
    sentence_tokenized_text = []
    for i, line in enumerate(lines):
        # if i > 5:     # 전체 wikipedia 문서는 사이즈가 크므로, 일부만 테스트.
        #     break

        line = line.strip()
        for sent in kss.split_sentences(line):
            sentence_tokenized_text.append(sent.strip())

    return sentence_tokenized_text

def clean_punc(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])

    for p in punct:
        text = text.replace(p, f' {p} ')

    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])
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
# def spell_check_text(texts):
#     corpus = []
#     for sent in texts:
#         spacing_text = spacing(sent)
#         spelling_text = spell_checker.check(spacing_text)
#         checked_spelling = spelling_text.checked
#         normalized_sent = repeat_normalize(checked_spelling)
#         for lownword in lownword_map:
#             normalized_sent = normalized_sent.replace(lownword, lownword_map[lownword])
#         corpus.append(normalized_sent)
#     return corpus

def pos_text(texts):
    corpus = []
    for sent in texts:
        pos_tagged = ''
        for word in api.analyze(sent):
            for morph in word.morphs:
                if morph.tag in significant_tags:
                    pos_tagged += morph.lex + '/' + morph.tag + ' '
        corpus.append(pos_tagged.strip())
    return corpus

def stemming_text(text):
    corpus = []
    for sent in text:
        ori_sent = sent
        mached_terms = re.findall(p1, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                modi_terms += lemma
            modi_terms += '다/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)

        mached_terms = re.findall(p2, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                if tag != 'VX':
                    modi_terms += lemma
            modi_terms += '다/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)

        mached_terms = re.findall(p3, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                modi_terms += lemma
            if '다' != modi_terms[-1]:
                modi_terms += '다'
            modi_terms += '/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)

        mached_terms = re.findall(p4, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                modi_terms += lemma
            if '다' != modi_terms[-1]:
                modi_terms += '다'
            modi_terms += '/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)
        corpus.append(ori_sent)
    return corpus

def remove_stopword_text(text):
    corpus = []
    for sent in text:
        modi_sent = []
        for word in sent.split(' '):
            if word not in stopwords:
                modi_sent.append(word)
        corpus.append(' '.join(modi_sent))
    return corpus

#-------------------/ 호출 및 코드 실행 /-------------------
file_clean_review_csv = open("/Users/gmnine/Pycharm_Projects/pythonProject/travel_processed_review.csv","a",encoding="utf-8")

#----------------- Basic PreProcessing -----------------
data = open("/Users/gmnine/Pycharm_Projects/pythonProject/sample_data.csv","r",encoding="utf-8")
lines = data.readlines()

#------------------- 라인별 텍스트 출력 --------------------
# for i in range(0, 3):
#     print("line",str(i),"=",lines[i])
#---------------------- 문장 분리 -------------------------
sentence_tokenized_text = sentence_strip(lines)
print("sentence_tokenized_text =",sentence_tokenized_text)

#------------------- 불 필요한 문자 치환 --------------------
cleaned_corpus = []
for sent in sentence_tokenized_text:
    cleaned_corpus.append(clean_punc(sent, punct, punct_mapping))

print("cleaned_corpus =",cleaned_corpus)

# for i in range(0, 3):
#     print(cleaned_corpus[i])

basic_preprocessed_corpus = clean_text(cleaned_corpus)

# for i in range(0, 3):
#     print(basic_preprocessed_corpus[i])

print("basic_preprocessed_corpus =",basic_preprocessed_corpus)

#------------------------ Spell check ------------------------
#------- 띄어쓰기 검사 (from pykospacing import Spacing) --------
#[예제]
# spacing_text = spacing("김형호영화시장분석가는'1987'의네이버영화정보네티즌10점평에서언급된단어들을지난해12월27일부터올해1월10일까지통계프로그램R과KoNLP패키지로텍스트마이닝하여분석했다.")
# spacing_text = spacing("내이름은구근모입니다.오투오에서교육받고있습니다")
# print(spacing_text)

#[적용]
spacing_text = []
for i in range(0, len(basic_preprocessed_corpus)):
    spacing_text.append(spacing(basic_preprocessed_corpus[i]))

print("spacing_text =", spacing_text)

#------- 맞춤법 검사 (from hanspell import spell_checker) --------
#[예제]
# sent = "대체 왜 않돼는지 설명을 해바"
# spelled_sent = spell_checker.check(sent)      # 스펠 체커 동작 후 스펠 체크 결과를 리턴함.
# checked_sent = spelled_sent.checked           # 스펠 체크 결과에서 스펠체크 하고 난 후 문장을 뽑아냄
# print("checked_sent",checked_sent)

#[적용]]
checked_spelling = []
for i in range(0, len(spacing_text)):
    spelling_text = spell_checker.check(spacing_text[i])
    checked_spelling.append(spelling_text.checked)

print("checked_spelling =",checked_spelling)

#------- 반복되는 이모티콘, 자모 정규화 Normalization (from soynlp.normalization) --------
#[예제]
# print(repeat_normalize('와하하하하하하하하하핫', num_repeats=2)) => num_repeats=2 : 반복되는 일정한 규칙을 2로 변형
# print(repeat_normalize('구근근근근근근모', num_repeats=1))

#[적용]
repeat_normalize_result = []
for i in range(0, len(checked_spelling)):
    normalize_text = repeat_normalize(checked_spelling[i], num_repeats=2)
    repeat_normalize_result.append(normalize_text)

print("repeat_normalize =",repeat_normalize_result)

#----------------- finished data PreProcessing -----------------
# update_file_processed_review_info
processed_review = repeat_normalize_result
print("finished_data =",processed_review)

update_file_processed_review(processed_review)

#----------------- 외래어 ------------------
# lownword_map = {}
# lownword_data = open("/Users/gmnine/Pycharm_Projects/pythonProject/sample_data2.csv","r",encoding="utf-8")
# lownword_line = lownword_data.readlines()

#-----------------------------------------
# for line in lownword_line:
#     line = line.strip()
#     miss_spell = line.split('\t')[0]
#     ori_word = line.split('\t')[0] # 기존값[1]
#     lownword_map[miss_spell] = ori_word

#------------------- 라인별 텍스트 출력 --------------------
#[ENG]
# for i in range(0, 3):
#     print("line =",str(i),lownword_line[i])

# spell_preprocessed_corpus_ENG = spell_check_text(lownword_line)
# print("spell_preprocessed_corpus_ENG =",spell_preprocessed_corpus_ENG)

#--------------- Part-Of-Speech(POS Tag) ---------------
#----------------------- Khaiii ------------------------

# api = KhaiiiApi()
#
# #[예제]
# # test_sents = ["나도 모르게 사버렸다.", "행복해야해!", "내가 안 그랬어!", "나는 사지 않았어.", "하나도 안 기쁘다.", "상관하지마", "그것 좀 가져와"]
# #
# # for sent in test_sents:
# #     for word in api.analyze(sent):
# #         for morph in word.morphs:
# #             print(morph.lex + '/' + morph.tag)
# #     print('\n')
#
# #[적용]
# test_sents = repeat_normalize_result
# for sent in test_sents:
#     for word in api.analyze(sent):
#         for morph in word.morphs:
#             print(morph.lex + '/' + morph.tag)
#     print('\n')
#
# significant_tags = ['NNG', 'NNP', 'NNB', 'VV', 'VA', 'VX', 'MAG', 'MAJ', 'XSV', 'XSA']
# pos_tagged_corpus = pos_text(repeat_normalize_result)
#
# for i in range(0, len(repeat_normalize_result)):
#     print("pos_tagged_corpus",str(i),"=",pos_tagged_corpus[i])
#
# #------------------- Stemming --------------------
# # 동사를 원형으로 복원
#
# p1 = re.compile('[가-힣A-Za-z0-9]+/NN. [가-힣A-Za-z0-9]+/XS.')
# p2 = re.compile('[가-힣A-Za-z0-9]+/NN. [가-힣A-Za-z0-9]+/XSA [가-힣A-Za-z0-9]+/VX')
# p3 = re.compile('[가-힣A-Za-z0-9]+/VV')
# p4 = re.compile('[가-힣A-Za-z0-9]+/VX')
#
# stemming_corpus = stemming_text(pos_tagged_corpus)
#
# for i in range(0, len(pos_tagged_corpus)):
#     print("stemming_corpus",str(i),"=",stemming_corpus[i])
#
# #------------------- Stopwords --------------------
# # 불용어 처리
# stopwords = ['한강공/NNP', '원/NNG', '수/NNB', '업/VA', '만큼/NNB', '좋/VA']
# removed_stopword_corpus = remove_stopword_text(stemming_corpus)
#
# for i in range(0, len(stemming_corpus)):
#     print("removed_stopword_corpus",str(i),"=",removed_stopword_corpus[i])





#------------------------------------------------------
# finished_data_preprocessing = repeat_normalize_result
# data = finished_data_preprocessing
# dataframe = pd.DataFrame(data)
# dataframe.to_csv("/Users/gmnine/Pycharm_Projects/pythonProject/clean_review_data.csv",
#                  columns=['review'], header=True, index= True)
#------------------------------------------------------

file_clean_review_csv.close()