#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Écrire un programme qui demande à l’utilisateur d’entrer 10 valeurs (entier, float, str), et qui ordonne la liste fournie
def order(values: list = None) -> list:
    if values is None:
        # demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Entrez les valeurs\n"))

    #tier les valeurs ici
    num_values = [float(value) for value in values if value.isdigit()] #mettre en ordre les float, seulement si ce sont des chiffres à virgule
    str_values = [value for value in values if not value.isdigit()]

    return sorted(num_values) + sorted(str_values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # demander les mots ici
        words = []
        while len(words) < 2:
            words.append(input("Entrez les deux mots\n"))

    return sorted(words[0]) == sorted(words[1]) #comparer the first sorted word to the second one
                                                #ça return true s'ils ont les mêmes lettres

def contains_doubles(items: list) -> bool:
    #vérifier si la liste contient que des éléments uniques
    #for items in list: indiqué dans l'énoncé

    return len(set(items)) !=len(items)   #Utilisez la fonction set () pour supprimer les doublons dans une liste
                                            #donc si la quantité d'élément dans la liste n'est pas égale (!=) à
                                            #la quanité de départ, c'est qu'il y a des doublons

#mal compris :(
def best_grades(student_grades: dict) -> dict:
    # Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict() #best_student --> dans le dictionnaire créer "student_grades"
    for key, value in student_grades.items():
        average = sum(value)/len(value)  #faire la moyenne des notes, key = nom des étudiants, value = leur note

        if len(best_student) == 0 or list(best_student.values())[0] < average:
            best_student = {key: average}

    return best_student


def frequence(sentence: str) -> dict:
    # Afficher les lettres affiché plus de 5 fois
    # Retourner le tableau de lettres --> pour retourner un tableau de lettre; dictionnaire obvi
    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter) #dans le dict de fréquence, count the letters in the sentence

    sorted_keys = sorted(frequency, key = frequency.__getitem__, reverse = True) #the key of the dict is the frequency of the letter
                                                                                    #and we sorted the letters out
    # getit: permet aux instances d’une classe d’utiliser l’indexation [] avec les variables de référence d’une classe pour accéder à la valeur d’une liste, d’un dictionnaire ou d’un tuple à partir d’un index spécifique.
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"Le caractère {key} revient {frequency[key]} fois.")

    return frequency


def get_recipes():
    # Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom = input("Quel est le nom de la recette ? \n")
    ingredient = input("Quels sont les ingrédients nécessaires pour cette recette ? Séparez les par un virgule \n").split(",")
    return {nom : ingredient}



#affiche les ingrédients d’une recette, en vérifiant au préalable si cette recette est dans notre livre de recettes.
def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Quel est le nom de la recette ? \n")
    if nom in ingredients:
        print(ingredients[nom])
    else:
        print("Cette recette ne figure pas dans le livre")
        print_recipe(ingredients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
