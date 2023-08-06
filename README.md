![Logo UCN](images/60x60-ucn-negro.png)
# Laboratorio 01: Cálculo de frecuencia peatonal 
Fernanda Adones Aranda

Escuela de Ingeniería, UCN, Coquimbo, RUT F.Adones: 20.798.199-0, Chile

Email: Fernanda.adones@alumnos.ucn.cl

## 1. Introducción 
Con el propósito de determinar los patrones de movilización de un gran número de personas en un espacio reducido, se procesa la información contenida en el archivo de texto: “ UNI_CORR_500_01”. 
Este archivo que contiene las coordenadas en que los distintos usuarios identificados como PersId  se mueven a través de los ejes X,Y y Z permitirá determinar información relevante como las rutas más transitadas,  calcular estadísticos importantes para el estudio de estos datos , además de generar gráficos que permitan visualizar los resultados obtenidos.

### 1.1 Justificación 

El presente laboratorio representa una oportunidad para abordar problemas reales y complejos respecto a la congestión que se genera en espacios reducidos y altamente transitados, tal como ocurre en el metro.
 Mediante el análisis de datos, se pueden examinar la movilidad, comprender las dinámicas de congestión y los puntos críticos de un sistema lo que fortalece los conocimientos y habilidades en el análisis y diseño de soluciones  a partir de las herramientas que entrega la ciencia de datos. 


### 1.2 Objetivos 

**Objetivo General**

Desarrollar un código en Python que analice el archivo "UNI_CORR_500_01.txt" para determinar y visualizar los espacios más congestionados.

**Objetivos específicos**

1.	Identificar las coordenadas X, Y y XY más frecuentes.
2.	Transformar las coordenadas de metro a píxeles.
3.	Identificar los espacios más congestionados basados en la frecuencia de las coordenadas.
4.	Realizar un análisis y visualización de los resultados obtenidos.


## 2. Marco teórico
Para el desarrollo del presente laboratorio, se hace uso del entorno de desarrollo Visual Studio Code con sus funciones de autocompletado y resaltado de sintaxis, junto con el lenguaje de programación Python. 

El uso de Python en Visual Studio permite  escribir y comprender el código de manera más eficiente  además de ofrecer herramientas  adicionales como : autocompletado de código, resaltado de sintaxis y depuración avanzada, lo que agiliza el proceso de desarrollo y mejora la productividad en el laboratorio.

Además, se emplean las bibliotecas numpy y matplotlib, que permiten realizar operaciones matemáticas y representar gráficamente los resultados. Estas herramientas se vuelven esenciales para calcular la varianza de las variables X, Y y Z, así como para identificar las coordenadas X, Y y XY más y menos frecuentes.


## 3. Materiales y métodos
Este estudio utiliza un archivo de texto llamado "UNI_CORR_500_01.txt" que contiene 25540 líneas de datos, pero el código utiliza solo 25536 líneas. Cada línea del archivo representa una persona y contiene su ID , “Frame” que indica el tiempo en segundos y sus coordenadas X, Y y Z. Los datos de ID son valores enteros (int), mientras que la columna Frame y las coordenadas X, Y y Z son valores decimales (float).

Cada línea del archivo se almacena en una lista llamada "Crd", y cada línea se divide en palabras y se guarda en sublistas. Estas sublistas representan las coordenadas X, Y y Z encontradas en el archivo.

Posteriormente, se crea una nueva lista llamada "Coordenadas", donde se almacenan las coordenadas X, Y y Z extraídas de "Crd" como valores numéricos flotantes.
El programa continúa creando tres diccionarios: "frecuenciasX", "frecuenciasY" y "frecuenciasXY". Estos diccionarios se utilizan para contar la frecuencia de las coordenadas X, Y y las combinaciones XY, respectivamente, presentes en la lista "Coordenadas". Se recorren las coordenadas una por una, incrementando las frecuencias correspondientes en los diccionarios.

A continuación, se buscan las coordenadas X e Y más repetidas a partir de las frecuencias almacenadas en los diccionarios. Se encuentran las frecuencias máximas de "frecuenciasX" y "frecuenciasY", y se identifican las coordenadas que tienen estas frecuencias máximas.
También se realizan cálculos para obtener las pendientes (necesarias para convertir coordenadas de metro a píxeles). Luego, se define una función llamada "Conversion" que toma coordenadas métricas como entrada y las convierte en coordenadas de píxel utilizando las pendientes previamente calculadas.

