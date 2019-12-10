from numpy import cos,sin,pi
from math import tan
Operacion= input('operacion ')
gravedad= 9.81
presion_atmosferica= 101.3
mmhg = 7.501
densidad_agua = 1e-3
densidad_agua_salada = 1.03e-3
Kilopascales = 1e3

def Fuerza_peso():
    Fuerza = float(input('ingresa la masa'))
    Fuerza = Fuerza * gravedad
    return(Fuerza)

def coversion_presion():
    print('Para esta calculadora trabajaremos en Kilopascales')
    pregunta1 = input('¿tienes mmhg, Atm, Pa?')
    if(pregunta1 == 'mmhg'):
        medida1 = float(input('cantidad en mmhg: '))
        return(medida1/mmhg)
    if(pregunta1 == 'Atm'):
        medida1 = float(input('inserta la cantidad de Atm'))
        return(medida1/presion_atmosferica)
    if(pregunta1 == 'Pa'):
        medida1 = float(input('inserta la cantidad de Pa'))
        return(medida1*Kilopascales)
def calculadora_areas():
    pregunta1 = input('¿Qué tipo de figura es?: ')
    if(pregunta1 == 'Cuadrado'):
        lados = int(input('Medida de uno de sus lados en metros: '))
        Area = lados*lados
        return(Area)

    if(pregunta1 == 'Circulo'):
        pregunta2 = input('¿Tienes diametro o Radio?: ')
        if(pregunta2 == 'Radio'):
            medida1 = int(input('ingresa el Radio en metros: '))
            Area = pi*medida1**2
            return(Area)
        if(pregunta2 == 'Diametro'):
            medida1 = int(input('inserta el diametro en metros: '))
            Diametro = medida1/2
            Diametro = pi*Diametro**2
            return(Diametro)
    
    if(pregunta1 == 'Rectangulo'):
        altura = int(input('Medida de la altura en metros: '))
        base = int(input('Medida de la base en metros: '))
        Area = base*altura
        return(Area)
    

def calculadora_Presion():
    print('Esto podemos calcular: Fuerza, Area, Presion ')
    pregunta1 = input('¿Cual buscas?: ')
    if(pregunta1 == 'Presion'):
        pregunta2 = input('Conoces el Area o tienes Longitudes: ')
        if(pregunta2 == Longitudes):
            medida1 = int(input('inserta la fuerza'))
            calculadora_areas()
            return(medida1* calculadora_areas())
        if(pregunta2 == 'Area'):
            medida1 = int(input('inserta la Fuerza'))
            medida2 = int(input('inserta Area'))
            return(medida1/medida2)
    if(pregunta1 == 'Fuerza'):
        pregunta2 = input('Conoces el Area o tienes Longitudes: ')
        if(pregunta2 == Longitudes):
            medida1 = int(input('inserta la Presion: '))
            Area = calculadora_areas()
            return( medida1 * Area) 
        if(pregunta2 == 'Area'):
            medida1 = int(input('inserta la Presion: '))
            medida2 = int(input('inserta Area: '))
            return(medida1/medida2)
    if(pregunta1 == 'Area'):
        medida1 = float(input('Inserta la Fuerza: ')) 
        medida2 = float(input('Inserta la Presion: '))
        return(medida1/medida2)

