from fnmatch import translate

from deep_translator import GoogleTranslator
from deep_translator import single_detection
import re

class Translator:
    my_translator = GoogleTranslator(source='auto', target='german')

    def __init__(self, original_text):
        translate(original_text)

    def get_text_list (original_text):
        text_list = [original_text]
        words = re.split(r'[^\w\b]', original_text)
        if words.__len__() > 0:
            text_list.extend(words)
            text_list = [item for item in text_list if item != ""]
        return text_list

    def get_target_languages (text):
        target_languages = ["en", "de", "nl", "fr", "it"]
        detected_language = single_detection(text, api_key='99788b9ff83963b15ac935fc8fe633c3')
        if detected_language and target_languages.__contains__(detected_language):
            target_languages.remove(detected_language)
            target_languages.insert(0, detected_language)
        return target_languages

    def translate_word(text_list, target_languages):
        # add original to dictionary and remove de from list
        text_in_languages_dic = {}
        text_in_languages_dic[target_languages[0]] = text_list
        target_languages.pop(0)

        # translate every item into target languages accordingly
        for language in target_languages:
            Translator.my_translator.target = language
            text_in_language_list = []
            for text in text_list:
                text_in_language = Translator.my_translator.translate(text=text)
                text_in_language_list.append(text_in_language)
            text_in_languages_dic[language] = text_in_language_list
        return text_in_languages_dic

    def translate (original_text):
        text_list = Translator.get_text_list(original_text)
        print(text_list)
        target_languages = Translator.get_target_languages(original_text)
        print(target_languages)
        text_in_languages_dic = Translator.translate_word(text_list, target_languages)
        return text_in_languages_dic

if __name__ == '__main__':
    print(translate("Ah das ist so cool."))

