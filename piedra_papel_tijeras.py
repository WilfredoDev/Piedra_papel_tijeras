#Importamos el modulo random para poder generar una eleccion de la computadora aleatoria
import random
#Creamos una tupla con las opciones disponibles
options=('piedra','papel','tijeras')
#Almacenamos el nombre del usuario, y le damos una introduccion con las reglas del juego
user_name = input('Bienvenido soy una IA llamada Hextech, cual es tu nombre?: ')
print('*' *10)
print("INSTRUCCIONES PIEDRA, PAPEL O TIJERAS")
print('\n1. Piedra gana a Tijeras.\n2.Tijeras gana a Papel.\n3.Papel gana a Piedra\n4.Son 3 rondas, gana el que consiga la victoria en 2')
print('*' *10)
#Nombre de la computadora
computer_name = "Hextech"

#Contador de victorias de cada jugador y contador de rondas
rounds=1
user_wins =0
computer_wins=0

#Inicio de Ciclo while para el juego de 3 rondas
while(rounds<=3):
    #Input para almacenar la opcion del usuario
    user_option = input('\nPiedra, papel o tijera => ')
    #La funcion lower nos ayuda a convertir el dato almacenado en minuscula, de esta forma evitamos errores en la comparacion, y el usuario podra escribir la opcion como quiera mayus o minusculas y no afectara.
    user_option =user_option.lower()
    #Declaramos la opcion de la computadora, con el atributo choice() se selecciona un elemento aleatorio del areglo de datos pasado como argumento
    computer_option = random.choice(options)
    
    #Condicional para cuando la opcion no esta dentro de los parametros
    if(user_option not in options):
        print(f'Lo siento {user_name} tienes que hacer una eleccion de las opciones dadas. Intentalo de nuevo')
        continue
    #Condicional para cuando las opciones son Iguales
    if(user_option == computer_option):
        print("ROUND ", rounds)
        print("User Option => ", user_option)
        print('Computer Option => ', computer_option)
        print("Empate!")
        rounds+=1
    #Condicional para cuando las opciones son Iguales

    #Condicional para cuando el usuario seleccione papel
    elif(user_option == 'papel'):
        if (computer_option == 'piedra'):
            print("ROUND ", rounds)
            print("User Option => ", user_option)
            print('Computer Option => ', computer_option)
            print(f'{user_option.capitalize()} gana a {computer_option.capitalize()}, {user_name} ganaste!.')
            rounds+=1
            user_wins=+1
        else:
            print("ROUND ", rounds)
            print("User Option => ", user_option)
            print('Computer Option => ', computer_option)
            print(f'{computer_option.capitalize()} gana a {user_option.capitalize()}, {computer_name} ganaste!.')
            rounds+=1
            computer_wins+=1
    #Condicional para cuando el usuario seleccione papel

    #Condicional para cuando el usuario seleccione tijeras
    elif(user_option == "tijeras" or user_option == 'tijera'):
        if(computer_option == 'piedra'):
            print("ROUND ", rounds)
            print("User Option => ", user_option)
            print('Computer Option => ', computer_option)
            print(f'{computer_option.capitalize()} gana a {user_option.capitalize()}, {computer_name} ganaste!.')
            rounds+=1
            computer_wins+=1
        else:
            print("ROUND ", rounds)
            print("User Option => ", user_option)
            print('Computer Option => ', computer_option)
            print(f'{user_option.capitalize()} gana a {computer_option.capitalize()}, {user_name} ganaste!.')
            rounds+=1
            user_wins=+1
    #Condicional para cuando el usuario seleccione tijeras

    #Condicional para cuando el usuario seleccione piedra
    elif(user_option=='piedra'):
        if(computer_option == 'tijeras'):
            print("ROUND ", rounds)
            print("User Option => ", user_option)
            print('Computer Option => ', computer_option)
            print(f'{user_option.capitalize()} gana a {computer_option.capitalize()}, {user_name} ganaste!.')
            rounds+=1
            user_wins=+1
        else:
            print("ROUND ", rounds)
            print("User Option => ", user_option)
            print('Computer Option => ', computer_option)
            print(f'{computer_option.capitalize()} gana a {user_option.capitalize()}, {computer_name} ganaste!.')
            rounds+=1
            computer_wins+=1
    #Condicional para cuando el usuario seleccione piedra

    #Condicional para cuando el usuario no seleccione ninguna de las tres validas
    else:
        print(f'{user_name}, debes seleccionar una opcion valida, intentalo de nuevo.')
    #Condicional para cuando el usuario no seleccione ninguna de las tres validas

#Parte final en donde mostramos el resultado del juego ya sea que el usuario o la computadora gano o que resulto en un empate
print('*' *10)
print('RESULTADOS')
if((rounds ==3) and user_wins > computer_wins):
    print(f'El juego ha terminado!, el ganador ha sido {user_name},Felicidades!')
    print("User Total Wins => ",user_wins)
    print("Computer Total Wins => ", computer_wins)
elif((rounds==3) and (computer_wins>user_wins)):
    print(f'El juego ha terminado!, el ganador ha sido {computer_name},Felicidades!')
    print("User Total Wins => ",user_wins)
    print("Computer Total Wins => ", computer_wins)
else:
    print(f'El juego ha terminado!, Ha terminado en un Empate')
    print("User Total Wins => ",user_wins)
    print("Computer Total Wins => ", computer_wins)
print('*' *10)


