import os
from providers.chrome_driver import *
from config import *
from selenium.webdriver.common.by import By
import pandas as pd

def login(driver):
    driver.get(LOGIN_URL)
    time.sleep(5)

    username = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_btn = driver.find_element(By.CLASS_NAME, 'btn__primary--large ')

    login_btn.click()
    time.sleep(5)

def get_tech_internships(driver):
    all_titles = []
    all_companies = []
    all_locations = []
    all_links = []
    driver.get(JOB_SEARCH_BASE_URL)
    time.sleep(5)
    job_search_url = driver.current_url + INTERNSHIP_FILTER + SW_COMPANIES_FILTER
    time.sleep(5)
    iterate = True
    idx = 0
    while iterate:
        jobs_not_found_element = driver.find_elements(By.CLASS_NAME, 'jobs-search-no-results-banner__image')
        if jobs_not_found_element:
            iterate = False
        else:
            url = job_search_url + INCREMENT_FILTER + str(idx)
            driver.get(url)
            time.sleep(3)
            x = driver.find_elements(By.CLASS_NAME, 'jobs-search-results-list')
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', x)
            jobs = driver.find_elements(By.CLASS_NAME, COMPANY_ELEMENT_CLASS)
            jobs.pop()
            titles, companies, locations, links = parse_jobs(jobs)
            all_titles += titles
            all_companies += companies
            all_locations += locations
            all_links += links
            idx += 25
            print(len(jobs))  
    # invalid last element

    return pd.DataFrame({
        "Title": all_titles,
        "Company": all_companies,
        "Location": all_locations,
        "Link": all_links
    })

def parse_jobs(jobs):
    print(len(jobs))
    titles = []
    companies = []
    locations = []
    links = []
    for job in jobs:
        title = ''
        company = ''
        location = ''
        link = ''
        title_element = job.find_elements(By.CLASS_NAME, 'artdeco-entity-lockup__title')
        # print(job_title_element)
        if title_element:
            title_element = title_element[0].find_element(By.TAG_NAME, 'a')
            title = title_element.text
            link = title_element.get_attribute('href')
        company_element = job.find_elements(By.CLASS_NAME, 'artdeco-entity-lockup__subtitle')
        # print(company_element)
        if company_element:
            company = company_element[0].text
        location_element = job.find_elements(By.CLASS_NAME, 'job-card-container__metadata-wrapper')
        if location_element:
            location = ''
            location_elements = location_element[0].find_elements(By.TAG_NAME, 'li')
            for element in location_elements:
                location += element.text
        titles.append(title)
        companies.append(company)
        locations.append(location)
        links.append(link)
    # df = pd.DataFrame({
    #     "Job Title": titles,
    #     "Company": companies,
    #     "Location": location
    # })

    # df.to_csv('jobs.csv')
    
    return titles, companies, locations, links

def get_HR_employees(company_name):
    pass

    

driver = get_driver()
login(driver)
df = get_tech_internships(driver)
df.to_csv('jobs.csv')






