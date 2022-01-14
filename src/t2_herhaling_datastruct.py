import  statistics

def maak_videokaart_dict(merk, naam, architectuur, geheugen, busbreedte, diesize, jaar):

    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.

    Bijvoorbeeld:
    >>> maak_videokaart_dict("NVIDIA", "RTX 3080", "Ampere", 10, 320, 628, 2020)
    {'merk': 'NVIDIA', 'naam': "RTX 3080", 'architectuur': "Ampere", 'geheugen': 10, 'busbreedte': 320, 'diesize': 628, "jaar": 2020}
    """

    videokaart = {
        "naam": naam,
        "merk": merk,
        "architectuur": architectuur,
        "geheugen": geheugen,
        "busbreedte": busbreedte,
        "diesize": diesize,
        "jaar": jaar,
    }

    return videokaart



def tel_videokaarten(lijst_videokaarten):

    """Geef het totaal aantal videokaarten in de lijst van videokaarten terug."""

    aantal = len(lijst_videokaarten)
    return aantal


def tel_videokaarten_per_merk(lijst_videokaarten):

    """Geef het aantal videokaarten per merk in de lijst van videokaarten terug.

    Het resultaat is dus een dictionary met 2 keys:
    {
        "AMD": x,
        "NVIDIA": y,
    }
    Met x het aantal AMD videokaarten in de lijst en y het aantal NVIDIA
    videokaarten in de lijst.
    """

    teller_AMD = 0
    teller_NVIDIA = 0

    for videokaart in lijst_videokaarten:
        merk = videokaart["merk"]
        if merk == "NVIDIA":
            teller_NVIDIA += 1
        if merk == "AMD":
            teller_AMD += 1

    return  {
        "AMD": teller_AMD,
        "NVIDIA": teller_NVIDIA,
    }


def grootste_videokaart(lijst_videokaarten):

    """Gegeven een lijst met videokaarten, geef je een de naam terug
    van de grootste videokaart.

    Bijvoorbeeld:
    >>> grootste_videokaart([{'naam': 'RTX 3080', 'diesize': 628}])
    RTX 3080
    """

    naam_grootste = None
    grootste = 0
    for videokaart in lijst_videokaarten:
        diesize = videokaart["diesize"]
        if diesize > grootste:
            grootste = diesize
            naam_grootste = videokaart["naam"]

    return naam_grootste




def grootste_videokaartgrootte_per_merk(lijst_videokaarten):

    """Gegeven een lijst met videokaarten, geef je een dictionary terug met
    voor ieder merk de omvang van de grootste kaart.

    Bijvoorbeeld:
    >>> grootste_videokaartgrootte_per_merk([{'naam': 'RTX 3080', 'diesize': 628}])
    {'AMD': 0, 'NVIDIA': 628}
    """

    teller_AMD = 0
    teller_NVIDIA = 0


    for videokaart in lijst_videokaarten:
        merk = videokaart["merk"]
        diesize = videokaart["diesize"]
        if merk == "NVIDIA":
            if diesize > teller_NVIDIA:
                teller_NVIDIA = diesize

        if merk == "AMD":
            if diesize > teller_AMD:
                teller_AMD = diesize

    return {
        "AMD": teller_AMD,
        "NVIDIA": teller_NVIDIA,
    }



def diesizes_videokaarten(lijst_videokaarten):

    """Gegeven een lijst van dictionaries met informatie over vidoekaarten,
    geef je een lijst van diesizes terug.

    Bijvoorbeeld:
    >>> diesizes_videokaarten([{"diesize": 500}, {"diesize": 300}])
    [421, 320]
    """

    videokaarten = []

    for videokaart in lijst_videokaarten:
        diesize = videokaart["diesize"]
        videokaarten.append(diesize)

    return videokaarten







def gemiddelde_diesize_videokaarten(lijst_videokaarten):

    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je de gemiddelde diesize terug.

    Bijvoorbeeld:
    >>> diesizes_videokaarten([{"diesize": 500}, {"diesize": 300}])
    400
    """

    lijst = diesizes_videokaarten(lijst_videokaarten)

    return statistics.mean(lijst)





def jaren_videokaarten(lijst_videokaarten):

    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van jaartalen terug waarin de videokaarten uitgebracht werden.

    Bijvoorbeeld:
    >>> videokaarten_voor_jaar([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}], 2020)
    [2020, 2020]
    """

    jaartallen = []

    for videokaart in lijst_videokaarten:
        jaartal = videokaart["jaar"]
        jaartallen.append(jaartal)

    return jaartallen


def videokaarten_voor_jaar(lijst_videokaarten, jaar):

    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van dictionaries terug met informatie over videokaarten
    voor het opgegeven jaar.

    Bijvoorbeeld:
    >>> videokaarten_voor_jaar([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}], 2020)
    [{"jaar": 2020, "diesize": 500}]
    """

    gegevens = []

    for videokaart in lijst_videokaarten:
        jaartal = videokaart["jaar"]
        if jaar == jaartal:
            gegevens.append(videokaart)

    return gegevens
