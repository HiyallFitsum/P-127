from selenium import webdriver
from bs4 import BeautifulSoup
import time, os, ssl
import csv

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("D:/MyPythonCode/Web_Scraping_1/chromedriver")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ["Proper name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 457):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for th_tag in soup.find_all("th", attrs={"class", "headerSort"}):
            tr_tags = th_tag.find_all("tr")
            temp_list = []
            for index, tr_tag in enumerate(tr_tags):
                if index == 0: 
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
        star_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper300.csv", "w")as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()