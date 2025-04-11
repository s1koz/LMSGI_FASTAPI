### Imports ##################################################
import json
import os  # per neteja la pantalla

import psycopg2

# Variables ###################################################

# Nom del fitxer on desar/carregar dades
dicAlumnes = "alumnes.json"  # Nom del fitxer per emmagatzemar la informació d'alumnes


### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla.

alumnat = []  # Llista per emmagatzemar els alumnes

#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    # Netejem la pantalla
    os.system('cls')  # Comanda per netejar la pantalla (Windows)

    # Mostrem les diferents opcions del menú
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

    # Retornem l'opció escollida per l'usuari
    return input()


### Programa ################################################

# Bucle infinit per mantenir el programa en execució fins que l'usuari esculli sortir
while True:

    # Executem una opció funció del que hagi escollit l'usuari
    match menu():  # Fem servir 'match' per seleccionar l'opció segons la resposta de l'usuari

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')  # Netejar la pantalla
            print("Mostrar alumnes")
            print("-------------------------------")

            # Mostrem tots els alumnes de la llista
            for alumne in alumnat:
                print(f"[{alumne['id']}]", alumne['nom'], alumne['cognom'])

            input()  # Esperem que l'usuari premi una tecla per continuar

        # Afegir alumne ##################################
        case "2":
            os.system('cls')  # Netejar la pantalla
            print("Afegir alumne")
            print("-------------------------------")

            # Sol·licitem les dades de l'alumne
            id_alumno = len(alumnat) + 1  # L'ID es genera automàticament basant-se en la longitud de la llista
            nom = input("Nom: ")
            cognom = input("Cognom: ")
            dia = int(input("Dia de la data: "))
            mes = int(input("Mes de la data: "))
            any = int(input("Any de la data: "))
            email = input("Email: ")
            feina = input("Feina (sí/no): ").lower() == "sí"  # Convertim la resposta a booleà
            curs = input("Curs: ")

            # Creem el diccionari de l'alumne
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
            alumnat.append(alumneInsert)  # Afegim l'alumne a la llista

            input()  # Esperem que l'usuari premi una tecla per continuar

        # Veure alumne ##################################
        case "3":
            os.system('cls')  # Netejar la pantalla
            print("Mostrar alumnes")
            print("-------------------------------")

            # Sol·licitem l'ID de l'alumne que volem veure
            id_buscat = int(input("Introdueix l'ID de l'alumne: "))

            # Busquem l'alumne per ID
            for alumne in alumnat:
                if alumne["id"] == id_buscat:
                    print("ID:", alumne["id"])
                    print("Nom:", alumne["nom"])
                    print("Cognom:", alumne["cognom"])
                    print("Data de naixement:", alumne["data"]["dia"], "/", alumne["data"]["mes"], "/",
                          alumne["data"]["any"])
                    print("Email:", alumne["email"])
                    print("Feina:", "Sí" if alumne["feina"] else "No")
                    print("Curs:", alumne["curs"])
                    break
            else:
                print("Alumne no trobat.")  # Si no trobem l'alumne, mostrem un missatge

            input()  # Esperem que l'usuari premi una tecla per continuar

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')  # Netejar la pantalla
            print("Esborrar alumne")
            print("-------------------------------")

            # Sol·licitem l'ID de l'alumne a eliminar
            id_a_borrar = int(input("Introdueix l'ID de l'alumne a eliminar: "))

            # Busquem l'alumne per ID i l'eliminem
            for i, alumne in enumerate(alumnat):
                if alumne["id"] == id_a_borrar:
                    del alumnat[i]  # Eliminem l'alumne de la llista
                    print("Alumne eliminat correctament.")
                    break
            else:
                print("No s'ha trobat cap alumne amb aquest ID.")  # Si no trobem l'alumne, mostrem un missatge

            input()  # Esperem que l'usuari premi una tecla per continuar

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')  # Netejar la pantalla
            print("Desar a fitxer")
            print("-------------------------------")

            # Desem la llista d'alumnes al fitxer JSON
            with open(dicAlumnes, "w") as f:
                json.dump(alumnat, f, indent=4)

            print(f"Dades desades correctament a {dicAlumnes}.")  # Mostrem missatge d'èxit

            input()  # Esperem que l'usuari premi una tecla per continuar

        # Llegir fitxer ##################################
        case "6":
            os.system('cls')  # Netejar la pantalla
            print("Llegir fitxer")
            print("-------------------------------")

            # Llegim el fitxer si existeix
            if os.path.exists(dicAlumnes):
                with open(dicAlumnes, "r") as f:
                    alumnat = json.load(f)  # Carreguem els alumnes des del fitxer

                # Mostrem els alumnes carregats
                if alumnat:  # Si la llista no està buida
                    print("Alumnes carregats des del fitxer:")
                    for alumne in alumnat:
                        print(
                            f"ID: {alumne['id']}, Nom: {alumne['nom']} {alumne['cognom']}, Email: {alumne['email']}, Curs: {alumne['curs']}")
                else:
                    print("No s'han trobat alumnes al fitxer.")  # Si no hi ha alumnes al fitxer
            else:
                print(f"No s'ha trobat el fitxer {dicAlumnes}.")  # Si el fitxer no existeix

            input()  # Esperem que l'usuari premi una tecla per continuar

        # Sortir ##################################
        case "0":
            os.system('cls')  # Netejar la pantalla
            print("Adeu!")  # Missatge de comiat

            # Trenquem el bucle infinit
            break

        # Qualsevol altra cosa #####################
        case _:
            print("\nOpció incorrecta\a")  # Si l'usuari introdueix una opció incorrecta
            input()  # Esperem que l'usuari premi una tecla per continuar
