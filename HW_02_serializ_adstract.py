from abc import ABCMeta, abstractmethod
import json
import pickle

class SerializationInterface(metaclass=ABCMeta):
     @abstractmethod
     def restore(self, file_name):
        pass

     @abstractmethod
     def save(self, file_name, data):
        pass

class JsonSerializ(SerializationInterface):
    def restore(self, file_name):
        with open(file_name, "rb+") as file:
            return json.load(file)
                
        
    def save(self, file_name, data):
        with open(file_name, "wb") as file:
            return json.dump(data, file) 
            
class BinSerializ(SerializationInterface):
    def restore(self, file_name):
        with open(file_name, "rb+") as file:
            return pickle.load(file)
                
        
    def save(self, file_name, data):
        with open(file_name, "wb") as file:
            return pickle.dump(data, file) 
            
some_data = {
    'flowers': '21', 
    2: [1, 2, 3], 
    'tuple': (5, 6), 
    'a': {'Englist': 'middle'}
    }


js = JsonSerializ()
bin = BinSerializ()

js.save(file_name='data3.json', data=some_data)
bin.save(file_name='data3.bin', data=some_data)


