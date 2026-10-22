---
jupytext:
  text_representation:
    format_name: myst
    extension: .md
kernelspec:
  name: python3
  display_name: Python 3
---

# Variables y datos

En el capítulo anterior definimos los **datos** como observaciones de algún aspecto de la realidad y vimos que, en ciencia de datos, esas observaciones se utilizan para responder preguntas sobre una muestra o para realizar inferencias sobre una población más amplia. En este capítulo nos concentraremos en el paso anterior a cualquier análisis: **cómo pasamos de un fenómeno real a un conjunto de datos que pueda ser estudiado**.

Este proceso parece sencillo, pero involucra varias decisiones importantes. Debemos establecer cuál es la unidad sobre la que observamos, qué características nos interesa registrar, cómo las medimos, qué tipo de valores pueden tomar y cómo organizamos y almacenamos finalmente esas observaciones.

## 1. Unidades de observación, variables y datos

### 1.1. Unidad de observación

Antes de hablar de variables conviene identificar **sobre qué estamos observando o midiendo**. Llamaremos **unidad de observación** al elemento, evento, lugar o instante sobre el que registramos una o más variables.

La unidad de observación depende del problema que estamos estudiando. Por ejemplo:

- en el control de calidad de una fábrica, cada **bulón ensayado** puede ser una unidad de observación;
- en un estudio de resistencia del hormigón, cada **probeta** puede ser una unidad de observación;
- en una serie histórica de viento, cada **año** puede constituir una unidad si registramos la velocidad máxima anual;
- en un estudio de tránsito, cada **avenida** puede ser una unidad de observación;
- en una imagen satelital, cada **pixel** puede considerarse una unidad de observación;
- en un relevamiento post-sismo, cada **estructura inspeccionada** puede ser una unidad.

```{admonition} La unidad de observación depende de la pregunta
:class: tip

Un mismo objeto físico puede generar muchas unidades de observación diferentes.

Por ejemplo, si instrumentamos un puente y registramos aceleraciones cada milisegundo, el puente es el sistema físico de interés, pero cada combinación **sensor–instante de tiempo** puede constituir una observación dentro del conjunto de datos.
```

### 1.2. Variables, valores y datos

Una **variable** es una característica observable o medible de las unidades de una población que puede tomar distintos valores.

Por ejemplo:

- resistencia a tracción de un bulón;
- velocidad máxima anual del viento;
- volumen diario de tránsito;
- relación agua/cemento de una mezcla;
- tipología estructural;
- nivel de daño de una estructura;
- uso del suelo de un pixel.

El **valor** de una variable es el valor particular que esa característica toma para una unidad específica. Si la variable es la resistencia a tracción, por ejemplo, dos bulones distintos pueden tener valores de 430 MPa y 447 MPa.

Un **dato** es el valor que finalmente registramos para una variable en una unidad de observación concreta.

```{admonition} Tres conceptos diferentes
:class: tip

**Unidad de observación:** aquello sobre lo que registramos información.

**Variable:** la característica que queremos registrar.

**Dato:** el valor registrado de esa variable para una unidad particular.

Por ejemplo:

- unidad: un bulón;
- variable: resistencia a tracción;
- dato: 438 MPa.
```

``````{card} Los ejemplos de la introducción vistos como variables

````{grid}

```{grid-item-card} Bulones
**Unidad:** bulón

**Variable:** resistencia a tracción

**Dato:** resistencia obtenida en el ensayo
```

```{grid-item-card} Viento
**Unidad:** año

**Variable:** velocidad máxima anual

**Dato:** máximo registrado durante ese año
```

```{grid-item-card} Tránsito
**Unidad:** avenida

**Variables:** volumen de tránsito, ancho de calzada, densidad poblacional

**Datos:** valores registrados para cada avenida observada
```

````

``````

```{admonition} Imagen sugerida
:class: note

Agregar un esquema visual con varias unidades de observación y, sobre cada una, distintas variables.

Por ejemplo, varias avenidas como filas conceptuales y, para cada una, ancho, densidad poblacional y tránsito como características medidas.
```

## 2. Del fenómeno de interés al dato

Los datos no son una copia exacta de la realidad. Para obtenerlos debemos decidir **qué aspecto del fenómeno queremos representar** y utilizar algún mecanismo para observarlo o registrarlo.

