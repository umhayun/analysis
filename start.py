from selenium import webdriver
import time
driver = webdriver.Chrome("c:\webdriver\chromedriver.exe")
driver.get("https://www.instagram.com")
time.sleep(2)
email = 'djagkdbs@naver.com'  
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = 'dytjq7169' 
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(3)

china=['중국여행','중국맛집','중국관광']
japan=['일본여행','일본맛집','일본관광']
america=['미국여행','미국맛집','미국관광']
taiwan=['태국여행','태국맛집','태국관광']
vietnam=['베트남여행','베트남맛집','베트남관광']
from crawling import crawling
words_list={'china':china,'japan':japan,'america':america,'taiwan':taiwan,'vietnam':vietnam}
import pandas as pd
for key in words_list:
    data=crawling(driver,words_list[key])
    results_df=pd.DataFrame(data)
    results_df.columns=['content','date','like','place','tags']
    results_df.to_excel('country/'+key+'.xlsx',index=False)