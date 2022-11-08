import pandas as pd
import os
import firebase_admin
from firebase_admin import credentials, firestore


#get current working directory
cwd = os.getcwd()

# import credentials for firebase 
cred = credentials.Certificate(cwd + "/FirebaseCredentials.json")

# initialise firebase
firebase_admin.initialize_app(cred)
db = firestore.client()

#create reference for Ford Fiesta
doc_ref  = db.collection(u"Makes/Ford/Models/Fiesta/Years/2000/Cars")

# import ford fiesta csv file to python dictionary
data = pd.read_csv(cwd + "/fiesta 2015.csv",  engine='python')
data_dict = data.to_dict(orient="records")

# for each element in the dictionary, add car to firebae
list(map(lambda x: doc_ref.add(x), data_dict))

#docs = doc_ref.stream()

#for doc in docs:
    #print(f"{doc.id} => {doc.to_dict()}")

# display
print(data_dict)