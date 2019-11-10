import numpy as np
import pandas as pd


class Genetic:

    def __init__(self, number_of_generations, df):
        self.number_of_generations = number_of_generations
        self.first_generation_DataFrame = df
        self.cursor = 1
        df.to_csv('mask.csv', sep=';', encoding='utf-8')

    def get_generation(self):
        df = self.first_generation_DataFrame
        mask_array_string = df[df.generation == self.cursor & df.selection]['mask']
        arr = []
        for sub_array in mask_array_string:
            arr.append(self.string_to_matrix(sub_array))

        return arr

    def generate_new_population(self):
        print()

    def selection(self):
        print()

    def string_to_matrix(self, str_):
        if str_.count(',') == 8:
            return np.array(list(map(float, str_.split(',')))).reshape(3, 3)
        elif str_.count(',') == 24:
            return np.array(list(map(float, str_.split(',')))).reshape(5, 5)
        
        elif str_.count(',') == 48:
            return np.array(list(map(float, str_.split(',')))).reshape(7, 7)