En el caso más simple, existe una correspondencia bastante directa entre aquello que nos interesa y lo que medimos. Si queremos conocer la resistencia a compresión de una probeta de hormigón, podemos ensayarla en una prensa y registrar la tensión máxima alcanzada de acuerdo con un procedimiento definido.

En otros problemas, sin embargo, aquello que realmente interesa no puede observarse directamente y debe representarse mediante una variable medible.

Podemos pensar el proceso de manera esquemática como:

> **Fenómeno de interés → variable de interés → mecanismo de medición → dato**

Y, cuando el fenómeno no puede medirse directamente:

> **Fenómeno de interés → variable observable o proxy → mecanismo de medición → dato**

### 2.1. Error y ruido de medición

Todo mecanismo de medición es imperfecto. La lectura obtenida puede diferir del valor que intentamos medir debido a la resolución del instrumento, ruido electrónico, variaciones del procedimiento, condiciones ambientales u otras fuentes de error.

``````{card} Medición de desplazamientos en una estructura

````{grid}

```{grid-item}
Supongamos que queremos medir el desplazamiento de un punto de un puente sometido a una determinada carga. Aunque el desplazamiento real permaneciera prácticamente constante, mediciones repetidas realizadas por un sensor podrían producir valores ligeramente distintos.

En este caso, la variable de interés y la variable medida son esencialmente la misma —el desplazamiento—, pero el **mecanismo de medición introduce ruido**.
```

```{grid-item}
**[IMAGEN A AGREGAR]**

Sensor de desplazamiento o instrumentación estructural.
```

````

``````

Esta diferencia entre el valor que queremos observar y el dato registrado es una de las razones por las cuales, como discutimos en la introducción, las observaciones contienen variabilidad aleatoria.

### 2.2. Cuando lo que medimos no es exactamente lo que nos interesa

Existe otro problema diferente al ruido instrumental: muchas veces el **fenómeno de interés no es directamente observable**, por lo que debemos representarlo mediante una variable que sí podamos registrar.

Por ejemplo:

| Fenómeno de interés | Variable que puede observarse |
| --- | --- |
| Daño sufrido por una estructura durante un sismo | Deformación máxima, ancho de fisuras, clasificación visual de daño |
| Capacidad de carga de un suelo | Tensión alcanzada bajo un criterio de deformación |
| Nivel de congestión de una vía | Velocidad media, tiempo de viaje o volumen de tránsito |
| Estado de deterioro de un pavimento | Número, extensión o tipo de fisuras detectadas |
| Uso del suelo | Propiedades espectrales registradas por un sensor satelital |

La variable utilizada actúa entonces como una **representación observable** del fenómeno que realmente nos interesa estudiar. A este tipo de variable se la suele denominar **proxy** cuando se utiliza como sustituto de otra característica que no puede medirse directamente.

```{admonition} Ruido de medición y proxy no son lo mismo
:class: important

Un instrumento imperfecto puede introducir **ruido** aun cuando mida directamente la variable de interés.

Un **proxy**, en cambio, puede medirse con enorme precisión y aun así no representar perfectamente el fenómeno que queremos estudiar.

Por ejemplo, podríamos medir la deformación máxima de una estructura con un instrumento prácticamente perfecto, pero eso no implica que la deformación máxima sea una representación perfecta del concepto más amplio de "daño estructural".
```

``````{card} Imágenes satelitales y uso del suelo

````{grid}

```{grid-item}
En el ejemplo de planificación urbano-ambiental de la introducción, lo que interesa conocer es el **uso o cobertura del suelo** en una cuenca.

El satélite no observa directamente etiquetas como "bosque", "agua" o "área urbana". Sus sensores registran intensidades de radiación en diferentes bandas espectrales. Esos valores constituyen los datos a partir de los cuales posteriormente intentamos inferir las categorías de interés.
```

```{grid-item}
![clasificación de imágenes satelitales](figuras/imagen_satelital_LU.jpg)
```

````

``````

## 3. Tipos de variables

Desde el punto de vista de los valores que pueden tomar, las variables suelen clasificarse en **numéricas** y **categóricas**.

```{figure} figuras/tipos_de_variables_tree.png
:scale: 25 %
:alt: Taxonomía de variables
:name: fig-tipos-variables

Clasificación habitual de variables según el tipo de valores que pueden tomar.
```

