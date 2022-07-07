import time
def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/"+word
    return url
def select_first(driver):
    first = driver.find_element_by_css_selector("div._aagw")
    first.click()
    time.sleep(4)
def move_next(driver):
    right = driver.find_element_by_css_selector("div._aaqg._aaqh>button")
    right.click()
    time.sleep(4)
def get_content(driver):
    import re
    from bs4 import BeautifulSoup
    import unicodedata  
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    try:
        content = soup.select("div._a9zs > span")[0].text
        content = unicodedata.normalize('NFC', content)
    except:
        content = ' '
    tags = re.findall(r'#[^\s#,\\]+', content)
    date = soup.select("time._aaqe")[0]['datetime'][:10]
    try:
        like = soup.select("div._aacl._aaco._aacw._aacx._aada._aade > span")[0].text
    except:
        like = 0
    try: 
        place = soup.select("a.oajrlxb2")[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place = ''
    data = [content, date, like, place, tags]
    return data 
    