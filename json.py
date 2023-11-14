#Imports the json library
import json


#Create the data dictionary

data = {

    'name': 'Jarod Atienzo',
    'age':20,
    'city':'Seattle,WA',
    'interests':['Gym', 'Running', 'videogames'],
    'is_student':True

}
#Opens and writes in a seperate json file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)
#Packages a seperate file with the data
print('Data has been written to data.json')


#Reading for the data
with open('data.json', 'r') as json_file:
    
    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#Modifying the json data
loaded_data['age'] = 21
loaded_data['interests'].append('Basketball')

#Updates the data.json file
with open('data.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')