### 3.1. Variables numéricas

Las **variables numéricas** toman valores que representan magnitudes y sobre los cuales las operaciones aritméticas tienen una interpretación sustantiva.

Pueden dividirse en **continuas** y **discretas**.

#### Variables continuas

Una variable continua puede, conceptualmente, tomar cualquier valor dentro de un intervalo.

Ejemplos de ingeniería civil incluyen:

- resistencia de un material;
- velocidad del viento;
- temperatura;
- desplazamiento de una estructura;
- nivel de agua;
- precipitación acumulada;
- densidad de una mezcla asfáltica.

```{admonition} Continua no significa "medida con infinitos decimales"
:class: note

Toda medición real tiene una resolución finita. Una velocidad registrada como 12.4 m/s sigue representando una variable conceptual continua aunque el instrumento solo reporte décimas.

La clasificación se refiere a la naturaleza de la variable, no a la precisión con la que fue almacenado el dato.
```

#### Variables discretas

Una variable numérica discreta toma valores separados, habitualmente asociados a conteos.

Ejemplos:

- número de vehículos que atraviesan una sección durante una hora;
- cantidad de fisuras detectadas en un tramo de pavimento;
- número de eventos de inundación registrados en un período;
- número de pisos de un edificio.

``````{card} Tránsito: variables continuas y discretas

En el ejemplo de la nueva avenida podemos registrar simultáneamente variables de distinta naturaleza:

- **volumen de vehículos por hora:** discreta si representa un conteo;
- **ancho de calzada:** continua;
- **densidad poblacional:** usualmente tratada como continua;
- **velocidad media:** continua.

Un mismo conjunto de datos puede contener diferentes tipos de variables.
``````

### 3.2. Variables categóricas

Las **variables categóricas** toman valores que representan grupos o categorías. Aunque estas categorías puedan almacenarse mediante números, esos números no necesariamente representan magnitudes.

Las variables categóricas suelen dividirse en **nominales** y **ordinales**.

#### Variables nominales

En una variable nominal las categorías son diferentes entre sí pero no poseen un orden natural.

Ejemplos:

- tipología estructural;
- tipo de suelo;
- material predominante;
- cuenca hidrográfica;
- tipo de uso del suelo;
- nombre o identificador de una estación de medición.

Asignar, por ejemplo, `1 = hormigón`, `2 = acero` y `3 = mampostería` no convierte a la tipología estructural en una magnitud numérica. Los números son simplemente códigos.

#### Variables ordinales

En una variable ordinal las categorías poseen un **orden natural**, pero las distancias entre categorías no están necesariamente definidas.

Por ejemplo, un relevamiento post-sismo puede clasificar el daño estructural como:

> sin daño < leve < moderado < severo < colapso

Sabemos que "severo" representa un nivel de daño mayor que "moderado", pero no podemos concluir que la diferencia entre ambos sea equivalente a la diferencia entre "leve" y "moderado".

``````{card} Evaluación de daño post-sismo

````{grid}

```{grid-item}
En el ejemplo de clasificación de daño discutido en la introducción, para cada estructura pueden registrarse variables como:

- tipología estructural: **categórica nominal**;
- material predominante: **categórica nominal**;
- nivel de daño observado: **categórica ordinal**;
- aceleración máxima del suelo: **numérica continua**;
- número de pisos: **numérica discreta**.

La clasificación de las variables condiciona las operaciones y métodos estadísticos que resultan adecuados.
```

```{grid-item}
![daño sísmico](figuras/dano_sismico.jpg)
```

````

``````

### 3.3. El tipo de variable y su rol en el problema son cosas diferentes

```{admonition} Variable de respuesta y variables explicativas
:class: note

Además de clasificarse por el tipo de valores que toman, las variables pueden cumplir distintos **roles dentro de un análisis**.

En muchos problemas existe una **variable de respuesta**, que representa aquello que queremos explicar o predecir, y una o más **variables explicativas o predictoras**, que aportan información para hacerlo.

En el ejemplo de tránsito:

- volumen de tráfico: variable de respuesta;
- ancho de calzada y densidad poblacional: variables explicativas.

Esta clasificación depende de la pregunta. Una misma variable puede funcionar como respuesta en un problema y como explicativa en otro.
```

## 4. De observaciones individuales a un conjunto de datos

