# Proiect: Pagina web cu cursele de Formula 1
# Program simplu in Python, fara Flask.
# Acest program creeaza automat o pagina web numita index.html.

curse = [
    {
        "nr": 1,
        "nume": "Marele Premiu al Bahrainului",
        "tara": "Bahrain",
        "circuit": "Bahrain International Circuit",
        "data": "2 martie 2024"
    },
    {
        "nr": 2,
        "nume": "Marele Premiu al Arabiei Saudite",
        "tara": "Arabia Saudita",
        "circuit": "Jeddah Corniche Circuit",
        "data": "9 martie 2024"
    },
    {
        "nr": 3,
        "nume": "Marele Premiu al Australiei",
        "tara": "Australia",
        "circuit": "Albert Park Circuit",
        "data": "24 martie 2024"
    },
    {
        "nr": 4,
        "nume": "Marele Premiu al Japoniei",
        "tara": "Japonia",
        "circuit": "Suzuka Circuit",
        "data": "7 aprilie 2024"
    },
    {
        "nr": 5,
        "nume": "Marele Premiu al Chinei",
        "tara": "China",
        "circuit": "Shanghai International Circuit",
        "data": "21 aprilie 2024"
    },
    {
        "nr": 6,
        "nume": "Marele Premiu de la Miami",
        "tara": "SUA",
        "circuit": "Miami International Autodrome",
        "data": "5 mai 2024"
    },
    {
        "nr": 7,
        "nume": "Marele Premiu al Emiliei-Romagna",
        "tara": "Italia",
        "circuit": "Imola",
        "data": "19 mai 2024"
    },
    {
        "nr": 8,
        "nume": "Marele Premiu al Principatului Monaco",
        "tara": "Monaco",
        "circuit": "Circuit de Monaco",
        "data": "26 mai 2024"
    },
    {
        "nr": 9,
        "nume": "Marele Premiu al Canadei",
        "tara": "Canada",
        "circuit": "Circuit Gilles Villeneuve",
        "data": "9 iunie 2024"
    },
    {
        "nr": 10,
        "nume": "Marele Premiu al Spaniei",
        "tara": "Spania",
        "circuit": "Circuit de Barcelona-Catalunya",
        "data": "23 iunie 2024"
    },
    {
        "nr": 11,
        "nume": "Marele Premiu al Austriei",
        "tara": "Austria",
        "circuit": "Red Bull Ring",
        "data": "30 iunie 2024"
    },
    {
        "nr": 12,
        "nume": "Marele Premiu al Marii Britanii",
        "tara": "Marea Britanie",
        "circuit": "Silverstone Circuit",
        "data": "7 iulie 2024"
    },
    {
        "nr": 13,
        "nume": "Marele Premiu al Ungariei",
        "tara": "Ungaria",
        "circuit": "Hungaroring",
        "data": "21 iulie 2024"
    },
    {
        "nr": 14,
        "nume": "Marele Premiu al Belgiei",
        "tara": "Belgia",
        "circuit": "Spa-Francorchamps",
        "data": "28 iulie 2024"
    },
    {
        "nr": 15,
        "nume": "Marele Premiu al Tarilor de Jos",
        "tara": "Tarile de Jos",
        "circuit": "Zandvoort",
        "data": "25 august 2024"
    },
    {
        "nr": 16,
        "nume": "Marele Premiu al Italiei",
        "tara": "Italia",
        "circuit": "Monza",
        "data": "1 septembrie 2024"
    },
    {
        "nr": 17,
        "nume": "Marele Premiu al Azerbaidjanului",
        "tara": "Azerbaidjan",
        "circuit": "Baku City Circuit",
        "data": "15 septembrie 2024"
    },
    {
        "nr": 18,
        "nume": "Marele Premiu al statului Singapore",
        "tara": "Singapore",
        "circuit": "Marina Bay Street Circuit",
        "data": "22 septembrie 2024"
    },
    {
        "nr": 19,
        "nume": "Marele Premiu al Statelor Unite",
        "tara": "SUA",
        "circuit": "Circuit of the Americas",
        "data": "20 octombrie 2024"
    },
    {
        "nr": 20,
        "nume": "Marele Premiu al Mexicului",
        "tara": "Mexic",
        "circuit": "Autodromo Hermanos Rodriguez",
        "data": "27 octombrie 2024"
    },
    {
        "nr": 21,
        "nume": "Marele Premiu al Braziliei",
        "tara": "Brazilia",
        "circuit": "Interlagos",
        "data": "3 noiembrie 2024"
    },
    {
        "nr": 22,
        "nume": "Marele Premiu al Las Vegasului",
        "tara": "SUA",
        "circuit": "Las Vegas Strip Circuit",
        "data": "23 noiembrie 2024"
    },
    {
        "nr": 23,
        "nume": "Marele Premiu al Qatarului",
        "tara": "Qatar",
        "circuit": "Lusail International Circuit",
        "data": "1 decembrie 2024"
    },
    {
        "nr": 24,
        "nume": "Marele Premiu din Abu Dhabi",
        "tara": "Emiratele Arabe Unite",
        "circuit": "Yas Marina Circuit",
        "data": "8 decembrie 2024"
    }
]


def creeaza_carduri():
    carduri = ""

    for cursa in curse:
        carduri += f"""
        <div class="card">
            <h3>{cursa["nr"]}. {cursa["nume"]}</h3>
            <p><b>Tara:</b> {cursa["tara"]}</p>
            <p><b>Circuit:</b> {cursa["circuit"]}</p>
            <p><b>Data:</b> {cursa["data"]}</p>
        </div>
        """

    return carduri


def creeaza_pagina():
    continut_html = f"""<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>Curse Formula 1 2024</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <h1>Curse Formula 1 - Sezonul 2024</h1>
        <p>Proiect realizat in Python, fara Flask</p>
    </header>

    <nav>
        <a href="#acasa">Acasa</a>
        <a href="#curse">Curse</a>
        <a href="#despre">Despre</a>
    </nav>

    <section id="acasa" class="intro">
        <h2>Bine ai venit!</h2>
        <p>
            Aceasta pagina prezinta cursele de Formula 1 din sezonul 2024.
            Pagina a fost generata automat cu ajutorul limbajului Python.
        </p>
    </section>

    <section id="curse">
        <h2>Lista curselor</h2>

        <div class="container-carduri">
            {creeaza_carduri()}
        </div>
    </section>

    <section id="despre" class="despre">
        <h2>Despre proiect</h2>
        <p>
            Proiectul este realizat pentru incepatori. Programul Python creeaza
            o pagina HTML, iar designul este facut cu CSS.
        </p>
    </section>

    <footer>
        <p>Proiect Python - Formula 1</p>
    </footer>

</body>
</html>
"""

    fisier = open("index.html", "w", encoding="utf-8")
    fisier.write(continut_html)
    fisier.close()

    print("Pagina index.html a fost creata cu succes!")
    print("Deschide fisierul index.html in browser.")


creeaza_pagina()
