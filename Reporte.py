''' Alfredo Halam Abascal Alonso'''

import pandas as pd
import matplotlib.pyplot as plt

# Crea una clase que permita obtener información estadística y gráfica de un
# conjunto de datos de las máquinas de clima en cierto periodo de tiempo

class report:
    def __init__(self, path, extension='pkl', del_tests=True):
        self.path = path # El path del archivo que contiene los datos
        self.del_tests = del_tests
        # De pendiendo de la extensión del archivo, se ejecuta una función diferente para leerlos
        if extension == 'pkl':
            self.data = pd.read_pickle(path)
        elif extension == 'txt':
            self.data = pd.read_csv(path, sep='\t', engine='python')
        elif extension == 'xlsx':
            self.data = pd.read_excel(path)
            
        # Creando una columna con la fecha y la hora de la prueba
        date = self.data['Fecha'] + ' ' + self.data['Hora']
        date = pd.to_datetime(date, format='%d.%m.%Y %H:%M:%S')
        # Dataframe solo con Denominación para tipo nombre de máquinas, codigo de error,
        # nombre del error y la fecha completa
        self.data = self.data[['Denominación para tipo','ProcessName', 'ProcessResult', 'Evaluaciones']]
        self.data.insert(loc=0, column='Date', value=date) # Añadiendo la fecha completa
        self.data.reset_index(inplace=True) # Reiniciando el index
        self.data.drop(columns='index', inplace=True) 
        self.data.set_index('Date', inplace=True) # Haciendo fechas de pruebas el index
        # Removiendo pruebas Test###
        if self.del_tests:
            test = self.data['Denominación para tipo'].str.contains('Test') # Filtro de pruebas Test
            self.data = self.data.loc[~test] # Eliminando las pruebas Test

    def datos_generales(self):
        return

    def gen_summary(self, time='all'):
        '''
        Crea un reporte general de los datos contenidos en el archivo que incluye
        número total de pruebas, cantidad de pruebas OK y NO_OK, errores más frecuentes,
        de las 3 máquinas por separado y en conjunto.
        time: str. Una string con formato datetime indicando los días del inicio y fin del reporte
        ('2019-08-04 2019-30-04'). Si es 'all', se hace el reporte con todos los datos del archivo.

        '''
        # Número de pruebas
        # Pruebas Ok y No OK
        # Errores más frecuentes






# Test
path = r'C:\Users\alfre\Documents\TT\Modelos\clima_months.pkl'
report = report(path) # Creando clase
print(report.data.head())