A continuación, se crea una matriz llamada "Matriz640x480" de tamaño 640x480, y un diccionario "FrecCoordPixel" para almacenar las frecuencias de las coordenadas X, Y en formato de píxeles.

Finalmente, se convierten las coordenadas XY que tienen la frecuencia máxima (obtenidas de "frecuenciasXY") en píxeles utilizando la función "Conversion". Estas coordenadas XY en píxeles se almacenan en el diccionario "FrecCoordPixel". Posteriormente, se encuentra la frecuencia máxima en "FrecCoordPixel" y se identifican las coordenadas XY correspondientes a esta frecuencia máxima. 

Los resultados se muestran en la salida estándar, mostrando las coordenadas X e Y que se repiten más frecuentemente en píxeles y su respectivo recuento de ocurrencias


## 4. Resultados obtenidos

En base a los resultados obtenidos del análisis del archivo "UNI_CORR_500_01" que contiene información sobre la ubicación de peatones en un espacio determinado de  5 metros de ancho y 18 metros de largo, se puede observar que se han identificado coordenadas específicas que se repiten con mayor frecuencia.

En primer lugar, las coordenadas X que más se repiten son [0.3181, 1.8166, 4.5432, -3.3463, -4.3735, 0.2158, -1.5014 y -4.1982], y cada una de ellas aparece 4 veces en el conjunto de datos.

En segundo lugar, se han identificado las coordenadas Y que tienen una mayor frecuencia de repetición. Las coordenadas Y que más se repiten son [2.988, 2.1367, 3.4871, 3.2746 y 3.7182], y cada una de ellas se presenta en 6 ocasiones.
Además, se han encontrado combinaciones de coordenadas X e Y que se repiten en el conjunto de datos.

 Estas combinaciones son [(-2.2467, 2.937), (1.4351, 3.6758), (-1.5874, 2.9933), (1.3043, 4.1939), (3.9211, 3.0781), (4.3135, 3.5566), (0.789, 4.1471), (0.8567, 1.4212), (3.052, 1.6044), (2.2966, 3.725), (-1.1189, 4.2663), (1.4193, 1.2044), (4.1194, 3.0263), (-2.6423, 3.3633), (-4.8022, 1.4552) y (-2.4232, 1.0602)]. Cada una de estas combinaciones aparece 2 veces en el análisis.

Como se observa las coordenadas X e Y que se repetían más veces, sugieren áreas populares donde las personas pasaban más tiempo. En cuanto a las combinaciones de coordenadas X e Y que se repetían, estas podrían indicar lugares de mayor tráfico o congestión es interesante indicar que identificar estos puntos puede ayudar a tomar medidas para mejorar la circulación y evitar posibles situaciones de aglomeración o riesgo.

 Además, al analizar las coordenadas a lo largo del tiempo (representado por la columna "Frame") se detectaron los patrones de movimiento a lo largo del tiempo, estos nos sirven para identificar momentos de mayor afluencia y patrones de movimiento de las personas.
Si extrapolamos esto a el caso de un metro, estos resultados podrían ser valiosos para mejorar la planificación y gestión del transporte público. Podrían rediseñarse áreas para facilitar la circulación de las personas, implementarse sistemas de control de afluencia en puntos críticos y ajustarse los horarios y capacidades de los trenes para adaptarse a las horas de mayor demanda. 
Todo esto contribuiría a un mejor flujo de personas, una experiencia más segura y cómoda para los usuarios y un servicio de transporte más eficiente en general.
Finalmente es importante mencionar que el programa tomó aproximadamente 2.949 segundos para completar su ejecución. Este valor se utiliza para medir la eficiencia y velocidad de un programa.



## 5. Conclusiones

El análisis de datos permitió determinar las frecuencias en el patrón de movimiento de las personas, pero no se pudo realizar la matriz de calor debido a la falta de algunos estadísticos. La matriz de calor es una representación gráfica que muestra la distribución de datos en forma de colores en una matriz bidimensional, y su creación requeriría considerar todas las combinaciones de variables.

Los resultados destacan que ciertas coordenadas X e Y se repiten con mayor frecuencia, indicando áreas más transitadas. También se identificaron combinaciones específicas de coordenadas X e Y con alta frecuencia, lo que podría señalar puntos críticos de congestión en el espacio analizado.

Aunque la matriz de calor no pudo ser generada en esta instancia, su creación puede ser considerada en futuras investigaciones para lograr una visualización más completa de la distribución de datos y mejorar el cumplimiento de los objetivos del laboratorio.





