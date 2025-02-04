from abc import ABC, abstractmethod
from time import time

class Comparator:
    @staticmethod
    @abstractmethod
    def compare():
        pass

class Algorithm_Comparator(Comparator):
    @staticmethod
    def compare(algorithm_class, inputs):
        methods = [method for method in dir(algorithm_class) 
                   if callable(getattr(algorithm_class, method))
                   and not method.startswith("__")]
        
        results = dict()
        
        for method in methods:
            method_result = []
            for input in inputs:
                start = time()
                getattr(algorithm_class, method)(input)
                end = time()
                method_result.append((end - start) * 1000)
            results.update({method : method_result})
        
        print(results)
        return results

                
