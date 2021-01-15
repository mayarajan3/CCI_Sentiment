import csv
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
driver = webdriver.Chrome('./chromedriver')

driver.get("https://twitter-sentiment-cnn.herokuapp.com/")
input_field = driver.find_element_by_id("tweet")
submit = driver.find_element_by_name("tweet_submit_button")

input_field.send_keys("h")
submit.click()

print(driver.find_element_by_tag_name("body").text.split()[10])

input_field = driver.find_element_by_id("tweet")
submit = driver.find_element_by_name("tweet_submit_button")
input_field.send_keys("hell no")
submit.click()

print(driver.find_element_by_tag_name("body").text.split()[10])
"""

all_scores = {}
with open('myhashtags.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        all_scores[row[0].lower().strip()] = []

driver = webdriver.Chrome('./chromedriver')
driver.get("https://twitter-sentiment-cnn.herokuapp.com/")

try:
    with open('mydata.csv', 'r', errors='ignore') as file:
        reader = csv.reader(file, delimiter = ',')
        for i, row in enumerate(reader):
            # Tweet text has index 3
            # Tweet hashtags have index -5
            text = row[3]
            hashtags = row[-4].split('|')
            input_field = driver.find_element_by_id("tweet")
            submit = driver.find_element_by_name("tweet_submit_button")
            input_field.send_keys(text)
            submit.click()
            
            for hashtag in hashtags:
                hashtag = hashtag.lower().strip()
                if hashtag in all_scores:
                    all_scores[hashtag].append((i, float(driver.find_element_by_tag_name("body").text.split()[10])))
except:
    print("Exception: logging current results")

average_scores = {}
for key in all_scores.keys():
    average_scores[key] = None if len(all_scores[key]) == 0 else sum(score[1] for score in all_scores[key]) / len(all_scores[key])

with open('all_scores_atlanta.json', 'w') as file:
    json.dump(all_scores, file)

with open('average_scores_atlanta.json', 'w') as file:
    json.dump(average_scores, file)