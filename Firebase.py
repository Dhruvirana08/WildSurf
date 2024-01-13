import firebase_admin
#import WildSurf
from firebase_admin import credentials
from firebase_admin import firestore
import os
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#importing data
# firestore_db.collection(u'AnimalData').add({'color': 'Brown', 'fur': 'yes'})

# reading data 
animalDictionary = list(db.collection(u'AnimalData').get())
animalLstDict = []
for animal in animalDictionary:
    animalLstDict.append(animal.to_dict())

plantDictionary = list(db.collection(u'PlantData').get())
plantLstDict = []
for plant in plantDictionary:
    plantLstDict.append(plant.to_dict())