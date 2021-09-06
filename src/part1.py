# Your exercises should appear in this file.


def add(x, y):

    add = x + y
    return add


def kwadraat(x):

    """Return het kwadraat van x"""

    kwadraat = x**2
    return kwadraat


def oppervlakte_kubus(z):

    """Return de oppervlakte van een kubus met zijde z"""

    oppervlakte = z * z * 6
    return oppervlakte


def seconds_in_days(days=1):

    """Geef het aantal seconden in het opgegeven aantal dagen

    Als er geen parameter doorgegeven wordt, geef dan het aantal
    seconden in 1 dag terug.
    """

    seconden = days * 86400

    return seconden


def seconds_in_weeks(weeks):

    """Return het aantal seconden in 'week' weken."""

    seconden = weeks * 604800

    return seconden


def seconds_in_years(years):

    """Return het aantal seconden in 'years' jaren.

    Veronderstel dat ieder jaar uit exact 52 weken bestaat.
    """

    seconden = years * 31449600

    return seconden


def seconds_remaining_in_life(age, is_female=False):

    """Return het aantal seconden dat overblijft in je leven.

    Ga uit van een maximale levensduur van 80 jaren voor mannen,
    en 84 jaren voor vrouwen.
    """

    if is_female == False:

        whole_life_men = 80 * 31449600
        leeftijd = age * 31449600
        levensduur = whole_life_men - leeftijd
        return levensduur
    else:
        whole_life_female = 84 * 31449600
        leeftijd = age * 31449600
        levensduur = whole_life_female - leeftijd
        return levensduur


def postcodes():

    """Return een dictionary met postcodes"""

    postcodes = {
        "3000" : "Leuven",
        "3650" : "Dilsen-Stokkem",
    }

    return postcodes


def oneven_getallen(x):

    """Return een lijst met de eerste 'x' oneven getallen."""


    return []