def Presion_en_un_fluido():
    pregunta1 = input('¿Quieres calcular Presion, Densidad, Altura?: ')
    if(pregunta1 == 'Presion'):
        pregunta2 = input('¿La densidad es de Agua salada, Agua natural o ninguna de las dos?')
        if(pregunta2 == 'Agua natural'):
            Altura = float(input('Solo ingresa la Altura: '))
            Presion = gravedad * Altura * densidad_agua 
            return(Presion)
        elif(pregunta2 == 'Agua salada'):
            Altura = float(input('Solo ingresa la Altura: '))
            Presion = gravedad * Altura * densidad_agua_salada
            return(Presion)
        else:
            densidad_objeto = float(input('Inserta la densidad del objeto en gramos: '))
            Altura = float(input('Solo ingresa la Altura: '))
            Presion = gravedad * Altura * densidad_objeto
            return(Presion)

    if(pregunta1 == 'Densidad'):
        pregunta2 = input('¿Conoces la presion? Si/No: ')
        if(pregunta2 == 'Si'):
            Altura = float(input('Ingresa la altura en metros: '))
            pregunta3 = input('¿La presion la tienes en Kilopascales? Si/No: ')
            if(pregunta3 == 'Si'):
                Presion = float(input('Ingresa la Presion en Kilopascales: '))
                Densidad = Presion/gravedad*Altura
                return(Densidad)
            elif(pregunta3 == 'No'):
                Altura = float(input('Ingresa la altura en metros: '))
                Presion = coversion_presion()
                Densidad = Presion/gravedad*Altura
                return(Densidad)
        if(pregunta2 == 'No'):
            Altura = float(input('Ingresa la altura en metros: '))
            Presion = calculadora_Presion()
            Densidad = calculadora_Presion()/gravedad*Altura
            return(Densidad)

    if(pregunta1 == 'Altura'):
        pregunta2 = ('¿Conoces la presion? Si/No: ')
        if(pregunta2 == 'Si'):
            pregunta3 = input('¿La densidad es de Agua salada, Agua natural o ninguna de las dos?: ')
            if(pregunta3 == 'Agua salada'):
                pregunta4 = input('¿Conoces la presion en Kilopascales? Si/No: ')
                if(pregunta4 == 'Si'):
                    Presion = float(input('Ingresa la presion en kilopascales: '))
                    return(Presion/densidad_agua_salada*gravedad)
                if(pregunta4 == 'No'):
                    return(coversion_presion()/densidad_agua_salada*gravedad)
            if(pregunta3 == 'Agua natural'):
                pregunta4 = input('¿Conoces la presion en Kilopascales? Si/No: ')
                if(pregunta4 == 'Si'):
                    Presion = float(input('Ingresa la presion en kilopascales: '))
                    return(Presion/densidad_agua_salada*gravedad)
                if(pregunta4 == 'No'):
                    return(coversion_presion()/densidad_agua*gravedad)
            if(pregunta3 == 'ninguna de las dos'):
                pregunta4 = input('¿Tienes que calcular la densidad? Si/No: ')
                if(pregunta4 == 'No'):
                    pregunta5 = input('¿Conoces presion en Kilopascales? Si/No: ')
                    if(pregunta5 == 'Si'):
                        Presion = float(input('Inserta la presion: '))
                        Densidad = float(input('Inserta la densidad: '))
                        Altura = Presion/Densidad*gravedad
                        return(Altura)
                    elif(pregunta5 =='No'):
                        Densidad = float(input('Inserta la densidad: '))
                        Altura = conversion_presion()/Densidad*gravedad
                        return(Altura)
                elif(pregunta4 == 'Si'):
                    Densidad = calculadora_Densidad()
                    pregunta5 = input('¿Conoces presion en Kilopascales? Si/No: ')
                    if(pregunta5 == 'Si'):
                        Presion = float(input('Inserta la presion: '))
                        Densidad = float(input('Inserta la densidad: '))
                        Altura = Presion/Densidad*gravedad
                        return(Altura)
                    elif(pregunta5 =='No'):
                        Densidad = float(input('Inserta la densidad: '))
                        Altura = conversion_presion()/Densidad*gravedad
                        return(Altura)

