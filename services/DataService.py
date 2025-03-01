import repository.DataRepository as dataRepository

def saveData(data, tiempo):
    dataRepository.saveData(data, tiempo)
    print('Datos enviados a  repository')