def bacon_com_ovos(numero):
    assert isinstance(numero, int), "numero deve ser int"

    if numero % 3 == 0 and numero % 5 == 0:
        return "Bacon com ovos"

    if numero % 3 == 0:
        return "Bacon"

    if numero % 5 == 0:
        return "Ovos"

    return "Passar fome"
