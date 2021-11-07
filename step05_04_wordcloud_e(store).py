import pandas as pd
from collections import Counter
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

data = pd.read_csv('/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_04_data_[id,review,morphs]_e.csv')
df = pd.DataFrame(data)

'''
324888,경복궁,10655 << √
553546,명동 쇼핑 거리,10352 <<
320359,창덕궁,4612
592506,인사동,6410 <<
1519813,한강 공원,1567 √
1169465,N 서울 타워,9456 << √
1046419,청계천,3946 √
1379963,북촌 한옥마을,5247 << √
1958940,홍대앞 거리,2256
6671988,동대문 디자인 플라자,2207 √
'''

# 스토어별 데이터
df_colunm = df[['store_id','morphs_selected']]
df_id = df_colunm.loc[df_colunm['store_id'] == 1169465]
print(df_id)

wordcloud_data = ''.join(list(df_id['morphs_selected']))
# print(wordcloud_data)
# print(type(wordcloud_data))

wc_data = wordcloud_data.split(', ')
# print('wc_data =',wc_data[:10])

# 리스트 요소 카운팅
counts = Counter(wc_data)
tags = counts.most_common(len(wc_data))
# print('tags =',tags)

# 이미지 마스크
m = Image.open('/Users/gmnine/Pycharm_Projects/pythonProject/png_file/mask_file/서울타워.png')
masks = np.array(m)

# ImageColorGenerator
img_color = masks
image_colors = ImageColorGenerator(img_color)

# 불용어 제거
dictionary = dict(tags)
del(dictionary['place'])

wordcloud_counts = Counter(dictionary)
tagss = wordcloud_counts.most_common(len(dictionary))
print(tagss)

# Wordcloud Setting 설정
wc = WordCloud(font_path= '/Users/gmnine/Library/Fonts/MaruBuri-Bold.otf', # 위에 나왔던 경로 중 원하는 폰트로 복사
               background_color = 'white',
               width = 1000,
               height = 1000,
               max_words = 100,
               max_font_size = 300,
               # ).generate_from_frequencies(dictionary)
               mask = masks).generate_from_frequencies(dictionary)

plt.figure(figsize=(10, 8))
plt.axis('off')
# plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_colors))
plt.show()

# wc.to_file('/Users/gmnine/Pycharm_Projects/pythonProject/png_file/wc_경복궁.png')
