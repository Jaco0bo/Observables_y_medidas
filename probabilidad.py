import numpy as np
import vec_and_mat
import math


def norma(vector):
    """Normaliza un vector con
    dos cifras significativas
    (list2D) -> list2D
    """
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    vector = np.round(vector / norm, 2)
    return vector


def prob(vector, pos):
    """Calcula la probabilidad de encontrar
     a la particula del sistema en una
     posición en particular.
     (list2D, int) -> float
    """
    pos = vector[pos]
    vector = (np.linalg.norm(vector))**2
    up = (np.linalg.norm(pos))**2
    resp = up / vector
    return np.round(resp, 2)


def amp_transit(vector1 = [1, 0-1j], vector2=[0+1j,1]):
    """ Halla la probabilidad de transitar
    del primer vector al segundo.
    (list2D.list2D) -> float
    """
    vector1 = norma(vector1)
    vector2 = norma(vector2)
    bra = np.conjugate(np.transpose(vector2))
    resp = np.dot(bra, vector1)
    proba = np.linalg.norm(resp)**2
    return np.round(resp, 2), np.round(proba,2)


print(amp_transit(vector1 = [1, 0-1j], vector2=[0+1j,1]))