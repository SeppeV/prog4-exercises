from math import pi, sqrt

# Your exercises should appear in this file.

def oppervlakte_kegel(r, h):

    # Zoek via Google naar "area cone"
    l = sqrt(r**2 + h**2)
    A = pi * r * l + pi * r**2

    return A


def last_element(l):

    """Return het laatste element uit een lijst"""

    resultaat = l[-1]

    return resultaat



def sum_of_list(l):

    """Return de som van alle elementen uit een lijst"""

    resultaat = sum(l)

    return resultaat


def average_of_list(l):

    """Return het gemiddelde van alle elementen uit een lijst"""

    resultaat = sum(l) / len(l)

    return resultaat


def min_max_of_list(l):

    """Return het minimum en het maximum van de elementen uit een lijst"""

    resultaat = min(l), max(l)

    return resultaat


def squared_list(l):

    """Return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst

    squared_list([2,3]) == [4, 9]
    """

    return []


def differences_list(l1, l2):
    return []


def replace_takis_mr_issaris(text):
    resultaat = text.replace("Takis", "Mr. Issaris")
    return resultaat
