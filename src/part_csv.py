# Haal de dataset met naam "Confirmed cases by date, age, sex and province"
# in CSV-formaat af van de Sciensano-website:
# https://epistat.wiv-isp.be/covid/
#
# Dit bestand heeft naam "COVID19BE_CASES_AGESEX.csv".

import csv

def determine_total_cases(age_category, gender):

    """Geeft het totaal aantal COVID19 gevallen terug voor de gegeven leeftijdscategorie en het gegeven geslacht
    B.v.
    determine_total_cases("20-29", "M") geeft het aantal besmettingen van mannen tussen de 20 en 29 jaar oud
    terug. 
    """


    f = open("COVID19BE_CASES_AGESEX.csv", "r")
    totaal = 0
    reader = csv.reader(f)

    for row in reader:
        g = row[-2]

        if g == "SEX":
            continue

        a = row[-3]
        c = int(row[-1])

        if g == gender and a == age_category:
            totaal = totaal + c

    return totaal

v = determine_total_cases("40-49", "M")
print(v)


def output_total_cases(input_filename, output_filename):

    """Schrijf een functie die het invoerbestand inleest
    en per leeftijdscategorie het totaal aantal besmettingen toont.
    Dus, volgende aanroep:
    create_total_cases("COVID19BE_CASES_AGESEX.csv", "overzicht.csv") 
    Maakt een bestand "overzicht.csv" met hierin:
    "0-9", 19999
    "10-19", 10020
    "29-39", 31231
    ...
    "90+", 123123
    """

    return 0

