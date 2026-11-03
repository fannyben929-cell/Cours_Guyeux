
import matplotlib.pyplot as plt
#chiffrement avec césar

def labo1(mess, cle):

    message_modifie = ""
    for letter in mess:

        if letter.isupper(): #si c'est en majuscule
            position = ord(letter) - ord("A") #position des lettres du message
            nouvelle_position = (position + cle) % 26 #position dans l'alphabet
            nouveau_caractere = chr(nouvelle_position + ord("A")) #remettre en caractère
            message_modifie += nouveau_caractere

        elif letter.islower(): #si c'est en minuscule
            position = ord(letter) - ord("a")
            nouvelle_position = (position + cle) % 26
            nouveau_caractere = chr(nouvelle_position + ord("a"))
            message_modifie += nouveau_caractere

        else:
            message_modifie += letter

    return message_modifie


def labo2(mess):
    resultats = []

    for cle in range(26):
        resultat = labo1(mess, -cle)
        resultats.append((cle, resultat))

    return resultats


# Analyse de fréquence du message
def labo3(mess):

    frequences = {}
    lettres = [lettre.lower() for lettre in mess
               if lettre.lower() in "abcdefghijklmnopqrstuvwxyz"]

    total = len(lettres)

    if total == 0:
        return frequences

    for lettre in lettres:
        frequences[lettre] = frequences.get(lettre, 0) + 1

    for lettre in frequences:
        frequences[lettre] = frequences[lettre] / total * 100

    return frequences


#labo 4
def labo4(resultats):

    frequences_francais = {
        'a': 7.6, 'b': 0.9, 'c': 3.3, 'd': 3.7,
        'e': 14.7, 'f': 1.1, 'g': 1.0, 'h': 0.7,
        'i': 7.5, 'j': 0.6, 'k': 0.1, 'l': 5.5,
        'm': 2.7, 'n': 7.1, 'o': 5.4, 'p': 3.0,
        'q': 1.4, 'r': 6.6, 's': 7.9, 't': 7.2,
        'u': 6.3, 'v': 1.8, 'w': 0.1, 'x': 0.4,
        'y': 0.3, 'z': 0.1
    }

    scores = []

    for cle, message in resultats:

        frequences = labo3(message)

        total = sum(
            1 for lettre in message.lower()
            if lettre in "abcdefghijklmnopqrstuvwxyz"
        )

        if total == 0:
            continue

        score = 0

        for lettre in frequences_francais:

            observe = frequences.get(lettre, 0)
            attendu = frequences_francais[lettre]

            score += ((observe - attendu) ** 2) / attendu

        scores.append((score, cle, message))

    scores.sort()

    return scores


def graphique_frequences(frequences):

    lettres = list(frequences.keys())
    valeurs = list(frequences.values())

    plt.bar(lettres, valeurs)

    plt.title("Fréquence des lettres")
    plt.xlabel("Lettres")
    plt.ylabel("Pourcentage (%)")

    plt.show()


#programme principal :


message = input("Entrez votre message chiffré : ")

resultats = labo2(message)

print("\n--- LABO 2 : LES 26 CLES ---")

for cle, texte in resultats:
    print("Clé", cle, ":", texte)


print("\n--- LABO 3 : FREQUENCES ---")

for cle, texte in resultats:
    print("\nClé :", cle)
    frequences = labo3(texte)

    for lettre, pourcentage in frequences.items():
        print(lettre, ":", round(pourcentage, 2), "%")


print("\n--- LABO 4 : CLASSEMENT ---")

classement = labo4(resultats)

for score, cle, texte in classement:
    print("Clé :", cle, "| Texte :", texte,
          "| Score :", round(score, 2))


if classement:
    score, cle, texte = classement[0]

    print("\n--- GRAPHIQUE DE LA MEILLEURE PROPOSITION ---")
    print("Clé :", cle)
    print("Message :", texte)

    frequences = labo3(texte)
    graphique_frequences(frequences)
