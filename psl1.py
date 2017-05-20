import os
import numpy as np
from docutils.nodes import math, status
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.firefox.webdriver import FirefoxProfile




# PROXY = "52.183.30.241:8888"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
executable_path = 'D:\Machine Learning\\Anaconda Python Workspace\\Anaconda3\\chromedriver.exe'
browser = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
# browser.get("http://whatismyipaddress.com")

# options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
# def get_score_per_over(inning_link):
#     scores = []
#     status = []
#     browser.get(inning_link)
#     score_blocks =  browser.find_elements(By.XPATH,'//div[@class="end-of-over-info"]')
#     for score_block in score_blocks:
#         score_block = score_block.text
#         score_block = score_block.split('\n')
#         score_block = score_block[0].split('(')[1]
#         scores.append(score_block.split(')')[0])
#         status.append((score_block.split(')')[1]).lstrip())
#
#     return (scores,status)
def get_commentory(commentroy,inning,match_name):
    browser.get(commentroy)
    try:
        commentories = browser.find_elements(By.XPATH,'//div[@class="commentary-event"]')

        ball =[]
        commentory_text = []
        Wicket = []
        check = 0
        for comentory in commentories:
            comentory = comentory.text.split('\n')
            if len(comentory)<2:
                Wicket.append(comentory)
            else:
                ball.append(comentory[0])
                commentory_text.append(comentory[1])
                if check != 0:
                    Wicket.append("")
                check = 1
        Wicket.append("")

        # (scores,status) = get_score_per_over(commentroy)

        index = 0

        all_data = []
        for i in range(len(ball)):
            # if '6' in ball[i].split('.')[1]:
            #     all_data.append({'Ball': ball[i], 'Commentary': commentory_text[i], 'Wicket': Wicket[i],'Score in Over':scores[index],'Status':status[index]})
            #     index +=1
            # else:
            all_data.append({'Ball': ball[i], 'Commentary': commentory_text[i], 'Wicket': Wicket[i]})

        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, match_name)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        all_da = pd.DataFrame(all_data)
        all_da.drop_duplicates(["Ball"], keep='last', inplace=True)
        all_da.to_csv(match_name + "\\" + inning, header='column_names', index=False)
    except:
        return



def get_scorecard(match,index):
    browser.get(match)
    scorecard =  browser.find_element(By.XPATH,'//div[@class="full-scorecard-block"]').text
    write_file = index + "\Scorecard.csv"
    with open(write_file, "w") as output:
        scorecard = scorecard.split('\n')
        for line in scorecard:
            output.write(line + '\n')

def find_all_match_details(match_link,index):
    get_commentory(match_link+"?innings=1;view=commentary","Innings_1.csv","Match"+str(index))
    get_commentory(match_link+"?innings=2;view=commentary","Innings_2.csv","Match"+str(index))
    get_scorecard(match_link,"Match"+str(index))
    #browser.get(match_link)



# browser.get("http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/series/1075974.html")
get_all_matches=['http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075986.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075987.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075988.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075989.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075990.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075991.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075992.html', 'http://www.espncricinfo.com/ci/engine/match/1075993.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075994.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075995.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075996.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075997.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075998.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1075999.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076000.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076001.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076002.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076003.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076004.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076005.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076006.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076007.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076008.html', 'http://www.espncricinfo.com/pakistan-super-league-2016-17/engine/match/1076009.html']
# grid = browser.find_element(By.XPATH,'//*[@id="viewport"]/div[3]/div/div[3]/div/div[1]/div/div/ul')
match_no = 9
# matches = grid.find_elements(By.XPATH,'//div[@class="large-15 medium-15 small-20 columns content_data"]')
# for match in matches:
#     get_all_matches.append( match.find_element_by_class_name("potMatchMenuLink").get_attribute("href"))
print(get_all_matches)
for i in range(8,len(get_all_matches)):
    print(match_no)
    find_all_match_details(get_all_matches[i],match_no)
    match_no+=1
    time.sleep(5)


