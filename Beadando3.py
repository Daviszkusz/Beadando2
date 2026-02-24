import datetime
import json
import os

DATA_FILE = "ebredesi_naplo_nevekkel.json"


def betolt_vagy_letrehoz():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return [
            ["Hétfő"],
            ["Kedd"],
            ["Szerda"],
            ["Csütörtök"],
            ["Péntek"],
            ["Szombat"],
            ["Vasárnap"]
        ]


def naplozas():
    naplo = betolt_vagy_letrehoz()

    most = datetime.datetime.now()

    nap_index = most.weekday()

    idopont = f"{most.hour:02d}:{most.minute:02d}"

    naplo[nap_index].append(idopont)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(naplo, f, ensure_ascii=False, indent=4)

    nap_neve = naplo[nap_index][0]
    print(f"Sikeresen naplózva: {nap_neve}, {idopont}")

    megjelenit_statisztika(naplo)


def megjelenit_statisztika(naplo):
    print("\n--- Ébredési Napló (7 nap) ---")
    for bejegyzesek in naplo:
        nap_neve = bejegyzesek[0]

        if len(bejegyzesek) > 1:
            idopontok = ", ".join(bejegyzesek[1:])
        else:
            idopontok = "Még nem léptél be"

        print(f"{nap_neve}: {idopontok}")


if __name__ == "__main__":
    naplozas()