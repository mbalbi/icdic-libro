## 5. Conjuntos de datos: estructura y almacenamiento

**Pregunta central — ¿Cómo se organizan muchas observaciones en un conjunto de datos y cómo se almacena esa información?**

Hasta ahora trabajamos principalmente con observaciones individuales: qué unidad observamos, qué variables registramos y cómo se generan esos datos. En la práctica, sin embargo, el análisis se realiza sobre **conjuntos de muchas observaciones organizadas de manera sistemática**.

A esa colección organizada de observaciones la llamaremos **conjunto de datos** o *dataset*.

En esta sección distinguiremos dos ideas diferentes:

> **estructura lógica:** cómo se organizan conceptualmente las observaciones y variables;

> **formato de almacenamiento:** cómo esa información se codifica y guarda en una computadora.

Esta distinción será importante porque una misma estructura lógica puede almacenarse de muchas maneras diferentes.

<!-- CITA SUGERIDA:
Agregar una referencia general sobre organización de datos tabulares.
Wickham (2014), "Tidy Data", es particularmente apropiado para la relación
variable-columna / observación-fila / valor-celda.
-->

### 5.1. De observaciones a un conjunto de datos

Supongamos que queremos estudiar el volumen de tránsito de distintas avenidas. Para cada avenida registramos su ancho de calzada, la densidad poblacional del área circundante y el volumen de vehículos observado.

Podemos organizar las mediciones en una tabla:

| avenida | ancho_m | densidad_hab_km2 | transito_veh_h |
| --- | ---: | ---: | ---: |
| A | 14.0 | 8500 | 1240 |
| B | 21.5 | 12300 | 2180 |
| C | 10.5 | 6100 | 870 |

En esta representación:

````{grid}
:gutter: 2

```{grid-item-card} Fila
:text-align: center

Una **observación**

En este ejemplo, una avenida.
```

```{grid-item-card} Columna
:text-align: center

Una **variable**

Por ejemplo, `ancho_m`.
```

```{grid-item-card} Celda
:text-align: center

Un **dato**

Por ejemplo, `14.0 m`.
```

````

La tabla permite reunir en una única estructura los valores de varias variables observadas sobre muchas unidades.

```{admonition} Una tabla no es solamente una matriz de números
:class: important

Cada fila y cada columna tienen un significado asociado al proceso mediante el cual se generaron los datos.

Antes de operar matemáticamente con una tabla debemos poder responder:

**¿qué representa cada fila?, ¿qué representa cada columna?, ¿qué significa cada valor?**
```

```{admonition} Identificadores y variables
:class: note

Una columna como `avenida`, `station_id` o `building_id` puede utilizarse para identificar una unidad de manera única.

Estas columnas son fundamentales para organizar y relacionar observaciones, aunque no necesariamente sean variables que queramos estudiar estadísticamente.
```

```{admonition} "Una observación por fila" es una convención tabular
:class: note

En una tabla bien organizada es habitual que cada fila represente una observación.

Sin embargo, no todos los conjuntos de datos se representan naturalmente como tablas. Imágenes, rasters, señales y otros arreglos multidimensionales pueden requerir estructuras diferentes.

La idea de **unidad de observación** sigue siendo válida, aunque su representación computacional no sea una fila.
```

```{admonition} Imagen sugerida
:class: note

Agregar una figura de una tabla sencilla señalando visualmente:

**fila → observación**

**columna → variable**

**celda → dato**
```

### 5.2. Estructuras de los conjuntos de datos

Los conjuntos de datos pueden organizar sus observaciones de maneras diferentes. Una forma útil de distinguir estas estructuras es preguntarnos:

> **¿Qué identifica o diferencia una observación de otra?**

Por ejemplo, las observaciones pueden diferenciarse por una unidad física, por un instante de tiempo, por una posición espacial o por una combinación de estos elementos.

| Estructura | Una observación se distingue por... | Ejemplo |
| --- | --- | --- |
| Transversal | unidad | una avenida |
| Serie temporal | tiempo | una medición horaria de viento |
| Longitudinal o panel | unidad + tiempo | puente + fecha |
| Espacial | localización o geometría | estación, edificio, pixel |
| Espacio-temporal | localización/unidad + tiempo | estación + hora |

````{tab-set}

