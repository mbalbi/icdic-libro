## 6. Acceso, lectura y representación computacional

**Pregunta central — ¿Cómo pasamos de datos almacenados a una representación computacional que podamos analizar correctamente?**

En la sección anterior distinguimos entre la **estructura lógica** de un conjunto de datos y el **formato utilizado para almacenarlo**. El paso siguiente consiste en acceder a esa información, interpretar correctamente su formato y construir en memoria una representación que preserve el significado de las observaciones y variables.

Leer datos no significa solamente "abrir un archivo". Implica recorrer una cadena como:

> **fuente de datos → formato almacenado → lectura e interpretación → representación computacional → análisis**

El objetivo final es disponer de una estructura sobre la que podamos realizar operaciones matemáticas, estadísticas y gráficas sin perder la información necesaria para interpretar correctamente los datos.

<!-- CITA SUGERIDA:
Esta idea desarrolla directamente el objetivo mostrado en la clase:
pasar desde el formato de adquisición hacia una estructura apta para operaciones
matemáticas y gráficas.
-->

### 6.1. Del almacenamiento a una representación computacional

Un archivo, una base de datos o un servicio remoto contienen información codificada de acuerdo con ciertas reglas. Para analizarla necesitamos que algún programa **interprete esa codificación** y construya un objeto computacional apropiado.

Podemos pensar el proceso de manera esquemática:

> **datos almacenados**  
> ↓  
> **lector / parser**  
> ↓  
> **objeto computacional**  
> ↓  
> **operaciones**

````{grid}
:gutter: 2

```{grid-item-card} Tabla CSV

`avenidas.csv`

↓

`pandas.read_csv()`

↓

`DataFrame`
```

```{grid-item-card} Vector espacial

`edificios.gpkg`

↓

`geopandas.read_file()`

↓

`GeoDataFrame`
```

```{grid-item-card} Raster

`inundacion.tif`

↓

`rasterio.open()`

↓

array + metadatos espaciales
```

```{grid-item-card} Archivo de instrumento

texto con encabezado + datos

↓

parser específico

↓

metadatos + tabla/array
```

````

```{admonition} Leer es interpretar
:class: important

Una función de lectura no puede adivinar el significado físico de los datos.

Puede reconocer delimitadores, números, fechas o geometrías, pero conceptos como:

> **qué representa una columna, cuáles son sus unidades, qué significa `-9999`, qué canal corresponde a cada sensor o qué sistema de coordenadas utiliza un raster**

dependen de la documentación y del proceso generador de los datos.
```

### 6.2. ¿Dónde están los datos? Mecanismos de acceso

La manera en que accedemos a los datos constituye otra dimensión diferente de su estructura lógica y de su formato de almacenamiento.

Un mismo tipo de información puede encontrarse en lugares muy distintos.

````{tab-set}

```{tab-item} Archivo local

El caso más simple es un archivo almacenado en la computadora desde la que trabajamos.

```python
import pandas as pd

df = pd.read_csv("datos/avenidas.csv")
```

La ruta indica dónde encontrar el archivo; el formato CSV determina cómo interpretar su contenido.
```

```{tab-item} Almacenamiento remoto

Los archivos también pueden encontrarse en servidores o sistemas de almacenamiento en la nube.

Conceptualmente el proceso sigue siendo el mismo:

> localizar el objeto → acceder a sus bytes → interpretar su formato.

Dependiendo de la herramienta utilizada, el archivo puede descargarse primero o leerse directamente desde su ubicación remota.
```

```{tab-item} Base de datos

En una base de datos no necesitamos necesariamente abrir un archivo completo.

Podemos realizar una **consulta** para obtener únicamente determinadas observaciones y variables.

El resultado de esa consulta puede transformarse luego en una tabla u otra estructura computacional.
```

```{tab-item} API / servicio web

Una **API** permite solicitar información a un servicio mediante un protocolo definido.

Por ejemplo, una consulta puede devolver observaciones meteorológicas codificadas como JSON.

La API define **cómo accedemos** a los datos. JSON define **cómo se representa la respuesta**. Ninguna de estas dos cosas determina por sí sola qué significan las variables recibidas.
```

````