Una vez definidas las unidades de observación y las variables que queremos registrar, las mediciones individuales deben organizarse en una estructura que permita analizarlas en conjunto. A esa colección organizada de observaciones la llamaremos **conjunto de datos** o *dataset*.

### 4.1. Datos tabulares

La estructura más habitual en estadística es una tabla en la que:

- cada **fila** representa una observación o unidad de observación;
- cada **columna** representa una variable;
- cada **celda** contiene el dato correspondiente a una variable y una observación.

Por ejemplo, el conjunto de datos utilizado para estudiar el tránsito de distintas avenidas podría tener la forma:

| avenida | ancho_m | densidad_poblacional | volumen_veh_h |
| --- | ---: | ---: | ---: |
| A | 14.0 | 8500 | 1240 |
| B | 21.5 | 12300 | 2180 |
| C | 10.5 | 6100 | 870 |

Aquí cada fila representa una avenida observada y las columnas contienen distintas variables medidas sobre ella.

```{admonition} Identificadores no son necesariamente variables de interés
:class: note

Una tabla suele contener columnas utilizadas para identificar de manera única las observaciones —por ejemplo `station_id`, `bridge_id` o `avenida`—.

Estas columnas son fundamentales para organizar y relacionar datos, aunque no necesariamente representan una variable que queramos modelar estadísticamente.
```

```{admonition} Imagen sugerida
:class: note

Agregar una figura que muestre una tabla señalando explícitamente:

**fila → observación**

**columna → variable**

**celda → dato**
```

### 4.2. Datos transversales

En un conjunto **transversal** (*cross-sectional*) observamos múltiples unidades diferentes, típicamente bajo un mismo contexto o período de referencia.

Ejemplos:

- resistencias de 50 probetas de una producción;
- características y tránsito de 200 avenidas;
- nivel de daño de edificios relevados después de un sismo;
- propiedades geotécnicas medidas en diferentes sondeos.

El ejemplo de las avenidas es esencialmente transversal: cada vía aporta una observación con varias variables.

### 4.3. Series temporales

En una **serie temporal** una misma variable —o conjunto de variables— se registra sucesivamente a lo largo del tiempo.

Ejemplos:

- velocidad del viento registrada cada 10 minutos;
- caudal diario de un río;
- desplazamiento de un puente registrado por sensores;
- volumen de tránsito horario en una autopista.

``````{card} Velocidad del viento

En la introducción utilizamos 40 años de observaciones de viento para razonar sobre posibles vientos futuros.

Si registramos, por ejemplo, la velocidad máxima de cada año, el conjunto puede representarse como una serie temporal:

| año | velocidad_max_m_s |
| ---: | ---: |
| 1986 | 31.2 |
| 1987 | 27.8 |
| 1988 | 34.1 |
| ... | ... |

En este caso el **tiempo** forma parte esencial de la estructura del conjunto de datos.
``````

### 4.4. Datos longitudinales o de panel

En los datos **longitudinales** observamos repetidamente las mismas unidades a través del tiempo.

Por ejemplo, podríamos medir:

- el desplazamiento de distintos puentes una vez por mes;
- el deterioro de distintos tramos de pavimento cada año;
- el tránsito en numerosas avenidas durante muchos días;
- asentamientos en varios puntos de una obra a lo largo de su construcción.

Una tabla de este tipo suele contener al menos un identificador de unidad y una variable temporal:

| puente_id | fecha | desplazamiento_mm |
| --- | --- | ---: |
| P01 | 2026-01-01 | 3.2 |
| P01 | 2026-02-01 | 3.6 |
| P02 | 2026-01-01 | 2.7 |

La combinación `puente_id + fecha` identifica cada observación.

### 4.5. Datos espaciales y espacio-temporales

Muchas aplicaciones de ingeniería civil incluyen información asociada a una localización.

Un conjunto espacial puede estar compuesto por:

- estaciones meteorológicas representadas como puntos;
- rutas o cursos de agua representados como líneas;
- parcelas, cuencas o jurisdicciones representadas como polígonos;
- imágenes o modelos de elevación representados mediante grillas o rasters.

Si además registramos cómo estas variables cambian en el tiempo, hablamos de datos **espacio-temporales**.

``````{card} Mapas de inundación

Un mapa raster de inundación puede representar el territorio mediante una grilla de celdas.

Para cada celda se registra una variable, por ejemplo:

- profundidad máxima de agua;
- velocidad de flujo;
- elevación;
- categoría de uso del suelo.

En este caso la posición espacial de cada dato es parte inseparable de su significado.
``````

```{admonition} Imagen sugerida
:class: note

Agregar una comparación visual entre:

1. tabla transversal;
2. serie temporal;
3. puntos/vector espacial;
4. raster.

La idea es mostrar que todos contienen observaciones y variables, pero organizadas de maneras diferentes.
```

## 5. ¿Cómo se obtienen los datos?

Los datos pueden generarse específicamente para responder una pregunta o pueden provenir de procesos de observación que ya existen. Conviene distinguir entre el **diseño de la obtención de datos** y el **instrumento o fuente** mediante el cual se registran.

### 5.1. Estudios experimentales y observacionales

#### Estudios experimentales

En un estudio experimental el investigador controla deliberadamente parte de las condiciones del sistema y puede modificar variables para estudiar su respuesta.

En general, los experimentos permiten:

- definir de antemano qué variables medir;
- elegir las condiciones bajo las cuales realizar las mediciones;
- manipular una o más variables;
- controlar, en diferente grado, otras condiciones relevantes;
- decidir cuántas observaciones realizar, sujeto a restricciones prácticas.

``````{card} Ensayos de hormigón

Para estudiar cómo influye la relación agua/cemento sobre la resistencia puede fabricarse una serie de mezclas bajo condiciones controladas, modificando deliberadamente la relación agua/cemento y ensayando luego probetas de cada mezcla.

En este caso las observaciones son producidas específicamente mediante un **experimento**.
``````

#### Estudios observacionales

En un estudio observacional los datos se registran a partir del proceso tal como ocurre, sin que el investigador controle o asigne deliberadamente las condiciones de interés.

Ejemplos:

- velocidades de viento registradas por una estación meteorológica;
- niveles de un río medidos durante décadas;
- tránsito observado en avenidas existentes;
- daño relevado después de un terremoto;
- imágenes satelitales de una región.

``````{card} Tránsito urbano

Para estudiar la relación entre densidad poblacional, ancho de calzada y volumen de tránsito, la agencia puede medir estas variables en avenidas existentes.

La agencia no asigna aleatoriamente densidades de población ni anchos de calzada: observa configuraciones que existen en la ciudad.

Este es un conjunto de datos **observacional**.
``````

```{admonition} Obtención de datos y causalidad
:class: note

La distinción entre estudios experimentales y observacionales será especialmente importante cuando estudiemos preguntas causales.

Observar una asociación entre variables en datos observacionales no alcanza, por sí solo, para concluir que modificar una de ellas causaría un cambio en la otra.
```

### 5.2. Instrumentos y fuentes de observación

Independientemente del diseño del estudio, los datos pueden provenir de mecanismos muy distintos.

#### Instrumentos construidos para medir una variable

Son dispositivos o procedimientos diseñados específicamente para registrar una magnitud:

- estaciones meteorológicas;
- acelerómetros;
- extensómetros;
- celdas de carga;
- piezómetros;
- equipos de laboratorio;
- aforos y estaciones hidrométricas.

La calidad de los datos depende, entre otras cosas, de la precisión, resolución, calibración, mantenimiento y procedimiento de uso del instrumento.

#### Sensores remotos y mediciones indirectas

Algunos fenómenos se observan a distancia o mediante señales relacionadas indirectamente con la variable de interés:

- imágenes satelitales;
- radar;
- LiDAR;
- fotografía aérea o mediante drones.

Estos sistemas pueden cubrir áreas enormes de manera repetida, pero normalmente requieren procesamiento antes de obtener la variable final de interés.

#### Relevamientos y registros humanos

Muchas variables se obtienen mediante observaciones realizadas por personas:

- inspecciones visuales de estructuras;
- inventarios de infraestructura;
- encuestas;
- relevamientos de daños;
- clasificación manual de imágenes.

Estos datos también dependen de un mecanismo de medición, aunque el "instrumento" incluya criterios de clasificación y juicio humano.

#### Datos secundarios

En muchos proyectos no realizamos nosotros mismos las mediciones sino que utilizamos datos previamente recolectados:

- organismos públicos;
- servicios meteorológicos;
- institutos geográficos;
- bases de datos de infraestructura;
- OpenStreetMap;
- repositorios científicos;
- datos de empresas o sistemas operativos existentes.

