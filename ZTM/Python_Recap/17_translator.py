from googletrans import Translator
import asyncio

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]


async def my_translate(list):
    """translate list of words to dictionary"""
    trans_dict = {}
    for word in list:
        async with Translator() as trans:
            translated = await trans.translate(word, src="fr", dest="en")
        trans_dict.update({word: translated.text})
    return trans_dict


print(asyncio.run(my_translate(french_words)))