```{admonition} No confundir niveles
:class: tip

**API**, **base de datos** y **almacenamiento en la nube** describen mecanismos de acceso.

**CSV**, **JSON**, **GeoTIFF** o **GeoPackage** describen formatos de almacenamiento o intercambio.

**Serie temporal**, **tabla**, **raster** o **panel** describen estructuras lógicas de los datos.

Son conceptos relacionados, pero no equivalentes.
```

### 6.3. Lectura según la estructura de los datos

La representación computacional adecuada depende de la estructura que necesitamos preservar.

````{tab-set}

```{tab-item} Tablas y series temporales

Para datos tabulares, una representación habitual en Python es un `DataFrame` de `pandas`.

```python
import pandas as pd

df = pd.read_csv("avenidas.csv")
```

Podemos inspeccionar las primeras observaciones:

```python
df.head()
```

Una serie temporal puede conservar una estructura tabular pero requerir que una columna sea interpretada explícitamente como fecha:

```python
viento = pd.read_csv(
    "viento.csv",
    parse_dates=["fecha_hora"]
)
```

De esta manera la representación computacional conserva el significado temporal de esa variable.
```

```{tab-item} Texto con estructura particular

Los archivos producidos por instrumentos suelen requerir una interpretación específica.

Por ejemplo:

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

Aquí no alcanza con indicar que el archivo "es texto".

Necesitamos determinar:

> dónde terminan los metadatos, dónde comienza la tabla, cuál es el separador, qué representan los canales y cuáles son sus unidades.

En estos casos es frecuente construir un **parser** específico que transforme el archivo original en dos objetos:

**metadatos + datos numéricos**.
```

```{tab-item} Vector espacial

Para datos vectoriales podemos utilizar `GeoPandas`:

```python
import geopandas as gpd

gdf = gpd.read_file("edificios.gpkg")
```

Un `GeoDataFrame` combina una estructura tabular con una columna especial de geometría.

Además de las variables de atributos debemos conservar información espacial, en particular el sistema de referencia de coordenadas.
```

```{tab-item} Raster y datos multidimensionales

Para un raster geoespacial podemos utilizar `rasterio`:

```python
import rasterio

with rasterio.open("inundacion.tif") as src:
    profundidad = src.read(1)
```

`profundidad` contiene los valores de una banda como un arreglo numérico, mientras que `src` permite acceder a metadatos como resolución, transformación espacial, sistema de coordenadas y valor `nodata`.

Para datos multidimensionales, como algunos conjuntos climáticos almacenados en NetCDF, una representación muy útil es `xarray`:

```python
import xarray as xr

ds = xr.open_dataset("clima.nc")
```

`xarray` permite conservar dimensiones y coordenadas con nombres explícitos, por ejemplo:

> `time`, `lat`, `lon`.
```

````

La correspondencia puede resumirse así:

| Estructura de interés | Representación computacional frecuente |
| --- | --- |
| Tabular | `pandas.DataFrame` |
| Serie temporal tabular | `DataFrame` con fechas/índice temporal |
| Vector espacial | `geopandas.GeoDataFrame` |
| Raster | array + metadatos espaciales |
| Multidimensional | `xarray.Dataset` / `DataArray` |

```{admonition} La representación debe preservar lo que importa
:class: tip

No existe una única estructura computacional ideal para todos los datos.

Una tabla puede ser excelente para regresión, pero convertir prematuramente una imagen o un raster multidimensional a una lista de filas puede hacer que perdamos información importante sobre su estructura espacial.

La representación debe elegirse de acuerdo con el análisis que queremos realizar.
```

### 6.4. Leer sin errores no significa haber leído correctamente

Que una función termine sin generar una excepción solamente indica que el software pudo interpretar los bytes de acuerdo con ciertas reglas. No garantiza que nuestra interpretación del contenido sea correcta.

Considere algunos ejemplos:

````{grid}
:gutter: 2

```{grid-item-card} Valores faltantes

`-9999`

puede ser leído perfectamente como un número entero, aunque en realidad signifique **sin dato**.
```

```{grid-item-card} Identificadores

`001234`

puede transformarse en `1234` si se interpreta como entero, perdiendo ceros que formaban parte del identificador.
```

```{grid-item-card} Fechas

`03/04/2026`

puede representar 3 de abril o 4 de marzo dependiendo de la convención utilizada.
```

