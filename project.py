from selenium import webdriver
import  time
# https://search.musinsa.com/category/001001 반팔티셔츠
# https://search.musinsa.com/category/001010 긴팔티셔츠
# https://search.musinsa.com/category/001002 셔츠/블라우스
# https://search.musinsa.com/category/001005 맨투맨/스웨트셔츠

url = 'https://search.musinsa.com/category/001001'
driver = webdriver.Chrome('./chromedriver')
# driver.implicitly_wait(3) # 대기
driver.get(url)
# driver.find_element_by_id('search_query').click()
# driver.find_element_by_id('search_query').send_keys('반팔 티셔츠')
# driver.find_element_by_id('search_button').click()
# driver.implicitly_wait(3)
html = driver.page_source
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
list = soup.select_one('#searchList')
# print(list)
# print(list.select('.list_img')[0])
inner = list.select('.li_inner')
for i in inner:
    img = i.select_one('.lazyload')['data-original']
    item = i.select_one('.item_title')
    info = i.select_one('.list_info')
    price = i.select_one('.price')
    count = i.select_one('.count')
    print(img)
    print(item.text)
    print(info.a['title'])
    print(price.text)
    if(count != None):
        print(count.text)


# #상품 이미지
# img=list.select('.list_img')
# for i in img :
#     print(i.select_one('.lazyload')['data-original'])
#
# #아이템 타이틀
# item = list.select('.item_title')
# for i in item:
#     print(i.text)
#
# #상품 제목
# info = list.select('.list_info')
# for i in info:
#     print(i.a['title'])
#
# #상품 가격
# price = list.select('.price')
# for i in price:
#     print(i.text)
#
# count = list.select('.count')
# for i in count:
#     print(i.text)
