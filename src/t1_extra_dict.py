def maak_persoonsinformatie_dict(naam, leeftijd, gewicht, lengte, oogkleur):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.
    Bijvoorbeeld:
    >>> maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw")
    {'naam': 'Jan', 'leeftijd': 32, 'gewicht': 79, 'lengte': 167, 'oogkleur': 'blauw'}
    """
    info = {
        "naam": naam,
        "leeftijd": leeftijd,
        "gewicht": gewicht,
        "lengte": lengte,
        "oogkleur": oogkleur,
    }

    return info


def tel_autos(lijst_autos):

    """Gegeven een lijst met automerken, geef je een dictionary terug met
    voor ieder automerk het aantal keer dat dit merk in de lijst voorkomt.
    Bijvoorbeeld:
    >>> tel_autos(["bmw", "audi", "audi", "ford", "bmw"])
    {'peugeot': 0, 'ford': 1, 'bmw': 2, 'audi': 2, 'nissan': 0}
    """
    automerken = {
        "audi": 0,
        "bmw": 0,
        "ford": 0,
        "nissan": 0,
        "peugeot": 0,
    }

    for i in lijst_autos:
        automerken[i] = automerken.get(i, 0) + 1
    return automerken





def leeftijden_acteurs(acteurs):
    """Gegeven een lijst van lijsten met informatie over acteurs,
    geef je een lijst van leeftijden van acteurs terug.
    Bijvoorbeeld:
    >>> leeftijden_acteurs([["Will Smith", 53], ["Tom Hanks", 65]])
    [53, 65]
    """

    for name in acteurs:
        return name[1]


def lengtes_acteurs(acteurs):
    """Gegeven een lijst van dictionaries met informatie over acteurs,
    geef je een lijst van lengtes van acteurs terug.
    Bijvoorbeeld:
    >>> lengtes_acteurs([{"naam": "Jennifer Lawrence", "leeftijd": 31, "lengte": 175}])
    [175]
    """

    l = acteurs['lengte']
    return l