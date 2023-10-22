import numpy as np
import vec_and_mat
import math
import matplotlib.pyplot as plt


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
    vector = (np.linalg.norm(vector)) ** 2
    up = (np.linalg.norm(pos)) ** 2
    resp = up / vector
    return np.round(resp, 2)


def amp_transit(vector1, vector2):
    """ Halla la probabilidad de transitar
    del primer vector al segundo.
    (list2D,list2D) -> float
    """
    vector1 = norma(vector1)
    vector2 = norma(vector2)
    bra = np.conjugate(np.transpose(vector2))
    resp = np.dot(bra, vector1)
    proba = np.linalg.norm(resp) ** 2
    return np.round(resp, 2), np.round(proba, 2)


def hermitiana(matriz, vector):
    """verifica si una matriz es hermitiana,
    si lo es calcula la media y la varianza.
    (list2D, list) -> float, float
    """
    if vec_and_mat.matriz_herm(matriz):
        ba = vec_and_mat.adjunta(vec_and_mat.accion_mv(matriz, vector))
        media = np.dot(ba, vector)
        l = vec_and_mat.esc_matco(np.identity(len(matriz)), media)
        p = vec_and_mat.resta_m(matriz, l)
        z = vec_and_mat.prod_cmat(p, p)
        varianza = 0
        for i in range(len(vector)):
            varianza += (vector[i] ** 2) * z[i][i]

        return media, varianza

    print("su matriz no es hermitiana")


def tran_prob(matriz):
    """Calcula los valores propios
    y la probabilidad de transitar a
    alguno de los vectores
    (list2D) -> float, float
    """
    val, vec = vec_and_mat.val_and_vec(matriz)
    _, r = amp_transit(vec[0], vec[1])
    print("posibilidad de transitar: ", r)

    return val, vec


# problema 4.3.1
r = amp_transit([1, 0], [0, 1])
print(r)
r = tran_prob([[1, 0], [0, -1]])


# problema 4.3.2
def grafica(estado=None):
    """devuelve una grafica que muestra las
    probabilidades de un vector de estados
    (list2D) -> graphic
    """
    if estado is None:
        estado = [0, 0]
    fig, ax = plt.subplots()
    caso = []
    for i in range(len(estado)):
        caso.append(i)

    ax.bar(caso, estado, )
    ax.set_ylabel("valores")
    ax.set_title("PROBABILIDAD")
    plt.show()


grafica()

# problema 4.4.1
def matriz_u(matriz):
    """verifica si una  matriz
    es matriz unitaria
    (list2D) -> Bool"""
    
    matriz1 = np.array(matriz)
    matriz_p = vec_and_mat.prod_cmat(vec_and_mat.adjunta(matriz1), matriz1)
    matriz_i = np.identity(len(matriz_p))

    if np.allclose(matriz_p, matriz_i, rtol=0.5, atol=0.5):
        return True
    else:
        return False


a = [[0, 1], [1, 0]]
b = [[math.sqrt(2)/2, math.sqrt(2)/2], [math.sqrt(2)/2, math.sqrt(2)/-2]]
s = matriz_u(a)
d = matriz_u(b)
print(s,d)

if s is True and d is True:
    mulp = vec_and_mat.prod_cmat(a,b)
    print(matriz_u(mulp))


# problema 4.4.2
def cuantico(inicialstate=None, dinamica=None,
             clicks=3):
    """Simula un sistema cuantico
    (list2D, list, int) -> list
    """
    if dinamica is None:
        dinamica = [[0, 1 / math.sqrt(2), 1 / math.sqrt(2), 0], [0 + 1j / math.sqrt(2), 0, 0, 1 / math.sqrt(2)],
                    [1 / math.sqrt(2), 0, 0, 0 + 1j / math.sqrt(2)], [0, 1 / math.sqrt(2), -1 / math.sqrt(2), 0]]
    if inicialstate is None:
        inicialstate = [1, 0, 0, 0]
    dinamica = np.linalg.matrix_power(dinamica, clicks)
    final_state = vec_and_mat.accion_mv(dinamica, inicialstate)

    return final_state


print(cuantico())  # La probabilidad es cero

val, vec = tran_prob([[1,0],[1,0]])

print(amp_transit([1, 0-1j],[0+1j,1]))
a, b = hermitiana([[1+0j, 0-1j],[0+1j, 2+0j]],[math.sqrt(2)/2, 0+1j * math.sqrt(2)/2])
print("media = ",a, "varianza =", b)
