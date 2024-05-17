import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://www.adamchoi.co.uk/fixtures"

# Specify the path to the EdgeDriver executable
path = r"C:\Users\DELL\chromedriver-win32\chromedriver.exe"

# Create a new instance of the Edge WebDriver with options
service = Service(path)
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(service=service, options=options)

# Open the specified website
driver.get(website)

matches = driver.find_elements(By.XPATH, '//tr[@data-ng-show="vm.fixturesLoaded && vm.fixtureMeetsThreshold(fixture)"]')
home = []
all=[]
home_team=[]
ko=[]
away_team=[]
all1=[]
away=[]

for match in matches:
    try:
        # Ensure the XPath is correct for the first cell of each row
        home_text = match.find_element(By.XPATH, './td[1]').text
        home.append(home_text)
        all_text = match.find_element(By.XPATH, './td[2]').text
        all.append(all_text)
        home_team_text = match.find_element(By.XPATH, './td[3]').text
        home_team.append(home_team_text)
        ko_text = match.find_element(By.XPATH, './td[4]').text
        ko.append(ko_text)
        away_team_text = match.find_element(By.XPATH, './td[5]').text
        away_team.append(away_team_text)
        all1_text = match.find_element(By.XPATH, './td[6]').text
        all1.append(all1_text)
        away_text = match.find_element(By.XPATH, './td[7]').text
        away.append(away_text)
    
    except Exception as e:
        print(f'Error extracting time: {e}')



df = pd.DataFrame({'home': home,'all': all, 'home_team':home_team, 'ko' : ko, 'away_team':away_team, 'all1': all1, 'away': away  })

print(df)
# Add a delay to keep the browser open for 10 seconds
time.sleep(300)

# Close the browser
driver.quit()
