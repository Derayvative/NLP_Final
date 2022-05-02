import json

def get_answer(answers):
    text = [a["text"] for a in answers]
    answer_start = [a["answer_start"] for a in answers]
    return {"text": text, "answer_start": answer_start}

def get_answer_recalc(answers, context):
    text = [a["text"] for a in answers]
    try:
        answer_start = [context.index(a["text"]) for a in answers]
    except ValueError:
        print(context)
        raise Exception("Unable to find original Answer")

    return {"text": text, "answer_start": answer_start}

def reformat_json(data, f, recalc_answers=False):
    new_data = {"data": []}
    for i in range(len(data["data"])):
        for qa in range(len(data["data"][i]["paragraphs"])):
            for q in range(len(data["data"][i]["paragraphs"][qa]["qas"])):
                if not recalc_answers:
                    d = {"id": data["data"][i]["paragraphs"][qa]["qas"][q]["id"], "title": data["data"][i]["title"], "context": data["data"][i]["paragraphs"][qa]["context"], "question": data["data"][i]["paragraphs"][qa]["qas"][q]["question"], "answers": get_answer(data["data"][i]["paragraphs"][qa]["qas"][q]["answers"])}
                else:
                    d = {"id": data["data"][i]["paragraphs"][qa]["qas"][q]["id"], "title": data["data"][i]["title"], "context": data["data"][i]["paragraphs"][qa]["context"], "question": data["data"][i]["paragraphs"][qa]["qas"][q]["question"], "answers": get_answer_recalc(data["data"][i]["paragraphs"][qa]["qas"][q]["answers"], data["data"][i]["paragraphs"][qa]["context"])}
                new_data["data"].append(d)
    json.dump(new_data, open(f, 'w'))

def create_control_set(data):
    for i in range(len(data["data"])):
        data["data"][i]["paragraphs"] = data["data"][i]["paragraphs"][:5]

    json.dump(data, open("contrast-set-control.json", 'w'))

# data = json.load(open("../squad_data/contrast-set-control.json"))
# reformat_json(data,"../squad_data/reformat-conrast-set-control.json")

data = json.load(open("../squad_data/contrast-set-v1.0.json"))
reformat_json(data,"../squad_data/reformat-contrast-set-v1.0.json", True)