```{admonition} Usar datos existentes no elimina el problema de medición
:class: important

Aunque recibamos un archivo ya terminado, los datos siguen siendo el resultado de un proceso de observación.

Para interpretarlos correctamente necesitamos saber, cuando sea posible, **qué se midió, sobre qué unidades, con qué instrumento o procedimiento, cuándo, con qué resolución y bajo qué criterios**.
```

## 6. Estructura lógica y formato de almacenamiento

Una distinción importante es que la **estructura conceptual de los datos** y el **formato del archivo donde se almacenan** no son lo mismo.

Una tabla puede guardarse como CSV, Excel, Parquet o dentro de una base de datos. Del mismo modo, un conjunto de geometrías espaciales puede almacenarse como Shapefile, GeoPackage o GeoJSON.

### 6.1. Datos tabulares

Los datos tabulares pueden almacenarse en formatos como:

- `.csv`;
- `.xlsx`;
- `.parquet`;
- tablas de una base de datos.

#### CSV

Un archivo CSV es un archivo de texto en el que cada línea representa generalmente una fila y los valores están separados por un delimitador.

```csv
avenida,ancho_m,densidad_poblacional,volumen_veh_h
A,14.0,8500,1240
B,21.5,12300,2180
C,10.5,6100,870
```

Su principal ventaja es su simplicidad y amplia compatibilidad. Sin embargo, el archivo por sí solo contiene poca información explícita sobre tipos de datos, unidades o metadatos.

#### Excel

Los archivos `.xlsx` permiten almacenar tablas, múltiples hojas, fórmulas y formato visual. Son comunes para intercambio manual de información, aunque su flexibilidad también facilita estructuras difíciles de procesar automáticamente: encabezados múltiples, celdas combinadas, comentarios o valores mezclados con unidades.

```{admonition} Una tabla legible por una persona no siempre está lista para analizar
:class: note

Una planilla puede verse perfectamente ordenada en Excel y, sin embargo, requerir una transformación considerable antes de poder realizar operaciones estadísticas.

El objetivo es obtener una representación donde cada observación y cada variable estén identificadas de manera consistente.
```

### 6.2. Texto estructurado y semi-estructurado

No todos los datos de texto están organizados como una tabla simple.

Podemos encontrar:

- archivos de ancho fijo;
- archivos producidos por instrumentos con encabezados y bloques;
- archivos de registro (*logs*);
- JSON;
- XML;
- otros formatos definidos por un software específico.

El ejemplo de registros de aceleración utilizado en aplicaciones estructurales puede contener primero información sobre fecha, hora, canales y rango del instrumento, seguida por una tabla temporal de aceleraciones. Antes de analizar la señal es necesario interpretar esa estructura y extraer las variables relevantes.

```text
Time        v0        v1        v2
0.000       0.0104    0.0107   -0.0022
0.001       0.0167    0.0088    0.0038
0.002       0.0177    0.0060    0.0031
...
```

```{admonition} Imagen sugerida
:class: note

Agregar captura de un archivo real de acelerómetro mostrando:

1. metadatos del instrumento;
2. encabezado;
3. bloque numérico de la serie temporal.
```

### 6.3. Datos raster e imágenes

Una imagen digital puede representarse computacionalmente como una matriz —o conjunto de matrices— de valores.

Ejemplos:

- fotografía RGB;
- imagen satelital multibanda;
- modelo digital de elevación;
- mapa raster de profundidad de inundación.

Formatos frecuentes incluyen `.png`, `.jpg` y `.tif`. En aplicaciones geoespaciales, GeoTIFF permite además almacenar información necesaria para ubicar el raster en el espacio.

``````{card} De una imagen a variables numéricas

Una imagen satelital puede verse como una fotografía, pero para un algoritmo es un arreglo de números.

Cada pixel constituye una posición y cada banda contiene una variable registrada por el sensor. La clasificación de uso del suelo consiste en utilizar esos valores para inferir una categoría de interés.
``````

### 6.4. Datos vectoriales geoespaciales

Los datos vectoriales representan entidades mediante geometrías:

- **puntos:** estaciones meteorológicas, edificios, sondeos;
- **líneas:** rutas, ríos, redes;
- **polígonos:** parcelas, cuencas, zonas administrativas.

