from pprint import pprint
from bs4 import BeautifulSoup
import json
import nltk

nltk.download("punkt")

with open("upto100.json", "r") as f1:
    data = json.loads(f1.read())

data = " ".join(data)
data = data.replace("\n", " ")
data = data.replace("\r", " ")
data = BeautifulSoup(data, "lxml").text

output = []

tok = nltk.sent_tokenize(data)
for sentence in tok:
    sentence = " ".join(sentence.split())
    spl = sentence.split("suggest")
    try:
        suggest = spl[1]
        if suggest[:3] == "ed ":
            suggest = suggest[2:]
        if suggest[:4] == "ing ":
            suggest = suggest[3:]
        if suggest[:2] == "s ":
            suggest = suggest[1:]
        try:
            suggest = suggest + "suggest" + spl[2]
        except:
            pass
        if suggest[:6] == " that ":
            output.append(suggest)
    except:
        pass

print(len(output))
with open("toots.txt", "w") as f2:
    for line in output:
        f2.write(line + "\n")
