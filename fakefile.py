import random
from faker import Faker

fake = Faker('de_DE')

# Eigene Liste von Sachwörtern
produkte = [
    "Tisch", "Stuhl", "Lampe", "Fenster", "Buch", "Computer", "Telefon", "Auto", "Koffer", "Glas",
    "Drucker", "Monitor", "Tastatur", "Maus", "USB-Stick", "Externe Festplatte", "Netzteil", "Router",
    "Kopfhörer", "Lautsprecher", "Smartphone", "Tablet", "Notebook", "Scanner", "Kabel", "Schreibtisch",
    "Bürostuhl", "Regal", "Aktenschrank", "Ordner", "Druckerpatrone", "Toner", "Bleistifte", "Kugelschreiber",
    "Papier", "Kopierpapier", "Briefumschläge", "Versandkarton", "Whiteboard", "Flipchart", "Kalender",
    "Büroklammern", "Heftklammern", "Tacker", "Locher", "Klebeband", "Marker", "Schere", "Notizbuch",
    "Reinigungsmittel", "Desinfektionsmittel", "Toilettenpapier", "Seife", "Handtücher", "Müllbeutel",
    "USB-Kabel", "HDMI-Kabel", "Adapter", "Dockingstation", "Projektor", "Beamer", "Mikrofon", "Webcam",
    "Software-Lizenz", "Antivirus-Software", "Cloud-Speicher", "Hosting-Dienst", "Wartungsvertrag",
    "Beratungsdienstleistung", "Schulungsgebühr", "Transportkosten", "Versandkosten", "Liefergebühr",
    "Energiegebühr", "Wasseranschluss", "Stromverbrauch", "Gasverbrauch", "Netzwerkdienst", "Wartungskosten",
    "Maschinenwartung", "Büromaterial", "Reparaturkosten", "Bautätigkeit", "Werbung", "Marketingkosten",
    "Druckkosten", "Grafikdesign", "Webdesign", "IT-Support", "Telefonrechnung", "Internetgebühr",
    "Software-Entwicklung", "Fahrzeugmiete", "Hotelübernachtung", "Flugticket", "Bahnticket", "Mietwagen",
    "Benzinkosten", "Kilometergeld", "Catering", "Verpflegungskosten", "Veranstaltungskosten"
]
amt = [
    "Sachbearbeiter/in",
    "Teamleiter/in",
    "Abteilungsleiter/in",
    "Referent/in",
    "Amtsleiter/in",
    "Bürgermeister/in",
    "Landrat/Landrätin",
    "Ordnungsamtsleiter/in",
    "Finanzamtsleiter/in",
    "Sozialamtsleiter/in",
    "Standesbeamter/Standesbeamtin",
    "Mitarbeiter/in Bürgerbüro",
    "Verwaltungsfachangestellte/r",
    "Bezirksbürgermeister/in",
    "Leiter/in Personalabteilung",
    "Leiter/in Bauamt",
    "Polizeipräsident/in",
    "Leiter/in Gesundheitsamt",
    "Umweltbeauftragte/r",
    "Leiter/in Ausländerbehörde",
    "Vollzugsbeamter/in",
    "Schuldnerberater/in",
    "Leiter/in des Jugendamts",
    "Leiter/in Katasteramt",
    "Stadtplaner/in",
    "Leiter/in Straßenverkehrsamt",
    "Pressesprecher/in der Stadt",
    "Leiter/in Meldeamt",
    "Leiter/in Gewerbeaufsicht",
    "Leiter/in Denkmalpflege",
    "Leiter/in Feuerwehr",
    "Leiter/in Katastrophenschutz",
    "Leiter/in Sozialamt",
    "Leiter/in Liegenschaftsamt",
    "Leiter/in Bauaufsicht",
    "Kämmerer/Kämmerin",
    "Hauptamtsleiter/in",
    "Direktor/in der Stadtbibliothek",
    "Leiter/in der Stadtwerke",
    "Stadtförster/in",
    "Leiter/in Wasserwirtschaft",
    "Leiter/in Energieversorgung",
    "Leiter/in der Schulverwaltung",
    "Datenschutzbeauftragte/r",
    "Justitiar/in",
    "Leiter/in Bürgerbeteiligung",
    "Verkehrsplaner/in",
    "Leiter/in Statistikamt",
    "Veterinäramtsleiter/in",
    "Leiter/in des Integrationsamts"
]
antrag = [
    "Personalausweis",
    "Reisepass",
    "Meldebescheinigung",
    "Wohnsitzummeldung",
    "Führungszeugnis",
    "Gewerbeanmeldung",
    "Gewerbeabmeldung",
    "Gewerbeummeldung",
    "Bauantrag",
    "Baugenehmigung",
    "Elterngeld",
    "Kindergeld",
    "Kinderreisepass",
    "Neuausstellung Fahrzeugschein",
    "Fahrzeugzulassung",
    "Fahrzeugabmeldung",
    "Fahrzeugummeldung",
    "Wunschkennzeichen",
    "Ersatzführerschein",
    "Erweiterung der Fahrerlaubnis",
    "Behindertenparkausweis",
    "Arbeitslosengeld",
    "Sozialhilfe",
    "Wohngeld",
    "Heiratsurkunde",
    "Geburtsurkunde",
    "Sterbeurkunde",
    "Namensänderung",
    "Schulbescheinigung",
    "BAföG-Leistungen",
    "Elternzeit",
    "Grundsicherung",
    "Erbschein",
    "Aufenthaltserlaubnis",
    "Niederlassungserlaubnis",
    "Duldung",
    "Staatsangehörigkeitsnachweis",
    "Fischereischein",
    "Jagdschein",
    "Waffenschein",
    "Lohnsteuerermäßigung",
    "Umschreibung ausländischer Führerschein",
    "Lärmschutzgenehmigung",
    "Versammlungsanzeige",
    "Gaststättenkonzession",
    "Baulastenauskunft",
    "Denkmalschutzgenehmigung",
    "Schwerbehindertenausweis",
    "Asylantrag",
    "Rundfunkbeitragsbefreiung",
    "Eheschließung",
    "Scheidungsurkunde",
    "Testamentshinterlegung",
    "Adoptionsverfahren",
    "Haushaltshilfe",
    "Pflegegeld",
    "Betreuungsausweis",
    "BaföG-Rückzahlung",
    "Studienplatzbewerbung",
    "Sperrmüllentsorgung",
    "Baumfällgenehmigung",
    "Hundesteuerbefreiung",
    "Feuerwerkserlaubnis",
    "Gartenwasserzähler",
    "Winterdienstregelung",
    "Schulbefreiung",
    "Parkausweis für Anwohner",
    "Zweitausfertigung einer Urkunde",
    "Leistungen nach dem Bundesversorgungsgesetz",
    "Stundung von Forderungen",
    "Härtefallregelung",
    "Ermäßigung öffentlicher Gebühren",
    "Bürgergeld",
    "Freiwilliges Wehrdienstjahr"
]
behoerde = [
    "Bürgeramt",
    "Einwohnermeldeamt",
    "Ordnungsamt",
    "Gewerbeamt",
    "Finanzamt",
    "Standesamt",
    "Jugendamt",
    "Sozialamt",
    "Gesundheitsamt",
    "Jobcenter",
    "Agentur für Arbeit",
    "Rentenversicherung",
    "Krankenkasse",
    "Straßenverkehrsamt",
    "Kfz-Zulassungsstelle",
    "Führerscheinstelle",
    "Ausländerbehörde",
    "Staatsanwaltschaft",
    "Polizeidirektion",
    "Landeskriminalamt",
    "Bundeskriminalamt",
    "Feuerwehrleitstelle",
    "Katastrophenschutz",
    "Veterinäramt",
    "Umweltamt",
    "Wasserwirtschaftsamt",
    "Denkmalschutzbehörde",
    "Bauamt",
    "Gewerbeaufsichtsamt",
    "Wirtschaftsprüfungsamt",
    "Liegenschaftsamt",
    "Vermessungsamt",
    "Katasteramt",
    "Grundbuchamt",
    "Amtsgericht",
    "Landgericht",
    "Oberlandesgericht",
    "Finanzgericht",
    "Verfassungsgerichtshof",
    "Verbraucherschutzamt",
    "Statistisches Bundesamt",
    "Zollamt",
    "Schulamt",
    "Hochschulamt",
    "BaföG-Amt",
    "Veteranenamt",
    "Integrationsamt",
    "Bauaufsichtsamt",
    "Naturschutzbehörde",
    "Wirtschaftsförderungsamt",
    "Stadtplanungsamt",
    "Wasser- und Schifffahrtsamt",
    "Luftfahrtbundesamt",
    "Deutsche Rentenversicherung Bund",
    "Bundesagentur für Arbeit",
    "Bundesamt für Migration und Flüchtlinge",
    "Bundesamt für Verfassungsschutz",
    "Bundesnetzagentur",
    "Bundesamt für Bevölkerungsschutz und Katastrophenhilfe",
    "Bundeskartellamt",
    "Deutsches Patent- und Markenamt",
    "Auswärtiges Amt",
    "Bundesamt für Naturschutz",
    "Bundespolizeidirektion",
    "Verkehrsministerium",
    "Ministerium für Bildung und Forschung",
    "Ministerium für Gesundheit",
    "Ministerium für Wirtschaft",
    "Ministerium für Finanzen",
    "Ministerium für Umwelt",
    "Verwaltungsgericht",
    "Sozialgericht",
    "Arbeitsgericht",
    "Familienkasse",
    "Elterngeldstelle",
    "Kindergeldkasse",
    "Stadtwerke",
    "Energieversorgungsunternehmen",
    "Wasserversorger",
    "Müllabfuhrbehörde",
    "Abfallwirtschaftsbetrieb",
    "Rathaus",
    "Bürgermeisteramt",
    "Bezirkshauptmannschaft",
    "Gemeindeverwaltung"
]


