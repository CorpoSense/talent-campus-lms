
import requests
import csv
import re
from bs4 import BeautifulSoup
import pandas as pd
import time


    
from bs4 import BeautifulSoup

def extract_details(description):
    details = {
        "Contract Type": "Not specified",
        "Skills": [],
        "Responsibilities": []
    }

    # Check if the description is None or empty
    if not description:
        return details

    # Clean HTML if present
    soup = BeautifulSoup(description, 'html.parser')
    cleaned_text = soup.get_text(separator="\n")

    # Split the text into lines
    lines = cleaned_text.split("\n")

    # Initialize flags to determine which section we're in
    in_skills_section = False
    in_responsibilities_section = False

    for line in lines:
        line = line.strip()

        # Detect and handle the "Responsibilities" section
        if line.lower().startswith(("responsibilities", "responsabilités","tâches","missions")):
            in_skills_section = False
            in_responsibilities_section = True
            continue
        
        # Detect and handle the "Skills" section
        elif line.lower().startswith(("skills", "compétences","exigences","profil")):
            in_skills_section = True
            in_responsibilities_section = False
            continue

        # Extract contract type, if mentioned directly
        elif "contract" in line.lower() or "contrat" in line.lower() or "type de contrat" in line.lower() or "type de contat" in line.lower():
            details["Contract Type"] = line.split(":")[-1].strip()
        
        # Add lines to skills or responsibilities based on the current section
        if in_skills_section:
            if line:
                details["Skills"].append(line)
        elif in_responsibilities_section:
            if line:
                details["Responsibilities"].append(line)
                

    return details





