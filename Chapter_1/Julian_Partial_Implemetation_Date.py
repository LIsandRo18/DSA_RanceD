#Implements a proleptic Gregorian calendar date as a Julian day number

class Date:
    #Crea una instancia del objeto para una especifica fecha Gregoriana
    def __init__(self, month, day, year):
        self._julianDay = 0
        #Evalua si la expresión es falsa
        assert self._isValidGregorian(month, day, year),"Fecha gregoriana invalida."

        #Para convertir una fecha gregoriana a Juliana, se usa la siguiente formaula T = (M - 14) / 12, donde 0 correspinde a Noviembre 24 de 4714 AC y todas las operaciones involucran una aritmétice entera
        #La ecuación T = (M - 14) / 12, auque correcta produce un reusltado ERRONEO en python debido a la implementación de la divisioón entera, la cual no es la misma a la definición matemática. Realiza redonde hacia arriba. Para corregirlo usar la libreria decimal y corregir el redondeo de Python por defecto.
        #Caso: Por definición el resultado de -11//12 = 0, pero python la calcula -11//12.0 = -1. Asi que se tiene que modificar la primera linea de la ecuación para producir la correcta fecha si el componente del mes es mayor que 2.
        tmp = 0
        if month < 3:
            tmp = -1

        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) \
                                      + (367 * (month - 2 - tmp * 12) // 12) \
                                      - (3 * ((year + 4900 + tmp) // 100) // 4)
    
    #Extrae la fecha Gregoriana apropiada
    def month(self):
        return (self._toGregorian())[0] #Retorna el día de la tupla (m,d,y)

    def day(self):
        return (self._toGregorian())[1] #Retorna el día de la tupla (m,d,y)
        
    def year(self):
        return (self._toGregorian())[2] #Retorna el año de la tupla (m,d,y)
    
    #Comprueba si el la fecha ingresada es una fecha gregoriana
    def _isValidGregorian(month, day, year) -> bool:
        return 0

    #Retorna el día de la semana con un entero entre 0 (Lunes) y 6 (Domingo)
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1

            return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7
    def __str__(self) -> str:
       month, day, year = self._toGregorian() 
       
       return "%02d/%02d/%04d" % (month, day, year)

    #Comparación lógica de dos fechas
    def __eq__(self, otherDate) -> bool:
        return self._julianDay == otherDate._julianDay
       
    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    #Retorna la fecha gregoriana como una tupla
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        
        return month, day, year