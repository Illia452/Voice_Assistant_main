# class TransformationLanguage():
#     pass
import re
import spacy

# nlp = spacy.load("uk_core_news_sm")
# doc = nlp("Привіт, включи музику, а також ще щось неламане\n\n")
# for token in doc:
#     print(token.text)


nlpp = ("Привіт!!! включи-музику, а також ще щось неламане &2,?")
nlpp = re.split(r"\W+", nlpp)
token_text = []
for i in nlpp:
    if i.split():
        token_text.append(i)
print(token_text)

    


print(nlpp)




# l = ["1", "1", "1", "2", "1", "1"]
# filtered = []
# for i in l:
#     if i == "1":
#         filtered.append(i)
# print(filtered)