```{grid-item-card} Coordenadas

Dos columnas `x`, `y` pueden contener coordenadas perfectamente válidas pero ser imposibles de ubicar correctamente si desconocemos el sistema de referencia.
```

````

Por esta razón, la lectura debe ir acompañada por una **verificación mínima** de la representación obtenida.

#### Tablas

Algunas inspecciones iniciales habituales son:

```python
df.head()
df.shape
df.columns
df.dtypes
```

Estas operaciones permiten verificar rápidamente:

> qué aspecto tienen las primeras observaciones, cuántas filas y columnas existen, qué variables fueron leídas y qué tipo computacional se asignó a cada una.

#### Series temporales

Además conviene verificar que las fechas hayan sido interpretadas correctamente y que el orden temporal sea el esperado.

```python
df["fecha_hora"].dtype
df["fecha_hora"].min()
df["fecha_hora"].max()
```

#### Datos vectoriales

```python
gdf.head()
gdf.crs
gdf.geometry.geom_type.value_counts()
```

Aquí nos interesa confirmar tanto los atributos como la interpretación espacial.

#### Raster

```python
with rasterio.open("inundacion.tif") as src:
    print(src.shape)
    print(src.crs)
    print(src.transform)
    print(src.nodata)
```

Estos metadatos pueden ser tan importantes como los valores del raster.

```{admonition} Un dato mal interpretado puede seguir siendo un número perfectamente válido
:class: important

Python puede sumar, promediar o graficar `-9999` sin ningún problema.

Solamente nosotros —a partir de la documentación y los metadatos— sabemos si ese número representa una medición real o un código utilizado para indicar que la observación no existe.

La verificación semántica debe preceder al análisis.
```

### 6.5. Caso integrado: de un registro de aceleraciones a datos analizables

Consideremos nuevamente un registro producido por un sistema de adquisición:

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
0.003000    0.015900  0.004500  0.001800
```

Antes de escribir código conviene interpretar conceptualmente el archivo.

````{grid}
:gutter: 2

```{grid-item-card} Metadatos

Fecha

Hora

Configuración de canales

Rango del instrumento
```

```{grid-item-card} Variables numéricas

`Time`

`v0`

`v1`

`v2`
```

```{grid-item-card} Estructura lógica

**Serie temporal multivariada**

Cada fila representa un instante de muestreo.
```

````

#### Paso 1 — interpretar y separar las partes del archivo

Para este pequeño ejemplo podemos representar el contenido directamente como texto y localizar el comienzo de la tabla.

```{code-cell} ipython3

raw_text = """8/21/2026
6:53:12 AM

0, CH+=0, CH-=199, Range=+/-10, y=a
1, CH+=1, CH-=199, Range=+/-10, y=b
2, CH+=2, CH-=199, Range=+/-10, y=c

Time v0 v1 v2
0.000000 0.010404 0.010720 -0.002230
0.001000 0.016721 0.008825 0.003771
0.002000 0.017669 0.005982 0.003139
0.003000 0.015900 0.004500 0.001800
"""

lines = raw_text.splitlines()
table_start = next(
    i for i, line in enumerate(lines)
    if line.startswith("Time")
)

metadata_lines = lines[:table_start]
data_lines = lines[table_start:]
```

En un archivo real, el parser debería utilizar reglas suficientemente robustas para identificar la estructura definida por el instrumento.

#### Paso 2 — construir una representación tabular

```{code-cell} ipython3

from io import StringIO
import pandas as pd

data_text = "\n".join(data_lines)

df = pd.read_csv(
    StringIO(data_text),
    sep=r"\s+"
)

df
```

Ahora los datos numéricos se encuentran en un `DataFrame`, donde cada fila representa un instante y cada columna una variable.

#### Paso 3 — verificar la representación

```{code-cell} ipython3

print("Dimensiones:", df.shape)
print()
print("Tipos:")
print(df.dtypes)
print()
print("Valores faltantes:")
print(df.isna().sum())
```

También podemos comprobar el intervalo de muestreo:

```{code-cell} ipython3

dt = df["Time"].diff().dropna()

