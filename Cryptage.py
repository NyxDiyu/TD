import string

def Cryptage(message):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    message_crypté = ""

    for lettre in message:
        if lettre in caracteres:
            index = caracteres.index(lettre)
            lettre_cryptée = caracteres[(index + 1) % len(caracteres)]
            message_crypté += lettre_cryptée
        else:
            message_crypté += lettre

    return message_crypté

# Exemple d'utilisation :
message = "Fizz est sur lol"
message_crypté = Cryptage(message)
print(message_crypté)
