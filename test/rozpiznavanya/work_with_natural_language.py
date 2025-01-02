# class TransformationLanguage():
#     pass
import re


nlpp = ("Привіт!!! включи-музику, а також ще щось неламане &2,?")
nlpp = re.split(r"\W+", nlpp)
token_text = []
for i in nlpp:
    if i.split():
        token_text.append(i)
print(token_text)

    
