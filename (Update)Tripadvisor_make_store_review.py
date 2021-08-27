from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

def parsing_store_info(driver):
    #print('parsing_store_info')
    title = driver.find_element_by_xpath('/html/head/title')
    title_text = title.get_attribute("text")
    list = title_text.split(' - ')
    store_name = list[0]
    #print(store_name)

    return store_name

def update_file_store_info(store_id):
    # file append store info
    file_store_csv.write(store_id + ",")
    file_store_csv.write(store_name + ",")
    file_store_csv.write("\n")
    print('update_file_store_info')

def parsing_review_info(driver,store_id,review_start_id):
    global reviews_list

    #review_id = "0"
    portal_id = "3000"
    list_bubble = []
    list_title = []
    list_contents = []

    #print('parsing_review_info')

    try:
        reviews = driver.find_element_by_class_name('_1c8_1ITO')
    except NoSuchElementException:
        return
    try:
        writers = reviews.find_elements_by_class_name('_1svEu5jc')
        # print('writers size', len(writers))
        bubbles = reviews.find_elements_by_class_name('zWXXYhVR')
        print('bubbles size', len(bubbles))
        # contents = reviews.find_elements_by_class_name("_2f_ruteS")
        review_data = reviews.find_elements_by_class_name("_2tsgCuqy")
        print('review_data size', len(review_data))

        for i in range(len(bubbles)):
            # 풍선 5개 중 5.0
            bubble_str = bubbles[i].get_attribute("title")
            buff = bubble_str.split("풍선 5개 중 ")
            list_bubble.append(buff[1])

            list_title.append(review_data[i * 2].text)
            list_contents.append(review_data[i * 2 + 1].text)

        '''
        print('writer size', len(list_writer), list_writer)
        print('bubble size', len(list_bubble), list_bubble)
        print('title size', len(list_title), list_title)
        '''
        print('contents size', len(list_contents), list_contents)

    except:
        print('Error')

    for i in range(len(list_bubble)):
        # print('data', i, list_writer[i], list_bubble[i], list_contents[i])
        reviews_list.append(str(review_start_id) + "," + store_id + "," + portal_id + "," + "" + "," + list_bubble[i] + "," + list_contents[i] + "," + "" +",")
    return 0

def update_file_review_info():

    for review in reviews_list:
        # file append store info
        file_review_csv.write(review + '\n')

    #print('update_file_review_info')
    pass

def parsing_max_review_count(driver):
    #print('parsing_max_review_count')
    # < div class ="_1NyglzPL" > 검색 결과 전체 & nbsp;2, 893 중 & nbsp;31-40 < / div >
    temp = driver.find_elements_by_xpath("//div[@class='_1NyglzPL']")
    if len(temp) == 0:
        return 10
    buff = temp[0].text.split('검색 결과 전체')
    value = buff[1].split(' ')[1]
    value = value.replace(',','')
    #print(buff,value)
    return int(value)

def parsing_store_id(access_url):
    #https://www.tripadvisor.co.kr/Attraction_Review-g294197-d324888-Reviews-or30-Gyeongbokgung_Palace-Seoul.html
    buff = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d"
    value = access_url.split(buff)
    value2 = value[1].split("-Reviews-")
    return value2[0]

####
# setup working directory and driver


file_url_list = open("/Users/gmnine/PycharmProjects/pythonProject/travel_link_list.txt","r",encoding="utf-8")
file_store_csv = open("/Users/gmnine/PycharmProjects/pythonProject/travel_store.csv","a",encoding="utf-8")
file_review_csv = open("/Users/gmnine/PycharmProjects/pythonProject/travel_review.csv","a",encoding="utf-8")

driver = webdriver.Chrome("/Users/gmnine/Documents/selenium/Chromedriver")
'''
멘토님주소
working_folder_path = '/home/jay/work_itc_train/o2o_project/'
file_url_list = open(working_folder_path + "travel_link_list.txt","r",encoding="utf-8")
file_store_csv = open(working_folder_path + "travel_store.csv","a",encoding="utf-8")
file_review_csv = open(working_folder_path + "travel_review.csv","a",encoding="utf-8")

driver = webdriver.Chrome("/home/jay/work_itc_train/chromedriver_linux64/chromedriver")
'''
####

access_url_index = 382
last_review_id = 0

reviews_list = []

# 접속할주소
# get link from file. file_url_list
# access_url = file_url_list.readline()
access_urls = file_url_list.readlines()
#print ('load total url list', len(access_urls))
while(True):

    access_url = access_urls[access_url_index]
    #print(access_url)

    # access url
    driver.get(access_url)
    print('url:', str(access_url_index), '/', str(len(access_urls)), access_url.replace('\n',''))
    time.sleep(2)

    # parse store info
    store_id = '0'
    store_name = ''
    store_id = parsing_store_id(access_url)
    store_name = parsing_store_info(driver)
    update_file_store_info(store_id)

    # parsing max review count
    max_review_count = parsing_max_review_count(driver)

    #for review_start_id in range(last_review_id, max_review_count, 10)
    for review_start_id in range(last_review_id,max_review_count,10):

        buff = access_url.split("-Reviews-")
        review_url = buff[0] + "-Reviews-or" + str(review_start_id) + "-" + buff[1]

        print('\nreview:', review_start_id, '/', max_review_count, 'url', review_url.replace('\n', ''))
        driver.get(review_url)

        time.sleep(3)
        try:
            button = driver.find_element_by_xpath("//*[text()='리뷰 원문 표시하기']")
            # button = driver.find_element_by_xpath("//button[@class='_3L3LNeQW']")
            print('translation button found and click. wait...')
            button.click()
            time.sleep(3)
        except:
            print('not found button')


        # parsing review info (10)
        reviews_list.clear()
        parsing_review_info(driver,store_id,review_start_id)
        if len(reviews_list) > 0:
            update_file_review_info()
        else:
            break
        time.sleep(3)

    access_url_index = access_url_index + 1
 
#-------------------------------
# parsing - get review info
# file append review info

file_url_list.close()
file_store_csv.close()
file_review_csv.close()
driver.close()
