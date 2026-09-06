from studieadviestext import *

def vraag_weken_studeren():
    print(AANTAL_WEKEN_VRAAG)
    weken_studeren = int(input("Hoeveel weken ben je al bezig met de opleiding? "))
    return weken_studeren

def vraag_stellingen(weken_studeren):
    antwoorden = []
    stellingen = [
        {"text": COMPETENTIE_STELLING_1, "options": [0, 1, 2, 3, 4]},
        {"text": COMPETENTIE_STELLING_2, "options": [0, 1, 2, 3, 4]},
        {"text": COMPETENTIE_STELLING_3, "options": [0, 1, 2, 3, 4]},
        {"text": COMPETENTIE_STELLING_4, "options": [0, 1, 2, 3, 4]},
        {"text": COMPETENTIE_STELLING_5, "options": [0, 1, 2, 3, 4]},
    ]
    if weken_studeren >= 10:
        stellingen.append({"text": COMPETENTIE_STELLING_6, "options": [0, 1, 2, 3, 4]})
        stellingen.append({"text": COMPETENTIE_STELLING_7, "options": [0, 1, 2, 3, 4]})
    for stelling in stellingen:
        print(stelling["text"])
        print(OPTIES)
        antwoord = int(input("Kies een optie: "))
        antwoorden.append(antwoord)
    return antwoorden

def bereken_score(antwoorden):
    score = sum(antwoorden)
    gemiddelde_score = score / len(antwoorden)
    return gemiddelde_score

def bereken_advies(gemiddelde_score, antwoorden):
    altijd_count = antwoorden.count(0)
    vaak_count = antwoorden.count(1)
    regelmatig_count = antwoorden.count(2)
    if gemiddelde_score <= 2 or (altijd_count + vaak_count) / len(antwoorden) > 0.5:
        return COMPETENTIE_ADVIES_ZORGELIJK
    elif gemiddelde_score <= 3 or (altijd_count + vaak_count + regelmatig_count) / len(antwoorden) > 0.5:
        return COMPETENTIE_ADVIES_TWIJFELACHTIG
    else:
        return COMPETENTIE_ADVIES_GERUSTSTELLEND


def main():
    print(STUDIEDOKTER_TITEL)
    weken_studeren = vraag_weken_studeren()
    antwoorden = vraag_stellingen(weken_studeren)
    gemiddelde_score = bereken_score(antwoorden)
    advies = bereken_advies(gemiddelde_score, antwoorden)
    print(COMPETENTIE_ADVIES_TITEL)
    print(advies)

if __name__ == "__main__":
    main()