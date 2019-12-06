import numpy as np


class Genetic:

    def __init__(self, number_of_generations, df):
        self.number_of_generations = number_of_generations
        self.actual_dataFrame = df
        self.cursor = 1
        df.to_csv('mask.csv', sep=';', encoding='utf-8')

    def get_generation(self):
        df = self.actual_dataFrame
        mask_array_string = df[df.generation == self.cursor & df.selection]['mask']
        arr = []

        for sub_array in mask_array_string:
            arr.append(self.string_to_matrix(sub_array))

        return arr

    def get_actual_generation_index(self):
        df = self.actual_dataFrame
        return df.index[df.generation == self.cursor & df.selection].tolist()

    def generate_new_population(self):
        self.cursor += 1
        ayni_boyut_varmi = False
        df = self.actual_dataFrame
        for index_dis, gen_mask_dis in enumerate(self.get_generation()):
            for index_ic, gen_mask_ic in enumerate(self.get_generation()):
                if index_ic == index_dis:
                    continue
                else:
                    if gen_mask_dis.shape == gen_mask_ic.shape:
                        ayni_boyut_varmi = True
                        new_gen = np.multiply(gen_mask_ic, gen_mask_dis)
                        new_gen /= new_gen.sum(axis=1)[:, np.newaxis]  # normalize
                        df = df.append({'mask': self.matrix_to_string(new_gen), 'generation': self.cursor,
                                        'match': 0, 'selection': True}, ignore_index=True)
        if ayni_boyut_varmi:
            df.to_csv('mask.csv', sep=';', encoding='utf-8')
        return ayni_boyut_varmi

    def selection(self):
        df = self.actual_dataFrame
        matched = df[df.generation == self.cursor & df.selection]['match']
        print(matched)
        if matched.mean() < 5:
            return False
        else:
            df.loc[df['match'] < matched.mean(), "selection"] = False
            df.to_csv('mask.csv', sep=';', encoding='utf-8')
            return False

    def string_to_matrix(self, str_):
        if str_.count(',') == 8:
            return np.array(list(map(float, str_.split(',')))).reshape(3, 3)

        elif str_.count(',') == 24:
            return np.array(list(map(float, str_.split(',')))).reshape(5, 5)

        elif str_.count(',') == 48:
            return np.array(list(map(float, str_.split(',')))).reshape(7, 7)

    def matrix_to_string(self, matrix):
        b = ''
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1] - 1):
                b += str(matrix[i, j]) + ','

        return b[:-1]
