  *I am a firm beliver that knowlegde leads to prosperity and am greatly passionate about education. Not only the education that is recieved in the lecture rooms, but also the practical, hands on expirince one gets during internships and co-ops inbetweeen the school year. As a former undergrad student myself I have seen how stressful and intimidating trying to land your first internship can be. I wanted to create a model that really shows and understands the vast data of students around the country sending application into the massive void of the job force.*
# Internship Demand Estimator(Based on Industry/Location): Overview
- Created a model the estimated the number of intern applicants for a job posting based on job location and industry. (Mean Absolute Error - 25.1 applications)
- Cleaned and organized data in Pandas to create the best possible Data Frame to use for exploritory data analysis and model building.
- Scrapped 10,000 job postings from LinkedIn using Selenium and BeautifulSoup
- Created different models: Linear Regression, Lasso Regression and Random Forest. Formulated a better Model by optimizing using GridsearchCV. 
- Using Flask made a client facing API that can is AWS accessible.

<p align="center">
  Job Posting Data by State
</p>

<p align="center">
  <img width="400" src="Additional%20Files/total_postings_mainland.PNG">
</p>
<p align="center">
 
  *The above image shows the location of the job postings by the state. We can see that states like California, New York and Texas are more oppertunity while states like Montana, Mississippi, and Kentuky are less. Exploratory Data like this helped us create our model.*
</p>



## Code
**Python**: Version 3.7.6  
**Packages**: Numpy, Pandas, Sklearn, matplotib, selinium, seaborn, beautifulsoup, flask, pickle, json 


## Rescources

https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven
https://www.ibisworld.com/united-states/list-of-industries/



## Data Scraping
In order to collect a wide variaty of data, the bot that we build for scrapingwent through a large variaty of internship inputs to recienve all different types of internship posting. It was also cruicial that I didnt sign into any linkedIn account when scraping because we did not want our account data to manipulate search results. In order to get even better data, it may have been benificial to run the scrapper through a VPN. 

list of different inputs we searched for during our scraping proccess:

https://github.com/samruthv/LinkedIn_DataScience_Project/blob/main/Additional%20Files/LinkedIn%20Scraper%20Search%20Inputs

list of information that we scraped from each individual job posting:

- Company Name
- Job Location
- Posted Time
- Number Of Applicants
- Seniority Level
- Employment Type
- Job Function
- Industries

<img src="Additional%20Files/Top20Companies.png" width="900" >

## Data Cleaning

In order to get the best reaults from our model building and EDA, I cleaned the Data to be easy to read and manipulate. The first step of cleaning throught the job postings was to go through and delete all the repeating postings. After, using the location I catogorized each application into a a state catogory. Using keywords from the scraped industry catagory, I was able to block job postings under my indutries catigories.

List of Industries:

https://github.com/samruthv/LinkedIn_DataScience_Project/blob/main/Additional%20Files/List%20of%20Industries

<img src="Additional%20Files/industry_vs_applicants_per_posting.PNG" width="900" >
<img src="Additional%20Files/industry_vs_job_postings.PNG" width="900" >

## Data Analysis

Before creating a model, I was able to use data visualization tools in Python to really understand the data. This analysis was important to interperate the data so we know what data to use and what models we want to make. Here is some cool data that I found:


<img src="Additional%20Files/Noprofit_image.PNG" width="900" >
<img src="Additional%20Files/Pharma_image.PNG" width="900" >
<img src="Additional%20Files/Tech_image.PNG" width="900" >
<img src="Additional%20Files/Tech_comapation_image.PNG" width="900" >
<img src="Additional%20Files/Tech_demand_image.PNG" width="900" >


<img src="Additional%20Files/Coorelation.png" width="900" >


![](Additional%20Files/Noprofit_image.PNG)

## Model

## Model API

## Contact Information

**Email:** samruthv@gmail.com
**Phone Number:** 732-317-9426

https://public.tableau.com/profile/samruth.vennapusala#!/
