import os

import numpy as np


class Genetic:

    def __init__(self, number_of_generations, df):
        self.number_of_generations = number_of_generations
        self.actual_dataFrame = df
        self.cursor = 1
        # df.to_csv('mask.csv', encoding='utf-8')
        if not os.path.isfile('filename.csv'):
            df.to_csv('mask.csv', header='column_names', sep=';', encoding='utf-8')  ####
        else:
            df.to_csv('mask.csv', mode='w', header=False, sep=';', encoding='utf-8')  ####

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    ###  Genetic Algorithm  ###
    ###########################
    def get_generation(self):
        mask_array_string = self.actual_dataFrame[self.actual_dataFrame.generation == self.cursor & self.actual_dataFrame.selection][
            'mask']
        arr = []

        for sub_array in mask_array_string:
            arr.append(self.string_to_matrix(sub_array))

        return arr

    # ------------------
    def get_actual_generation_index(self):
        return self.actual_dataFrame.index[
            self.actual_dataFrame.generation == self.cursor & self.actual_dataFrame.selection].tolist()

    # ------------------
    def crossing_over(self, A, B):
        new_gen = np.subtract(A, B)
        # new_gen = np.multiply(A, B)
        new_gen /= new_gen.sum(axis=1)[:, np.newaxis]  # normalize
        return np.round(new_gen, 2)

    # ------------------
    def generate_new_population(self):
        if self.number_of_generations == self.cursor:
            return False

        global same_dimension
        same_dimension = True
        get_gen = self.get_generation()
        for index_dis, gen_mask_dis in enumerate(get_gen):
            for index_ic in range(index_dis + 1, len(get_gen)):
                if gen_mask_dis.shape == get_gen[index_ic].shape:
                    same_dimension = True
                    new_gen = self.crossing_over(get_gen[index_ic], gen_mask_dis)
                    self.actual_dataFrame = self.actual_dataFrame.append({'mask': self.matrix_to_string(new_gen),
                                                                          'generation': self.cursor + 1,
                                                                          'match': 0, 'selection': True},
                                                                         ignore_index=True)

        if same_dimension:
            self.cursor += 1
            self.actual_dataFrame.to_csv('mask.csv', mode='w', header='column_names', sep=';', encoding='utf-8',
                                         index=True, index_label='id')  ####

        return same_dimension

    # ------------------
    def selection(self):
        matched = self.actual_dataFrame[self.actual_dataFrame.generation == self.cursor & self.actual_dataFrame.selection]['match']
        if matched.mean() < 5:
            return False
        else:
            self.actual_dataFrame.loc[self.actual_dataFrame['match'] < matched.mean(), "selection"] = False
            self.actual_dataFrame.to_csv('mask.csv', mode='w', header='column_names', sep=';', encoding='utf-8',
                      index=True, index_label='id')  ####

            return True

    #### Matrix Operations ###
    def string_to_matrix(self, str_):
        if str_.count(',') == 8:
            return np.array(list(map(float, str_.split(',')))).reshape(3, 3)

        elif str_.count(',') == 24:
            return np.array(list(map(float, str_.split(',')))).reshape(5, 5)

        elif str_.count(',') == 48:
            return np.array(list(map(float, str_.split(',')))).reshape(7, 7)

    # ------------------
    def matrix_to_string(self, matrix):
        b = ''
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1] - 1):
                b += str(matrix[i, j]) + ','

        return b[:-1]
