from numpy import mean, std
from random import choice

class Gosc:
    def __init__(self, machine_count, testing_pulls = 10):
        self.machine_results = {}
        self.results = []
        self.testing_pulls = testing_pulls
        for i in range(machine_count):
            self.machine_results[i] = []

    def receive_result(self, result, machine):
        self.results.append(result)
        self.machine_results[machine].append(result)

    def get_data(self):
        return mean(self.results), std(self.results)
    
    def get_data_from_machine(self, machine):
        return mean(self.machine_results[machine]), std(self.machine_results[machine])
    
    def choose_machine(self):
        if len(self.results) < self.testing_pulls:
            machine_numbers = list(self.machine_results.keys())
        else:
            machine_numbers = [machine for machine in self.machine_results.keys() if self.get_data_from_machine(machine)[0] >= self.get_data()[0]]
        return choice(machine_numbers)
    
    def get_favorite_machine(self):
        biggest = 0
        favorite = -1
        for key, val in self.machine_results.items():
            if len(val) > biggest:
                biggest = len(val)
                favorite = key
        return favorite