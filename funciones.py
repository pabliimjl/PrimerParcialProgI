'''
Apellido y nombre: Pablo Jesus Funciones
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion I
Instancia: Primer Examen Parcial
'''

import json
from os import system

def cantidad_elementos(variable)->int:
    """Determina la cantidad de elementos de cualquier tipo de dato

    Args:
        variable (any): dato a corroborar

    Returns:
        int: cantidad de elementos del dato
    """    
    contador = 0
    for elemento in variable:
        contador += 1
    
    return contador

def leer_json(nombre_archivo:str, key:str)->list:
    """Lee el json segun el nombre de archivo y key que se le pase

    Args:
        nombre_archivo (str): nombre de archivo a leer. Ej: 'data.json'
        key (str): llave del archivo a leer. Ej: 'pasajeros'

    Returns:
        list: lista con todos los valores de la llave en el json
    """    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)

    return(data[key])

def es_digito(variable:str)->bool:
    """Determina si una cadena de caracteres esta compuesta exclusivamente por numeros, por tanto, es un digito.

    Args:
        variable (str): cadena de caracteres a analizar

    Returns:
        bool: True si es digito, False si no es digito
    """    
    
    retorno = True
    for caracter in variable:
        if caracter > '9' or caracter < '0':
            retorno = False
            break

    return retorno

def alta_aerolinea()->str:
    """Ingreso de aerolinea validado

    Returns:
        str: aerolinea validada
    """    
    aerolineas = ['AA','LATAM','IBERIA']
    aerolinea = input("Ingrese aerolinea: ")
    while aerolinea not in aerolineas:
        aerolinea = input("Ingrese aerolinea correcta: ")
    return aerolinea

def alta_apellido_y_nombre(tab:str)->str: 
    """Ingreso de apellido y nombre, comprueba que sean caracteres y que tenga hasta 30 caracteres. Recibe la tabulacion deseada en formato de string

    Args:
        tab (str): cantidad de tabulaciones. Ej: '\\t\\t'

    Returns:
        str: apellido y nombre validados
    """    
    
    apellido_nombre_pasajero = input(f"{tab}Ingrese Apellido y Nombre del pasajero: ")
    while es_digito(apellido_nombre_pasajero) or apellido_nombre_pasajero == "" or cantidad_elementos(apellido_nombre_pasajero) > 30:
        apellido_nombre_pasajero = input("Ingrese Apellido y Nombre valido: ")
    return apellido_nombre_pasajero

def alta_dni_pasajero(tab:str)->str:
    """Ingreso de DNI, comprueba que sean numeros y que tenga 8 caracteres. Recibe la tabulacion deseada en formato de string

    Args:
        tab (str): cantidad de tabulaciones. Ej: '\\t\\t'

    Returns:
        str: DNI validado
    """    
    dni_pasajero = input(f"{tab}Ingrese DNI pasajero: ")
    while not es_digito(dni_pasajero) or cantidad_elementos(dni_pasajero) != 8:
        dni_pasajero = input("Ingrese DNI valido: ")
    return dni_pasajero

def alta_precio()->str:
    """Ingreso de precio, verifica que sean digitos y que entre en el rango entre 500.000 y 2.000.000

    Returns:
        str: precio validado
    """    
    precio = input("Ingrese precio: ")
    while not es_digito(precio) or int(precio) > 2000000 or int(precio) < 500000:
        precio = input("Ingrese precio valido: ")
    return precio

def alta_origen_y_destino(origen="")->str:
    """Ingreso de origen/destino, validando que el mismo sea un destino valido 
    'Buenos Aires','Madrid','Paris','Roma','Tokio', que el origen sea distinto al destino y retorna el dato validado

    Args:
        origen (str, optional): en caso de estar ingresando el origen no pasar ningun valor. Defaults to "".

    Returns:
        str: origen/destino validado
    """    
    destinos = ['Buenos Aires','Madrid','Paris','Roma','Tokio']
    destino = input("Ingrese destino: ")
    while destino not in destinos:
        destino = input("Ingrese destino valido: ")
    return destino

def alta_clase()->str:
    """Ingreso de clase del vuelo. Valida que sea una clase valida (Turista o Ejecutivo) y retorna el ingreso validado

    Returns:
        str: clase validada
    """    
    clases = ['Turista','Ejecutivo']
    clase = input("Ingrese clase: ")
    while clase not in clases:
        clase = input("Ingrese clase correcta: ")

    return clase

