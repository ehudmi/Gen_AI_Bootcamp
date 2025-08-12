import os
from translate import Translator


def my_translate():
    """translate file of words to another file"""
    directory = os.path.dirname(os.path.abspath(__file__))
    source_file = "readme_1.txt"
    destination_file = "translated.txt"
    source_file_path = os.path.join(directory, source_file)
    destination_file_path = os.path.join(directory, destination_file)
    translator = Translator(to_lang="zh")
    if os.path.exists(destination_file_path):
        print("file exists")
    else:
        with open(destination_file_path, "x") as dest:
            print("created file")
    with open(source_file_path, "r") as source, open(
        destination_file_path, "a", encoding="utf-8"
    ) as dest:
        for line in source:
            words = line.split(" ")
            print(words)
            for word in words:
                translation = translator.translate(word)
                dest.write(f"{translation} ")


my_translate()