print("Intervalo de muestreo:", dt.median(), "s")
print("Frecuencia aproximada:", 1 / dt.median(), "Hz")
```

Para este registro:

\[
\Delta t = 0.001\ \text{s}
\]

y por lo tanto:

\[
f_s = \frac{1}{\Delta t} = 1000\ \text{Hz}.
\]

#### Paso 4 — realizar una inspección gráfica mínima

En este punto todavía no estamos realizando un análisis exploratorio completo. Solamente verificamos que la señal cargada tenga una forma razonable.

```{code-cell} ipython3

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 3.5))

ax.plot(df["Time"], df["v0"])
ax.set_xlabel("Tiempo [s]")
ax.set_ylabel("Aceleración")
ax.set_title("Canal v0")

plt.show()
```

```{admonition} ¿Qué aprendimos del archivo antes de analizar la señal?
:class: tip

Ya sabemos que:

- contiene una serie temporal multivariada;
- las observaciones están separadas aproximadamente `0.001 s`;
- la frecuencia de muestreo es aproximadamente `1000 Hz`;
- existen tres canales de medición;
- parte de la información necesaria para interpretarlos se encuentra en los metadatos.

Todavía necesitamos conocer, entre otras cosas, las **unidades físicas** de cada canal y su correspondencia con la instrumentación antes de realizar interpretaciones ingenieriles.
```

### Compruebe su comprensión

````{tab-set}

```{tab-item} Caso 1

Un archivo CSV fue leído correctamente, pero una columna de identificadores aparece como:

`17`, `18`, `19`

mientras que la documentación indica que deberían ser:

`00017`, `00018`, `00019`.

```{dropdown} ¿El archivo fue leído correctamente?

Sintácticamente, sí: el software pudo leer la columna.

Semánticamente, **no necesariamente**. La columna fue interpretada como numérica cuando probablemente debería conservarse como texto.

La lectura debe especificar el tipo apropiado.
```
```

```{tab-item} Caso 2

Un raster contiene muchos valores `-9999` y el promedio espacial resulta extremadamente negativo.

```{dropdown} ¿Qué verificaría primero?

El valor `nodata`.

Es posible que `-9999` sea un código para representar celdas sin información y no una observación física válida.
```
```

```{tab-item} Caso 3

Una tabla contiene una columna `fecha`, pero `df.dtypes` indica que fue leída como texto.

```{dropdown} ¿Por qué importa?

Porque aunque los caracteres sean visibles y correctos, la computadora todavía no interpreta esa columna como una variable temporal.

Convertirla a un tipo de fecha permite ordenar, filtrar y realizar operaciones temporales correctamente.
```
```

```{tab-item} Caso 4

Un GeoPackage puede abrirse y las geometrías aparecen, pero no sabemos qué sistema de coordenadas utiliza.

```{dropdown} ¿Está listo para un análisis espacial?

No.

La ubicación y las distancias no pueden interpretarse correctamente sin conocer el sistema de referencia de coordenadas.
```
```

````

### 6.6. ¿Cuándo están los datos listos para comenzar el análisis?

No existe una frontera absolutamente rígida entre lectura, preparación y análisis exploratorio. Sin embargo, antes de comenzar a extraer conclusiones deberíamos haber verificado, como mínimo, que:

````{grid}
:gutter: 2

```{grid-item-card} Significado

Sabemos qué representan las observaciones y variables.
```

```{grid-item-card} Procedencia

Comprendemos, al menos de manera básica, cómo fueron generados los datos.
```

```{grid-item-card} Estructura

Sabemos cómo están organizadas las observaciones.
```

```{grid-item-card} Representación

La estructura computacional conserva correctamente tipos, fechas, geometrías y otros elementos relevantes.
```

````

```{admonition} Idea central
:class: tip

Un conjunto de datos está listo para **comenzar** a analizarse cuando sabemos:

> **qué representan sus observaciones y variables, cómo fueron generadas, cómo están organizadas y almacenadas, y hemos verificado que su representación computacional conserva correctamente ese significado.**

A partir de ese punto podemos comenzar a preguntarnos qué patrones contienen los datos.
```

Ese será el objetivo del próximo capítulo: **explorar las observaciones mediante resúmenes y visualizaciones, detectar problemas en los datos y comenzar a reconocer los patrones que pueden resultar relevantes para la inferencia**.
