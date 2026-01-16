import time
import sys

# ===== KLEUREN =====
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def typewriter(text, delay=0.05, color=GREEN):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

# ===== START WACHTWOORD (ONBEPERKT) =====
while True:
    typewriter("wachtwoord:", 0.07)
    wachtwoord = input("> ")

    if wachtwoord == "1908":
        typewriter("Het wachtwoord is correct!\n")
        break
    else:
        typewriter("Onjuist wachtwoord.\n", color=RED)

# ===== VRAGEN =====
vragen = [
    {
        "vraag": "Vraag 1: Hoeveel meer radioactieve straling was er bij de superwolven dan wat volgens de menselijke veiligheidslimiet mag?",
        "antwoorden": ["6 keer", "6x", "zes keer"],
        "hint": "Het is een enkel cijfer, en best een klein getal."
    },
    {
        "vraag": "Vraag 2: Hoeveel ton woog de deksel die werd weggeblazen door de stoomexplosie?",
        "antwoorden": ["1000 ton", "1000ton", "duizend ton"],
        "hint": "Het is in tonnen uitgedrukt, niet in kilo’s."
    },
    {
        "vraag": "Vraag 3: Welke naburige stad werd ook getroffen door de explosie van Tsjernobyl?",
        "antwoorden": ["pripjat", "pripyat"],
        "hint": "De stad ligt op korte afstand van de kerncentrale."
    },
    {
        "vraag": "Vraag 4: Hoe groot was de vervreemdingszone rond de kerncentrale?",
        "antwoorden": ["30 km", "30km", "dertig km"],
        "hint": "Het aantal is kleiner dan 50, een mooi rond getal."
    }
]

def vraag_stel(vraag, antwoorden, hint):
    fouten = 0
    typewriter("\n" + vraag)

    antwoorden = [a.lower() for a in antwoorden]

    while True:
        respons = input("antwoord: ").strip().lower()

        if respons in antwoorden:
            typewriter("Correct! ✅")
            return
        else:
            fouten += 1
            typewriter("Fout antwoord.", color=RED)

            if fouten == 3:
                typewriter(f"Hint: {hint}")

def main():
    for v in vragen:
        vraag_stel(v["vraag"], v["antwoorden"], v["hint"])

    typewriter("\nAlle vragen beantwoord!")
    typewriter("Voer het eindwachtwoord in:")

    while True:
        laatste = input("> ")
        if laatste == "9128":
            typewriter("Eindwachtwoord correct! Je hebt het gehaald!", 0.06)
            break
        else:
            typewriter("Fout eindwachtwoord. Probeer opnieuw.", color=RED)

main()
