import json
import random
import sys

arg = sys.argv[1]
 
# Opening JSON file
f = open(arg)
 
# returns JSON object as
# a dictionary
data = json.load(f)

questions = list()
for i in data['data']:
    questions.append(i['question'])
 
#Assigns random questions to every data element
for i in data['data']:
    i['question'] = random.choice(questions)

json_string = json.dumps(data)
print("done")

#with open('test.json', 'w') as g:
#    json.dump(data, g)
f.close()