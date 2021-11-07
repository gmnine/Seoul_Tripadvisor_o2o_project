# 파일 준비
source_file = open("/pythonProject/step01_data_travel_review.csv", "r", encoding="utf-8")
extraction_data = open("/pythonProject/step02_01_data_travel_review_line_up.csv", "a", encoding="utf-8")

def update_file_review_extraction(review_real_buf):
    extraction_data.write(review_real_buf)
    extraction_data.write("\n")
    print("update_file_review_extraction")

# total_line = data.readline_count()
review_real_buf = ''
index = 0

# for line_index in range(30):
for review_line in source_file:
    # 라인 읽기
    # review_line = source_file.readline()
    print("line =",review_line)

    # if index > 5:
    #     break
    index = index + 1

    # 라인에 데이터가 있는지 확인
    # if review_line != " ":
    #     print("Yes")
    # elif review_line == " ":
    #     print("no")

    # (,)가 몇개 있는지 확인
    review_line_in_comma = review_line.count(",")
    print("review_line_in_comma =",review_line_in_comma)

    # (,)가 5이상인경우 리뷰 시작
    # start_review = review_line_in_comma >= 5
    # print(start_review)

    is_review_line_end = False
    if review_line.strip().endswith(",,"):
        print("check",review_line)
        is_review_line_end = True

    # check first 3 value is number
    is_3data_digit = False
    temp_list = review_line.split(",")
    if review_line_in_comma >= 5:
        if temp_list[0].isdigit() and temp_list[1].isdigit() and temp_list[2].isdigit():
            print('first 3 value is digit')
            is_3data_digit = True


    # (,)개수가 5개이상 리뷰가 처음 시작하는 라인
    if review_line_in_comma >= 5 and is_3data_digit:

        # review_real_buf 에 있는 데이터 저장 (다음 라인 리뷰가 위의 리뷰에 이어지는 내용이라면 합친다)
        if len(review_real_buf) > 0:
            review_real_buf = review_real_buf.replace('\n',' ')
            update_file_review_extraction(review_real_buf)

        # 다음 라인 리뷰가 위의 리뷰에 이어지는 내용이지만 (,)>=5으로 인식이 힘든 경우
        if len(review_line) > 0:
            temp_list = review_line.split(",")
            review_real_buf = ','.join(temp_list)
            print('review_real_buf + review_line =', review_real_buf)

    #(,)가 5개 미만일 경우 순수한 리뷰데이터 buf에 저장 # 다음 라인의 리뷰가 (,)<5이지만 위의 리뷰에 이어지는 내용이라면 합친다
    else:
        review_real_buf = review_real_buf + review_line
        print('review_real_buf + review_line =',review_real_buf)

update_file_review_extraction(review_real_buf)

source_file.close()
extraction_data.close()