training_data = [
    (
        "Jeg kommer fra byen Struer.",
        {"entities": [(20, 26, "LOCATION")]},
    ),
    (
        "Jeg købte en gris for 50 kr. af Apple",
        {"entities": [(0, 3, "PERSON"), (22, 28, "LITERAL"), (32, 37, "ORG")]},
    ),
    (
        "For 25 kr. kan du købe meget.",
        {"entities": [(4, 10, "LITERAL"), (15, 17, "PERSON")]},
    ),
    (
        "Du kan købe meget for 1337 kr.",
        {"entities": [(0, 2, "PERSON"), (22, 30, "LITERAL")]},
    ),
    (
        "for 50 år siden var prisen på brød ihvertfald 10 kr. mindre",
        {
            "entities": [
                (0, 15, "LITERAL"),
                (46, 52, "LITERAL"),
            ]
        },
    ),
    (
        "Lars købte mælk den anden dag.",
        {
            "entities": [
                (0, 4, "PERSON"),
                (16, 29, "LITERAL"),
            ]
        },
    ),
    (
        "Jens købte gris den anden dag.",
        {
            "entities": [
                (0, 4, "PERSON"),
                (16, 29, "LITERAL"),
            ]
        },
    ),
    (
        "Simon købte vin sidste uge.",
        {
            "entities": [
                (0, 5, "PERSON"),
                (16, 26, "LITERAL"),
            ]
        },
    ),
    (
        "for 45 år siden var der ikke meget.",
        {"entities": [(0, 15, "LITERAL")]},
    ),
    (
        "jeg betalte 125,5 kr. for en legobil",
        {"entities": [(12, 21, "LITERAL")]},
    ),
    (
        "Vestjyllands borgmester er nice.",
        {"entities": [(0, 12, "LOCATION"), (13, 23, "PERSON")]},
    ),
    (
        "Nuvia blev tirsdag d. femte December opkøbt af Qualcomm",
        {"entities": [(0, 5, "ORG"), (11, 36, "LITERAL"), (47, 55, "ORG")]},
    ),
    (
        "Jeg flyttede fra Struer d. 11.06.2020",
        {"entities": [(17, 23, "LOCATION"), (24, 37, "LITERAL")]},
    ),
    (
        "Jeg flyttede fra Vestjylland d. 11.06.2020",
        {"entities": [(17, 28, "LOCATION"), (29, 42, "LITERAL")]},
    ),
    (
        "for fem dage siden var det mandag.",
        {"entities": [(0, 18, "LITERAL"), (27, 33, "LITERAL")]},
    ),
    (
        "for 5 dage siden var det mandag.",
        {"entities": [(0, 16, "LITERAL"), (25, 31, "LITERAL")]},
    ),
    (
        "for 3 uger siden var det d. 11/11/2023.",
        {"entities": [(0, 16, "LITERAL"), (25, 38, "LITERAL")]},
    ),
    (
        "Jeg spiste rugbrød, for 3 dage siden.",
        {"entities": [(20, 36, "LITERAL")]},
    ),
    (
        "Jeffrey Epstein er en person.",
        {"entities": [(0, 15, "PERSON")]},
    ),
    (
        "Epstein gjorde det ikke.",
        {"entities": [(0, 7, "PERSON")]},
    ),
    (
        "Peter så Epstein gøre det.",
        {"entities": [(0, 5, "PERSON"), (9, 16, "PERSON")]},
    ),
    (
        "Ingen har set Epstein gøre det.",
        {"entities": [(14, 21, "PERSON")]},
    ),
    (
        "Man ved endnu ikke hvem der er skyld i 9/11.",
        {"entities": [(39, 43, "LITERAL")]},
    ),
    (
        "Jeg flyttede til Aalborg d. 29/07/2018.",
        {"entities": [(17, 24, "LOCATION"), (25, 38, "LITERAL")]},
    ),
    (
        "I dag er det mandag.",
        {"entities": [(0, 5, "LITERAL"), (13, 19, "LITERAL")]},
    ),
    (
        "Mette Frederiksen og hendes børn, er blevet væk.",
        {"entities": [(0, 17, "PERSON"), (21, 32, "PERSON")]},
    ),
    (
        "Efter John Koefoed, var der ikke flere.",
        {"entities": [(6, 18, "PERSON")]},
    ),
    (
        "Jørgen Kofoed og hans børn, er blevet myrdet.",
        {"entities": [(0, 13, "PERSON"), (17, 26, "PERSON")]},
    ),
    (
        "Det er pga. Peter, at dette virker.",
        {"entities": [(12, 17, "PERSON")]},
    ),
    (
        "Sammen med Peter, har Nichlas, hjulpet til.",
        {"entities": [(11, 16, "PERSON"), (22, 29, "PERSON")]},
    ),
    (
        "Jørgen Koefoed er en politiker i Danmark.",
        {"entities": [(0, 14, "PERSON")]},
    ),
    (
        "iPhone blev udgivet i 2007 af Apple.",
        {"entities": [(20, 26, "LITERAL"), (30, 35, "ORG")]},
    ),
    (
        "iPhone 10 blev udgivet i 2017 af Apple.",
        {"entities": [(0, 9, "MISC"), (23, 29, "LITERAL"), (33, 38, "ORG")]},
    ),
    (
        "iPhone SE blev udgivet i 2016 af Apple.",
        {"entities": [(0, 9, "MISC"), (23, 29, "LITERAL"), (33, 38, "ORG")]},
    ),
    (
        "Microsoft Windows blev udgivet i 1985 af Microsoft.",
        {"entities": [(0, 17, "MISC"), (31, 37, "LITERAL"), (41, 50, "ORG")]},
    ),
    (
        "Apple er et firma.",
        {"entities": [(0, 5, "ORG")]},
    ),
    (
        "Microsoft er også et firma.",
        {"entities": [(0, 9, "ORG")]},
    ),
    (
        "Microsoft er et firma, men det er Microsoft Windows ikke.",
        {"entities": [(0, 9, "ORG"), (34, 51, "ORG")]},
    ),
    (
        "I 1943 var Hitler diktator.",
        {"entities": [(0, 6, "LITERAL")]},
    ),
    (
        "COVID 19 startede i 2019.",
        {"entities": [(18, 24, "LITERAL")]},
    ),
    (
        "Jeg skulle i skole i dag.",
        {"entities": [(19, 24, "LITERAL")]},
    ),
    (
        "I morgen holder vi lukket i butikken.",
        {"entities": [(0, 8, "LITERAL")]},
    ),
    (
        "I anledningen af i fredags, spiser vi kage.",
        {"entities": [(17, 26, "LITERAL")]},
    ),
    (
        "Første verdenskrig foregik i 1914-1918.",
        {"entities": [(27, 38, "LITERAL")]},
    ),
    (
        "Mødet er planlagt til den 5. december 2023.",
        {"entities": [(22, 42, "LITERAL")]},
    ),
    (
        "Bussen ankom kl. 14:30 præcis.",
        {"entities": [(13, 22, "LITERAL")]},
    ),
    (
        "Prisen for varen er 500 kr.",
        {"entities": [(20, 27, "LITERAL")]},
    ),
    (
        "Festen starter kl. 20:00 på lørdag.",
        {"entities": [(15, 34, "LITERAL")]},
    ),
    (
        "Købmanden åbner kl. 7:00 om morgenen.",
        {"entities": [(16, 36, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes inden den 1. juni 2024.",
        {"entities": [(31, 47, "LITERAL")]},
    ),
    (
        "Vi forventer levering d. 10/02/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Billetterne koster 150 DKK hver.",
        {"entities": [(19, 26, "LITERAL")]},
    ),
    (
        "Deadline for rapporten er d. 15-03-2023.",
        {"entities": [(26, 39, "LITERAL")]},
    ),
    (
        "Træningen begynder kl. 18:45 i fitnesscentret.",
        {"entities": [(19, 28, "LITERAL")]},
    ),
    (
        "Bogen koster 89,95 kr. i butikken.",
        {"entities": [(13, 22, "LITERAL")]},
    ),
    (
        "Værten annoncerede vinderen kl. 21:15.",
        {"entities": [(28, 37, "LITERAL")]},
    ),
    (
        "Mødet starter præcist kl. 09:30.",
        {"entities": [(22, 31, "LITERAL")]},
    ),
    (
        "Vi skal aflevere rapporten inden d. 8. maj 2024.",
        {"entities": [(33, 47, "LITERAL")]},
    ),
    (
        "Temperaturen steg til 27 grader celsius.",
        {"entities": [(22, 39, "LITERAL")]},
    ),
    (
        "Koncerten begynder kl. 19:00 på fredag.",
        {"entities": [(19, 38, "LITERAL")]},
    ),
    (
        "Den samlede pris er 2000 DKK.",
        {"entities": [(20, 28, "LITERAL")]},
    ),
    (
        "Vi forventer solskin kl. 12:00 i morgen.",
        {"entities": [(21, 39, "LITERAL")]},
    ),
    (
        "Hun betalte 350 kr. for den nye telefon.",
        {"entities": [(12, 19, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes senest d. 1/6/2024.",
        {"entities": [(25, 43, "LITERAL")]},
    ),
    (
        "Mødet er planlagt til d. 5/12/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Bussen ankom kl. 15:00 præcis.",
        {"entities": [(13, 22, "LITERAL")]},
    ),
    (
        "Prisen for varen er 299 kr.",
        {"entities": [(20, 27, "LITERAL")]},
    ),
    (
        "Festen starter kl. 21:30 på lørdag.",
        {"entities": [(15, 34, "LITERAL")]},
    ),
    (
        "Købmanden åbner kl. 6:30 om morgenen.",
        {"entities": [(16, 36, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes inden d. 2. juni 2024.",
        {"entities": [(25, 46, "LITERAL")]},
    ),
    (
        "Vi forventer levering d. 15/02/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Billetterne koster 200 DKK hver.",
        {"entities": [(19, 26, "LITERAL")]},
    ),
    (
        "Deadline for rapporten er d. 20-03-2023.",
        {"entities": [(26, 39, "LITERAL")]},
    ),
    (
        "Træningen begynder kl. 19:00 i fitnesscentret.",
        {"entities": [(19, 28, "LITERAL")]},
    ),
    (
        "Bogen koster 99,95 kr. i butikken.",
        {"entities": [(13, 22, "LITERAL")]},
    ),
    (
        "Værten annoncerede vinderen kl. 22:00.",
        {"entities": [(28, 37, "LITERAL")]},
    ),
    (
        "Mødet starter præcist kl. 10:00.",
        {"entities": [(22, 31, "LITERAL")]},
    ),
    (
        "Vi skal aflevere rapporten inden d. 10. maj 2024.",
        {"entities": [(27, 48, "LITERAL")]},
    ),
    (
        "Temperaturen steg til 30 grader celsius.",
        {"entities": [(22, 39, "LITERAL")]},
    ),
    (
        "Koncerten begynder kl. 20:00 på fredag.",
        {"entities": [(19, 38, "LITERAL")]},
    ),
    (
        "Den samlede pris er 2500 DKK.",
        {"entities": [(20, 28, "LITERAL")]},
    ),
    (
        "Vi forventer solskin kl. 13:00 i morgen.",
        {"entities": [(21, 39, "LITERAL")]},
    ),
    (
        "Hun betalte 400 kr. for den nye telefon.",
        {"entities": [(12, 19, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes senest d. 3/6/2024.",
        {"entities": [(25, 43, "LITERAL")]},
    ),
    (
        "Mødet er planlagt til d. 10/12/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Bussen ankom kl. 15:30 præcis.",
        {"entities": [(13, 22, "LITERAL")]},
    ),
    (
        "Prisen for varen er 399 kr.",
        {"entities": [(20, 27, "LITERAL")]},
    ),
    (
        "Festen starter kl. 22:00 på lørdag.",
        {"entities": [(15, 34, "LITERAL")]},
    ),
    (
        "Købmanden åbner kl. 6:00 om morgenen.",
        {"entities": [(16, 36, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes inden d. 3. juni 2024.",
        {"entities": [(25, 46, "LITERAL")]},
    ),
    (
        "Vi forventer levering d. 20/02/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Billetterne koster 300 DKK hver.",
        {"entities": [(19, 26, "LITERAL")]},
    ),
    (
        "Deadline for rapporten er d. 25-03-2023.",
        {"entities": [(23, 39, "LITERAL")]},
    ),
    (
        "Træningen begynder kl. 20:00 i fitnesscentret.",
        {"entities": [(19, 28, "LITERAL")]},
    ),
    (
        "Bogen koster 109,95 kr. i butikken.",
        {"entities": [(13, 23, "LITERAL")]},
    ),
    (
        "Værten annoncerede vinderen kl. 23:00.",
        {"entities": [(28, 37, "LITERAL")]},
    ),
    (
        "Mødet starter præcist kl. 11:00.",
        {"entities": [(22, 31, "LITERAL")]},
    ),
    (
        "Vi skal aflevere rapporten inden d. 15. maj 2024.",
        {"entities": [(33, 48, "LITERAL")]},
    ),
    (
        "Temperaturen steg til 35 grader celsius.",
        {"entities": [(22, 39, "LITERAL")]},
    ),
    (
        "Koncerten begynder kl. 21:00 på fredag.",
        {"entities": [(19, 38, "LITERAL")]},
    ),
    (
        "Den samlede pris er 3000 DKK.",
        {"entities": [(20, 28, "LITERAL")]},
    ),
    (
        "Vi forventer solskin kl. 14:00 i morgen.",
        {"entities": [(21, 39, "LITERAL")]},
    ),
    (
        "Hun betalte 450 kr. for den nye telefon.",
        {"entities": [(12, 19, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes senest d. 5/6/2024.",
        {"entities": [(32, 43, "LITERAL")]},
    ),
    (
        "Mødet er planlagt til d. 15/12/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Bussen ankom kl. 16:00 præcis.",
        {"entities": [(13, 22, "LITERAL")]},
    ),
    (
        "Prisen for varen er 499 kr.",
        {"entities": [(20, 27, "LITERAL")]},
    ),
    (
        "Festen starter kl. 23:30 på lørdag.",
        {"entities": [(19, 34, "LITERAL")]},
    ),
    (
        "Købmanden åbner kl. 5:30 om morgenen.",
        {"entities": [(16, 36, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes inden d. 4. juni 2024.",
        {"entities": [(25, 46, "LITERAL")]},
    ),
    (
        "Vi forventer levering d. 25/02/2023.",
        {"entities": [(22, 35, "LITERAL")]},
    ),
    (
        "Billetterne koster 400 DKK hver.",
        {"entities": [(19, 26, "LITERAL")]},
    ),
    (
        "Deadline for rapporten er d. 30-03-2023.",
        {"entities": [(26, 39, "LITERAL")]},
    ),
    (
        "Træningen begynder kl. 21:00 i fitnesscentret.",
        {"entities": [(19, 28, "LITERAL")]},
    ),
    (
        "Bogen koster 119,95 kr. i butikken.",
        {"entities": [(13, 23, "LITERAL")]},
    ),
    (
        "Værten annoncerede vinderen kl. 00:00.",
        {"entities": [(28, 37, "LITERAL")]},
    ),
    (
        "Mødet starter præcist kl. 12:00.",
        {"entities": [(22, 31, "LITERAL")]},
    ),
    (
        "Vi skal aflevere rapporten inden d. 20. maj 2024.",
        {"entities": [(33, 48, "LITERAL")]},
    ),
    (
        "Temperaturen steg til 40 grader celsius.",
        {"entities": [(22, 39, "LITERAL")]},
    ),
    (
        "Koncerten begynder kl. 22:00 på fredag.",
        {"entities": [(19, 38, "LITERAL")]},
    ),
    (
        "Den samlede pris er 3500 DKK.",
        {"entities": [(20, 28, "LITERAL")]},
    ),
    (
        "Vi forventer solskin kl. 15:00 i morgen.",
        {"entities": [(21, 39, "LITERAL")]},
    ),
    (
        "Hun betalte 500 kr. for den nye telefon.",
        {"entities": [(12, 19, "LITERAL")]},
    ),
    (
        "Projektet skal afsluttes senest d. 6/6/2024.",
        {"entities": [(32, 43, "LITERAL")]},
    ),
    (
        "Mødet er planlagt til d. 20/12.",
        {"entities": [(22, 30, "LITERAL")]},
    ),
    (
        "I dag er det mandag 11/01",
        {"entities": [(0, 5, "LITERAL"), (20, 25, "LITERAL")]},
    ),
    (
        "Bussen kommer 15:00",
        {"entities": [(14, 19, "LITERAL")]},
    ),
    (
        "11:20 er det frokost",
        {"entities": [(0, 5, "LITERAL")]},
    ),
    (
        "Jeg skal d. 2/9 til fødselsdag",
        {"entities": [(9, 16, "LITERAL")]},
    ),
    (
        "Jeg skal d. 3/4/2023 til fødselsdag",
        {"entities": [(9, 21, "LITERAL")]},
    ),
    (
        "Jeg skal d. 7/11/23 til fødselsdag",
        {"entities": [(9, 19, "LITERAL")]},
    ),
    (
        "Jeg har en aftale d. 7/11/2023",
        {"entities": [(18, 30, "LITERAL")]},
    ),
    (
        "Næste år er det d. 29/11/2024",
        {"entities": [(16, 29, "LITERAL")]},
    ),
    (
        "1/3/2024 skal jeg til bryllup",
        {"entities": [(0, 8, "LITERAL")]},
    ),
    (
        "Jeg skal til bryllup d. 1/3/2024",
        {"entities": [(21, 32, "LITERAL")]},
    ),
    (
        "Vi har 5 æbler i kurven", 
        {"entities": [(7, 8, "LITERAL")]}
    ),
    ("Prisen er 399 kr.", {"entities": [(10, 17, "LITERAL")]}),
    ("Mødet starter kl. 14:30", {"entities": [(14, 23, "LITERAL")]}),
    ("Hun købte billetterne den 5/10/2023", {"entities": [(22, 35, "LITERAL")]}),
    ("Temperaturen er 25 grader", {"entities": [(16, 25, "LITERAL")]}),
    ("Bogen koster 49.99 kr.", {"entities": [(13, 22, "LITERAL")]}),
    ("Der er 3 hunde i haven", {"entities": [(7, 8, "LITERAL")]}),
    ("Der er 7 dage i en uge", {"entities": [(7, 13, "LITERAL")]}),
    ("Temperaturen faldt til -10 grader", {"entities": [(23, 33, "LITERAL")]}),
    ("Hun løb 10 kilometer på en time", {"entities": [(8, 20, "LITERAL")]}),
    ("Prisen på huset er 1.5 millioner kroner", {"entities": [(19, 39, "LITERAL")]}),
    ("Han scorede 3 mål i kampen", {"entities": [(12, 13, "LITERAL")]}),
    ("Antallet af studerende er 250", {"entities": [(26, 29, "LITERAL")]}),
    ("Jeg har reserveret bord til 4 personer", {"entities": [(28, 29, "LITERAL")]}),
    ("Hun blev født den 12. maj 1990", {"entities": [(14, 16, "LITERAL")]}),
    ("Hastighedsgrænsen er 100 km/t", {"entities": [(21, 29, "LITERAL")]}),
    ("Bogen indeholder 500 sider", {"entities": [(17, 20, "LITERAL")]}),
    ("Prisen steg med 15%", {"entities": [(16, 19, "LITERAL")]}),
    ("25 personer deltog i arrangementet", {"entities": [(0, 2, "LITERAL")]}),
    ("3.14 er værdien af pi", {"entities": [(0, 4, "LITERAL")]}),
    ("100 kroner er prisen for billetten", {"entities": [(0, 10, "LITERAL")]}),
    ("2022 er året for det næste store event", {"entities": [(0, 4, "LITERAL")]}),
    ("10 grader er den aktuelle temperatur", {"entities": [(0, 9, "LITERAL")]}),
    ("5 kilometer er distancen til målet", {"entities": [(0, 11, "LITERAL")]}),
    ("7 dage er varigheden af ferien", {"entities": [(0, 6, "LITERAL")]}),
    ("49.99 kr. er prisen for produktet", {"entities": [(0, 9, "LITERAL")]}),
    ("12 point blev scoret i kampen", {"entities": [(0, 2, "LITERAL")]}),
    ("-15 grader er den laveste temperatur", {"entities": [(0, 10, "LITERAL")]}),
]
