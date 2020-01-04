from selenium import webdriver
from bs4 import BeautifulSoup
import time
try:
    driver = webdriver.Chrome('D:\\python_practice\\chromedriver.exe')
    main_url="https://www.sarkariresult.com/latestjob.php"
    driver.get(main_url)
    time.sleep(5)
    soup=BeautifulSoup(driver.page_source, 'lxml')
    page=soup.find('table')
    fp = open('sarkari_result.csv','a')
    fp.write('Name of Post,Link\n')
    for ul in page.find_all('ul'):
        
        link = ul.find_all('a')
        
        url = link[1]['href']
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup('table')
        table_all = table[0].find_all('table')
        table_top = table_all[0]
        table_bot = table_all[1]
        
        all_text = ''
        for td_all in table[0].find_all('tr'):
            for td in td_all.find_all('td'):
                all_text += ' ' + td.text.strip()
        
        search_pattern = 'Engineering'
        
        if search_pattern in all_text:
            fp.write(str(link[1].text)+','+str(link[1]['href'])+'\n')
    #        print(link[1]['href'])
    #        print(link[1].text)
finally:
    fp.close()