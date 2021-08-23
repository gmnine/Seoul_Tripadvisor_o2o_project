from selenium import webdriver
import time

def parsing_store_info(driver):
    print('parsing_store_info')

    title = driver.find_element_by_xpath('/html/head/title')
    title_text = title.get_attribute("text")
    list = title_text.split(' - ')
    store_name = list[0]
    print(store_name)

    return store_name

def update_file_store_info():
    # file append store info
    file_store_csv.write(store_id + ",")
    file_store_csv.write(store_name + ",")
    file_store_csv.write(store_tel + ",")
    file_store_csv.write("\n")
    print('update_file_store_info')

def parsing_review_info(driver):
    global reviews_list
    writer_list = []
    title_list = []
    contents_list = []

    print('parsing_review_info')
    # review list
    # <div class="_1c8_1ITO"><div>
    # <span data-ft="true"><span data-ft="true"><div class="_2nBYkPk3"><div class="_1o0NHSNc"><div class="_3t0zrF_f"><div class="HiSmthtM"><div class="_1Ear6tw9" style="z-index: 0;"><div class="f3gJ-yIA _1UrkpMOY"><a target="_self" tabindex="-1" aria-hidden="true" href="/Profile/George_Korean" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr"><div class="WullykOU _2L7OTqqK"><picture class="_2f-Th360 _3YW9cIgT" style="width: 48px; height: 48px;"><img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/74/7a/54/george-korean.jpg?w=100&amp;h=-1&amp;s=1" width="100" height="100" alt="George_Korean" loading="lazy"></picture></div></a></div></div></div></div><div class="_1svEu5jc"><span class="DrjyGw-P _1SRa-qNz _2AAjjcx8"><a target="_self" href="/Profile/George_Korean" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL">George_Korean</a></span><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy"><span>서울, 대한민국</span></div></div><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy">포스팅 469건</div></div></div></div><div class="_2WOrDRiF"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-label="클릭하여&nbsp;도움이&nbsp;된다는&nbsp;평가&nbsp;추가하기" type="button"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M3.025 9.963c-.566 0-1.025.459-1.025 1.025v9.732h2.051v-9.732c0-.566-.459-1.025-1.026-1.025zM21.493 9.111a2.05 2.05 0 00-1.546-.703h-4.306l.541-2.67c.122-.606-.032-1.228-.424-1.706s-.97-.753-1.588-.753h-2.348l-5.72 7.358V20.72h12.59a2.038 2.038 0 002.027-1.74l1.261-8.241a2.045 2.045 0 00-.487-1.628zm-2.799 9.557H8.154v-7.326l4.672-6.01h1.345l-1.037 5.128 6.816-.015-1.256 8.223z"></path></svg><span class="_37Nr884k"><span class="DrjyGw-P _1fMYVrTC"><span class="DrjyGw-P _26S7gyB4 _3SccQt-T">57</span></span></span></button><div class="_1ia-z9S2"><div class="vqgb0SM-"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-haspopup="menu" aria-label="옵션 메뉴 열기" type="button"><svg x="0" y="0" viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><circle cx="12" cy="19.4" r="2.5"></circle><circle cx="12" cy="4.4" r="2.5"></circle><circle cx="12" cy="11.9" r="2.5"></circle></svg></button></div></div></div></div><div class="_3HXgtLZQ"></div><div><svg class="zWXXYhVR" viewBox="0 0 88 16" width="88" height="16" aria-label="풍선 5개 중 5.0" title="풍선 5개 중 5.0"><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(18 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(36 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(54 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(72 0) scale(0.6666666666666666)"></path></svg></div><a target="_blank" href="/ShowUserReviews-g294197-d324888-r775124833-Gyeongbokgung_Palace-Seoul.html" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL"><div class="DrjyGw-P _1SRa-qNz _19gl_zL- _1z-B2F-n _2AAjjcx8"><span class="_2tsgCuqy">대한민국의 역사</span></div></a><div class="_3JxPDYSx">2020년 10월</div><div class="_2f_ruteS _1bona3Pu"><div class="cPQsENeY u7nvAeyZ" style="line-break: normal; cursor: auto;"><div class="DrjyGw-P _26S7gyB4 _2nPM5Opx"><span class="_2tsgCuqy">대한민국의 역사가 잠들어 있는 곳. 서울을 방문했다면 꼭 방문해야 되는 곳. 경복궁은 우리의 역사다. 넓은 경복궁을 산책할 수 있는 것은 언제나 행복이다.</span></div></div><div class="_36B4Vw6t" style="line-height: 22.4px;"><button class="LgQbZEQC _60W8Fwrs _1v-QphLm" type="button"><span class="DrjyGw-P _1l3JzGX1">더보기</span><div class="_19mTgobr"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M18.4 7.4L12 13.7 5.6 7.4 4.2 8.8l7.8 7.8 7.8-7.8z"></path></svg></div></button></div></div><div></div><div class="_1b1HH8jx"><div class="DrjyGw-P _26S7gyB4 _1z-B2F-n _1dimhEoy">2020년 10월 21일 작성</div><div class="DrjyGw-P _26S7gyB4 vFpB-FtZ _1dimhEoy">이 리뷰는 트립어드바이저 LLC의 의견이 아닌 트립어드바이저 회원의 주관적인 의견입니다.</div></div></span></span></div><div><hr class="_1viGa88t _3HjraUgL _3inaU6d-"><span data-ft="true"><span data-ft="true"><div class="_2nBYkPk3"><div class="_1o0NHSNc"><div class="_3t0zrF_f"><div class="HiSmthtM"><div class="_1Ear6tw9" style="z-index: 0;"><div class="f3gJ-yIA _1UrkpMOY"><a target="_self" tabindex="-1" aria-hidden="true" href="/Profile/hshdsc408" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr"><div class="WullykOU _2L7OTqqK"><picture class="_2f-Th360 _3YW9cIgT" style="width: 48px; height: 48px;"><img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/f6/f3/7c/default-avatar-2020-29.jpg?w=100&amp;h=-1&amp;s=1" width="100" height="100" alt="hshdsc408" loading="lazy"></picture></div></a></div></div></div></div><div class="_1svEu5jc"><span class="DrjyGw-P _1SRa-qNz _2AAjjcx8"><a target="_self" href="/Profile/hshdsc408" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL">hshdsc408</a></span><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy"></div></div><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy">포스팅 12건</div></div></div></div><div class="_2WOrDRiF"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-label="클릭하여&nbsp;도움이&nbsp;된다는&nbsp;평가&nbsp;추가하기" type="button"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M3.025 9.963c-.566 0-1.025.459-1.025 1.025v9.732h2.051v-9.732c0-.566-.459-1.025-1.026-1.025zM21.493 9.111a2.05 2.05 0 00-1.546-.703h-4.306l.541-2.67c.122-.606-.032-1.228-.424-1.706s-.97-.753-1.588-.753h-2.348l-5.72 7.358V20.72h12.59a2.038 2.038 0 002.027-1.74l1.261-8.241a2.045 2.045 0 00-.487-1.628zm-2.799 9.557H8.154v-7.326l4.672-6.01h1.345l-1.037 5.128 6.816-.015-1.256 8.223z"></path></svg><span class="_37Nr884k"><span class="DrjyGw-P _1fMYVrTC"><span class="DrjyGw-P _26S7gyB4 _3SccQt-T">1</span></span></span></button><div class="_1ia-z9S2"><div class="vqgb0SM-"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-haspopup="menu" aria-label="옵션 메뉴 열기" type="button"><svg x="0" y="0" viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><circle cx="12" cy="19.4" r="2.5"></circle><circle cx="12" cy="4.4" r="2.5"></circle><circle cx="12" cy="11.9" r="2.5"></circle></svg></button></div></div></div></div><div class="_3HXgtLZQ"></div><div><svg class="zWXXYhVR" viewBox="0 0 88 16" width="88" height="16" aria-label="풍선 5개 중 5.0" title="풍선 5개 중 5.0"><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(18 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(36 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(54 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(72 0) scale(0.6666666666666666)"></path></svg></div><a target="_blank" href="/ShowUserReviews-g294197-d324888-r768664216-Gyeongbokgung_Palace-Seoul.html" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL"><div class="DrjyGw-P _1SRa-qNz _19gl_zL- _1z-B2F-n _2AAjjcx8"><span class="_2tsgCuqy">국민이 공감하는 장소</span></div></a><div class="_3JxPDYSx">2020년 7월</div><div class="_2f_ruteS _1bona3Pu"><div class="cPQsENeY u7nvAeyZ" style="line-break: normal; cursor: auto;"><div class="DrjyGw-P _26S7gyB4 _2nPM5Opx"><span class="_2tsgCuqy">경복궁은 국민들이 자주 찾는곳으로 작성자는 주말에 자주 가족들과 방문<br>하고 있음.<br>특히 가족들과 방문시 옛고궁의 멋을 즐길수 있으며 쾌적한 공기와<br>역사를 체험하고 힐링할수 있는곳임.</span></div></div><div class="_36B4Vw6t" style="line-height: 22.4px;"><button class="LgQbZEQC _60W8Fwrs _1v-QphLm" type="button"><span class="DrjyGw-P _1l3JzGX1">더보기</span><div class="_19mTgobr"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M18.4 7.4L12 13.7 5.6 7.4 4.2 8.8l7.8 7.8 7.8-7.8z"></path></svg></div></button></div></div><div></div><div class="_1b1HH8jx"><div class="DrjyGw-P _26S7gyB4 _1z-B2F-n _1dimhEoy">2020년 9월 3일 작성</div><div class="DrjyGw-P _26S7gyB4 vFpB-FtZ _1dimhEoy">이 리뷰는 트립어드바이저 LLC의 의견이 아닌 트립어드바이저 회원의 주관적인 의견입니다.</div></div></span></span></div><div><hr class="_1viGa88t _3HjraUgL _3inaU6d-"><span data-ft="true"><span data-ft="true"><div class="_2nBYkPk3"><div class="_1o0NHSNc"><div class="_3t0zrF_f"><div class="HiSmthtM"><div class="_1Ear6tw9" style="z-index: 0;"><div class="f3gJ-yIA _1UrkpMOY"><a target="_self" tabindex="-1" aria-hidden="true" href="/Profile/Expedition705263" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr"><div class="WullykOU _2L7OTqqK"><picture class="_2f-Th360 _3YW9cIgT" style="width: 48px; height: 48px;"><img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/49/e7/39/expedition705263.jpg?w=100&amp;h=-1&amp;s=1" width="100" height="100" alt="예솔 정" loading="lazy"></picture></div></a></div></div></div></div><div class="_1svEu5jc"><span class="DrjyGw-P _1SRa-qNz _2AAjjcx8"><a target="_self" href="/Profile/Expedition705263" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL">예솔 정</a></span><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy"><span>서울, 대한민국</span></div></div><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy">포스팅 4건</div></div></div></div><div class="_2WOrDRiF"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-label="클릭하여&nbsp;도움이&nbsp;된다는&nbsp;평가&nbsp;추가하기" type="button"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M3.025 9.963c-.566 0-1.025.459-1.025 1.025v9.732h2.051v-9.732c0-.566-.459-1.025-1.026-1.025zM21.493 9.111a2.05 2.05 0 00-1.546-.703h-4.306l.541-2.67c.122-.606-.032-1.228-.424-1.706s-.97-.753-1.588-.753h-2.348l-5.72 7.358V20.72h12.59a2.038 2.038 0 002.027-1.74l1.261-8.241a2.045 2.045 0 00-.487-1.628zm-2.799 9.557H8.154v-7.326l4.672-6.01h1.345l-1.037 5.128 6.816-.015-1.256 8.223z"></path></svg><span class="_37Nr884k"><span class="DrjyGw-P _1fMYVrTC"><span class="DrjyGw-P _26S7gyB4 _3SccQt-T">2</span></span></span></button><div class="_1ia-z9S2"><div class="vqgb0SM-"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-haspopup="menu" aria-label="옵션 메뉴 열기" type="button"><svg x="0" y="0" viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><circle cx="12" cy="19.4" r="2.5"></circle><circle cx="12" cy="4.4" r="2.5"></circle><circle cx="12" cy="11.9" r="2.5"></circle></svg></button></div></div></div></div><div class="_3HXgtLZQ"></div><div><svg class="zWXXYhVR" viewBox="0 0 88 16" width="88" height="16" aria-label="풍선 5개 중 5.0" title="풍선 5개 중 5.0"><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(18 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(36 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(54 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(72 0) scale(0.6666666666666666)"></path></svg></div><a target="_blank" href="/ShowUserReviews-g294197-d324888-r752955452-Gyeongbokgung_Palace-Seoul.html" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL"><div class="DrjyGw-P _1SRa-qNz _19gl_zL- _1z-B2F-n _2AAjjcx8"><span class="_2tsgCuqy">산책하기 좋은 경복궁</span></div></a><div class="_3JxPDYSx">2020년 3월</div><div class="_2f_ruteS _1bona3Pu"><div class="cPQsENeY u7nvAeyZ" style="line-break: normal; cursor: auto;"><div class="DrjyGw-P _26S7gyB4 _2nPM5Opx"><span class="_2tsgCuqy">날씨 좋은 날 종종 산책하러 경복궁에 가는데 마음이 편온해지는 기분이라고 할까요? 특히 봄이나 가을에 산책가는 걸 추천해요!</span></div></div><div class="_36B4Vw6t" style="line-height: 22.4px;"><button class="LgQbZEQC _60W8Fwrs _1v-QphLm" type="button"><span class="DrjyGw-P _1l3JzGX1">더보기</span><div class="_19mTgobr"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M18.4 7.4L12 13.7 5.6 7.4 4.2 8.8l7.8 7.8 7.8-7.8z"></path></svg></div></button></div></div><div></div><div class="_1b1HH8jx"><div class="DrjyGw-P _26S7gyB4 _1z-B2F-n _1dimhEoy">2020년 4월 27일 작성</div><div class="DrjyGw-P _26S7gyB4 vFpB-FtZ _1dimhEoy">이 리뷰는 트립어드바이저 LLC의 의견이 아닌 트립어드바이저 회원의 주관적인 의견입니다.</div></div></span></span></div><div><hr class="_1viGa88t _3HjraUgL _3inaU6d-"><span data-ft="true"><span data-ft="true"><div class="_2nBYkPk3"><div class="_1o0NHSNc"><div class="_3t0zrF_f"><div class="HiSmthtM"><div class="_1Ear6tw9" style="z-index: 0;"><div class="f3gJ-yIA _1UrkpMOY"><a target="_self" tabindex="-1" aria-hidden="true" href="/Profile/guuming" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr"><div class="WullykOU _2L7OTqqK"><picture class="_2f-Th360 _3YW9cIgT" style="width: 48px; height: 48px;"><img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/f6/f0/d5/default-avatar-2020-17.jpg?w=100&amp;h=-1&amp;s=1" width="100" height="100" alt="그미냐" loading="lazy"></picture></div></a></div></div></div></div><div class="_1svEu5jc"><span class="DrjyGw-P _1SRa-qNz _2AAjjcx8"><a target="_self" href="/Profile/guuming" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL">그미냐</a></span><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy"></div></div><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy">포스팅 4건</div></div></div></div><div class="_2WOrDRiF"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-label="클릭하여&nbsp;도움이&nbsp;된다는&nbsp;평가&nbsp;추가하기" type="button"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M3.025 9.963c-.566 0-1.025.459-1.025 1.025v9.732h2.051v-9.732c0-.566-.459-1.025-1.026-1.025zM21.493 9.111a2.05 2.05 0 00-1.546-.703h-4.306l.541-2.67c.122-.606-.032-1.228-.424-1.706s-.97-.753-1.588-.753h-2.348l-5.72 7.358V20.72h12.59a2.038 2.038 0 002.027-1.74l1.261-8.241a2.045 2.045 0 00-.487-1.628zm-2.799 9.557H8.154v-7.326l4.672-6.01h1.345l-1.037 5.128 6.816-.015-1.256 8.223z"></path></svg><span class="_37Nr884k"><span class="DrjyGw-P _1fMYVrTC"><span class="DrjyGw-P _26S7gyB4 _3SccQt-T">1</span></span></span></button><div class="_1ia-z9S2"><div class="vqgb0SM-"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-haspopup="menu" aria-label="옵션 메뉴 열기" type="button"><svg x="0" y="0" viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><circle cx="12" cy="19.4" r="2.5"></circle><circle cx="12" cy="4.4" r="2.5"></circle><circle cx="12" cy="11.9" r="2.5"></circle></svg></button></div></div></div></div><div class="_3HXgtLZQ"></div><div><svg class="zWXXYhVR" viewBox="0 0 88 16" width="88" height="16" aria-label="풍선 5개 중 5.0" title="풍선 5개 중 5.0"><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(18 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(36 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(54 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(72 0) scale(0.6666666666666666)"></path></svg></div><a target="_blank" href="/ShowUserReviews-g294197-d324888-r752707011-Gyeongbokgung_Palace-Seoul.html" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL"><div class="DrjyGw-P _1SRa-qNz _19gl_zL- _1z-B2F-n _2AAjjcx8"><span class="_2tsgCuqy">Good</span></div></a><div class="_3JxPDYSx">2020년 4월</div><div class="_2f_ruteS _1bona3Pu"><div class="cPQsENeY u7nvAeyZ" style="line-break: normal; cursor: auto;"><div class="DrjyGw-P _26S7gyB4 _2nPM5Opx"><span class="_2tsgCuqy">Goooooood 다 좋습니다 다음에 또 오고 싶네요 근처 관광지도많고 먹을거리도많네요 서울올때마다 자주이용중인데 또오고싶습니다</span></div></div><div class="_36B4Vw6t" style="line-height: 22.4px;"><button class="LgQbZEQC _60W8Fwrs _1v-QphLm" type="button"><span class="DrjyGw-P _1l3JzGX1">더보기</span><div class="_19mTgobr"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M18.4 7.4L12 13.7 5.6 7.4 4.2 8.8l7.8 7.8 7.8-7.8z"></path></svg></div></button></div></div><div></div><div class="_1b1HH8jx"><div class="DrjyGw-P _26S7gyB4 _1z-B2F-n _1dimhEoy">2020년 4월 17일 작성</div><div class="DrjyGw-P _26S7gyB4 vFpB-FtZ _1dimhEoy">이 리뷰는 트립어드바이저 LLC의 의견이 아닌 트립어드바이저 회원의 주관적인 의견입니다.</div></div></span></span></div><div><hr class="_1viGa88t _3HjraUgL _3inaU6d-"><span data-ft="true"><span data-ft="true"><div class="_2nBYkPk3"><div class="_1o0NHSNc"><div class="_3t0zrF_f"><div class="HiSmthtM"><div class="_1Ear6tw9" style="z-index: 0;"><div class="f3gJ-yIA _1UrkpMOY"><a target="_self" tabindex="-1" aria-hidden="true" href="/Profile/ruffy1977" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr"><div class="WullykOU _2L7OTqqK"><picture class="_2f-Th360 _3YW9cIgT" style="width: 48px; height: 48px;"><img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/f6/e7/fe/default-avatar-2020-58.jpg?w=100&amp;h=-1&amp;s=1" width="100" height="100" alt="JONGHYUK MUN" loading="lazy"></picture></div></a></div></div></div></div><div class="_1svEu5jc"><span class="DrjyGw-P _1SRa-qNz _2AAjjcx8"><a target="_self" href="/Profile/ruffy1977" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL">JONGHYUK MUN</a></span><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy"><span>도쿄, 일본</span></div></div><div class="_22DaYeMb"><div class="DrjyGw-P _26S7gyB4 _1dimhEoy">포스팅 413건</div></div></div></div><div class="_2WOrDRiF"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-label="클릭하여&nbsp;도움이&nbsp;된다는&nbsp;평가&nbsp;추가하기" type="button"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M3.025 9.963c-.566 0-1.025.459-1.025 1.025v9.732h2.051v-9.732c0-.566-.459-1.025-1.026-1.025zM21.493 9.111a2.05 2.05 0 00-1.546-.703h-4.306l.541-2.67c.122-.606-.032-1.228-.424-1.706s-.97-.753-1.588-.753h-2.348l-5.72 7.358V20.72h12.59a2.038 2.038 0 002.027-1.74l1.261-8.241a2.045 2.045 0 00-.487-1.628zm-2.799 9.557H8.154v-7.326l4.672-6.01h1.345l-1.037 5.128 6.816-.015-1.256 8.223z"></path></svg><span class="_37Nr884k"><span class="DrjyGw-P _1fMYVrTC"><span class="DrjyGw-P _26S7gyB4 _3SccQt-T">1</span></span></span></button><div class="_1ia-z9S2"><div class="vqgb0SM-"><button class="_23XJjgWS _60W8Fwrs _19q-BrlM _1XffX-CB" aria-haspopup="menu" aria-label="옵션 메뉴 열기" type="button"><svg x="0" y="0" viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><circle cx="12" cy="19.4" r="2.5"></circle><circle cx="12" cy="4.4" r="2.5"></circle><circle cx="12" cy="11.9" r="2.5"></circle></svg></button></div></div></div></div><div class="_3HXgtLZQ"></div><div><svg class="zWXXYhVR" viewBox="0 0 88 16" width="88" height="16" aria-label="풍선 5개 중 5.0" title="풍선 5개 중 5.0"><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(18 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(36 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(54 0) scale(0.6666666666666666)"></path><path d="M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z" transform="translate(72 0) scale(0.6666666666666666)"></path></svg></div><a target="_blank" href="/ShowUserReviews-g294197-d324888-r752479234-Gyeongbokgung_Palace-Seoul.html" class="_7c6GgQ6n _60W8Fwrs _37QDe3gr WullykOU _3WoyIIcL"><div class="DrjyGw-P _1SRa-qNz _19gl_zL- _1z-B2F-n _2AAjjcx8"><span class="_2tsgCuqy">가족단위로 방문하기 좋은곳</span></div></a><div class="_3JxPDYSx">2020년 4월 • 가족</div><div class="_2f_ruteS _1bona3Pu"><div class="cPQsENeY u7nvAeyZ" style="line-break: normal; cursor: auto;"><div class="DrjyGw-P _26S7gyB4 _2nPM5Opx"><span class="_2tsgCuqy">요새 더더욱 코로나로 인해 사람 방문이 적음. 두자녀 동반시 성인 입장무료. 지금 시기에 나들이 하기 딱 좋은곳. 지하철 광화문역이나 종각역이용 편리.</span></div></div><div class="_36B4Vw6t" style="line-height: 22.4px;"><button class="LgQbZEQC _60W8Fwrs _1v-QphLm" type="button"><span class="DrjyGw-P _1l3JzGX1">더보기</span><div class="_19mTgobr"><svg viewBox="0 0 24 24" width="20px" height="20px" class="_3nS1tofR iG08Yf8B"><path d="M18.4 7.4L12 13.7 5.6 7.4 4.2 8.8l7.8 7.8 7.8-7.8z"></path></svg></div></button></div></div><div></div><div class="_1b1HH8jx"><div class="DrjyGw-P _26S7gyB4 _1z-B2F-n _1dimhEoy">2020년 4월 10일 작성</div><div class="DrjyGw-P _26S7gyB4 vFpB-FtZ _1dimhEoy">이 리뷰는 트립어드바이저 LLC의 의견이 아닌 트립어드바이저 회원의 주관적인 의견입니다.</div></div></span></span></div><button class="_3L3LNeQW _60W8Fwrs _3l9jVnOs _3UmqBW4M _39EfpzKn _2nBsAkQY" type="button"><span class="DrjyGw-P IT-ONkaj">더 보기</span></button></div>
    reviews = driver.find_elements_by_xpath("//div[@class='_1c8_1ITO']")
    if len(reviews) == 0:
        return -1

    '''
    try:
        writers = reviews[0].find_elements_by_xpath("//span[@class='DrjyGw-P _1SRa-qNz _2AAjjcx8']")
        print('\nwriters size', len(writers))
        for writer in writers:
            print(writer.text)
            writer_list.append(writer.text)
    except:
        pass
    '''
    titles = reviews[0].find_elements_by_xpath("//div[@class='DrjyGw-P _1SRa-qNz _19gl_zL- _1z-B2F-n _2AAjjcx8']")
    print('\ntitle size', len(titles))
    for title in titles:
        print(title.text)
        title_list.append(title.text)

    contents = reviews[0].find_elements_by_xpath("//div[@class='_2f_ruteS _1bona3Pu']")
    print('\ncontents size', len(contents))
    i = 0
    for content in contents:
        print('i', str(i), content.text)
        contents_list.append(content.text)

    for i in range(len(title_list)):
        reviews_list.append('writer' + ',' + title_list[i] +',' + contents_list[i])

    return 0

