import re
import pandas as pd
from khaiii import KhaiiiApi
from tqdm import tqdm
import time

#-----------------------/ def 함수 /--------------------------
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

def get_selected_morphs(review_morphs_result,morphs_type):
    print('get_selected_morphs()',morphs_type)
    review_morphs_result_list = []
    for sent in review_morphs_result:
        for morphs_data_and_type in sent.split(' '):
            buff = morphs_data_and_type.split('/')
            print('buff =',buff)
            if buff[1] in morphs_type:
                print('type_found')
                review_morphs_result_list.append(buff[0])
                # review_morphs_result_list.append(word)
            else:
                print('type_not_found')
                review_morphs_result_list.append(' ')
    return review_morphs_result_list

def get_morphs_from_line(input_str, search_type):
    return_val = ''
    print('input_str =',input_str)

    input_str_split_space = input_str.split(' ')
    # print('input_str_split_space =',input_str_split_space)

    for list_in_data_num in range(0,len(input_str_split_space)):
        input_str_split_count = input_str_split_space[list_in_data_num]
        # print('1. str/type =',input_str_split_count)

        input_str_split_slash = input_str_split_count.split('/')
        # print("2. 'str','type' =",input_str_split_slash)

        if input_str_split_slash[1] in search_type:
            # print('3. type_found :',search_type)

            return_val = return_val + input_str_split_slash[0] + ', '
            # print('4. return_val =',return_val)

        else:
            # print('3. type_not_found')
            pass

    return return_val

#-------------------/ 호출 및 코드 실행 /-------------------
api = KhaiiiApi()
#-------------------------------------------------------
data = pd.read_csv("/pythonProject/csv_file/step03_01_data_travel_review_k_ppc.csv", index_col=0)
# df = pd.DataFrame(data)
# print(df["processed_review"])
reviews = list(data['processed_review'])
# print(type(reviews))

# reviews = ["나도 모르게 사버렸다.", "행복해야해!", "내가 안 그랬어!", "나는 사지 않았어.", "하나도 안 기쁘다.", "상관하지마", "그것 좀 가져와"]

index = 0
#--------------- Part-Of-Speech(POS Tag) ---------------
#----------------------- Khaiii ------------------------
#[예제]
# test_sents = ["나도 모르게 사버렸다.", "행복해야해!", "내가 안 그랬어!", "나는 사지 않았어.", "하나도 안 기쁘다.", "상관하지마", "그것 좀 가져와"]
#
# for sent in test_sents:
#     for word in api.analyze(sent):
#         for morph in word.morphs:
#             print(morph.lex + '/' + morph.tag)
#     print('\n')

# for line in tqdm(reviews, desc="형태소 분석 진행 상황 "):
#[적용]
#-----------------------/ 중요한 Tag /-----------------------
significant_tags = ['NNG', 'NNP', 'NNB', 'VV', 'VA', 'VX', 'MAG', 'MAJ', 'XSV', 'XSA']
# 사용할_tags = ['NNG', 'NNP', 'NNB', 'VV', 'VA']

#--------------------------------------------------------
pos_tagged_corpus = pos_text(reviews)
# print('pos_tagged_corpus =',pos_tagged_corpus)

#--------------------------------------------------------
p1 = re.compile('[가-힣A-Za-z0-9]+/NN. [가-힣A-Za-z0-9]+/XS.')
p2 = re.compile('[가-힣A-Za-z0-9]+/NN. [가-힣A-Za-z0-9]+/XSA [가-힣A-Za-z0-9]+/VX')
p3 = re.compile('[가-힣A-Za-z0-9]+/VV')
p4 = re.compile('[가-힣A-Za-z0-9]+/VX')

#----------------------/ Stemming /----------------------
# 동사를 원형으로 복원
stemming_corpus = stemming_text(pos_tagged_corpus)
# print("stemming_corpus =",stemming_corpus)

#-----------------------/ 불용어 제거 /-----------------------
# 한국어는 불용어를 사용자 임의로 설정
# stopwords = ['데/NNB', '좀/MAG', '수/NNB', '등/NNB', '안/MAG' , '렇/VA']
# removed_stopword_corpus = remove_stopword_text(stemming_corpus)
# print("removed_stopword_corpus =",removed_stopword_corpus)

#-----------------------/ 형태소 분석한 데이터를 데이터 프레임으로 추가 /-----------------------
morphs_all = {'morphs_all' : stemming_corpus}
df_morph_all = pd.DataFrame(morphs_all)
# print(df_morph_all)

#-----------------------/ [1]형태소 분석한 데이터를 특정 타입의 형태소를 /-----------------------
# finishd_corpus_selected = get_selected_morphs(stemming_corpus,'NNG, NNP, NNB, VV, VA')
# print('finishd_corpus_selected =',finishd_corpus_selected)

morphs_selected = []
for line in stemming_corpus:
    # select moprhs
    morphs_selected_data = get_morphs_from_line(line,'NNG, NNP, NNB, VV, VA')
    morphs_selected.append(morphs_selected_data)
# print(morphs_selected)

#-----------------------/ [2]특정 타입의 데이터를 데이터프레임에 추가 /-----------------------
morph_data_selected = {'morphs_selected' : morphs_selected}
df_morph_selected = pd.DataFrame(morph_data_selected)
# print(df_morph_selected)

#-----------------------/ [1],[2]의 데이터 프레임을 합치기 /-----------------------
morphs_join_data = df_morph_all.join(df_morph_selected)
print(morphs_join_data)

#------------------/ 새로운 csv파일로 저장하기 /------------------
# morphs_join_data.to_csv("/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_01_data_morpheme_analysis_k(이상파일).csv", index=False)
morphs_join_data.to_csv("/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_01_data_morpheme_analysis_k.csv")