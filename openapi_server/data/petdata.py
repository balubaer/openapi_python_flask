import json
from openapi_server.models.pet import Pet  # noqa: E501
import typing

pets = []

def readPets():
    pets.clear()
    # Opening JSON file
    f = open('pets.json',)
   
    # returns JSON object as 
    # a array
    data = json.load(f)
   
    # Iterating through the json
    # list
    for petdict in data:
        apet = Pet.from_dict(petdict)
        apet.photo_urls = petdict['photo_urls']
        pets.append(apet)
   
    #Closing file
    f.close()
    return pets

def addPet(pet: Pet):
    pets.append(pet)
    newArray = []
    for pet in pets:
        newArray.append(pet.to_dict())

    with open("pets.json", "w") as outfile:
        json.dump(newArray, outfile)

def nextPetID():
    result = 0
    for pet in pets:
        if pet.id > result:
            result = pet.id
    return (result + 1)