def update_file_review_info():

    for review in reviews_list:
        # file append store info
        file_review_csv.write(review + '\n')

    print('update_file_review_info')
    pass

def parsing_max_review_count(driver):
    print('parsing_max_review_count')
    # < div class ="_1NyglzPL" > 검색 결과 전체 & nbsp;2, 893 중 & nbsp;31-40 < / div >
    temp = driver.find_elements_by_xpath("//div[@class='_1NyglzPL']")
    buff = temp[0].text.split('검색 결과 전체')
    value = buff[1].split(' ')[1]
    value = value.replace(',','')
    print(buff,value)
    return int(value)

file_url_list = open("/Users/gmnine/Documents/selenium/travel_link_list.txt","r",encoding="utf-8")
file_store_csv = open("/Users/gmnine/Documents/selenium/travel_store.csv","a",encoding="utf-8")
file_review_csv = open("/Users/gmnine/Documents/selenium/travel_review.csv","a",encoding="utf-8")

driver = webdriver.Chrome("/Users/gmnine/Documents/selenium/Chromedriver")

link_access_count = 0
reviews_list = []
while(True):

    # 접속할주소
    # get link from file. file_url_list
    access_url = file_url_list.readline()
    print('link_access_count', link_access_count, access_url)

    # access url
    driver.get(access_url)
    time.sleep(1)
    #-------------------------------
    # parsing - get store info
    store_id = '0'
    store_name = ''
    store_tel = ''

    # parse store info
    store_name = parsing_store_info(driver)
    update_file_store_info()

    # parsing review info (10)
    reviews_list.clear()
    parsing_review_info(driver)
    #reviews_list

    #if return_value >=0:
    if len(reviews_list) >0:
        update_file_review_info()

        # parsing max review count
        max_review_count = parsing_max_review_count(driver)


        for idx in range(10,max_review_count,10):
            time.sleep(20)
            print('access url to get more review', idx)

            buff = access_url.split("-Reviews-")
            review_url = buff[0] + "-Reviews-or" + str(idx) + "-" + buff[1]
            print(review_url)
            driver.get(review_url)

            # parsing review info (10)
            reviews_list.clear()
            parsing_review_info(driver)
            update_file_review_info()

    else:
        print("no review data")

    link_access_count = link_access_count + 1
    if link_access_count > 1:
        break
#-------------------------------
# parsing - get review info
# file append review info

file_url_list.close()
file_store_csv.close()
file_review_csv.close()
driver.close()