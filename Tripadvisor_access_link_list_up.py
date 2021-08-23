# 라이브러리 설치
from selenium import webdriver
import time

# 데이터 추가, 저장할 곳
f=open("/Users/gmnine/Documents/selenium/travel_link_list.txt","a",encoding="utf-8")
link_str_old = ''
start_number = 0

# Chrome driver 연결
driver = webdriver.Chrome("/Users/gmnine/Documents/selenium/Chromedriver")

while(True):

    # 접속할주소
    #access_url = "https://www.tripadvisor.co.kr/Attractions-g294197-Activities-oa00-Seoul.html"
    #access_url = "https://www.tripadvisor.co.kr/Attractions-g294197-Activities-oa30-Seoul.html"

    # 주소 규칙성 찾기 및 가져오기
    start_url = "https://www.tripadvisor.co.kr/Attractions-g294197-Activities-oa"
    end_url = "-Seoul.html"

    # 균등한 데이터를 가져오기 위한 처리작업
    access_url = start_url + str(start_number) +'0' + end_url
    print(access_url)

    driver.get(access_url)
    time.sleep(1)
    travel_site_list = driver.find_elements_by_xpath('//a[contains(@href,"/Attraction_Review")]')

    for travel_site in travel_site_list:
        link_str = travel_site.get_attribute("href")

        # 같은 주소 pass하기
        if link_str == link_str_old:
            # print('same string. pass')
            pass
        # 원하지 않는 주소 pass하기
        # elif link_str.contain("#REVIEWS"):
        elif "#REVIEWS" in link_str:
            # print('invalid string. pass')
            pass
        else:
            # print(link_str)

            f.write(link_str)
            f.write("\n")

            link_str_old = link_str

    # 시작 넘버가 3의 규칙성을 가지게 하며, 249가 넘을시 멈추도록 함
    start_number = start_number + 3
    if start_number > 249:
        break

f.close()
driver.close()


'''

    for j in range(0,10,1):
        reviews = driver.find_elements_by_css_selector(".review-container")
        rating_code = reviews[0].find_element_by_css_selector(".ui_bubble_rating")

        cls_attr = rating_code.get_attribute("class")
        cls_attr = str(cls_attr).split("ui_bubble_rating")

        score = str(cls_attr[1])
        print(score)

        time.sleep(3)

        Temp_review = reviews[j].find_element_by_css_selector(".partial_entry").text

        time.sleep(3)
        review = Temp_review.replace("\n"," ")
        print(review)

        f.write("평점:" + score)
        f.write("/n/n")
        f.write("리뷰:"+review)
f.close()

'''