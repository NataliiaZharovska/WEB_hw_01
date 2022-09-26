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
            json.load(file)
                
        
    def save(self, file_name, data):
        with open(file_name, "wb") as file:
            json.dump(data, file) 
            
class BinSerializ(SerializationInterface):
    def restore(self, file_name):
        with open(file_name, "rb+") as file:
            pickle.load(file)
                
        
    def save(self, file_name, data):
        with open(file_name, "wb") as file:
            pickle.dump(data, file,protocol=pickle.HIGHEST_PROTOCOL) 
            print("savwd")
            
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

a= js.restore(file_name='data3.json')
b= bin.restore(file_name='data3.bin')
