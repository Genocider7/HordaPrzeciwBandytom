from numpy import mean
from random import choice

class Gosc:
    def __init__(self, machine_count):
        self.machine_results = {}
        self.results = []
        self.tried_machines = 0
        for i in range(machine_count):
            self.machine_results[i] = []

    def receive_result(self, result, machine):
        self.results.append(result)
        self.machine_results[machine].append(result)

    def get_mean(self):
        return mean(self.results)
    
    def get_mean_from_machine(self, machine):
        return mean(self.machine_results[machine])
    
    def choose_machine(self):
        if self.tried_machines < len(self.machine_results):
            self.tried_machines += 1
            return self.tried_machines - 1
        else:
            global_mean = self.get_mean()
            machine_numbers = [machine for machine in self.machine_results.keys() if self.get_mean_from_machine(machine) >= global_mean]
            return choice(machine_numbers)
    
    def get_favorite_machine(self):
        biggest = 0
        favorite = -1
        for key, val in self.machine_results.items():
            if len(val) > biggest:
                biggest = len(val)
                favorite = key
        return favorite