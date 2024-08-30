import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import requests
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--remote-debugging-port=9222')

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# URL to scrape
url = 'https://www.emploipartner.com/fr/offre-emploi'

# Open the webpage
driver.get(url)
time.sleep(5)  # Allow time for the page to load
# Scroll to load all job offers
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Allow time for content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

job_links = []
job_data = []
with open('job_offers_EmploiPartner3.csv', mode='w', newline='', encoding='utf-8') as file:
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
            #link
            link = job_offer_div.find_element(By.CSS_SELECTOR, 'h3.function-title a').get_attribute('href')
            job_links.append(link)

            job_data.append([title, location, description, date, contract_type, link])

            #  CSV file
            writer.writerow([title, location, description, date, contract_type])

        except Exception as e:
            print(f"Error extracting job offer details: {e}")
       # Close the WebDriver
driver.quit()

# Open CSV file for writing
with open('job_offers_EmploiPartner3.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Location', 'Description', 'Date', 'Contract Type', 'Missions', 'Profil'])

    # Loop through all job links and parse details using BeautifulSoup
    for job in job_data:
        title, location, description, date, contract_type, link = job
        try:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                description_tag = soup.find('div', class_='job-description')
                description = description_tag.text.strip() if description_tag else "No description"

                # Extract missions
                missions_section = soup.find('h3', class_='offer-title', string='Missions')
                missions = missions_section.find_next('ul').text.strip() if missions_section else "No missions"

                # Extract profil
                profil_section = soup.find('h3', class_='offer-title', string='Profil')
                profil = profil_section.find_next('ul').text.strip() if profil_section else "No profil"

                # Write to CSV
                writer.writerow([title, location, description, date, contract_type, missions, profil])

            else:
                print(f"Failed to retrieve {link}: Status code {response.status_code}")

        except Exception as e:
            print(f"Error processing job link {link}: {e}")

            

print("Scraping completed and data written to CSV.")






# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()  
# driver.get('https://www.emploipartner.com/fr/offre-emploi')


# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3) 

#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break  

#     last_height = new_height


# with open('job_offers_EmploiPartner.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Title', 'Location', 'Description', 'Date', 'Contract Type'])  

#     # job offers
#     job_offers_container = driver.find_element(By.ID, 'ep_job_list')
#     job_offer_divs = job_offers_container.find_elements(By.CLASS_NAME, 'col-xs-12.margin-top-10') 
#     for job_offer_div in job_offer_divs:
#         try:
#             #  job title
#             title_tag = job_offer_div.find_element(By.TAG_NAME, 'h3')
#             title = title_tag.text.strip() if title_tag else "No title"

#             #  job location
#             location_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'p.logo-location.hidden-xs')
#             location = location_tag.text.strip() if location_tag else "No location"

#             #job description
#             description_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'p.hide-on-mobile span')
#             description = description_tag.text.strip() if description_tag else "No description"

#             #  job date
#             date_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'div.col-xs-8.col-md-9 span')
#             date = date_tag.text.strip() if date_tag else "No date"

#             # contract type
#             contract_type_tag = job_offer_div.find_element(By.CSS_SELECTOR, 'div.col-xs-4.col-md-3 h5.contract-type')
#             contract_type = contract_type_tag.text.strip() if contract_type_tag else "No contract type"

#             #  CSV file
#             writer.writerow([title, location, description, date, contract_type])

#         except Exception as e:
#             print(f"Error extracting job offer details: {e}")

# driver.quit()