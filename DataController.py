import serial
import time
import datetime
import services.DataService as dataService

# Clase para simular el puerto serial
class SerialSimulado:
    def __init__(self,puerto, baudrate):
        self.puerto = puerto
        self.baudrate = baudrate
        self.in_waiting = 1
        self.buffer = []

    def write(self, data):
        print(data)

    def readline(self):
        time.sleep(1)
        if not self.buffer:
            self.buffer = [
            "1.1;2.2;3.3;4.4",
            "5.5;6.6;7.7;8.8",
            "9.9;10.1;11.2;12.3",
            "13.4;14.5;15.6;16.7",
            "17.8;18.9;19.0;20.1"
        ]
        return self.buffer.pop(0).encode('utf-8')
    def close(self):
        print('Puerto cerrado')


#puerto = 'COM3'

#baudrate = 9600
def getData():
    try:
        #ser = serial.Serial(puerto, baudrate)
        ser = SerialSimulado('COM3', 9600)
        print('Conectado')

        #tokens = []

        while True:
            if ser.in_waiting > 0:
                ##dataService.saveData(ser.readline().decode('utf-8').rstrip())
                tiempo = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                ##tokens = ser.readline().decode('utf-8').rstrip().split(';')
                # Se envia los datos a la DB test
                tokens1 = ser.readline().decode('utf-8').rstrip()
                if tokens1:
                    dataService.saveData(tokens1,tiempo)
                    
                print('-------------------')
                print(tiempo)
                ##for campo in tokens:
                print(tokens1)
                print('-------------------')
    except serial.SerialException:
        print('Error al conectar a ')

    except KeyboardInterrupt:
        print('Desconectando de ')

    finally:
        if 'ser' in locals():
            ser.close()
            print('Desconectado')

def loadData():