import Morse as morse

option = ""
while option != "E":
    option = input("C para Codificar\nD para Descodificar\nE para salir")
    if option.upper() == "C":
        string = input("Inserte Mensaje a Codificar")
        print(morse.turnToMorse(string))
    elif option.upper() == "D":
        string = input("Inserte Mensaje a Descodificar separado por punto y coma(;)")
        print(morse.turnToString(string))
