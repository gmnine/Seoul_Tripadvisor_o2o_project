import pandas as pd



data = pd.read_csv('/pythonProject/csv_file/step03_02_data_travel_review_e_ppc.csv')
df1 = pd.DataFrame(data)
df2 = df1[['store_id','review','processed_review']]
# print(df2)

data2 = pd.read_csv('/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_02_data_morpheme_analysis_e.csv')
df3 = pd.DataFrame(data2)
df4 = df3[['morphs_all','morphs_selected']]
# print(df4)

df9 = df2.join(df4)
print(df9)

df9.to_csv('/Users/gmnine/Pycharm_Projects/pythonProject/csv_file/step04_04_data_[id,review,morphs]_e.csv')


