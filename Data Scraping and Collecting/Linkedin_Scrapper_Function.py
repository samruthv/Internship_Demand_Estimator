from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
from bs4 import BeautifulSoup
import re


def Linkedin_Scrapper(keyword, num_jobs, verbose):
    
    driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
    driver.maximize_window()
    time.sleep(5)    
    #Open login page
    driver.get('https://www.linkedin.com/jobs/search?keywords='+keyword+'&location=&redirect=false&position=1&pageNum=0')
    
    jobs = 1
    data = []
    
    while jobs < num_jobs:
        
        try:
            
            print(jobs)
            jobbutton = driver.find_element_by_xpath("//li[@data-row='"+str(jobs)+"']")
            jobbutton.click()
            time.sleep(2)
            src = driver.page_source
            soup = BeautifulSoup(src, 'lxml')
            time.sleep(2)
            title_block = soup.find('div',{'class': 'topcard__content'})
            
            
            pos_title = title_block.find('h2',{'class': 'topcard__title'}).get_text().strip()
            #time.sleep(.5)
            
            comp_name = title_block.find('a',{'class': 'topcard__org-name-link topcard__flavor--black-link'}).get_text().strip()
            #time.sleep(.5)
            
            comp_loc = title_block.find('span',{'class': 'topcard__flavor topcard__flavor--bullet'}).get_text().strip()
            #time.sleep(.5)
            
            try:
                posted_time = title_block.find('span',{'class': 'topcard__flavor--metadata posted-time-ago__text'}).get_text().strip()
            except Exception:  
                posted_time = title_block.find('span',{'class': 'topcard__flavor--metadata posted-time-ago__text posted-time-ago__text--new'}).get_text().strip()
            #time.sleep(.5)
            
            try:
                applicants = title_block.find('span',{'class': 'topcard__flavor--metadata topcard__flavor--bullet num-applicants__caption'}).get_text().strip()
            except Exception:
                applicants = title_block.find('figcaption',{'class': 'num-applicants__caption'}).get_text().strip()
            
            
            #time.sleep(.5)
            
            more_info = soup.find('ul',{'class': 'job-criteria__list'}).get_text()
            
            
            result = re.search('Seniority level(.*)Employment type', more_info)  
            senority_level = result.group(1)
             
            
            result = re.search('Employment type(.*)Job function', more_info)  
            employment_type = result.group(1)
             
            
            result = re.search('Job function(.*)Industries', more_info)  
            job_function = result.group(1)
            
            
            result = re.search('Industries(.*)', more_info)  
            industries = result.group(1)
             
            
            jobs = jobs+1
            
            #employmwnt_type
            #job_function
            #industries
            
            if verbose:
                print("Position of Title: {}".format(pos_title))
                print("Company Name: {}".format(comp_name))
                print("Job Location: {}".format(comp_loc))
                print("Posted Time: {}".format(posted_time))
                print("Number Of Applicants: {}".format(applicants))
                print("Seniority Level: {}".format(senority_level))
                print("Employment Type: {}".format(employment_type))
                print("Job Function: {}".format(job_function))
                print("Industries: {}".format(industries))
                print("======================================================")
            
            
            data.append({"Position of Title" : pos_title,
            "Company Name" : comp_name,
            "Job Location" : comp_loc,
            "Posted Time" : posted_time,
            "Number Of Applicants" : applicants,
            "Seniority Level" : senority_level,
            "Employment Type" : employment_type,
            "Job Function" : job_function,
            "Industries" : industries,})
            
            
        except Exception:
            driver.back()
    
    driver.close()        
            
    
    return pd.DataFrame(data)
    