def alta_fecha(tab:str)->str:
    """Ingreso de fecha validada en formato AAAAMMDD. Puede ser formateada con tabulaciones. Retorna la fecha validada

    Args:
        tab (str): cantidad de tabulaciones. Ej: '\\t\\t'

    Returns:
        str: fecha validada
    """    
    fecha = input(f"{tab}Ingrese fecha (AAAAMMDD): ")
    while not es_digito(fecha) or cantidad_elementos(fecha) != 8:
        fecha = input("Ingrese fecha valida (AAAAMMDD): ")

    return fecha
    
def listar_id_nombre(lista:list):
    """Funcion para mostrar en pantalla los pasajeros por Id y Apellido y nombre.\n

    Ej de impresion:\n
    1 | Pablo Jesus

    Args:
        lista (list): lista de pasajeros a mostrar
    """
    for persona in lista:
        print(f"{persona['Id']}\t| {persona['Apellido_Nombre_Pasajero']}")

def alta(lista:list)->list:
    """Ejecuta el alta de un nuevo pasajero, pidiendole los datos correspondientes

    Args:
        lista (list): lista a agregarle el pasajero

    Returns:
        list: lista con pasajero agregado
    """    
    ultimo_id = cantidad_elementos(lista)
    aerolinea = alta_aerolinea()
    apellido_nombre_pasajero = alta_apellido_y_nombre("")
    dni_pasajero = alta_dni_pasajero("")
    precio = alta_precio()
    origen = alta_origen_y_destino()
    destino = alta_origen_y_destino(origen)
    clase = alta_clase()
    fecha = alta_fecha("")
    lista_pasajero = []
    lista_pasajero.append(ultimo_id+1)
    lista_pasajero.append(aerolinea)
    lista_pasajero.append(apellido_nombre_pasajero)
    lista_pasajero.append(dni_pasajero)
    lista_pasajero.append(precio)
    lista_pasajero.append(origen)
    lista_pasajero.append(destino)
    lista_pasajero.append(clase)
    lista_pasajero.append(fecha)
    diccionario = {}
    contador_lista = 0
    for key in lista[0].keys():
        diccionario.update({key : lista_pasajero[contador_lista]})
        contador_lista += 1
    lista.append(diccionario)

    return lista
    
def imprimir_menu():
    """Imprime las opciones del simulacro
    """    
    print ("MENU PRINCIPAL")
    print ("\tA - CARGAR ARCHIVO JSON")
    print ("\tB - ALTA DE DATOS")
    print ("\tC - MODIFICAR DATOS")
    print ("\tD - BORRAR DATOS")
    print ("\tE - LISTAR TODOS LOS PASAJES")
    print ("\tF - SUBMENU DEL PARCIAL")
    print ("\tG - SALIR")

def imprimir_submenu_parcial():
    """Imprime las opciones del submenu del parcial 
    """    
    print ("\t\t1 - LISTAR POR PANTALLA LOS PASAJES CON MAYOR Y MENOR VALOR")
    print ("\t\t2 - CALCULAR LA CANTIDAD DE PASAJES DE UN DESTINO DETERMINADO")
    print ("\t\t3 - LISTAR LOS PASAJES ORDENADOS POR FECHA(ASC O DESC)")
    print ("\t\t4 - GENERAR JSON ORDENADO POR FECHA")
    print ("\t\t5 - GENERAR CSV CON PASAJES MAYOR Y MENOR PRECIO")

def listar_pasajeros(lista:list):
    """Lista los pasajeros en el formato exigido en el parcial

    Args:
        lista (list): lista de pasajeros a mostrar
    """    
    print("Fecha\t |  Aerolinea  | Clase         | Origen        | Destino       | Precio         | DNI          | Apellido y nombre")
    for pasajero in lista:
        linea = generar_linea(pasajero)
        print(linea)
        
def generar_linea(diccionario:dict)->str:
    """Genera una linea formateada de acuerdo al formato exigido en el parcial

    Args:
        diccionario (dict): diccionario a formatear

    Returns:
        str: linea formateada
    """        
        
    linea = ""
    linea += f'{diccionario['Fecha']}\t{diccionario['Aerolínea']}\t'
    linea += f'{diccionario['Clase']} \t' if cantidad_elementos(diccionario['Clase']) >8 else f'{diccionario['Clase']} \t'
    linea += f'{diccionario['Origen']} \t\t' if cantidad_elementos(diccionario['Origen']) <8 else f'{diccionario['Origen']}\t'
    linea += f'{diccionario['Destino']} \t\t' if cantidad_elementos(diccionario['Destino']) <8 else f'{diccionario['Destino']}\t'
    linea += f'{diccionario['Precio']}\t\t' if cantidad_elementos(diccionario['Precio']) < 8 else f'{diccionario['Precio']}\t'
    linea += f'{diccionario['DNI_Pasajero']}\t{diccionario['Apellido_Nombre_Pasajero']}'
    return linea

