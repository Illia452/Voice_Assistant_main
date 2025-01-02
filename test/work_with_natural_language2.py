# import spacy
#from transformers import MarianMTModel, MarianTokenizer


# # model_name = r"..models\translate\opus-2020-01-16_uk-en"
# model_name = "Helsinki-NLP/opus-mt-uk-en"
# tokenizer = MarianTokenizer.from_pretrained(model_name)
# model = MarianMTModel.from_pretrained(model_name)
# test_text = ["Коти гуляють по дахах будинків."]
# inputs = tokenizer(test_text, return_tensors="pt", padding=True)
# translated = model.generate(**inputs)
# tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
# print(tgt_text)

# from translate import Translator
# translator= Translator(from_lang="uk", to_lang="en")
# translation = translator.translate("Коти гуляють по дахах будинків")
# print(translation)

# translator= Translator(from_lang="en", to_lang="uk")
# translation2 = translator.translate(translation)
# print(translation2)


# import argostranslate.package
import argostranslate.translate

from_code = "uk"
to_code = "en"

# # Download and install Argos Translate package
# argostranslate.package.update_package_index()
# available_packages = argostranslate.package.get_available_packages()
# package_to_install = next(
#     filter(
#         lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
#     )
# )
# argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate("Кіт лежав на дивані", from_code, to_code)
print(translatedText)
translatedText = argostranslate.translate.translate("Кіт лежав на дивані", from_code, to_code)
print(translatedText)
translatedText = argostranslate.translate.translate("Кіт лежав на дивані", from_code, to_code)
print(translatedText)
translatedText = argostranslate.translate.translate("Кіт лежав на дивані", from_code, to_code)
print(translatedText)
translatedText = argostranslate.translate.translate("Кіт лежав на дивані", from_code, to_code)
print(translatedText)
translatedText = argostranslate.translate.translate("Кіт лежав на дивані", from_code, to_code)
print(translatedText)
# '¡Hola Mundo!'