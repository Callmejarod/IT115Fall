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
##
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')