# 파일 준비
# source_file = open("/Users/gmnine/Pycharm_Projects/pythonProject/data.csv","r",encoding="utf-8")
source_file = open("/Users/gmnine/Pycharm_Projects/pythonProject/travel_review.csv","r",encoding="utf-8")
extraction_data = open("/Users/gmnine/Pycharm_Projects/pythonProject/review_extraction.csv","a",encoding="utf-8")

def update_file_review_extraction(review_real_buf):
    extraction_data.write(review_real_buf)
    extraction_data.write("\n")
    print("update_file_review_extraction")

# total_line = data.readline_count()
review_real_buf = ''
# for line_index in range(30):
for review_line in source_file:
    # 라인 읽기
    # review_line = source_file.readline()
    print("line =",review_line)

    # 라인에 데이터가 있는지 확인
    # if review_line != " ":
    #     print("Yes")
    # elif review_line == " ":
    #     print("no")

    # (,)가 몇개 있는지 확인
    review_line_in_comma = review_line.count(",")
    print("review_line_in_comma =",review_line_in_comma)

    # (,)가 5이상인경우 리뷰 시작
    start_review = review_line_in_comma >= 5
    # print(start_review)

    # (,)개수가 5개이상 리뷰가 처음 시작하는 라인
    if start_review :

        # review_real_buf 에 있는 데이터 저장
        if len(review_real_buf) > 0:
            review_real_buf = review_real_buf.replace('\n','')
            # review_real_buf = [item.replace('\n','') for item in review_real_buf]
            update_file_review_extraction(review_real_buf)

        if len(review_line) > 0:
            # (,)가 5이상이면 리뷰 데이터만 추출
            temp_list = review_line.split(",")[5:]
            review_real_buf = ','.join(temp_list)
            # print('review_real_buf =',review_real_buf)

        # elif len(review_line) < 0:
        #     # 비운다
        #     review_real_buf = ''

    #(,)가 5개 미만일 경우 순수한 리뷰데이터 buf에 저장
    else:
        #tail_plus = review_real_buf.replace('\n',"")
        review_real_buf = review_real_buf + review_line
        print('review_real_buf + review_line =',review_real_buf)

update_file_review_extraction(review_real_buf)

source_file.close()
extraction_data.close()