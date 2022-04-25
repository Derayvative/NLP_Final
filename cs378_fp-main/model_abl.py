import json
import random
 
# Opening JSON file
f = open('../squad_data/example_set.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

questions = list()
for i in data['data']:
    questions.append(i['question'])
 
#Assigns random questions to every data element
for i in data['data']:
    i['question'] = random.choice(questions)

with open('test.json', 'w') as g:
    json.dump(data, g)
f.close()