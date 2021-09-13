# We gaan nu een adresboek opstellen met behulp van
# een list van dictionaries.


def addressbook_search(addressbook, search_name):

    """Return het adres van de gevraagde persoon
    Als de persoon niet in het adresboek staat, geef dan None terug.
    addressbook: een list van lists met hierin naam, adres paren
    search_name: de naam van de te zoeken persoon
    """

    for i in addressbook:
        if i["name"] == search_name:
            result = i["address"]
            return result

    return None


def addressbook_add(addressbook, name, address):

    """Voeg het 'adres' voor 'name' aan de lijst toe.
    Als voor deze persoon al een adres in het adresboek zit,
    voeg het dan niet toe, maar toon "persoon reeds in adresboek"
    op het scherm.
    """

    resultaat = addressbook_search(addressbook, name)
    if resultaat == address:
        print(f"persoon reeds in adresboek")
        return

    boek = {"name": name, "address": address}
    addressbook.append(boek)
    return address
