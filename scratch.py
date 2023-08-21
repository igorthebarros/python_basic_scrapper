from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

print("Hey, punk! The application has started...")

url = 'https://www.thesecret.tv/the-secret-stories'
pageURLPath = '/page'
pageCounter = 1

driver = webdriver.Chrome()

driver.get(url)

sleep(3)

stories_fields = driver.find_elements(By.XPATH, "//*[@id='content']/section/div/div/div[2]/div")

for story in stories_fields:

    date_element = story.find_element(By.CLASS_NAME, "date")
    # date = date_element.text.strip()
    
    # title_element = story.find_element(By.TAG_NAME, "h2")
    # title = title_element.text.strip()
    
    # post_element = story.find_element(By.XPATH, "p[2]")
    # post = post_element.text.strip()
    
    print(date_element)
    # print("Title:", title)
    # print("Post:", post)

driver.quit()




# We need to use pageResponse.content rather than
# pageResponse.text because html.fromstring implicity
# expects bytes as input
# tree = html.fromstring(pageResponse.content)
# storiesXPath = ''
# stories = tree.xpath('')