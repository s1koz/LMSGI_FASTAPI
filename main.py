### Imports ##################################################
import json
import os  # per neteja la pantalla

# Variables ###################################################

# Nom del fitxer on desar/carregar dades
dicAlumnes = "alumnes.json"


### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla.

alumnat = []

#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    # Netejem la pantalla
    os.system('cls')

    # Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")

    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    # i retornem l'opció escollida per l'usuari
    return input()


### Programa ################################################

# Fins a l'infinit (i més enllà)
while True:

    # Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")

            # Introduiu el vostre codi per mostrar alumnes aquí


            print("[",Alumne1["id"],"]",Alumne1["nom"],Alumne["cognom"])

            input()

        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")

            # Introduiu el vostre codi per afegir un alumne aquí
            id_alumno = len(alumnat) + 1
            nom = input("Nom: ")
            cognom = input("Cognom: ")
            dia = int(input("Dia de la data: "))
            mes = int(input("Mes de la data: "))
            any = int(input("Any de la data: "))
            email = input("Email: ")
            feina = input("Feina (sí/no): ").lower() == "sí"
            curs = input("Curs: ")

            alumneInsert = {
                "id": id_alumno,
                "nom": nom,
                "cognom": cognom,
                "data": {
                    "dia": dia,
                    "mes": mes,
                    "any": any
                },
                "email": email,
                "feina": feina,
                "curs": curs
            }
            alumnat.append(alumneInsert)
            dicAlumnes = open("alumnes.py", "wt")
            json.dump(alumneInsert, dicAlumnes)
            dicAlumnes.close()
            alumnat[id_alumno] = alumneInsert

            input()

        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")

            # Introduiu el vostre codi per veure un alumne aquí

            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")

            # Introduiu el vostre codi per esborrar un alumne aquí

            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            # Introduiu el vostre codi per desar a fitxer aquí

            input()

        # Llegir fitxer ##################################
        case "6":
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            # Introduiu el vostre codi per llegir de fitxer aquí

            input()

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            # Trenquem el bucle infinit
            break

        # Qualsevol altra cosa #####################
        case _:
            print("\nOpció incorrecta\a")
            input()