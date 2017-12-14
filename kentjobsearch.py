from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def go_to_kent(browser):
    browser.get("http://jobs.kent.edu")
    assert "kent" in browser.title

def go_to_search_results(browser, target):

    input_element = browser.find_element_by_id('search-keyword')   
    assert input_element != None
    input_element.clear()
    input_element.send_keys(target)
    input_element.send_keys(Keys.RETURN)
    time.sleep(2)

def scrape_search_results(browser):
    
    search_list = browser.find_element_by_id("search-results-content")
    job_name = search_list.find_elements_by_class_name("job-link")
    assert job_name!= None
    job_id = search_list.find_elements_by_class_name("job-externalJobNo")
    job_title = []
    job_ids = []
    for j in job_id:
        job_ids.append(j)

    for i in job_name:
        job_title.append(i)

    print("Job ID           Job Name")
    k = 0
    while k < len(job_ids):
        print(job_ids[k].text," ", job_name[k].text)
        k = k + 1

 
if __name__ == "__main__":
    #browser = webdriver.Chrome('/Users/Mahesha/Downloads/sem 3/Software Testing Methodology/HomeWork/3amazonwebdriver/chromedriver')
    browser = webdriver.PhantomJS()
    go_to_kent(browser)
    go_to_search_results(browser,"chemistry")
    scrape_search_results(browser)
