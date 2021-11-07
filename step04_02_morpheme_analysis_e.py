import pandas as pd
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

#-----------------------/ def 함수 /--------------------------
def get_morphs_from_line(input_str, search_type):
    return_val = ''
    # print('input_str =',input_str)

    input_str_split_space = input_str.strip().split(' ')
    # print('input_str_split_space =',input_str_split_space)

    for list_in_data_num in range(0,len(input_str_split_space)):
        input_str_split_split_one_item = input_str_split_space[list_in_data_num]
        # print('1. str/type =',input_str_split_split_one_item)

        input_str_split_slash = input_str_split_split_one_item.split('/')
        # print("2. 'str','type' =",input_str_split_slash)

        if input_str_split_slash[1] in search_type:
            # print('3. type_found :',search_type)

            return_val = return_val + input_str_split_slash[0] + ', '
            # print('4. return_val =',return_val)

        else:
            # print('3. type_not_found')
            pass

    return return_val

def token_slash_pos(doc):
    return ["/".join(p) for p in tagged_list]

#-------------------/ 호출 및 코드 실행 /-------------------
data = pd.read_csv("/pythonProject/csv_file/step03_02_data_travel_review_e_ppc.csv", index_col=0)
# data = pd.read_csv("/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/test_csv/test_e_ppc.csv", index_col=0)
# df = pd.DataFrame(data)
# print(df["processed_review"])
reviews = '?'.join(list(data['processed_review']))
# reviews = data['processed_review']
# print(type(reviews))
# reviews = list(data['processed_review'])
# print(reviews)

# #-----------/ 토큰화 (Penn Treebank Tokenization) /-----------
tokenizer = TreebankWordTokenizer()
PennTreebank = tokenizer.tokenize(reviews)
# print('PennTreebank =',PennTreebank[:10])

#------------------/ 불용어 (stopwords) 제거 /------------------
# 불용어 정보
# stopwords = stopwords.words('english')[:10]
# print(stopwords)

stop_words = set(stopwords.words('english'))
word_tokens = PennTreebank

stopwords_result = []
for w in word_tokens:
    if w not in stop_words:
        stopwords_result.append(w)

# print('stopwords =',stopwords_result[:10])

# #------------------/ 정규화 (Nomalization) /------------------
# #-----------------/ 원형복원 (Lemmatization) /-----------------
lemmatization = WordNetLemmatizer()
lemmatization_result = [lemmatization.lemmatize(w) for w in stopwords_result]
# print('Lemmatization =',lemmatization_result[:10])

# #---------------/ Part-Of-Speech(POS Tag) /---------------
tagged_list = pos_tag(lemmatization_result)
# print('tagged_list =',tagged_list[:20])

token_slash_pos_list = token_slash_pos(lemmatization_result)
# print('token_slash_pos_list =',token_slash_pos_list[:100])

# #----------------/ 문장 토큰화 (sent_tokenize) /---------------
# # from nltk.tokenize import sent_tokenize
# # print('sent_tokenize =',sent_tokenize(reviews))
#
PennTreebank_join = ' '.join(token_slash_pos_list)
# print(PennTreebank_join)

sent_text = PennTreebank_join.split('?/.')
# print('sent_text =',sent_text[:5])

#------------------/ 원하는 품사 추출 /------------------
# 방법[1]
# nouns_list = [t[0] for t in tagged_list if t[1] == "NN" or t[1] == "VV"]
# print('nouns_list =',nouns_list[:20])

# 방법[2]
# selected_morphs_list = []
# for word, tag in tagged_list:
#     if tag in ['NN' , 'NNP', 'JJ', 'JJR', 'JJS', 'VB', 'VBP']:
#         selected_morphs_list.append(word)
# print('NN_VV_list =',selected_morphs_list[:20])

#--------------------------------------------------------
# #------------------/ 새로운 csv파일로 저장하기 /------------------
# morph_data_selected = {'morphs_selected' : selected_morphs_list}
# df_morph_selected = pd.DataFrame(morph_data_selected)
# # print(df_morph_selected)
# df_morph_selected.to_csv("/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_02_data_morpheme_analysis_e.csv")

###############################/ 한국어 py.code 활용 /###############################

# 참고파일경로 : (/Users/gmnine/Pycharm_Projects/pythonProject/step04_01_morpheme_analysis_k.py)
#-----------------------/ 형태소 분석한 데이터를 데이터 프레임으로 추가 /-----------------------
morphs_all = {'morphs_all' : sent_text}
df_morph_all = pd.DataFrame(morphs_all)
# print(df_morph_all)

#-----------------------/ [1]형태소 분석한 데이터를 특정 타입의 형태소를 /-----------------------
morphs_selected = []
for line in sent_text:
    # select moprhs
    morphs_selected_data = get_morphs_from_line(line,'NN, NNP, JJ, JJR, JJS, VB, VBP')
    morphs_selected.append(morphs_selected_data)
# print(morphs_selected)

# #-----------------------/ [2]특정 타입의 데이터를 데이터프레임에 추가 /-----------------------
morph_data_selected = {'morphs_selected' : morphs_selected}
df_morph_selected = pd.DataFrame(morph_data_selected)
# print(df_morph_selected)

#-----------------------/ [1],[2]의 데이터 프레임을 합치기 /-----------------------
morphs_join_data = df_morph_all.join(df_morph_selected)
# print(morphs_join_data)

#------------------/ 새로운 csv파일로 저장하기 /------------------
morphs_join_data.to_csv("/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_02_data_morpheme_analysis_e.csv")

###################################################################################
