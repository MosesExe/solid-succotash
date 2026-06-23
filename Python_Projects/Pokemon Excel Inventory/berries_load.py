# I kept getting obsessd with the idea of making a middleware
#  when I realize what I'm describing is just a second file
# This file will be left as a call file dedicated to fetching the requests in v2 
import requests 
import pandas as pd
import json
from PIL import Image
from urllib.request import urlopen
import io
import os

#6th Function Writes the information to the berry sheet on the excel
# Come back later on and strip these all to bare minimum functions            
def writeToFrame(berryDF):
    with pd.ExcelWriter("Pokeitem_data.xlsx", engine="xlsxwriter") as writer:
        berryDF.style.set_properties(**{'text-align':'center'}).to_excel(writer, sheet_name="Berries", startrow=0,header=True, index=False)
        for row_num, image_path in enumerate(berryDF["Berry Image"], start=1):
            # Sets the name of the sheet we're on for here it's berries
            worksheet = writer.sheets["Berries"]
            worksheet.set_column("B:B", 15)
            worksheet.set_column("C:C", 15)
            worksheet.set_column("E:E", 90)
            worksheet.set_row(row_num, 30)
            # Actually shoves the image directly into the cell of the selected worksheet and category
            worksheet.embed_image(row_num,1,image_path)

# 5th function is responsible for finally setting up the actual Dataframe and calling the write for it
def setupDataFrame(berryList):
    berryDF = pd.DataFrame(berryList, columns=["Berry ID","Berry Image","Berry Name","Cost","Berry Effect"])
    berryDF.to_excel("Pokeitem_data.xlsx")
    # Will write to the excel file should try and have it return a dataframe then pass that
    writeToFrame(berryDF)

#Function 4.5? Feel like it could be a long function but still
# For Later: Item ID would be berryDetails["id"]
def getBerryDescription(berry):
    berryEffect = ""
    berryDetails = requests.get(berry["item"]["url"]).json()
    berryCost = berryDetails["cost"]
    for berryEntry in berryDetails["effect_entries"]:
        if berryEntry["language"]["name"]=='en':
            berryEffect = berryEntry["short_effect"]
    berryImg = Image.open(urlopen(berryDetails["sprites"]["default"]))
    berryImgRef = io.BytesIO()
    berryImg.save(berryImgRef,format='PNG')
    return berryImgRef,berryCost,berryEffect
# 4th Function parses actual data for the berry items
# Parse json for each individual json sent in 
def parseBerryData(berry):
    berryDetailsResp = requests.get(berry["url"], params=params)
    berryDetails = berryDetailsResp.json()
    berryData = []
    berryData.extend(getBerryDescription(berryDetails))
    berryData.insert(0, berryDetails["id"])
    berryData.insert(2, str.capitalize(berry["name"]))
    return berryData

# 3rd Function adds to itemList
# Need to add more function later to have it split items
def getBerryList(berryJSON):
    berryList=[]
    for berry in berryJSON["results"]:
        berryList.append(parseBerryData(berry))
    return berryList

# 2nd Function calls the actual API and passes the response to a function
# Added some text for fun, but might change it for fun
# This can be fixed later on to work with multiple API that can get passed from the first file, but let's not fly completely out of scope
def fetchBerryResponse():
    # There's like 3 non-bedazzled berries that don't get called back for some reason? 
    # Might fetch em later I guess.
    # This gets us the rest for now
    api_url = "https://pokeapi.co/api/v2/berry?limit=64"
    params = {}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        print(f"Successfully retrieved inventory")
        setupDataFrame(getBerryList(response.json()))
        print("Went and Bought em all! PokeBux! Storing in Bills computer")
        print("Successfully uploaded to Bill's computer!")
        os.startfile('Pokeitem_data.xlsx',show_cmd=3)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        print("Bill's PC is currently experiencing issues")

# First Function that checks if the file actually exists
# If it exist remove the file and start the program
def berryFileCheckAndStart():
    existingFile = "Pokeitem_data.xlsx"
    if(os.path.isfile(existingFile)):
        print("Okay Berry List! \n Oh great here comes GENGAR!")
        with open(r'Gengar.txt', 'r', encoding="utf-8") as f:
            for line in f:
                # end="" prevents adding double newlines
                print(line, end="")
        os.remove(existingFile)
        print("\n ...So Gengar ate all the berries...I'll order more")
        fetchBerryResponse()
    else:
        print("Bag's Empty! Let's go berry picking!")
        fetchBerryResponse()

params=''