# Vos import ici
import csv
import doctest
from collections import defaultdict

# le path du fichier de données
FILENAME = "population.csv"


def read_file(filename):
    """retourne les données sous la forme d'une liste de dictionnaires

    Args:
        filename (str): le nom du fichier de données (n lignes)

    Returns:
        list: n-1 dictionnaires dont les clés sont les champs de la première ligne du fichier
    
    >>> data = read_file(FILENAME)
    >>> type(data)
    <class 'list'>
    >>> len(data)
    140827
    >>> type(data[0])
    <class 'dict'>
    >>> len(data[0])
    15
    >>> data[1000]["Nom Officiel Région"]
    'Grand Est'
    >>> data[5000]["Code Officiel Département"]
    '02'
    >>> data[10000]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25000]["Nom Officiel Commune / Arrondissement Municipal"]
    'Baneuil'
    >>> data[50000]["Population totale"]
    '1898.0'
    >>> data[75000]["Année de recensement"]
    '2018'
    >>> data[100000]["Nom Officiel EPCI"]
    'CC de la Région de Bar-sur-Aube'
    >>> data[125000]["Nom Officiel Département"]
    'Charente-Maritime'
    >>> data[1500]["Nom Officiel Région"]
    'Occitanie'
    >>> data[5500]["Code Officiel Département"]
    '25'
    >>> data[10500]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25500]["Nom Officiel Commune / Arrondissement Municipal"]
    'Fontenoy'
    >>> data[50500]["Population totale"]
    '52.0'
    >>> data[75500]["Année de recensement"]
    '2015'
    >>> data[100500]["Nom Officiel EPCI"]
    'CC de Yenne'
    >>> data[125500]["Nom Officiel Département"]
    'Aube'
    """
    # votre code ici
    with open(filename, newline='', encoding='utf-8') as dataset:
        reader = csv.DictReader(dataset, delimiter=';')  
        return list(reader)



def main():
    # votre code de test ici
    # le code ci dessous est exécuté avec la commande :
    # python population.py
    #pass
    # Exemples d'appels
    data = read_file(FILENAME)
    # l = build_list_departements(data)
    # c = build_list_communes(data)
    # p = get_pop_commune(data, '39124')
    # d = build_dict_departements(data)
    # s = stat_by_dpt(d, '77')

    
# Ne pas modifier le code ci-dessous
if __name__ == '__main__':
    dt = True
    #dt = False # Décommenter pour exécuter "main()"
    if dt:
        # la ligne suivante teste la fonction "read_file"
        doctest.run_docstring_examples(read_file, globals(), verbose=True)
    else:
        main()
