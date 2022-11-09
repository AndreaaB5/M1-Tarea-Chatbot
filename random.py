import random


def random_string():
    random_list = [
        "Lo siento, no te entendí bien",
        "Podrías repetirlo porfavor?",
        "No puedo responde eso todavía, porfavor intenta otra vez"
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