Cada geometría puede estar acompañada por una tabla de atributos. Por ejemplo, un conjunto de edificios puede contener geometría, tipología, número de pisos y nivel de daño.

Formatos habituales incluyen:

- GeoPackage (`.gpkg`);
- Shapefile (`.shp`);
- GeoJSON (`.geojson`).

```{admonition} Imagen sugerida
:class: note

Agregar una figura con puntos, líneas y polígonos y mostrar al costado una pequeña tabla de atributos asociada.
```

## 7. Acceso y lectura de datos

Una vez que conocemos qué representa un conjunto de datos y cómo está almacenado, necesitamos cargarlo en un entorno donde podamos realizar operaciones sobre él.

Los datos pueden encontrarse:

- en archivos locales;
- en almacenamiento remoto o en la nube;
- en una base de datos;
- disponibles mediante una API o servicio web.

El mecanismo de acceso cambia, pero el objetivo conceptual es el mismo: **transformar la representación utilizada para almacenar o transmitir los datos en una estructura computacional apropiada para analizarlos**.

### 7.1. Lectura de tablas

En Python, una tabla puede cargarse habitualmente en un `DataFrame` de `pandas`.

```python
import pandas as pd

df = pd.read_csv("avenidas.csv")
```

Una vez cargada, podemos acceder a las variables, seleccionar observaciones, calcular resúmenes o producir gráficos.

```python
df["volumen_veh_h"].mean()
```

### 7.2. Lectura de datos espaciales

Los datos vectoriales y raster requieren estructuras capaces de conservar también la información espacial.

```python
import geopandas as gpd
import rasterio

# Datos vectoriales
gdf = gpd.read_file("cuencas.gpkg")

# Datos raster
with rasterio.open("profundidad_inundacion.tif") as src:
    profundidad = src.read(1)
```

### 7.3. Bases de datos y servicios remotos

En proyectos reales, los datos pueden no existir como un archivo individual. Una base de datos permite consultar solo las observaciones requeridas, mientras que una API permite solicitar información a un servicio remoto mediante un protocolo definido.

En esta etapa introductoria no necesitamos estudiar en detalle estas tecnologías. Lo importante es reconocer que **la forma en que accedemos a los datos es distinta de la naturaleza de las variables y de la estructura lógica del conjunto**.

## 8. Del dato crudo al dato analizable

Los datos obtenidos de un instrumento, archivo, base de datos o servicio rara vez están inmediatamente listos para ser analizados.

El proceso de lectura y preparación busca convertirlos desde su **formato de adquisición o almacenamiento** hacia una representación donde podamos realizar operaciones matemáticas, estadísticas y gráficas de manera consistente.

````{grid}

```{grid-item-card} Datos tabulares
Habitualmente se representan mediante tablas o `DataFrames`.
```

```{grid-item-card} Series temporales
Tablas o arreglos donde el índice temporal forma parte explícita de la estructura.
```

```{grid-item-card} Raster e imágenes
Arreglos numéricos de dos o más dimensiones.
```

```{grid-item-card} Vectores espaciales
Geometrías asociadas a tablas de atributos.
```

````

Para gran parte de los modelos estadísticos que utilizaremos en este curso, el resultado final será una representación tabular de la forma:

| observación | $X_1$ | $X_2$ | $\cdots$ | $Y$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | | | | |
| 2 | | | | |
| $\vdots$ | | | | |
| $N$ | | | | |

donde cada fila corresponde a una observación y las columnas representan las variables disponibles.

Pero no todos los análisis requieren convertir literalmente la información a una tabla. En procesamiento de imágenes, análisis espacial o señales, puede ser necesario preservar su estructura multidimensional.

```{admonition} Idea central
:class: tip

**Leer datos no significa solamente abrir un archivo.**

Significa interpretar qué representa cada observación, qué variable contiene cada valor, cómo fue obtenida y transformar esa información a una estructura computacional adecuada para el análisis.
```

```{admonition} Puente hacia el siguiente capítulo
:class: note

Una vez que los datos están correctamente identificados, organizados y cargados, el siguiente paso consiste en **explorarlos**: estudiar sus distribuciones, identificar valores faltantes o anómalos, visualizar relaciones entre variables y evaluar si el conjunto de datos es adecuado para responder la pregunta de interés.
```
