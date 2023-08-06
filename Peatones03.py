import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo UNI_CORR_500_01.txt y guardar las líneas en una lista llamada Crd
with open('UNI_CORR_500_01.txt', 'r') as UNI:
    Crd = [line[0:29].split() for line in UNI]

# Extraer las coordenadas X, Y, Z de la lista Crd y guardarlas en la lista Coordenadas
Coordenadas = [[float(ListAux[2]), float(ListAux[3]),
                float(ListAux[4])] for ListAux in Crd[4:]]

# Crear diccionarios para contar la frecuencia de las coordenadas X, Y, XY en las Coordenadas
frecuenciasX = {coord[0]: 0 for coord in Coordenadas}
frecuenciasY = {coord[1]: 0 for coord in Coordenadas}
frecuenciasXY = {tuple(coord[:2]): 0 for coord in Coordenadas}

# Contar la frecuencia de las coordenadas X, Y, XY y almacenarla en los diccionarios correspondientes
for coord in Coordenadas:
    frecuenciasX[coord[0]] += 1
    frecuenciasY[coord[1]] += 1
    frecuenciasXY[tuple(coord[:2])] += 1

# Calcular la coordenada X más repetida
max_frecuenciaX = max(frecuenciasX.values())
X_mas_repetida = [cordX for cordX,
                  freqX in frecuenciasX.items() if freqX == max_frecuenciaX]
print(
    f"La(s) coordenadas X que más se repiten: {X_mas_repetida} con un recuento de {max_frecuenciaX} veces")

# Calcular la coordenada Y más repetida
max_frecuenciaY = max(frecuenciasY.values())
Y_mas_repetida = [cordY for cordY,
                  freqY in frecuenciasY.items() if freqY == max_frecuenciaY]
print(
    f"La(s) coordenadas Y que más se repiten: {Y_mas_repetida} con un recuento de {max_frecuenciaY} veces")

# Calcular la coordenada XY más repetida
max_frecuenciaXY = max(frecuenciasXY.values())
XY_mas_repetida = [cordXY for cordXY,
                   freqXY in frecuenciasXY.items() if freqXY == max_frecuenciaXY]
print(
    f"La(s) coordenadas X,Y que más se repiten: {XY_mas_repetida} con un recuento de {max_frecuenciaXY} veces")

# Calcular las pendientes para convertir coordenadas de metro a pixel
Xm1, Xp1, Xm2, Xp2 = 0, 320, 9, 640
Ym1, Yp1, Ym2, Yp2 = 0, 480, 5, 0


def calcular_pendiente(ValorMetrico1, ValorPixel1, ValorMetrico2, ValorPixel2):
    m = (ValorPixel2 - ValorPixel1) / (ValorMetrico2 - ValorMetrico1)
    return m


Mx = calcular_pendiente(Xm1, Xp1, Xm2, Xp2)
My = calcular_pendiente(Ym1, Yp1, Ym2, Yp2)

# Función para convertir coordenadas de metro a pixel


def Conversion(CoordenadaMetro):
    Xmetro, Ymetro = CoordenadaMetro
    Xpixel = int(Mx * Xmetro + 320)
    Ypixel = int(My * Ymetro + 480)
    return Xpixel, Ypixel


# Crear una matriz de posiciones de 640x480 y un diccionario de posiciones
heatmap_data = np.zeros([640, 480])
FrecCoordPixel = {(ValorX, ValorY): 0 for ValorX in range(641)
                  for ValorY in range(481)}

# Convertir las coordenadas de metro a pixel y almacenar las frecuencias en el diccionario
for coord, frecuencia in frecuenciasXY.items():
    CoordenadaPixel = Conversion(coord)
    FrecCoordPixel[CoordenadaPixel] = frecuencia
    heatmap_data[CoordenadaPixel] = frecuencia

# Calcular la coordenada XY más repetida en PIXEL
max_frecuenciaPixelXY = max(FrecCoordPixel.values())
XYPixel_mas_repetida = [CordXY for CordXY, freqXY in FrecCoordPixel.items(
) if freqXY == max_frecuenciaPixelXY]
print(
    f"La(s) coordenadas X,Y que más se repiten en pixel: {XYPixel_mas_repetida} con un recuento de {max_frecuenciaPixelXY} veces")