```{tab-item} Transversal

En un conjunto **transversal** observamos múltiples unidades diferentes bajo un mismo contexto o período de referencia.

Por ejemplo:

| avenida | ancho_m | densidad | transito_veh_h |
| --- | ---: | ---: | ---: |
| A | 14.0 | 8500 | 1240 |
| B | 21.5 | 12300 | 2180 |
| C | 10.5 | 6100 | 870 |

Cada fila representa una avenida distinta.

Otros ejemplos son un conjunto de probetas ensayadas en una campaña o un relevamiento de edificios realizado después de un sismo.
```

```{tab-item} Serie temporal

En una **serie temporal** una variable, o conjunto de variables, se observa sucesivamente a través del tiempo.

Por ejemplo:

| fecha_hora | viento_m_s |
| --- | ---: |
| 2026-08-01 10:00 | 8.4 |
| 2026-08-01 10:10 | 9.1 |
| 2026-08-01 10:20 | 8.8 |

Aquí el **tiempo** forma parte esencial de la estructura de las observaciones.

En el ejemplo de viento de la introducción, podríamos construir otra serie temporal utilizando un único valor por año:

| año | velocidad_max_m_s |
| ---: | ---: |
| 2023 | 31.2 |
| 2024 | 27.9 |
| 2025 | 34.1 |

La resolución temporal depende de cómo definamos las observaciones.
```

```{tab-item} Longitudinal / panel

En datos **longitudinales** o de **panel** observamos repetidamente las mismas unidades a través del tiempo.

Por ejemplo:

| puente_id | fecha | desplazamiento_mm |
| --- | --- | ---: |
| P01 | 2026-01-01 | 3.2 |
| P01 | 2026-02-01 | 3.6 |
| P02 | 2026-01-01 | 2.7 |
| P02 | 2026-02-01 | 2.9 |

Una fila no está identificada solamente por el puente ni solamente por la fecha.

La observación se identifica por la combinación:

> **unidad + tiempo**
```

```{tab-item} Espacial

En los datos **espaciales**, la localización o geometría forma parte del significado de la observación.

Podemos encontrar distintas representaciones.

**Vector**

Las unidades se representan mediante geometrías:

- puntos: estaciones meteorológicas, sondeos, edificios;
- líneas: rutas, ríos, redes;
- polígonos: parcelas, cuencas, áreas administrativas.

Cada geometría puede tener asociadas numerosas variables.

**Raster**

El espacio se divide en una grilla regular de celdas o *pixels*. Cada celda posee una localización y uno o más valores.

Por ejemplo, un mapa de inundación puede registrar para cada pixel la profundidad máxima de agua.

```{admonition} Imagen sugerida
:class: note

Mostrar lado a lado:

**vector:** puntos/líneas/polígonos + tabla de atributos

**raster:** grilla de pixels + valores

La figura debería enfatizar que ambas son formas distintas de representar información espacial.
```
```

```{tab-item} Espacio-temporal

Un conjunto **espacio-temporal** combina localización y tiempo.

Por ejemplo, una red meteorológica puede registrar:

| station_id | fecha_hora | temperatura_C |
| --- | --- | ---: |
| S01 | 2026-08-01 10:00 | 14.1 |
| S01 | 2026-08-01 11:00 | 15.0 |
| S02 | 2026-08-01 10:00 | 13.6 |

Cada observación está asociada simultáneamente a una **localización** y a un **instante de tiempo**.

Muchos problemas ambientales, hidrológicos y de monitoreo de infraestructura tienen naturalmente esta estructura.
```

````

```{admonition} Las estructuras pueden representarse de distintas maneras
:class: tip

Una serie temporal puede almacenarse en una tabla.

Un conjunto espacial de puntos también puede representarse mediante una tabla con coordenadas.

Por lo tanto, términos como **temporal**, **espacial** o **longitudinal** describen principalmente el significado y organización lógica de las observaciones, no necesariamente el formato del archivo donde se guardan.
```

### Compruebe su comprensión: ¿qué identifica una observación?

````{tab-set}

```{tab-item} Caso 1

Un conjunto contiene resistencia a compresión de 100 probetas ensayadas una única vez.

```{dropdown} Ver respuesta

La estructura es principalmente **transversal**.

Cada observación se identifica por una **probeta** diferente.
```
```

```{tab-item} Caso 2

Se registra el desplazamiento del mismo punto de un puente cada segundo.

```{dropdown} Ver respuesta

Es una **serie temporal**.

Las observaciones se distinguen principalmente por el **instante de tiempo**.
```
```