def main():
    url = "https://api.ouedkniss.com/graphql"
    headers = {
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXV0aC9sb2dpbi9zb2NpYWwiLCJpYXQiOjE3MjQ0NDM3NDEsImV4cCI6MTcyNTczOTc0MSwibmJmIjoxNzI0NDQzNzQxLCJqdGkiOiJydDhFTEFKY2dZSDBuSGRZIiwic3ViIjoiMTE1MDA5OTIiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3IiwidXNlciI6eyJpZCI6MTE1MDA5OTIsInVzZXJuYW1lIjoiOGNianl0bzFndjA4MTIiLCJpc19hbm9ueW1vdXMiOjAsInJvbGVzIjpbIk1FTUJFUiIsIk1FU1NBR0lORyJdLCJwZXJtaXNzaW9ucyI6WyJjYW5fcmVjZWl2ZV9tZXNzYWdlIiwiY2FuX2NyZWF0ZV90aHJlYWQiLCJjYW5fbGlzdF90aHJlYWQiXX19.BoqGdGIKAfWl1iVrQuyBl0dVeT-QlGDJzKI_P5wX6yHK4WafAWGFHy3ZgyAIuhcf3sFTKPa2452VKSWiEJ8qSvpK7OimsyMedhTrUnZeWRaDf3c6vxuVRqEPiE5YMDiJPB2ZaQh5Mc8R8phemIRtRC4GhmyCQR3yU3_Yk1dsC7JuBWGsq9Y3poTTWn9v4V0xlXqS7xIVl4vDsvRxx9hxSTZ6ptfAhye6BXsMf4lxcIlISsawNnfZvKfctkTHeZelB0tAotpgP8BENCbq7fQjTt1pVfN3_3oHBF0ceJwtcquYwOzIsVthOOMwxgisMedLlJ1UqcT8MYIcGAh4XC0tHg",
        "content-type": "application/json",
        "x-app-version": "3.0.40",
        "referer": "https://www.ouedkniss.com/emploi_offres-informatique-internet/1",
        "origin": "https://www.ouedkniss.com",
        "user-agent": "Mozilla/5.0"
    }

    all_announcements = []
    page = 1
    has_more_pages = True

    while has_more_pages:
        time.sleep(1)
        payload = {
            "operationName": "SearchQuery",
            "variables": {
                "mediaSize": "MEDIUM",
                "q": None,
                "filter": {
                    "categorySlug": "emploi_offres-informatique-internet",
                    "origin": None,
                    "connected": False,
                    "delivery": None,
                    "regionIds": [],
                    "cityIds": [],
                    "priceRange": [None, None],
                    "exchange": False,
                    "hasPictures": False,
                    "hasPrice": False,
                    "priceUnit": None,
                    "fields": [],
                    "page": page,
                    "count": 48
                }
            },
            "query": """
            query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {
                search(q: $q, filter: $filter) {
                    announcements {
                        data {
                            id
                            title
                            description
                            price
                            createdAt
                            cities {
                                name
                            }
                            defaultMedia(size: $mediaSize) {
                                mediaUrl
                            }
                        }
                        paginatorInfo {
                            lastPage
                            hasMorePages
                        }
                    }
                }
            }
            """
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            announcements = data['data']['search']['announcements']['data']
            all_announcements.extend(announcements)

            has_more_pages = data['data']['search']['announcements']['paginatorInfo']['hasMorePages']
            print(f"Page {page} fetched. More pages? {has_more_pages}")
            page += 1
        else:
            print(f"Request error: {response.status_code}")
            print(response.text)
            break

    flattened_data = []
    for announcement in all_announcements:
        description = announcement.get('description', '')
        
       
        details = extract_details(description)

        flattened_data.append({
            "ID": announcement.get('id'),
            "Title": announcement.get('title'),
            "Description": description,
            "Price": announcement.get('price'),
            "Created At": announcement.get('createdAt'),
            "City": announcement['cities'][0]['name'] if announcement.get('cities') else '',
            "Contract Type": details["Contract Type"],
            "Skills": ', '.join(details["Skills"]),
            "Responsibilities": ', '.join(details["Responsibilities"])
        })

    df = pd.DataFrame(flattened_data)
    df.to_csv('ouedkniss_all_announcements_detailed.csv', index=False)
    print("All data saved to ouedkniss_all_announcements_detailed.csv")

if __name__ == "__main__":
    main()


# import requests
# import pandas as pd
# import time

# url = "https://api.ouedkniss.com/graphql"

# headers = {
#     "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXV0aC9sb2dpbi9zb2NpYWwiLCJpYXQiOjE3MjQ0NDM3NDEsImV4cCI6MTcyNTczOTc0MSwibmJmIjoxNzI0NDQzNzQxLCJqdGkiOiJydDhFTEFKY2dZSDBuSGRZIiwic3ViIjoiMTE1MDA5OTIiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3IiwidXNlciI6eyJpZCI6MTE1MDA5OTIsInVzZXJuYW1lIjoiOGNianl0bzFndjA4MTIiLCJpc19hbm9ueW1vdXMiOjAsInJvbGVzIjpbIk1FTUJFUiIsIk1FU1NBR0lORyJdLCJwZXJtaXNzaW9ucyI6WyJjYW5fcmVjZWl2ZV9tZXNzYWdlIiwiY2FuX2NyZWF0ZV90aHJlYWQiLCJjYW5fbGlzdF90aHJlYWQiXX19.BoqGdGIKAfWl1iVrQuyBl0dVeT-QlGDJzKI_P5wX6yHK4WafAWGFHy3ZgyAIuhcf3sFTKPa2452VKSWiEJ8qSvpK7OimsyMedhTrUnZeWRaDf3c6vxuVRqEPiE5YMDiJPB2ZaQh5Mc8R8phemIRtRC4GhmyCQR3yU3_Yk1dsC7JuBWGsq9Y3poTTWn9v4V0xlXqS7xIVl4vDsvRxx9hxSTZ6ptfAhye6BXsMf4lxcIlISsawNnfZvKfctkTHeZelB0tAotpgP8BENCbq7fQjTt1pVfN3_3oHBF0ceJwtcquYwOzIsVthOOMwxgisMedLlJ1UqcT8MYIcGAh4XC0tHg",
#     "content-type": "application/json",
#     "x-app-version": "3.0.40",
#     "referer": "https://www.ouedkniss.com/emploi_offres-informatique-internet/1",
#     "origin": "https://www.ouedkniss.com",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
# }

# all_announcements = []
# page = 1

# # Fetch the first page to get the lastPage value
# response = requests.post(url, json={
#     "operationName": "SearchQuery",
#     "variables": {
#         "mediaSize": "MEDIUM",
#         "q": None,
#         "filter": {
#             "categorySlug": "emploi_offres-informatique-internet",
#             "origin": None,
#             "connected": False,
#             "delivery": None,
#             "regionIds": [],
#             "cityIds": [],
#             "priceRange": [None, None],
#             "exchange": False,
#             "hasPictures": False,
#             "hasPrice": False,
#             "priceUnit": None,
#             "fields": [],
#             "page": page,  # Pagination: First page
#             "count": 48    # Number of items per page
#         }
#     },
#     "query": """
#     query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {
#         search(q: $q, filter: $filter) {
#             announcements {
#                 data {
#                     id
#                     title
#                     description
#                     price
#                     createdAt
#                     cities {
#                         name
#                     }
#                     defaultMedia(size: $mediaSize) {
#                         mediaUrl
#                     }
#                 }
#                 paginatorInfo {
#                     lastPage  # Total number of pages
#                     hasMorePages
#                 }
#             }
#         }
#     }
#     """
# }, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     last_page = data['data']['search']['announcements']['paginatorInfo']['lastPage']
#     announcements = data['data']['search']['announcements']['data']
#     all_announcements.extend(announcements)
    
    
#     # Fetch all remaining pages
#     for page in range(2, last_page + 1):
#         time.sleep(1)
#         payload = {
#             "operationName": "SearchQuery",
#             "variables": {
#                 "mediaSize": "MEDIUM",
#                 "q": None,
#                 "filter": {
#                     "categorySlug": "emploi_offres-informatique-internet",
#                     "origin": None,
#                     "connected": False,
#                     "delivery": None,
#                     "regionIds": [],
#                     "cityIds": [],
#                     "priceRange": [None, None],
#                     "exchange": False,
#                     "hasPictures": False,
#                     "hasPrice": False,
#                     "priceUnit": None,
#                     "fields": [],
#                     "page": page,  # Pagination: Current page
#                     "count": 48    # Number of items per page
#                 }
#             },
#             "query": """
#             query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {
#                 search(q: $q, filter: $filter) {
#                     announcements {
#                         data {
#                             id
#                             title
#                             description
#                             price
#                             createdAt
#                             cities {
#                                 name
#                             }
#                             defaultMedia(size: $mediaSize) {
#                                 mediaUrl
#                             }
#                         }
#                         paginatorInfo {
#                             hasMorePages
#                         }
#                     }
#                 }
#             }
#             """
#         }

#         response = requests.post(url, json=payload, headers=headers)
#         if response.status_code == 200:
#             data = response.json()
#             announcements = data['data']['search']['announcements']['data']
#             all_announcements.extend(announcements)
            
#         else:
#             print(f"Erreur de requête: {response.status_code}")
#             print(response.text)
#             break
# else:
#     print(f"Erreur de requête: {response.status_code}")
#     print(response.text)

# # Flatten data for CSV export
# flattened_data = []
# for announcement in all_announcements:
#     flattened_data.append({
#         "ID": announcement.get('id'),
#         "Title": announcement.get('title'),
#         "Description": announcement.get('description'),
#         "Price": announcement.get('price'),
#         "Created At": announcement.get('createdAt'),
#         "City": announcement['cities'][0]['name'] if announcement.get('cities') else '',
#     })

# # Convert to DataFrame
# df = pd.DataFrame(flattened_data)

# # Save to CSV
# df.to_csv('ouedkniss_all_announcements.csv', index=False)
# print("All data saved to ouedkniss_all_announcements.csv")
