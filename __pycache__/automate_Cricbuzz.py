from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t
import pandas as pd

#varable for website
website = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches"

#path for chrome web driver
path = r"C:\Users\DELL\chromedriver-win32\chromedriver.exe"

#service and options declaration
service = Service(path)
options = webdriver.ChromeOptions()
options.add_argument("'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'")

#driver declaration
driver = webdriver.Chrome(service= service , options= options)
#getting website
driver.get(website)

matches = driver.find_elements(By.XPATH , '//div[@class="cb-col-60 cb-col cb-srs-mtchs-tm"]')

match_details=[]
stadium = []
result=[]

for match in matches:
    try:
        A_text = match.find_element(By.XPATH , './a[1]').text
        match_details.append(A_text)
    except Exception as e:
        print(f"Error")
        match_details.append(None)
    try:
        B_text = match.find_element(By.XPATH , './div').text
        stadium.append(B_text)
    except Exception as e:
        print(f"Error")
        stadium.append(None)
    try:
        R_text = match.find_element(By.XPATH , './a[2]').text
        result.append(R_text)
    except Exception as e:
        print(f"Error")
        result.append(None)


df = pd.DataFrame({'match_deatails' :match_details , 'Stadium' : stadium , 'Result' : result})
df.to_csv('Cricbuzz_data.csv' ,index= False)
print(df)

t.sleep(300)

driver.quit()


