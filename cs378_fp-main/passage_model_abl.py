import json
import random
import sys

arg = sys.argv[1]
 
# Opening JSON file
f = open(arg)
 
# returns JSON object as
# a dictionary
data = json.load(f)
total = 0
word_counter = dict()
count = 0
for i in data['data']:
    print(count, len(data['data']))
    count+=1
    p = (i['context'])
    for w in p.split():
        if w not in word_counter:
            word_counter[w]=0
        word_counter[w]+=1
        total+=1

def get_random():
    r = random.randrange(total)
    for key in word_counter:
        r = r - word_counter[key]
        if (r < 0):
            return key
    return "NAN"


#Assigns gibberish using unigram model
for i in data['data']:
    p = i['context']
    txt = (p.split())

    ans=(i["answers"])
    ans_st = ans["answer_start"]
    ans_txt = ans["text"]
    
    ans_map = dict()
    for j in range(len(ans_st)):
        if ans_st[j] not in ans_map:
            ans_map[ans_st[j]] = list()
        ans_map[ans_st[j]].append(ans_txt[j])
        ans_map[ans_st[j]].sort(reverse=True)
    
    randoms = dict()
    for k in ans_map:
        n = random.randrange(len(txt))
        randoms[k] = (n)

    res = ""
    new_ans_st = list()
    new_ans_text = list()
    for idx in range(len(txt)):
        temp = (get_random())
        added=False

        for k in ans_map:
            st = len(res)
            if (idx == randoms[k]):
                for w in ans_map[k]:
                    new_ans_st.append(st)
                    new_ans_text.append(w)
                res += ans_map[k][0] + " "
                added=True

        if (not added):
            res+=(temp) + " "
    i["context"] = res
    ans["answer_start"] = new_ans_st
    ans["text"] = new_ans_text

with open('test.json', 'w') as g:
    json.dump(data, g)
f.close()