import pandas as pd
import re
import time
from tqdm import tqdm

punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-",
                 "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity',
                 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi',
                 '\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': '',}

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

def rm_emoji(data):
    return data.encode('ascii','ignore').decode('ascii')

#----------------- Convert text to lowercase -----------------
#--------------------- 텍스트를 소문자로 변환 ----------------------
# [예제]
# input_str = "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil."
# input_str = input_str.lower()
# print(input_str)

# [적용]
#     lower_text = review.lower()
#     print("소문자 변환 =",lower_text)

data = pd.read_csv("/pythonProject/csv_file/step02_02_data_travel_review_e.csv", index_col=0)
reviews = data['review']
index = 0
temp = []

for review in tqdm(reviews, desc="전처리 진행 상황 "):
    # time.sleep(0.1)
    # print("review =",review)

    # if index == 30:
    #     break
    index = index + 1

    # review_split = []
    # for i in range(0,10):
    #     text_spilt = review.split()
    #     review_split.append(text_spilt[i])
    # print("review_split =",review_split)

#------------------- 불 필요한 문자 치환 --------------------
    cleaned_corpus = []
    cleaned_corpus.append(clean_punc(review, punct, punct_mapping))
    # print("cleaned_corpus =",cleaned_corpus)

    basic_preprocessed_corpus = clean_text(cleaned_corpus)
    # print("basic_preprocessed_corpus =",basic_preprocessed_corpus)

        # for i in range(0,len(basic_preprocessed_corpus)):
        #     str_corpus = "".join(basic_preprocessed_corpus[i])
        # print("str_corpus =",str_corpus)

    str_corpus = " ".join(basic_preprocessed_corpus)
    # print("str_corpus =",str_corpus)

#------------------- emoji 이모티콘 제거 --------------------
    review_in_remove_emoji = rm_emoji(str_corpus)
    # print('remove_emoji_text =',review_in_remove_emoji)

    # finished_review_data = review_in_remove_emoji
    # data['processed_review'] = finished_review_data
    temp.append(review_in_remove_emoji)

data['processed_review'] = temp
print(data['processed_review'])

#------------------ 새로운 csv에 저장하기 ------------------
data.to_csv("/Users/gmnine/Pycharm_Projects/pythonProject/step03_02_data_travel_review_e_ppc.csv")