import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

data = pd.read_csv('/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_03_data_[id,review,morphs]_k.csv')
df = pd.DataFrame(data)
wordcloud_data = ''.join(list(df['morphs_selected']))
# print(wordcloud_data)
# print(type(wordcloud_data))

wc_data = wordcloud_data.split(', ')
# print('wc_data =',wc_data[:10])

# 리스트 요소 카운팅
counts = Counter(wc_data)
tags = counts.most_common(len(wc_data))
# print(tags)

# 이미지 마스크
m = Image.open('/Users/gmnine/Pycharm_Projects/pythonProject/png_file/mask_file/서울.png')
masks = np.array(m)

# ImageColorGenerator
img_color = masks
image_colors = ImageColorGenerator(img_color)

# 불용어 제거
dictionary = dict(tags)
del(dictionary['있다'])
del(dictionary['오다'])
del(dictionary['주다'])
del(dictionary['정도'])
del(dictionary['때문'])
del(dictionary['거'])
del(dictionary['싶다'])
del(dictionary['기'])
del(dictionary['맛'])
del(dictionary['잔'])
del(dictionary['다음'])
del(dictionary['안'])
del(dictionary['넓'])
del(dictionary['찾다'])
del(dictionary['분'])
del(dictionary['들다'])
del(dictionary['크'])
del(dictionary['중'])
del(dictionary['닐'])
del(dictionary['좋'])
del(dictionary['원'])
del(dictionary['시'])
del(dictionary['ㅎ'])
del(dictionary['힘들'])
del(dictionary['등'])
del(dictionary['만하다'])
del(dictionary['없'])
del(dictionary['나다'])
del(dictionary['번'])
del(dictionary['살다'])
del(dictionary['편'])
del(dictionary['나오다'])
del(dictionary['탈출'])
del(dictionary['받다'])
del(dictionary['방'])
del(dictionary['앞'])
del(dictionary['수'])
del(dictionary['같'])
del(dictionary['작'])
del(dictionary['되다'])
del(dictionary['날'])
del(dictionary['층'])
del(dictionary['않다'])
del(dictionary['많'])
del(dictionary['듯'])
del(dictionary['후'])
del(dictionary['대'])
del(dictionary['가다'])
del(dictionary['지다'])
del(dictionary['위하다'])
del(dictionary['느끼다'])
del(dictionary['들르다'])
del(dictionary['어렵'])
del(dictionary['그렇'])
del(dictionary['때'])
del(dictionary['알다'])
del(dictionary['전'])
del(dictionary['쉽'])
del(dictionary['그러다'])
del(dictionary['아쉽'])
del(dictionary['점'])
del(dictionary['데'])
del(dictionary['줄'])
del(dictionary['예전'])
del(dictionary['년'])
del(dictionary['다니다'])
del(dictionary['모르다'])
del(dictionary['처음'])
del(dictionary['듯하다'])
del(dictionary['비싸'])
# del(dictionary['보다'])
del(dictionary['하다'])
del(dictionary['곳'])
del(dictionary['것'])
del(dictionary['타다'])
del(dictionary['길'])
del(dictionary['시간'])

# wordcloud_counts = Counter(dictionary)
# tagss = wordcloud_counts.most_common(len(dictionary))
# print(tagss)

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

# wordcloud.to_file('/Users/gmnine/Pycharm_Projects/pythonProject/png_file/step05_data_wordcloud_k.png')
