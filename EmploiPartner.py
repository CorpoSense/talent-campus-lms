import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()  
driver.get('https://www.emploipartner.com/fr/offre-emploi')


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) 

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  

    last_height = new_height


with open('job_offers_EmploiPartner.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Location', 'Description', 'Date', 'Contract Type'])  

    # job offers
    job_offers_container = driver.find_element(By.ID, 'ep_job_list')
    job_offer_divs = job_offers_container.find_elements(By.CLASS_NAME, 'col-xs-12.margin-top-10') 
    for job_offer_div in job_offer_divs:
        try:
            #  job title
            title_tag = job_offer_div.find_element(By.TAG_NAME, 'h3')
            title = title_tag.text.strip() if title_tag else "No title"

            #  job location
            location_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'p.logo-location.hidden-xs')
            location = location_tag.text.strip() if location_tag else "No location"

            #job description
            description_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'p.hide-on-mobile span')
            description = description_tag.text.strip() if description_tag else "No description"

            #  job date
            date_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'div.col-xs-8.col-md-9 span')
            date = date_tag.text.strip() if date_tag else "No date"

            # contract type
            contract_type_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'div.col-xs-4.col-md-3 h5.contract-type')
            contract_type = contract_type_tag.text.strip() if contract_type_tag else "No contract type"

            #  CSV file
            writer.writerow([title, location, description, date, contract_type])

        except Exception as e:
            print(f"Error extracting job offer details: {e}")

driver.quit()