def obtener_pasajes_menor_valor(lista:list)->list:
    """Obtiene lo/s pasajes de menor valor. Retorna una lista con los mismos

    Args:
        lista (list): lista a buscar

    Returns:
        list: lista con resultados
    """    
    bandera_minimo = True
    for pasajero in lista:
        if bandera_minimo or float(pasajero['Precio']) < precio_minimo:
            precio_minimo = float(pasajero['Precio'])
            bandera_minimo = False

    lista_minimos = []
    for pasajero in lista:
        if float(pasajero['Precio']) == precio_minimo:
            lista_minimos.append(pasajero)

    return lista_minimos

def obtener_pasajes_mayor_valor(lista:list)->list:
    
    """Obtiene lo/s pasajes de mayor valor. Retorna una lista con los mismos

    Args:
        lista (list): lista a buscar

    Returns:
        list: lista con resultados
    """    
    bandera_maximo = True
    for pasajero in lista:
        if bandera_maximo or float(pasajero['Precio']) > precio_maximo:
            precio_maximo = float(pasajero['Precio'])
            bandera_maximo = False
    lista_maximos = []
    for pasajero in lista:
        if float(pasajero['Precio']) == precio_maximo: 
            lista_maximos.append(pasajero)
     
    return lista_maximos

def modificar_pasajero(lista:list):
    """Lista id y nombre de pasajeros para luego seleccionar un ID (lo valida) y modificar ciertos datos del pasaje (DNI/Fecha/Apellido y Nombre).

    Recibe lista por parametro y modifica la misma.

    Args:
        lista (_type_): lista a modificar
    """    
    listar_id_nombre(lista)
    id = input("\tIngrese ID a modificar")
    while not es_digito(id) or int(id) > cantidad_elementos(lista):
        id = input("\tIngrese ID valido")
    id = int(id)
    tipo = input("\tIngrese tipo de dato a modificar(DNI/Apellido y nombre/Fecha):")
    while es_digito(tipo) or tipo == "" or (tipo != "DNI" and tipo !="Apellido y nombre" and tipo != "Fecha"):
        tipo = input("\tIngrese tipo valido(DNI/Apellido y nombre/Fecha): ")
    if tipo == "DNI":    
        dato = alta_dni_pasajero("\t")
        lista[id-1]['DNI_Pasajero'] = dato
    elif tipo == "Apellido y nombre":
        dato = alta_apellido_y_nombre("\t")
        lista[id-1]['Apellido_Nombre_Pasajero'] = dato
    else:
        dato = alta_fecha("\t")
        lista[id-1]['Fecha'] = dato

def pausa():
    """Funcion meramente estetica que solicita al usuario presionar enter para continuar
    """    
    var = input("Presione enter para continuar...")

def borrar_pasajero(lista:list):
    """Borra un pasajero, solicitando un id del mismo y valida que existe

    Recibe la lista por parametro
    Args:
        lista (list): lista a modificar
    """    
    
    listar_id_nombre(lista)
    id = input("\tIngrese ID a eliminar")
    while not es_digito(id) or int(id) > cantidad_elementos(lista):
        id = input("\tIngrese ID valido")
    id = int(id)
    for clave in lista[id-1].keys():
        if clave != 'Id':
            lista[id-1][clave] = ""

def obtener_y_validar_subopcion()->str:
    """Validacion de opciones del parcial

    Returns:
        str: opcion validada
    """    
    subopcion = input("Ingrese una opcion: ")
    while not es_digito(subopcion) or int(subopcion) < 1 or int(subopcion) > 5:
        subopcion = input("Ingrese una opcion valida: ")

    return subopcion

def calcular_y_mostrar_cantidad_pasajes_destino(lista:list):
    """Solicita un destino y muestra la cantidad de pasajes con el mismo.

    Args:
        lista (list): lista a trabajar
    """    
    destino = alta_origen_y_destino()
    contador = 0
    for pasajero in lista:
        if pasajero['Destino'] == destino:
            contador += 1
    
    print(f"La cantidad de pasajes con destino '{destino}' son {contador}")

