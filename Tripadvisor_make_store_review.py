from selenium import webdriver
import time

file_url_list = open("/Users/gmnine/Documents/selenium/travel_link_list.txt","r",encoding="utf-8")
file_store_csv = open("/Users/gmnine/Documents/selenium/travel_store.csv","a",encoding="utf-8")
file_review_csv = open("/Users/gmnine/Documents/selenium/travel_review.csv","a",encoding="utf-8")

driver = webdriver.Chrome("/Users/gmnine/Documents/selenium/Chromedriver")

#-------------추가내용------------
parsing_count = 0
while(True):
#-------------------------------

    # 접속할주소
    # get link from file. file_url_list
    access_url = file_url_list.readline()
    print(access_url)

    # access url
    driver.get(access_url)
    time.sleep(1)
    #-------------------------------
    # parsing - get store info
    store_id = '0'
    store_name = ''
    store_tel = ''

    title = driver.find_element_by_xpath('/html/head/title')
    title_text = title.get_attribute("text")
    list = title_text.split(' - ')
    store_name = list[0]
    print(store_name)

    # file append store info
    file_store_csv.write(store_id + ",")
    file_store_csv.write(store_name + ",")
    file_store_csv.write(store_tel+ ",")
    file_store_csv.write("\n")

#-------------추가내용------------
    parsing_count = parsing_count + 1
    if parsing_count > 2:
        break
#-------------------------------
# parsing - get review info

#-------------추가내용------------
# bubble = driver.find_element_by_xpath('//svg[@class="zWXXYhVR"]/svg[@viewbox="0 0 88 16"]/svg[@width="88"]/svg[@height="16"]/svg[@title="풍선 5개 중 4.0"]')
# score = bubble.get_attribute("title")
# print(score)
#-------------------------------

'''
reviews = driver.find_elements_by_css_selector(".review-container")
rating_code = reviews[0].find_element_by_css_selector(".ui_bubble_rating")

cls_attr = rating_code.get_attribute("class")
cls_attr = str(cls_attr).split("ui_bubble_rating")

score = str(cls_attr[1])
print('score',score)

'''
#-------------추가내용------------
# review = driver.find_elements_by_class_name("_2tsgCuqy")
# print(review)

#[1]
# review = driver.find_element_by_xpath('//div[@class="DrjyGw-P _26S7gyB4 _2nPM5Opx"]/span[@class="_2tsgCuqy"]')
# review_text = review.get_attribute("text")
# store_review = review_text
# print(store_review)
#-------------------------------

#[2]
# review = driver.find_element_by_css_selector("#tab-data-qa-reviews-0 > div > div._1c8_1ITO > div:nth-child(1) > span > span > div._2f_ruteS._1bona3Pu > div.cPQsENeY.u7nvAeyZ > div > span").text
# store_review = review.replace("\n"," ")
# print(store_review)
#-------------------------------

# file append review info

#-------------추가내용------------
#file_review_csv.write(store_review + ",")
#file_review_csv.write("\n")
#-------------------------------

file_url_list.close()
file_store_csv.close()
file_review_csv.close()
driver.close()