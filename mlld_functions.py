import numpy as np

"""
:param MLLD_functions: this class has several functions that are usually used by myself.
"""

class MLLD_functions:

    def standardization(self, variable):
        """
        :param variable: the array with the variables you wish to standardize
        :return: standardized array
        """
        var_average = np.average(variable)
        var_std     = np.std(variable)
        new_variable = []
        for i in range(variable.size):
            new_variable_i = (variable[i] - var_average)/var_std
            new_variable.append(new_variable_i)
        self.new_variable = np.array(new_variable)
        return self.new_variable
