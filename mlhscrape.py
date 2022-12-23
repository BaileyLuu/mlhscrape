import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import json

URL = "https://mlh.io/seasons/2023/events"
response = requests.get(URL)


soup = BeautifulSoup(response.content, "html.parser") #response.content works better than response.text for text representations
# print(findIcon)
iconLink = []
path = os.getcwd()  #get the absolute path of the current working directory
directoryIcon = "hackathonIcon"
directoryImg = "hackathonBg"

fullPathIcon = os.path.join(path, directoryIcon)
fullPathImg = os.path.join(path, directoryImg)
# os.mkdir(fullPathIcon)        #uncomment this to automatically create a director to contain logos/images
# os.mkdir(fullPathImg)

load_dotenv(find_dotenv())
username= os.environ.get("MONGODB_USERNAME")
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://{username}:{password}@tutorial.ed3hnwb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client.list_database_names()
mlhscrape_db = client.mlhscrape #use specific database
collection = mlhscrape_db.mlhscrape

def main():
    id = 1
    for icon in soup.find_all("div", class_="event-wrapper"):
        if icon.h3 and icon.img:
            title = icon.find("h3", class_="event-name").text
            weburl = icon.find("a", class_="event-link").get('href')
            iconLogo = icon.find("div", class_="event-logo")
            iconLink = iconLogo.img['src']
            date = icon.find("p", class_="event-date").text
            city =  icon.find("span", itemprop="city").text
            state = icon.find("span", itemprop="state").text
            format = icon.find("div", class_="event-hybrid-notes").span.text            
    
            #-----Only uncomment this if you would like to download MLH's hackathons logos and images in the folder
            #This is to download the larger image

            # if ".png" in icon.img['src'].lower():
            #     extension = "png"
            # elif ".jpg" in icon.img['src'].lower():
            #     extension = "jpg"
            # elif ".jpeg" in icon.img['src'].lower():
            #     extension = "jpeg"
            # elif ".svg" in icon.img['src'].lower():
            #     extension = "svg"

            # if "/" not in title: #get the HTTP 403 Error using wget, therefore using urllib
            #     urllib.request.urlretrieve(icon.img['src'], f'{path}/hackathonBg/{title}.{extension}')
            # else:
            #     altString = icon.img['alt']
            #     urllib.request.urlretrieve(icon.img['src'],  f'{path}/hackathonBg/{altString}.{extension}')
            # #This is to download the larger image


            # #This is to download the logo, smaller image
            
            # if ".png" in iconLogo.img['src'].lower():
            #     extension = "png"
            # elif ".jpg" in iconLogo.img['src'].lower():
            #     extension = "jpg"
            # elif ".jpeg" in iconLogo.img['src'].lower():
            #     extension = "jpeg"
            # elif ".svg" in iconLogo.img['src'].lower():
            #     extension = "svg"

            # if "/" not in title:
            #     urllib.request.urlretrieve(iconLogo.img['src'], f'{path}/hackathonIcon/{title}.{extension}')
            # else:
            #     altString = iconLogo.img['alt']
            #     urllib.request.urlretrieve(iconLogo.img['src'],  f'{path}/hackathonIcon/{altString}.{extension}')
            
            # #This is to download the logo, smaller image
            #-----Only uncomment this if you would like to download MLH's hackathons logos and images in the folder

            insert_hackathon_info(id, title, weburl, iconLink, icon.img['src'], date, city, state, format)
            id += 1
            hackathonjson = []
            for item in collection.find(): #get the data from the database collection
                hackathonjson.append(item)
            with open("hackathonsdb.json", "w") as writeJSON: #store the hackathons information in json file
                json.dump(hackathonjson, writeJSON, ensure_ascii=False, default=str, indent=4) #beautify the json file

def insert_hackathon_info(id, name, weburl, icon, img, date, city, state, format):
    mlhscrape_document = {
        "_id": id,
        "name": name,
        "url": weburl,
        "icon_url": icon,
        "img_url": img,
        "date": date,
        "city": city,
        "state": state,
        "format": format
    }
    collection.insert_one(mlhscrape_document)

main()
