import csv
import re

# 파일 준비
source_file = open("/pythonProject/csv_file/step02_01_data_travel_review_line_up.csv", "r", encoding="utf-8")
review_k_data = open("/pythonProject/step02_02_data_travel_review_k_sample.csv", "a", encoding="utf-8")
review_e_data = open("/pythonProject/csv_file/step02_02_data_travel_review_e.csv", "a", encoding="utf-8")
review_z_data = open("/pythonProject/csv_file/step02_02_data_travel_review_z.csv", "a", encoding="utf-8")

header = ['','store_id','portal_id','o2o_score','score','review','processed_review','']

writer_k = csv.writer(review_k_data)
writer_k.writerow(header)
writer_e = csv.writer(review_e_data)
writer_e.writerow(header)
writer_z = csv.writer(review_z_data)
writer_z.writerow(header)

def check_lang(line):

    if re.search('.[ㄱ-힣].[ㄱ-힣].[ㄱ-힣].[ㄱ-힣]', line):
        # line_in_k >= 1
        print('k_work_1 =', line)
        if re.search('^[ㄱ-힣]', line):
            # line_start_k
            print('k_work_2 =', line)
            return 1

    elif re.search('.[a-zA-Z].[a-zA-Z].[a-zA-Z].[a-zA-Z]', line):
        # line_in_e >= 1
        print('e_work_1 =',line)
        if re.search('^[a-zA-Z]', line):
            # line_start_e
            print('e_work_1 =', line)
            return 0

    # 1 = k, 0 = e, 9 = z
    return 9

def update_file_review(ltype, buf):
    print('update_file_review',ltype,buf)
    review_buf = buf.strip().split(',')
    if ltype == 1:
        # writer_k저장
        writer_k.writerow(review_buf)
    elif ltype == 0:
        # writer_e저장
        writer_e.writerow(review_buf)
    else:
        # writer_e저장
        writer_z.writerow(review_buf)

review_header_buf = ''
review_data_buf = ''
index = 0

for review_line in source_file:
    print("line =",review_line)

    # if index > 60:
    #     break
    index = index + 1

    'a,b,c,d,e,fff,fffff'
    temp_list = review_line.split(",")[:6] # a,b,c,d
    review_header_buf = ','.join(temp_list)

    temp_list = review_line.split(",")[5:] # fffffff
    review_data_buf = ' '.join(temp_list)
    print('after =',review_data_buf)
    # plus_review = review_header_buf + review_data_buf  # a,b,c,d,e,ffffffff

    # 한글인지, 영어인지, 다른것인지 검사하고, 0,1,9로 값을 반환해주는 함수 호출. 리뷰 데이터만 인자로 넘김.
    language_check_type = check_lang(review_data_buf)
    # 언어 타입 그리고, 리뷰 헤더 + 데이터를 저장하기위해서 함수 호출
    update_file_review(language_check_type,review_header_buf + review_data_buf)

    '''
    # review_real_buf 에 있는 데이터 저장
    if len(review_real_buf) > 0:
        review_real_buf = review_real_buf.replace('\n',' ')

        # find language type
        lang_type = check_lang(review_real_buf)
        review_real_buf = review_real_buf.split(",")
        update_file_review(lang_type,review_header_buf + review_real_buf)

    if len(review_line) > 0:
        review_header_buf = review_line.split(",")[:4]
        # (,)가 5이상이면 리뷰 데이터만 추출
        temp_list = review_line.split(",")[5:]
        review_real_buf = ','.join(temp_list)
        # review_real_buf_join = ','.join(temp_list)
        # review_real_buf =''.join(review_real_buf_join)
        print('review_real_buf + review_line =', review_real_buf)
    '''

source_file.close()
review_k_data.close()
review_e_data.close()
review_z_data.close()