```{tab-item} Caso 3

Se mide anualmente el deterioro de 500 tramos de pavimento durante diez años.

```{dropdown} Ver respuesta

Es un conjunto **longitudinal o de panel**.

Cada observación se identifica por:

**tramo + año**.
```
```

```{tab-item} Caso 4

Una grilla contiene la profundidad máxima de inundación para cada celda de una ciudad.

```{dropdown} Ver respuesta

Es un conjunto **espacial raster**.

Cada observación está asociada a una posición de la grilla.
```
```

````

### 5.3. Almacenamiento de datos

Una vez organizada conceptualmente la información, necesitamos guardarla de alguna manera.

Es fundamental distinguir:

```{admonition} Estructura lógica ≠ formato de almacenamiento
:class: important

La **estructura lógica** describe cómo está organizada y qué significa la información.

El **formato de almacenamiento** define cómo esa información se codifica y guarda en un archivo o sistema.

Por ejemplo, una misma tabla puede almacenarse como `CSV`, `Excel` o `Parquet`. Cambia el formato del archivo, pero no necesariamente cambia el significado de sus observaciones y variables.
```

Podemos pensar algunos ejemplos de correspondencia:

```text
TABLA
├── CSV
├── XLSX
├── Parquet
└── tabla de una base de datos

VECTOR ESPACIAL
├── GeoPackage
├── Shapefile
└── GeoJSON

RASTER
├── GeoTIFF
├── NetCDF
└── otros formatos raster
```

El objetivo de esta clasificación no es memorizar extensiones, sino comprender que el **mismo tipo de información puede representarse mediante formatos diferentes**, cada uno con propiedades prácticas distintas.

#### 5.3.1. Formatos tabulares, de texto y semi-estructurados

##### Datos tabulares

Los formatos tabulares son especialmente comunes cuando las observaciones pueden representarse mediante filas y variables mediante columnas.

````{tab-set}

```{tab-item} CSV

Un archivo **CSV** (*Comma-Separated Values*) es un archivo de texto donde cada línea representa normalmente una fila y los valores se separan mediante un delimitador.

```csv
avenida,ancho_m,densidad_hab_km2,transito_veh_h
A,14.0,8500,1240
B,21.5,12300,2180
C,10.5,6100,870
```

Es simple, ampliamente compatible y fácil de inspeccionar.

Sin embargo, un CSV contiene poca información explícita sobre tipos de variables, unidades, significado de las columnas o metadatos.
```

```{tab-item} Excel

Los archivos **Excel** (`.xlsx`) permiten guardar tablas, múltiples hojas, fórmulas y elementos de formato.

Son muy utilizados para intercambio y revisión manual de datos.

Su flexibilidad también puede generar estructuras difíciles de procesar automáticamente, por ejemplo:

encabezados múltiples, celdas combinadas, notas dentro de la tabla o unidades escritas junto a los valores.

```{admonition} Legible para una persona no significa listo para analizar
:class: note

Una planilla puede verse perfectamente ordenada en Excel y aun así requerir una transformación importante antes de poder realizar operaciones estadísticas de manera reproducible.
```
```

```{tab-item} Parquet

**Parquet** es un formato binario orientado a columnas, muy utilizado para almacenar conjuntos tabulares de gran tamaño.

A diferencia de un CSV, conserva información sobre los tipos de datos y permite leer y procesar grandes tablas de manera más eficiente.

No está pensado para inspeccionarse manualmente con un editor de texto, sino para ser utilizado por software.
```

````

##### Texto con estructura particular

No todos los instrumentos producen directamente una tabla limpia.

Un archivo puede contener encabezados, configuraciones, metadatos y luego uno o varios bloques numéricos.

Por ejemplo, un registro de aceleraciones puede tener una estructura similar a:

```text
8/21/2026
6:53:12 AM

0, CH+=0, CH-=199, Range=+/-10, y=a
1, CH+=1, CH-=199, Range=+/-10, y=b
2, CH+=2, CH-=199, Range=+/-10, y=c

Time        v0        v1        v2
0.000000    0.010404  0.010720 -0.002230
0.001000    0.016721  0.008825  0.003771
0.002000    0.017669  0.005982  0.003139
...
```

El archivo contiene al menos dos tipos de información:

````{grid}
:gutter: 2

```{grid-item-card} Metadatos

Fecha y hora

Configuración de canales

Rango del instrumento

Información del ensayo
```