def ordenar_por_fecha(lista:list)->list:
    """Ordena una lista por fecha, solicita un criterio (ASC/DESC)

    Args:
        lista (list): lista a ordenar

    Returns:
        list: lista ordenada
    """    

    criterios = ['ASC','DESC']
    criterio = input('Ingrese critero para ordenar por fecha (ASC/DESC): ')
    while criterio not in criterios:
        criterio = input('Ingrese un criterio valido (ASC/DESC): ')

    for i in range (cantidad_elementos(lista)-1):
        for j in range (i+1,cantidad_elementos(lista)):
            if int(lista[i]['Fecha']) > int(lista[j]['Fecha']) and criterio == 'ASC':
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
            if int(lista[i]['Fecha']) < int(lista[j]['Fecha']) and criterio == 'DESC':
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    
    return lista

def exportar_json(lista:list):
    """Exporta un JSON formateado con lo solicitado en el parcial

    Args:
        lista (list): lista a exportar al JSON
    """    
    with open('ordenado_por_fecha.json','w', encoding='utf-8') as archivo:
        json.dump({'pasajeros':lista}, archivo, indent=4, ensure_ascii=False)

def generar_csv(lista_mayor,lista_menor):
    """Genera un CSV formateado de acuerdo al formato del parcial

    Args:
        lista_mayor (_type_): lista de mayores valores
        lista_menor (_type_): lista de mayores valores
    """    

    with open('pasajes_mayor_y_menor_valor.csv','w',encoding='utf-8') as archivo:
        archivo.write('Fecha,Aerolinea,Clase,Origen,Destino,Precio,DNI,Apellido y nombre\n')
        for pasajero in lista_mayor:
            linea = f'{pasajero['Fecha']},{pasajero['Aerolínea']},{pasajero['Clase']},{pasajero['Origen']},{pasajero['Destino']}, {pasajero['Precio']},{pasajero['DNI_Pasajero']},{pasajero['Apellido_Nombre_Pasajero']}\n'
            archivo.write(linea)
        for pasajero in lista_menor:
            linea = f'{pasajero['Fecha']},{pasajero['Aerolínea']},{pasajero['Clase']},{pasajero['Origen']},{pasajero['Destino']}, {pasajero['Precio']},{pasajero['DNI_Pasajero']},{pasajero['Apellido_Nombre_Pasajero']}\n'
            archivo.write(linea)

def main():
    """Funcion principal
    """    
    bandera_continuar = True
    bandera_json = False
    while bandera_continuar:
        system('cls')
        imprimir_menu()
        opcion = input("Ingrese opcion: ").upper()
        while es_digito(opcion) or opcion < "A" or opcion > "G":
            opcion = input("Ingrese opcion valida: ").upper()
        if opcion == 'A':
            lista_pasajeros = leer_json("data.json","pasajeros")
            bandera_json = True
            print("Archivo abierto")
        elif bandera_json:
            match(opcion):
                case 'B':
                    alta(lista_pasajeros)
                case 'C':
                    modificar_pasajero(lista_pasajeros)
                case 'D':
                    borrar_pasajero(lista_pasajeros)
                case 'E':
                    listar_pasajeros(lista_pasajeros)
                case 'F':
                    imprimir_submenu_parcial()
                    subopcion = obtener_y_validar_subopcion()
                    match(subopcion):
                        case '1':
                            print("Listando los pasajes con mayor valor...")
                            listar_pasajeros(obtener_pasajes_mayor_valor(lista_pasajeros))
                            print("Listando los pasajes con menor valor...")
                            listar_pasajeros(obtener_pasajes_menor_valor(lista_pasajeros))
                        case '2':
                            calcular_y_mostrar_cantidad_pasajes_destino(lista_pasajeros)
                        case '3':
                            listar_pasajeros(ordenar_por_fecha(lista_pasajeros))
                        case '4':
                            exportar_json(ordenar_por_fecha(lista_pasajeros))
                        case '5':
                            generar_csv(obtener_pasajes_mayor_valor(lista_pasajeros),obtener_pasajes_menor_valor(lista_pasajeros))


                case 'G':
                    bandera_continuar = False
        else:
            print("Es necesario abrir el archivo primero")
        
        pausa()
                
