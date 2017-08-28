from selenium import webdriver
import selenium
import time
import re
import random
import json

driver = webdriver.Chrome('/home/zheka/chromedriver')

driver.get('https://www.parimatch.com/en/live.html')
tennisOutput = {}
basketballOutput = {}
volleyballOutput = {}
regex = r"^(.+ - .+)$\n^(\d+)-(\d+)\(([\d,\-]+)\)"
while True:

    timenew, timeold = [int(time.strftime('%M')), 3]
    if timenew % 15 == 0 and timenew != timeold:
        timeold = int(time.strftime('%M'))
        output = open('tennis.txt', 'w')
        output.write(str(json.dumps(tennisOutput, indent=4)))
        output.close()
        output = open('volleyball.txt', 'w')
        output.write(str(json.dumps(volleyballOutput, indent=4)))
        output.close()
        output = open('basketball.txt', 'w')
        output.write(str(json.dumps(basketballOutput, indent=4)))
        output.close()
        driver.get('https://www.parimatch.com/en/live.html')

    try:
        tabletennisItem = driver.find_element_by_id('tabletennisItem').text
    except selenium.common.exceptions.NoSuchElementException: tabletennisItem = None
    except selenium.common.exceptions.StaleElementReferenceException:
        tabletennisItem = driver.find_element_by_id('tabletennisItem').text
        tennis = re.findall(regex, tabletennisItem, re.MULTILINE)
        for i in tennis:
            tmp = list(map(int, re.findall('(\d+)', i[-1])))
            if i[1] != '0' and i[2] != '0':
                tennisOutput[i[0]] = {'score': i[1] + ' - ' + i[2], 'total in match - ':str(sum(tmp)), 'total in quater - ':str(sum(tmp)/(int(i[1])+int(i[2]))), 'last quater score': str(tmp[-2]) + " " + str(tmp[-1])}
    else:
        tennis = re.findall(regex, tabletennisItem, re.MULTILINE)
        for i in tennis:
            tmp = list(map(int, re.findall('(\d+)', i[-1])))
            if i[1] != '0' and i[2] != '0':
                tennisOutput[i[0]] = {'score': i[1] + ' - ' + i[2], 'total in match - ':str(sum(tmp)), 'total in quater - ':str(sum(tmp)/(int(i[1])+int(i[2]))), 'last quater score': str(tmp[-2]) + " " + str(tmp[-1])}

    try:
        basketballItem = driver.find_element_by_id('basketballItem').text
    except selenium.common.exceptions.NoSuchElementException: basketballItem = None
    except selenium.common.exceptions.StaleElementReferenceException:
        basketballItem = driver.find_element_by_id('basketballItem').text
        basketball = re.findall(regex, basketballItem, re.MULTILINE)
        for i in basketball:
            tmp = list(map(int, re.findall('(\d+)', i[-1])))
            if i[1] != '0' and i[2] != '0':
                basketballOutput[i[0]] = {'score': i[1] + ' - ' + i[2], 'total in match - ':str(sum(tmp)), 'total in quater - ':str(sum(tmp)/(int(i[1])+int(i[2]))), 'last quater score':str(tmp[-2]) + " " + str(tmp[-1])}
    else:
        basketball = re.findall(regex, basketballItem, re.MULTILINE)
        for i in basketball:
            tmp = list(map(int, re.findall('(\d+)', i[-1])))
            if i[1] != '0' and i[2] != '0':
                basketballOutput[i[0]] = {'score': i[1] + ' - ' + i[2], 'total in match - ':str(sum(tmp)), 'total in quater - ':str(sum(tmp)/(int(i[1])+int(i[2]))), 'last quater score':str(tmp[-2]) + " " + str(tmp[-1])}

    try:
        volleyballItem = driver.find_element_by_id('volleyballItem').text
    except selenium.common.exceptions.NoSuchElementException: volleyballItem = None
    except selenium.common.exceptions.StaleElementReferenceException:
        volleyballItem = driver.find_element_by_id('volleyballItem').text
        volleyball = re.findall(regex, volleyballItem, re.MULTILINE)
        for i in volleyball:
            tmp = list(map(int, re.findall('(\d+)', i[-1])))
            if i[1] != '0' and i[2] != '0':
                volleyballOutput[i[0]] = {'score': i[1] + ' - ' + i[2], 'total in match - ':str(sum(tmp)), 'total in quater - ':str(sum(tmp)/(int(i[1])+int(i[2]))), 'last quater score':str(tmp[-2]) + " " + str(tmp[-1])}
    else:
        volleyball = re.findall(regex, volleyballItem, re.MULTILINE)
        for i in volleyball:
            tmp = list(map(int, re.findall('(\d+)', i[-1])))
            if i[1] != '0' and i[2] != '0':
                volleyballOutput[i[0]] = {'score': i[1] + ' - ' + i[2], 'total in match - ':str(sum(tmp)), 'total in quater - ':str(sum(tmp)/(int(i[1])+int(i[2]))), 'last quater score':str(tmp[-2]) + " " + str(tmp[-1])}

    if tabletennisItem is None and basketballItem is None and volleyballItem is None:
        time.sleep(random.randint(90, 600))
        driver.get('https://www.parimatch.com/en/live.html')
        continue

    time.sleep(random.randint(3, 5))
