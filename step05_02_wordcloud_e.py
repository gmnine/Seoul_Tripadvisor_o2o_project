import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

data = pd.read_csv('/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_04_data_[id,review,morphs]_e.csv')
df = pd.DataFrame(data)
wordcloud_data = ''.join(list(df['morphs_selected']))
# print(wordcloud_data)

wc_data = wordcloud_data.split(', ')
# print('wc_data =',wc_data[:10])

# 리스트 요소 카운팅
counts = Counter(wc_data)
tags = counts.most_common(len(wc_data))
# print(tags)

# 이미지 마스크
m = Image.open('/Users/gmnine/Pycharm_Projects/pythonProject/png_file/mask_file/seoul.png')
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
               mask = masks).generate_from_frequencies(dictionary)
               # ).generate_from_frequencies(dictionary)

plt.figure(figsize=(10, 8))
plt.axis('off')
# plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_colors))
plt.show()

#
# wordcloud.to_file('/Users/gmnine/Pycharm_Projects/pythonProject/png_file/step05_data_wordcloud_e.png')