```{grid-item-card} Datos

Tiempo

Canal `v0`

Canal `v1`

Canal `v2`
```

````

Antes de analizar las aceleraciones necesitamos **interpretar la estructura del archivo** y transformar el bloque relevante en una representación computacional adecuada.

```{admonition} Imagen sugerida
:class: note

Agregar una captura de un archivo real de acelerómetro y marcar visualmente:

1. encabezado;
2. metadatos;
3. nombres de variables;
4. comienzo del bloque numérico.
```

##### Datos semi-estructurados

Formatos como `JSON` o `XML` permiten almacenar información con una estructura explícita sin requerir una tabla rectangular.

Por ejemplo, un registro JSON puede contener valores simples, listas y estructuras anidadas:

```json
{
  "station_id": "S01",
  "location": {
    "lat": -34.61,
    "lon": -58.38
  },
  "variables": ["temperature", "wind_speed"]
}
```

Estos formatos son frecuentes en APIs, configuraciones y sistemas de intercambio de información.

No los estudiaremos en detalle en esta sección; lo importante es reconocer que **no todo conjunto de datos se almacena naturalmente como una tabla rectangular**.

#### 5.3.2. Formatos geoespaciales

Los datos geoespaciales requieren almacenar no solo atributos, sino también información que permita ubicar las observaciones en el espacio.

##### Datos vectoriales

En una representación vectorial cada entidad posee una geometría —punto, línea o polígono— y puede tener variables asociadas en una tabla de atributos.

Formatos frecuentes incluyen:

````{grid}
:gutter: 2

```{grid-item-card} GeoPackage
`*.gpkg`

Formato moderno que puede almacenar múltiples capas vectoriales y sus atributos en un único archivo.
```

```{grid-item-card} Shapefile
`*.shp`

Formato histórico muy difundido.

En realidad está compuesto por varios archivos relacionados y posee distintas limitaciones heredadas.
```

```{grid-item-card} GeoJSON
`*.geojson`

Representación basada en texto JSON para geometrías y atributos.

Es especialmente común en aplicaciones web e intercambio de datos.
```

````

```{admonition} La geometría no reemplaza a las variables
:class: note

Un archivo vectorial puede contener polígonos de edificios, pero además cada edificio puede tener variables como:

`material`, `numero_pisos`, `uso`, `nivel_dano`.

La geometría describe **dónde y qué forma tiene la unidad**; la tabla de atributos contiene otras variables asociadas a ella.
```

##### Datos raster

En un raster el espacio se representa mediante una grilla regular.

Cada celda contiene uno o más valores, por ejemplo:

> elevación, profundidad de inundación, temperatura o reflectancia espectral.

Formatos frecuentes incluyen **GeoTIFF** y, en determinados tipos de datos multidimensionales, **NetCDF**.

``````{card} Ejemplo: mapa de inundación

Un GeoTIFF podría representar la profundidad máxima de inundación.

Cada pixel posee:

**posición espacial + valor de profundidad**

El hecho de que el archivo sea `.tif` no indica por sí solo qué representa ese valor. Esa información debe conocerse a partir de la documentación y los metadatos.
``````

```{admonition} El formato no define el significado
:class: important

Un `GeoTIFF` puede representar:

> elevación, precipitación, temperatura, profundidad de inundación, uso del suelo...

Un `GeoPackage` puede contener:

> edificios, rutas, cuencas, estaciones, parcelas...

La extensión del archivo describe **cómo se almacena la información**, no qué fenómeno físico representan sus variables.
```

<!-- CITA SUGERIDA:
Para detalles técnicos de GeoTIFF, GeoPackage, NetCDF, etc., es preferible
referenciar documentación oficial cuando esos formatos se utilicen de manera práctica,
en lugar de sobrecargar esta introducción con referencias técnicas.
-->

#### 5.3.3. Metadatos: información necesaria para interpretar los datos

Los valores almacenados no siempre son suficientes para comprender un conjunto de datos.

Llamamos **metadatos** a la información que describe los propios datos y permite interpretarlos correctamente.

````{grid}
:gutter: 2

```{grid-item-card} Sobre las variables

Nombre y definición

Unidades

Tipo de variable

Códigos utilizados

Valores faltantes
```

```{grid-item-card} Sobre la observación

Fecha y hora

Frecuencia de medición

Instrumento

Procedimiento

Resolución
```

