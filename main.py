from functions import Wow
import spacy

nlp = spacy.load('en')
wow = Wow()

b = wow.get_boss(24723)
# c = wow.get_all_bosses()

text = b['description']

doc = nlp(text)

for i in range(len(doc.ents)):
    print('{} is a {}'.format(doc.ents[i], doc.ents[i].label_))



