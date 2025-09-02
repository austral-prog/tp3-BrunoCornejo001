def check_vowels():
    nombre = input("Ingrese su nombre: ").lower()
    contiene_a = "a" in nombre
    contiene_e = "e" in nombre
    contiene_i = "i" in nombre
    contiene_o = "o" in nombre
    contiene_u = "u" in nombre

    print("Contiene a:" + " " + str(contiene_a))
    print("Contiene e:" + " " + str(contiene_e))
    print("Contiene i:" + " " + str(contiene_i))
    print("Contiene o:" + " " + str(contiene_o))
    print("Contiene u:" + " " + str(contiene_u))
check_vowels()
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