```{grid-item-card} Sobre información espacial

Sistema de coordenadas

Resolución espacial

Extensión

Valor `nodata`
```

```{grid-item-card} Sobre procedencia

Fuente

Versión

Fecha de descarga

Procesamientos realizados
```

````

Por ejemplo, una columna llamada:

```text
precipitation = 12.5
```

no puede interpretarse correctamente si no sabemos si la variable representa:

> `mm/h`, `mm/día`, `mm acumulados durante un evento`, u otra definición.

De manera similar, un raster espacial puede contener valores numéricamente correctos pero resultar imposible de utilizar si desconocemos su sistema de coordenadas o el significado de sus valores `nodata`.

```{admonition} Datos correctos pueden ser datos inutilizables
:class: important

Un conjunto de datos puede contener valores perfectamente correctos y, aun así, ser imposible de interpretar adecuadamente si carece de los metadatos necesarios.

La documentación forma parte de la calidad del conjunto de datos.
```

<!-- CITA SUGERIDA:
Aquí puede agregarse una referencia sobre data provenance / metadata / FAIR data
si se desea desarrollar formalmente el tema.
-->

### Compruebe su comprensión: estructura o formato

Clasifique cada término como **estructura lógica** o **formato de almacenamiento**.

````{tab-set}

```{tab-item} Serie temporal

```{dropdown} Ver respuesta

**Estructura lógica.**

Describe observaciones organizadas a través del tiempo.

Una serie temporal podría almacenarse, por ejemplo, como CSV, Parquet o dentro de una base de datos.
```
```

```{tab-item} CSV

```{dropdown} Ver respuesta

**Formato de almacenamiento.**

Describe cómo una tabla puede codificarse como texto.
```
```

```{tab-item} Panel longitudinal

```{dropdown} Ver respuesta

**Estructura lógica.**

Las observaciones se identifican por una combinación de unidad y tiempo.
```
```

```{tab-item} GeoTIFF

```{dropdown} Ver respuesta

**Formato de almacenamiento.**

Se utiliza frecuentemente para almacenar rasters georreferenciados.
```
```

```{tab-item} Raster

```{dropdown} Ver respuesta

**Estructura o representación lógica de datos espaciales.**

Un raster puede almacenarse utilizando diferentes formatos.
```
```

```{tab-item} GeoPackage

```{dropdown} Ver respuesta

**Formato de almacenamiento.**

Puede contener distintas capas de información geoespacial.
```
```

````

### Compruebe su comprensión: inspeccione un archivo

Considere nuevamente el registro de aceleraciones:

```text
8/21/2026
6:53:12 AM

0, CH+=0, CH-=199, Range=+/-10, y=a
1, CH+=1, CH-=199, Range=+/-10, y=b
2, CH+=2, CH-=199, Range=+/-10, y=c

Time        v0        v1        v2
0.000000    0.010404  0.010720 -0.002230
0.001000    0.016721  0.008825  0.003771
...
```

```{dropdown} ¿Dónde están los metadatos?

La fecha, hora y configuración de los canales son ejemplos de **metadatos**.

Describen las condiciones y configuración asociadas al registro.
```

```{dropdown} ¿Dónde comienzan los datos que probablemente queremos analizar?

En la tabla que comienza con:

`Time  v0  v1  v2`
```

```{dropdown} ¿Cuáles son las variables?

Al menos:

`Time`, `v0`, `v1` y `v2`.

La documentación del instrumento debería indicar qué representa físicamente cada canal y sus unidades.
```

```{dropdown} ¿Qué estructura lógica tiene el bloque principal?

Es esencialmente una **serie temporal multivariada**.

Cada fila corresponde a un instante y contiene los valores de varios canales registrados en ese tiempo.
```

```{admonition} Idea central
:class: tip

Para trabajar correctamente con un conjunto de datos debemos distinguir tres niveles:

**qué representan las observaciones y variables**  
↓  
**cómo están organizadas lógicamente**  
↓  
**cómo se encuentran almacenadas y documentadas**

Confundir estos niveles puede llevar a interpretar incorrectamente los datos incluso antes de comenzar el análisis.
```

La siguiente etapa consiste en **acceder y leer** estas representaciones desde un entorno computacional. El objetivo no será simplemente abrir archivos, sino transformar los datos desde su formato de almacenamiento hacia estructuras que permitan realizar operaciones matemáticas, estadísticas y gráficas sin perder su significado.
