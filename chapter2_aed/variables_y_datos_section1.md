# Variables y datos

**Pregunta central — ¿Qué estamos observando, qué característica registramos y qué valor obtenemos?**

En el capítulo anterior vimos que la ciencia de datos busca extraer conocimiento a partir de observaciones. Antes de analizar esas observaciones necesitamos precisar **qué estamos observando**, **qué característica registramos** y **qué valor obtenemos**.

Supongamos, por ejemplo, que una fábrica selecciona un bulón de una tanda y realiza un ensayo de tracción. El objeto sobre el que hacemos la observación es el **bulón**; la característica que nos interesa es su **resistencia a tracción**; y el ensayo devuelve, por ejemplo, un valor de **438 MPa**.

````{grid}
:gutter: 2

```{grid-item-card} Bulón #17
:text-align: center

**Unidad de observación**
```

```{grid-item-card} Resistencia a tracción
:text-align: center

**Variable**
```

```{grid-item-card} 438 MPa
:text-align: center

**Dato registrado**
```

````

```{admonition} Imagen sugerida
:class: note

Reemplazar o complementar las tres tarjetas anteriores con una figura horizontal:

**bulón → resistencia a tracción → 438 MPa**

y debajo:

**unidad de observación → variable → dato**.
```

## 1.1. Unidad de observación y variable

Llamaremos **unidad de observación** al elemento, evento, lugar, instante o combinación de estos sobre el que registramos una o más características.

Una **variable** es una característica observable o registrable de las unidades de una población que puede tomar distintos valores.

En el ejemplo anterior, cada bulón ensayado constituye una unidad de observación y su resistencia a tracción es una variable. Si además registráramos su diámetro, longitud y tipo de acero, estaríamos observando varias variables sobre la misma unidad.

La unidad de observación depende del problema y de cómo se hayan organizado las mediciones. No tiene por qué coincidir necesariamente con un único objeto físico.

```{admonition} La unidad de observación depende del problema
:class: tip

Si instrumentamos un puente y registramos aceleraciones en varios sensores cada milisegundo, el puente es el sistema físico de interés, pero cada combinación **sensor–instante de tiempo** puede constituir una observación dentro del conjunto de datos.
```

## 1.2. De la variable al dato

Para una unidad determinada, una variable toma un **valor**. Sin embargo, aquello a lo que tenemos acceso en la práctica es el valor que logramos registrar mediante un procedimiento de observación o medición: el **dato**.

En el ejemplo de los bulones, la resistencia es una propiedad del bulón, mientras que `438 MPa` es el valor registrado mediante el ensayo.

Esta distinción puede parecer innecesaria al principio, pero será importante en la siguiente sección: el dato registrado no necesariamente coincide de manera perfecta con el valor de la característica que queremos observar.

```{admonition} Tres conceptos para recordar
:class: tip

**Unidad de observación:** aquello sobre lo que registramos información.

**Variable:** característica que puede tomar distintos valores entre unidades u observaciones.

**Dato:** valor que registramos para una variable en una unidad particular.
```

### Los ejemplos de la introducción

````{tab-set}

```{tab-item} Bulones

**Unidad de observación:** un bulón.

**Variable:** resistencia a tracción.

**Dato:** por ejemplo, `438 MPa`.

En este caso registramos una misma variable para distintos elementos de una producción.
```

```{tab-item} Viento

Supongamos que trabajamos con la velocidad máxima anual registrada en una estación meteorológica.

**Unidad de observación:** un año.

**Variable:** velocidad máxima anual del viento.

**Dato:** por ejemplo, `31.2 m/s`.

Aquí la unidad no es un objeto físico sino un período temporal sobre el cual definimos la observación.
```

```{tab-item} Tránsito

Supongamos que estudiamos distintas avenidas de una ciudad.

**Unidad de observación:** una avenida.

**Variables:** ancho de calzada, densidad poblacional y volumen de tránsito.

**Datos para una avenida particular:** por ejemplo, `14 m`, `8.500 hab/km²` y `1.240 veh/h`.

Una misma unidad puede tener muchas variables asociadas.
```

```{tab-item} Daño sísmico

Después de un sismo se inspeccionan distintos edificios.

**Unidad de observación:** una estructura inspeccionada.

**Variables:** tipología estructural, número de pisos, nivel de daño, entre otras.

**Dato:** por ejemplo, `daño moderado` para una estructura determinada.

Los datos no tienen por qué ser siempre números; algunas variables toman valores categóricos.
```

````

```{admonition} Sobre el término "observación"
:class: note

En estadística y ciencia de datos, la palabra **observación** puede utilizarse con dos sentidos cercanos: para referirse a un valor observado o para referirse al conjunto de valores registrados para una unidad.

Cuando pueda existir ambigüedad, en este libro utilizaremos **dato** para un valor individual y **unidad de observación** para aquello sobre lo que se registran las variables.
```

### Compruebe su comprensión

Una estación meteorológica registra cada hora la temperatura, la precipitación y la velocidad del viento.

**¿Cuál sería la unidad de observación? ¿Cuáles son las variables? ¿Qué sería un dato concreto?**

```{dropdown} Ver respuesta

Si el conjunto contiene una fila por estación y hora, la unidad de observación es una combinación **estación–instante de tiempo**.

Las variables incluyen **temperatura**, **precipitación** y **velocidad del viento**.

Un valor como `23.4 °C`, registrado para una estación a una hora determinada, es un **dato** de la variable temperatura.
```

```{dropdown} Otro ejemplo

Después de un sismo se inspeccionan 300 edificios y se registra para cada uno su tipología estructural, número de pisos y nivel de daño.

**Unidad de observación:** cada edificio inspeccionado.

**Variables:** tipología estructural, número de pisos y nivel de daño.

**Datos:** los valores registrados para cada variable en cada edificio, por ejemplo `mampostería`, `3 pisos` y `daño severo`.
```

La relación entre variable y dato parece directa, pero en la práctica interviene siempre algún **proceso de observación o medición**. Ese proceso puede introducir errores y, además, no siempre podemos medir exactamente el fenómeno que realmente nos interesa. Ese será el punto de partida de la siguiente sección.
