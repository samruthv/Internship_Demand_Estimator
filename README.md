  *I am a firm beliver that knowlegde leads to prosperity and one of my greatest passions is education. Not only the education that is recieved in the lecture rooms, but also the practical, hands on expirince one gets during internships and co-ops inbetweeen the school year. As a former undergrad student myself I have seen how stressful and intimidating trying to land your first internship can be. I wanted to create a model that really shows and understands the vast data of students around the country sending application into the massive void of the job force.*
# Internship Demand Estimator(Based on Industry/Location): Overview
- Created a model the estimated the number of intern applicants for a job posting based on job location and industry. (Mean Absolute Error - 25.1 applications)
- Cleaned and organized data in Pandas to create the best possible Data Frame to use for exploritory data analysis and model building.
- Scrapped 10,000 job postings from LinkedIn using Selenium and BeautifulSoup
- Created different models: Linear Regression, Lasso Regression and Random Forest. Formulated a better Model by optimizing using GridsearchCV. 
- Using Flask made a client facing API that can is AWS accessible.

## Code
**Python**: Version 3.7.6  
**Packages**: Numpy, Pandas, Sklearn, matplotib, selinium, seaborn, beautifulsoup, flask, pickle, json 


## rescources

https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven

## Contact Information

## Scraping
In order to collect a wide variaty of data, the bot that we build for scrapingwent through a large variaty of internship inputs to recienve all different types of internship posting. It was also cruicial that I didnt sign into any linkedIn account when scraping because we did not want our account data to manipulate search results. In order to get even better data, it may have been benificial to run the scrapper through a VPN. Here is a list of different inputs we searched for during our scraping proccess. 

[Intern,Design Internship jobs,Management Intern job,Mechanical Engineering Intern jobs,Electrical Engineering Intern jobs,Chemical Engineering Intern jobs,Systems Engineering Intern jobs,Quality Engineering Intern job,Software Engineering Intern jobs,research Engineering Intern jobs,Industrial Engineering Intern jobs,Manufacturing Engineering Intern jobs,"Psychology Intern jobs,Information Intern jobs,Biology Intern jobs,Human Resources Intern jobs,Communications Intern jobs,Medical Intern jobs,nurse Intern jobs,Finance Intern job,Economics Intern jobs,Public Health Intern Jobs,Exercise Science Intern Jobs,Logistics Intern Jobs,Materials Intern Jobs,Supply Chain Intern Jobs,Electronics Intern Jobs,Criminal Justice Intern Jobs,safety Intern Jobs,Politics Intern Jobs,Journalism Intern Jobs,Labor Intern Job,Accounting Intern Jobs,English Intern Jobs,Education Intern Jobs,Marketing Intern Jobs,Sales Intern Jobs,History Intern Jobs,Mathamatics Intern Jobs,Data Science Intern Jobs,Animal Intern,Human Rights Intern,Biomedical Intern,Bioengineering Intern,Health Intern,Management Intern,Civil Engineering Intern,Structural Intern,nutrition science Intern,Social Work Intern,Physics Intern,astronomy Intern,chemistry Intern,sports Intern,music Intern,Statistics Intern,sociology Intern,art Intern,UI Intern,UX Intern,Environment Intern,Policy Intern,Drama Intern,Theatre Intern,molecular biology Intern,Biotechnology Intern,philosophy Intern,Food Science Intern,Design Intern,Business Intern,Business administration Intern,Biochemistry Intern,Linguistics Intern,Anthropology Intern,Dance Intern,Ceramic Intern,Plant Science Inter,cinema Intern,film Intern,media Intern,PR Inter,microbiology Intern,policy,Urban Intern,Architecture Intern,marine biology Intern,Astrophysics Intern,geology Intern,spanish Intern,Biometry Intern,Cognative Intern,Geography Intern,Therapeutics Intern,Agriculture Intern,Language Intern,Student Intern,Summer Intern,Tech Intern,Non Tech Intern,food Intern,Culinary Intern,clothing Intern]

**Email:** samruthv@gmail.com
**Phone Number:** 732-317-9426
