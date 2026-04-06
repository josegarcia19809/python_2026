import os
from os.path import isdir, join

matches = []


def file_search(root, filename):
    print(f"Searching in: {root} 🔎")

    for file in os.listdir(root):
        full_path = os.path.join(root, file)

        # Si encontramos el archivo
        if filename in file:
            matches.append(full_path)  # Guardar resultado 📍

        # Si es carpeta, buscar dentro (recursividad)
        if os.path.isdir(full_path):
            file_search(full_path, filename)


def main():
    # file_search("C:/tools", "README.md")
    file_search("/Users/josegarcia/Documents/", "README.md")

    for m in matches:
        print("Matched:", m)


main()
