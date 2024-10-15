def anadir_comentario ():
    while True:
        print("Por favor, introduzca una puntuacion en una escala de 1 al 5")
        point = input()
        point = es_decimal(point)
        if point is not None:
          if point <= 0 or point > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
            print('Indíquelo en una escala de 1 a 5')
          else:
            print('Por favor, introduzca un comentario')
            comment = input()
            post = f'punto: {point} comentario: {comment}'
            file_pc = open("data.txt", 'a')
            file_pc.write(f'{ post } \n')
            file_pc.close()
            break  
        else:
         print('Por favor, introduzca la puntuación en números')



def ver_resultados():
    print("Resultados hasta la fecha")
    read_file = open("data.txt","r")
    print(read_file.read())
    read_file.close

def salir():
    if True:
     print("Finalizando")
     pass
     
            
            
    
    
    
def es_decimal(n):
    if n.isdecimal():
        return int(n)
    return None


while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    num = input()
    num = es_decimal(num)
    if num is not None:
        if num == 1:
            anadir_comentario()
        elif num == 2:
            ver_resultados()
        elif num == 3:
            salir()
            break
        else:
            print("Introduzca un numero de 1 al 3")
    else:
        print("Introduzca un numero entero")        
        

        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

