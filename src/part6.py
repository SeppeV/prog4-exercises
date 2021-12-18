def find_problematic_scores(scores):

    """Geef het aantal punten minder dan 5 terug."""

    count = 0
    for i in scores:
        if i < 5:
            count += 1

    return count


def count_ice_cream_flavors(ice_creams):

    """Geef een dictionary terug met voor iedere smaak het aantal ijsjes
    De volgende smaken zijn voorzien: vanille, chocolade, banaan, aardbei
    """

    smaak = {
        "vanille": 0,
        "chocolade": 0,
        "banaan": 0,
        "aardbei": 0,
    }
    for i in ice_creams:
        smaak[i] += 1
    return smaak


def count_words(text):

    """Return het aantal woorden in de tekst"""

    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.lower()
    aantal = 0
    for i in text.split():
        aantal += 1
    return aantal


def count_word_frequency(text):
    """Return een dictionary met voor ieder woord het aantal keren dat het voorkomt
    Voor deze versie worden hoofdletters en kleine letters als verschillend beschouwd.
    Dus, voor de tekst "hello hello world World", krijg je de dictionary:
    {
        "hello": 2,
        "world": 1,
        "World": 1,
    }
    """

    dicte = {}
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")

    for i in text.split():
        if i in dicte:
            dicte[i] += 1
        else:
            dicte[i] = 1

    return dicte


def count_word_frequency_nocase(text):

    """Return een dictionary met voor ieder woord het aantal keren dat het voorkomt
    Voor deze versie worden hoofdletters en kleine letters als hetzelfde beschouwd.
    Dus, voor de tekst "hello hello world World", krijg je de dictionary:
    {
        "hello": 2,
        "world": 2,
    }
    """

    dicte = {}
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.lower()

    for i in text.split():
        if i in dicte:
            dicte[i] += 1
        else:
            dicte[i] = 1

    return dicte