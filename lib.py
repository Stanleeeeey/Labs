import numpy as np
import math

GRAVITY = 9.8115

def ua(values:np.array):

    length = len(values)
    mean   = np.mean(values)

    return np.sqrt(sum([(i - mean)**2 for i in values]) / (length*(length - 1)))



def ub(accuracy: np.float64, reaction_time: np.float64 = 0.0):
    return np.sqrt(accuracy**2 / 3 + reaction_time**2 / 3)

def get_maximums(values: np.array, accuracy: np.float64,  reaction_time: np.float64 = 0.0):

    
    uc =  np.sqrt(ua(values)**2 + ub(accuracy, reaction_time)**2)
    
    mean   = np.mean(values)

    return mean-uc, mean+uc