def generate_data():
    daten = {}

    for j in range(1, 11):
        daten[f'name{j}'] = fake.name()
        daten[f'strasse{j}'] = fake.street_name()
        daten[f'hausnummer{j}'] = fake.building_number()
        daten[f'ort{j}'] = fake.city()
        daten[f'plz{j}'] = fake.postcode()
        daten[f'land{j}'] = fake.country()
        daten[f'email{j}'] = fake.free_email()
        daten[f'tel{j}'] = fake.phone_number()
        daten[f'kvnr{j}'] = fake.kvnr()
        daten[f'amt{j}'] = random.choice(amt)
        daten[f'behoerde{j}'] = random.choice(behoerde)
        daten[f'antrag{j}'] = random.choice(antrag)
        daten[f'firmenname{j}'] = fake.company()
        daten[f'job{j}'] = fake.job()
        daten[f'catchphrase{j}'] = fake.catch_phrase()
        daten[f'www{j}'] = fake.url()
        daten[f'rechnungsnummer{j}'] = f"r-{fake.random_number(digits=6)}"
        daten[f'rn{j}'] = f"r-{fake.random_number(digits=8)}"
        daten[f'id{j}'] = f"{fake.random_number(digits=8)}"
        daten[f'euro{j}'] = f"{random.uniform(0, 1000):.2f} €"
        daten[f'betrag{j}'] = f"{random.uniform(0, 10000):.2f}"
        daten[f'datum{j}'] = fake.date_this_year().strftime('%d.%m.%Y')
        daten[f'beschreibung{j}'] = fake.text(max_nb_chars=50)
        daten[f'wort{j}'] = fake.word()
        daten[f'text{j}'] = fake.text(max_nb_chars=100)
        daten[f'iban{j}'] = fake.iban()
        daten[f'swift{j}'] = fake.swift()
        daten[f'ding{j}'] = random.choice(produkte)
        daten[f'anzahl{j}'] = f"{random.randint(1, 100)}"

    return daten