def Principio_de_pascal():
    pregunta1 = input('Podemos calcular Fuerza1, Fuerza2, Area1, Area2: ')
    if(pregunta1 == 'Fuerza1'):
        pregunta2 = input('¿Tienes que convertir la Fuerza2? Si/No: ')
        if(pregunta2 == 'Si'):
            Fuerza2 = Fuerza_peso()
            pregunta3 = input('¿Tienes que calcular ambas areas, solo Area1, Solo Area2, ninguna?: ')
            if(pregunta3 == 'Ambas'):
                Area1 = calculadora_areas()
                Area2 = calculadora_areas()
                Fuerza1 = Fuerza2/Area2
                Fuerza1 = Fuerza1*Area1
                return(Fuerza1)            
            if(pregunta3 == 'Area1'):
                Area1 = calculadora_areas()
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza1 = Fuerza2/Area2
                Fuerza1 = Fuerza1*Area1
                return(Fuerza1)
            if(pregunta3 == 'Area2'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = calculadora_areas()
                Fuerza = Fuerza2/Area2
                Fuerza1 = Fuerza*Area1
                return(Fuerza1)            
            if(pregunta3 == 'ninguna'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza = Fuerza2/Area2
                Fuerza1 = Fuerza*Area1
                return(Fuerza1)
        if(pregunta2 == 'No'):
            Fuerza2 = float(input('Inserta el valor de la fuerza en newtons: '))
            pregunta3 = input('¿Tienes que calcular ambas areas, solo Area1, Solo Area2, ninguna?: ')
            if(pregunta3 == 'Ambas'):
                Area1 = calculadora_areas()
                Area2 = calculadora_areas()
                Fuerza1 = Fuerza2/Area2
                Fuerza1 = Fuerza1*Area1
                return(Fuerza1)            
            elif(pregunta3 == 'Area1'):
                Area1 = calculadora_areas()
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza1 = Fuerza2/Area2
                Fuerza1 = Fuerza1*Area1
                return(Fuerza1)
            elif(pregunta3 == 'Area2'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = calculadora_areas()
                Fuerza1 = Fuerza2/Area2
                Fuerza1 = Fuerza1*Area1
                return(Fuerza1)            
            elif(pregunta3 == 'ninguna'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza1 = Fuerza2/Area2
                Fuerza1 = Fuerza1*Area1
                return(Fuerza1)
    
    if(pregunta1 == 'Fuerza2'):
        pregunta2 = input('¿Tienes que convertir la Fuerza1? Si/No: ')
        if(pregunta2 == 'Si'):
            Fuerza1 = Fuerza_peso()
            pregunta3 = input('¿Tienes que calcular ambas areas, solo Area1, Solo Area2, ninguna?: ')
            if(pregunta3 == 'Ambas'):
                Area1 = calculadora_areas()
                Area2 = calculadora_areas()
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)            
            elif(pregunta3 == 'Area1'):
                Area1 = calculadora_areas()
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)
            elif(pregunta3 == 'Area2'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = calculadora_areas()
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)            
            elif(pregunta3 == 'ninguna'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)
        if(pregunta2 == 'No'):
            Fuerza2 = float(input('Inserta el valor de la fuerza en newtons: '))
            pregunta3 = input('¿Tienes que calcular ambas areas, solo Area1, Solo Area2, ninguna?: ')
            if(pregunta3 == 'Ambas'):
                Area1 = calculadora_areas()
                Area2 = calculadora_areas()
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)            
            elif(pregunta3 == 'Area1'):
                Area1 = calculadora_areas()
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)
            elif(pregunta3 == 'Area2'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = calculadora_areas()
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)            
            elif(pregunta3 == 'ninguna'):
                Area1 = float(input('Valor del Area2 en metros: ')
                Area2 = float(input('Valor del Area2 en metros: ')
                Fuerza2 = Fuerza1/Area1
                Fuerza2 = Fuerza2*Area2
                return(Fuerza2)

    if(pregunta1 == 'Area1'):
        pregunta2 = input('¿Conoces el Area2?: Si/No: ')
        if(pregunta2 == 'Si'):
            Area2 = float(input('Ingresa el valor del Area2 en metros: '))
            pregunta3 = input('¿Tienes que convertir Fuerza1, Fuerza2, Ambos, Ninguno?')
            if(pregunta3 == 'Ambos'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = Fuerza_peso()
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
            elif(pregunta3 == 'Fuerza1'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
            elif(pregunta3 == 'Fuerza2'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = Fuerza_peso()
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
            elif(pregunta3 == 'Ninguno'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
        if(pregunta2 == 'No'):
            Area2 = calculadora_areas()
            pregunta3 = input('¿Tienes que convertir Fuerza1, Fuerza2, Ambos, Ninguno?')
            if(pregunta3 == 'Ambos'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = Fuerza_peso()
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
            elif(pregunta3 == 'Fuerza1'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
            elif(pregunta3 == 'Fuerza2'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = Fuerza_peso()
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
            elif(pregunta3 == 'Ninguno'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area1 = Fuerza1*Area2
                Area1 = Area1/Fuerza2
                return(Area1)
    
    if(pregunta1 == 'Area2'):
        pregunta2 = input('¿Conoces el Area1?: Si/No: ')
        if(pregunta2 == 'Si'):
            Area1 = float(input('Ingresa el valor del Area1 en metros: '))
            pregunta3 = input('¿Tienes que convertir Fuerza1, Fuerza2, Ambos, Ninguno?')
            if(pregunta3 == 'Ambos'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = Fuerza_peso()
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
            elif(pregunta3 == 'Fuerza1'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
            elif(pregunta3 == 'Fuerza2'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = Fuerza_peso()
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
            elif(pregunta3 == 'Ninguno'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
        if(pregunta2 == 'No'):
            Area1 = calculadora_areas()
            pregunta3 = input('¿Tienes que convertir Fuerza1, Fuerza2, Ambos, Ninguno?')
            if(pregunta3 == 'Ambos'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = Fuerza_peso()
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
            elif(pregunta3 == 'Fuerza1'):
                Fuerza1 = Fuerza_peso()
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
            elif(pregunta3 == 'Fuerza2'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = Fuerza_peso()
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
            elif(pregunta3 == 'Ninguno'):
                Fuerza1 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Fuerza2 = float(input('Inserta el valor de la Fuerza2 en newtons: '))
                Area2 = Area1*Fuerza2
                Area2 = Area1/Fuerza1
                return(Area1)
                                
def Principio_de_Arquimedes():
    pregunta1 = input('¿Quieres calcular Presion total hacia abajo, Presion total hacia arriba, Fuerza1, Fuerza2, Fuerza bollante?: ')
    if(pregunta1 == 'Presion total hacia arriba'):
        pregunta2 = input('¿Quieres calcular la Presion total hacia abajo, Densidad o Altura?: ')
        if(pregunta2 == 'Presion total hacia abajo'):
            pregunta3 = input('¿Tienes que calcular la densidad o es densidad de Agua natural, Agua salada? Si/No/Agua natural/Agua salada: ')                    
            if(pregunta3 == 'Si'):
                Densidad = calculadora_Densidad()
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)
            if(pregunta3 == 'No'):
                Densidad1 = float(input('inserta la Densidad1 en Kg/M: '))
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)
            if(pregunta3 == 'Agua natural'):
                Densidad1 = densidad_agua
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)
            if(pregunta3 == 'Agua salada'):
                Densidad1 = densidad_agua_salada
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)

        if(pregunta2 == 'Densidad'):
            Presion_total_abajo = float(input('inserta la Presion total hacia abajo en Kilo pascales: '))     
            Altura1 = float(input('inserta la Altura1 en metros: '))
            Densidad1 = Presion_en_un_fluido/gravedad*Altura1-presion_atmosferica            
            return(Densidad1)
        
        if(pregunta2 == 'Altura'):
            Presion_total_hacia_abajo = float(input('inserta la Presion total hacia abajo en Kilo pascales: '))
            pregunta3= input('¿Tienes que calcular la Densidad o es Densidad de Agua natural o Densidad de agua salada? Si/No/Agua natural/Agua salada ')
            if(pregunta3 == 'Si'):
                Densidad1 = float(input('Inserta el valor de la densidad en Kg/m'))
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            if(pregunta3 == 'No'):
                Densidad1 = calculadora_Densidad()
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            if(pregunta3 == 'Agua natural'):
                Densidad1 = densidad_agua
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            if(pregunta3 == 'Agua salada'):
                Densidad1 = densidad_agua_salada
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
                

    #P1=Pa+densidad·gravedad·altura1    
    elif(pregunta1 == 'Presion total hacia abajo'):
        pregunta2 = input('¿Quieres calcular la Presion total hacia abajo, Densidad o Altura?: ')
        if(pregunta2 == 'Presion total hacia abajo'):
            pregunta3 = input('¿Tienes que calcular la densidad o es densidad de Agua natural, Agua salada? Si/No/Agua natural/Agua salada: ')                    
            if(pregunta3 == 'Si'):
                Densidad = calculadora_Densidad()
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)
            if(pregunta3 == 'No'):
                Densidad1 = float(input('inserta la Densidad1 en Kg/M: '))
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)
            if(pregunta3 == 'Agua natural'):
                Densidad1 = densidad_agua
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)
            if(pregunta3 == 'Agua salada'):
                Densidad1 = densidad_agua_salada
                Altura1 = float(input('inserta la Altura1 en metros: '))
                Presion_total_hacia_arriba = presion_atmosferica + Densidad*gravedad*Altura1
                return(Presion_total_hacia_arriba)

        if(pregunta2 == 'Densidad'):
            Presion_total_abajo = float(input('inserta la Presion total hacia abajo en Kilo pascales: '))     
            Altura1 = float(input('inserta la Altura1 en metros: '))
            Densidad1 = Presion_en_un_fluido/gravedad*Altura1-presion_atmosferica            
            return(Densidad1)
        
        if(pregunta2 == 'Altura'):
            Presion_total_hacia_abajo = float(input('inserta la Presion total hacia abajo en Kilo pascales: '))
            pregunta3= input('¿Tienes que calcular la Densidad o es Densidad de Agua natural o Densidad de agua salada? Si/No/Agua natural/Agua salada ')
            if(pregunta3 == 'Si'):
                Densidad1 = float(input('Inserta el valor de la densidad en Kg/m'))
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            if(pregunta3 == 'No'):
                Densidad1 = calculadora_Densidad()
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            if(pregunta3 == 'Agua natural'):
                Densidad1 = densidad_agua
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            if(pregunta3 == 'Agua salada'):
                Densidad1 = densidad_agua_salada
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
                
    
    #P2=Pa+densidad·gravedad·altura1
    elif(pregunta1 == 'Fuerza1'):
        
    #F1 = P1·A
    elif(pregunta1 == 'Fuerza2'):
    
    #F1 = P1·A
    elif(pregunta1 == 'Fuerza bollante'):
    
    #FB = P1·densidad·gravedad·Volumen
    if(pregunta3 == 'No'):
                Densidad1 = calculadora_Densidad
                Altura = Presion_total_hacia_abajo/gravedad
                Altura = Altura-presion_atmosferica-gravedad
                return(Altura)                             
            


    
def Peso_Masa():
    Peso= float(input('¿Cual es el peso?'))
    Masa= Peso/gravedad

def Volumen_poligono():
    Forma = input('¿Es un Prisma, Piramide, Cono, Cilindro?')
    if(Forma == 'Prisma'):
        Base = float(input('inserta el valor de la base ')) 
        Altura= float(input('inserta el valor de la altura '))
        Volumen_poligono = (Base*Altura)
    if(Forma == 'Piramide'):
        Base = float(input('inserta el valor de la base ')) 
        Altura= float(input('inserta el valor de la altura '))
        Volumen_piramide = Base*Altura/3
    if(Forma == 'Cono'):
        pregunta1= input('¿Tienes Radio o Diametro?')
        if(pregunta1 == 'Radio'):
            print('usaremos radio')
            Radio=float(input('inserta el Radio'))
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi/3*Radio**2*Altura
        
        elif(pregunta1 == 'Diametro'):
            print('usaremos diametro')
            Diametro=float(input('inserta el Diametro'))
            Diametro = Diametro/2
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi/3*Diametro**2*Altura

    if(Forma == 'Cilindro'):
        pregunta1= input('¿Tienes Radio o Diametro?')
        if(pregunta1 == 'Radio'):
            print('usaremos radio')
            Radio=float(input('inserta el Radio'))
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi*Radio**2*Altura
        
        elif(pregunta1 == 'Diametro'):
            print('usaremos diametro')
            Diametro=float(input('inserta el Diametro'))
            Diametro = Diametro/2
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi*Diametro**2*Altura

def calculadora_Densidad():
    print('esto podemos calcular')
    print('Densidad, Masa, Volumen')
    cal_valor = input('¿cual quieres calcular?')
    
    if(cal_valor == 'Densidad'):
        print('¿conoces el volumen o lo tienes que calcular?')
        respuesta= input('Si o No')
        if( respuesta == 'Si'):
            magnitud1 = float(input('inserta la masa'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
        if(respuesta == 'No'):
            respuesta2= input('¿tienes Area o Medidas?: ')
            if(respuesta2 == 'Area'):
                Volumen_poligono()
                print(Volumen_poligono + 'usalo en la ecuacion')
                magnitud1 = float(input('inserta la masa'))
                magnitud2 = float(input('inserta la Volumen'))

            if(respuesta2 == 'Medidas'):
                print('perdon estamos trabajando en ello')

    elif(cal_valor == 'Masa'):
        print('¿conoces el volumen o lo tienes que calcular?')
        respuesta= input('Si o No')
        if( respuesta == 'Si'):
            magnitud1 = float(input('inserta la masa'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
        if(respuesta == 'No'):
            respuesta2= input('¿tienes Area o Medidas?: ')
            if(respuesta2 == 'Area'):
                Volumen_poligono()
                print(Volumen_poligono + 'usalo en la ecuacion')
                magnitud1 = float(input('inserta la Densidad'))
                magnitud2 = float(input('inserta la Volumen'))
                print(magnitud1*magnitud2)
            if(respuesta2 == 'Medidas'):
                print('perdon estamos trabajando en ello')
   
    elif(cal_valor == 'Volumen'):
        print('¿conoces la Masa o el Peso?')
        respuesta= input('Masa o Peso')
        if(respuesta == 'Masa'):
            magnitud1 = float(input('inserta la Densidad'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
        if(respuesta == 'Peso'):
            Peso_Masa()
            print(Peso_Masa +'usa la Masa para calcular el Volumen')
            magnitud1 = float(input('inserta la Densidad'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)

def Longitud():

    print('esto es lo que podemos convertir')

    tipo_conversion1=input('¿que quieres converitir?')
    medida1=float(input('inserta la longitud que quieres convertir'))
    
    if(tipo_conversion1=='centimetros a pulgadas' or tipo_conversion1=='cm a in'):
        print(str(medida1*2.5)+' in')
    
    elif(tipo_conversion1 == 'pulgadas a centimetros' or tipo_conversion1=='in a cm'):
        print(str(medida1/2.5)+' cm')
    
    elif(tipo_conversion1 == 'metros a pies' or tipo_conversion1=='m a ft'):
        print(str(medida1*3.281) + ' ft')
    
    elif(tipo_conversion1 == 'pie a metros'or tipo_conversion1=='ft a m'):
        print(str(medida1/.3048) + ' m')
    
    elif(tipo_conversion1 == 'kilometros a millas' or tipo_conversion1=='Km a milles'):
        print(str(medida1*1.609) + 'milles')
    
    elif(tipo_conversion1 == 'metros a millas' or tipo_conversion1=='m a milles'):
        print(str(medida1*1609.344) + 'milles')

def Tiempo():
    print('esto es lo que podemos convertir')
    print('segundo a hora, hora a segundo, segundos en un dia, segundos en un año')
    tipo_conversion1=input('¿Que quieres convertir?')
    valor1= float(input('Cuanto '))
    if(tipo_conversion1 == 'segundo a hora' or tipo_conversion1=='S a H'):
        return(valor1*60)
    if(tipo_conversion1 == 'hora a segundo' or tipo_conversion1=='H a S'):
        return(valor1/60)
    if(tipo_conversion1 == 'segundos en un dia'):
        return(valor1*3600)
    if(tipo_conversion1 == 'segundos en un año'):
        return(valor1*3600*365)
        



while True:
    if(Operacion== 'Calcular densidad'):
        calculadora_Densidad()

    if(Operacion== 'Conversion de unidades'):
        print('Esto es lo que podemos convertir')
        print('Volumen','Area','Tiempo','Peso','Masa','Longitud','Velocidad','Fuerza','Potencia','Densidad', 'Energia','Presion')
        tipo_conversion= input('tipo de unidad ')

        if(tipo_conversion=='Longitud'):
            Longitud()

        elif(tipo_conversion=='Tiempo'):
            Tiempo()
        
        elif(tipo_conversion=='Area'):
            Area()
            