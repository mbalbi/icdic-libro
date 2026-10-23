---
jupytext:
  text_representation:
    format_name: myst
    extension: .md
kernelspec:
  name: python3
  display_name: Python 3
---

# Variables, poblaciones y datos

Los datos son mediciones (observaciones) de las variables. No son exactamente realizaciones de las variables ya que en la gran mayoría de los casos existe cierto error en la medición (por ejemplo, en la medición de la resistencia de los bulones).

## Tipos de variables

Las variables pueden ser clasificadas en _numéricas_ o _categóricas_. Dentro de las numéricas se encuentran las _continuas_, como la resistencia de los bulones o la velocidad del viento, y las _discretas_ como la cantidad de coches en la avenida. Por su parte las _categóricas_ son aquellas variables no-cuantificables que toman valores dentro de un conjunto fijo y finito de grupos (categorías o labels) posibles. Dentro de esta categoría se dividen en _nominales_, donde las categorías no tienen un orden ni una distancia entre ellas, como los colores o los nombres de las avenidas; y _ordinales_, donde las categorías tienen un orden jerárquico entre sí, como los grados de daño de las estructuras estimado de campañas en terreno.

```{figure} figuras/tipos_de_variables_tree.png
:scale: 25 %
:alt: Taxonomía de variables
:name: fig-tipos-variables

Taxonomía más utilizada para clasificar los tipos de variables según su dominio de definición.

```

Esta clasificación suele ser la más relevante ya que nos permite definir el tipo de modelo de inferencia estadística a utilizar.

Desde el punto de vista de la modelación probabilística, sin embargo, hay solo dos tipos de variables: continuas y discretas. Es decir, las variables categóricas, que no responden a valores numéricos son caracterizadas como una variable aleatoria discreta simplemente asignando valores numéricos a cada una de las categorías. Para los _ordinales_ en particular, el código numérico debe respetar el orden jerárquico y las distancias previstas entre las categorías.

Otra clasificación común para las variables desde el punto de vista de la estadística es entre _variables de respuesta_ y _variables explicativas_. Esta clasificación es completamente independiente de la naturaleza matemática de la variable, y hace solo referencia al lugar que ocupa dentro del problema específico en cuestión. Se denomina "variable de respuesta" a aquella que se tiene como objetivo inferir para poder dar respuesta a la pregunta en cuestión. Por ejemplo, en el ejemplo de la agencia de tránsito, el volumen de autos es la variable de respuesta del problema ya que es la que nos interesa inferir para poder responder la pregunta. Por otro lado, las _variables predictoras_ son aquellas que se asumen como "dadas" (es decir, medidas) al responder la pregunta en cuestión. En ese mismo ejemplo, el ancho de calzada y la densidad poblacional aparecen como _variables predictoras_ ya que queremos saber el volumen de tráfico para unos valores dados de ancho y densidad. En este sentido, no nos interesa conocer la distribución de probabilidad poblacional de las _variables predictoras_ (más allá de que tengan una) porque, para nuestro problema específico van a ser "medidas" o "dadas".

Esta clasificación es central en los problemas de regresión y clasificación de variables (también denominado problemas de "aprendizaje supervisado"), donde nos interesa conocer la distribución de probabilidad de la (o las) _variable de respuesta_ para distintos valores fijos ("dados") de las _variables predictoras_.


## Tipos de datos

Tipos de mediciones: ratio, limite, discreta, etc.

Una muestra puede estar compuesta por mediciones correspondientes a una sola variable (univariada), o a muchas variables (multivariada). Por su parte, a las observaciones de una variable que varía en el tiempo se las denomina _serie de tiempo_, mientras que a observaciones de una variable que varía en el espacio se las suele denominar _mapas_.

En general, una muestra _estática_ aparece como un conjunto de valores (numéricos o no numéricos) sin un orden en particular, ya que se considera que el valor de cada observación es independiente del valor de las otras.

Datos estructurados versus no-estructurados.

### Tablas



### Series temporales

En una serie temporal o espacial (o tempo-espacial), sin embargo, los datos tienen un orden, una posición, dada por un índice asociado a la dimensión _tiempo_ o _espacio_. Los datos deben, si o si, interpretarse respetando este ordenamiento dado por el proceso de recolección.

### Datos espaciales

Los datos espaciales tienen distintas maneras de estar estructurados ya que no hay un orden lineal natural como en el caso del tiempo (siempre fluye de pasado a futuro en esa única dirección). Esto hace que la estructura de los datos espaciales pueda tomar distintas formas que podemos encasillar en dos tipos:

1. Grillas uniformes (mapas de bits): El orden viene dado por la contiguidad espacial de las celdas que se distribuyen de manera uniforme en todas las direcciones.
2. Grillas no uniformes (mapas de vectores): El orden viene dado por la contiguidad espacial, aunque ahora las unidades (celdas) no tienen un ordenamiento uniforme, ni una misma cantidad de vecinos en las distintas direcciones.
3. Redes (mapas de vectores): cada dato tiene una ubicación espacial aunque ahora el orden y "cecanía" entre los datos está definido a través de conectores que definen la red.

Los datos espaciales puede, además, tener una ubicación geográfica (geolocalizada).

## Recolectando datos

Los datos pueden venir de diferentes fuentes: mediciones de sensores, eventos, textos, imágenes y videos. Esta información la podemos encontrar de manera estructurada y lista para el análisis, o puede aparecer de manera no-estructurada como en el caso de la recolección de imágenes.

Existen básicamente dos maneras de obtener datos:

1. **Ensayos experimentales**: consiste en desarrollar un entorno controlado (en laboratorio o in-situ) en el cual se supone que se controlan ciertas variables (tratamientos) para ver su impacto en otras de interés (variables de respuesta). Es el caso del ensayo de los bulones, donde tenemos que agarrar cada bulón y someterlo a distintas fuerzas controladas hasta llevarlo a la falla.
2. **Ensayos observacionales**: consiste en medir las variables de interés pero sin intentar modificar (hasta donde sea posible) los procesos en estudio. Por ejemplo, en el caso de las observaciones de las velocidades de viento, o en el caso de la cantidad de autos que circulan por una avenida. Es la manera más sencilla de obtener mediciones, y con la que se obtienen la inmensa mayoría de datos de los que disponemos en ingeniería civil.


## Almacenando y leyendo los datos

Archivos de texto

Mapas de bits

Archivos de vectores


### Cómo los almacenamos y procesamos? 

bases de datos

Lenguajes de programación


