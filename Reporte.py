''' Alfredo Halam Abascal Alonso'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    def plots(self):
        climas = self.data.loc[self.data['ProcessResult'] != 0]
        clima1 = climas.loc[(climas['ProcessName'] == 'Clima TWIN 1')]
        clima2 = climas.loc[(climas['ProcessName'] == 'Clima TWIN 2')]
        climabk = climas.loc[(climas['ProcessName'] == 'Clima TWIN Backup')]
        climas_h = []
        clima1_h = []
        clima2_h = []
        climabk_h = []
        climas_d = []
        clima1_d = []
        clima2_d = []
        climabk_d = []
        pruebas= [climas, clima1, clima2, climabk]
        pruebas_h = [climas_h, clima1_h, clima2_h, climabk_h]
        pruebas_d = [climas_d, clima1_d, clima2_d, climabk_d]
        for prueba in range(len(pruebas)):
            for hour in range(24):
                if hour in pruebas[prueba].index.hour.value_counts():
                    pruebas_h[prueba].append(pruebas[prueba].index.hour.value_counts()[hour])
                else:
                    pruebas_h[prueba].append(0)
            for day in range(7):
                if day in pruebas[prueba].index.dayofweek.value_counts():
                    pruebas_d[prueba].append(pruebas[prueba].index.dayofweek.value_counts()[day])
                else:
                    pruebas_d[prueba].append(0)
                
        #Esto es para los últimos gráficos
        b_climabk_h = np.add(clima1_h,clima2_h)
        b_climabk_d = np.add(clima1_d, clima2_d)
        days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        hours = list(range(24))
        fig, axs = plt.subplots(4, 2, figsize=(15, 15))
        fig.subplots_adjust(hspace=0.3)
        axs[1,0].set_title('Clima 1')
        axs[1,0].bar(hours, clima1_h)
        axs[1,0].set_xticks(hours)
        axs[1,1].set_title('Clima 1')
        axs[1,1].bar(days, clima1_d)
        axs[2,0].set_title('Clima 2')
        axs[2,0].bar(hours, clima2_h, color='darkorange')
        axs[2,0].set_xticks(hours)
        axs[2,1].set_title('Clima 2')
        axs[2,1].bar(days, clima2_d, color='darkorange')
        axs[3,0].set_title('Clima Backup')
        axs[3,0].bar(hours, climabk_h, color='forestgreen')
        axs[3,0].set_xticks(hours)
        axs[3,1].set_title('Clima Backup')
        axs[3,1].bar(days, climabk_d, color='forestgreen')
        axs[0,0].set_title('General')
        axs[0,0].bar(hours, clima1_h, label='Clima1')
        axs[0,0].bar(hours, clima2_h, bottom=clima1_h, label="Clima2")
        axs[0,0].bar(hours, climabk_h, bottom=b_climabk_h, label="Climabk")
        axs[0,0].set_xticks(hours)
        axs[0,1].set_title('General')
        axs[0,1].bar(days, clima1_d, label="Clima1")
        axs[0,1].bar(days, clima2_d, bottom=clima1_d, label="Clima2")
        axs[0,1].bar(days, climabk_d, bottom=b_climabk_d, label="Climabk")
        





# Test
path = r'C:\Users\alfre\Documents\TT\Modelos\clima_months.pkl'
report = report(path) # Creando clase
print(report.data.head())
report.plots()
