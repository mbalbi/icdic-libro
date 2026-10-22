## 3. Tipos de variables

**Pregunta central — ¿De qué maneras podemos clasificar una variable y qué nos dice cada clasificación?**

Una misma variable puede clasificarse de distintas maneras dependiendo de **qué aspecto de ella nos interese describir**.

Por ejemplo, la velocidad del viento es una variable **numérica continua** por el tipo de valores que puede tomar. Sin embargo, dentro de un problema de inferencia puede actuar como **variable de respuesta** si queremos predecirla, o como **variable explicativa** si la utilizamos para estudiar otro fenómeno.

Por lo tanto, no existe una única clasificación de variables. En este capítulo utilizaremos tres criterios diferentes y complementarios:

````{grid}
:gutter: 2

```{grid-item-card} Según los valores que puede tomar
:text-align: center

**Numérica / categórica**

y sus subtipos.
```

```{grid-item-card} Según su rol en el análisis
:text-align: center

**Respuesta / explicativa**
```

```{grid-item-card} Según cómo se obtiene
:text-align: center

**Observada / derivada**
```

````

```{admonition} Una variable puede tener varias clasificaciones al mismo tiempo
:class: tip

Estas taxonomías son **independientes entre sí**.

Una variable puede ser, por ejemplo, simultáneamente:

> **numérica continua + variable de respuesta + variable derivada**

Las etiquetas responden a preguntas diferentes sobre la misma variable.
```

<!-- CITA SUGERIDA:
Agregar aquí una referencia general de estadística introductoria para la clasificación
numérica/categórica y la terminología response/predictor.
-->

### 3.1. Según los valores que puede tomar

La clasificación más fundamental distingue a las variables de acuerdo con la naturaleza de sus posibles valores.

De manera general utilizaremos la siguiente taxonomía:

```text
Variable
├── Numérica
│   ├── Continua
│   └── Discreta
└── Categórica
    ├── Nominal
    └── Ordinal
```

```{admonition} Imagen sugerida
:class: note

Utilizar o redibujar `figuras/tipos_de_variables_tree.png` como esquema principal de esta taxonomía.

Idealmente, incorporar debajo de cada rama un ejemplo de ingeniería civil:
resistencia, número de vehículos, tipología estructural y nivel de daño.
```

````{tab-set}

```{tab-item} Numérica continua

Una **variable numérica continua** representa una magnitud que, conceptualmente, puede tomar cualquier valor dentro de un intervalo.

Algunos ejemplos son la resistencia de un material, la velocidad del viento, la temperatura, el desplazamiento de una estructura o la profundidad de agua durante una inundación.

En estas variables las diferencias y operaciones aritméticas entre valores tienen una interpretación física o cuantitativa.

```{admonition} Continua no significa "infinitos decimales"
:class: note

Toda medición real posee una resolución finita.

Una velocidad almacenada como `12.4 m/s` puede representar una variable continua aunque el instrumento solo registre décimas. La clasificación se refiere a la **naturaleza de la variable**, no al número de decimales con que se almacena el dato.
```
```

```{tab-item} Numérica discreta

Una **variable numérica discreta** toma valores separados entre sí, frecuentemente porque representa un conteo.

Por ejemplo, pueden ser discretas la cantidad de vehículos que atraviesan una sección durante una hora, el número de pisos de un edificio, la cantidad de fisuras observadas o el número de eventos de inundación registrados durante un período.

```{admonition} Los conteos forman un caso especialmente importante
:class: note

Una variable de conteo toma típicamente valores:

\[
0,1,2,3,\ldots
\]

y más adelante veremos que su naturaleza discreta condiciona los modelos probabilísticos que tiene sentido utilizar.
```
```

```{tab-item} Categórica nominal

Una **variable categórica nominal** toma valores que representan categorías diferentes entre sí, sin un orden natural.

Ejemplos:

| Variable | Categorías posibles |
| --- | --- |
| Tipología estructural | mampostería, hormigón, acero |
| Tipo de suelo | arena, limo, arcilla |
| Uso del suelo | urbano, bosque, agua, cultivo |
| Material predominante | acero, hormigón, madera |

Los nombres de las categorías pueden reemplazarse por códigos numéricos para almacenarlos o procesarlos, pero esos códigos **no convierten a la variable en una magnitud numérica**.
```

```{tab-item} Categórica ordinal

Una **variable categórica ordinal** toma categorías que poseen un orden natural.

Por ejemplo, el nivel de daño de una estructura podría clasificarse como:

> **sin daño < leve < moderado < severo < colapso**

Sabemos que `severo` representa un nivel de daño mayor que `moderado`. Sin embargo, ese orden no implica que exista una distancia cuantitativa definida entre categorías.

```{admonition} Orden no significa distancia
:class: important

Si codificamos:

`1 = leve`, `2 = moderado`, `3 = severo`

el orden de los números respeta el orden de las categorías, pero no podemos concluir automáticamente que la diferencia entre `leve` y `moderado` sea equivalente a la diferencia entre `moderado` y `severo`.

El código numérico sigue representando una **variable categórica ordinal**.
```
```

````

<!-- CITA SUGERIDA:
Referencia introductoria de estadística para variable cuantitativa/categórica,
continua/discreta y nominal/ordinal.
-->

#### Algunos casos particulares

No es necesario crear una taxonomía diferente para cada tipo de variable que encontremos. Sin embargo, algunos casos aparecen con tanta frecuencia que conviene reconocerlos explícitamente.

````{grid}
:gutter: 2

```{grid-item-card} Variable binaria

Es una variable categórica con solamente dos resultados posibles.

Por ejemplo:

> edificio colapsado: **sí / no**

> tramo inundado: **sí / no**
```

```{grid-item-card} Variable de conteo

Es una variable numérica discreta cuyo valor representa cuántas veces ocurre algo.

Por ejemplo:

> número de vehículos por hora

> cantidad de fisuras
```

```{grid-item-card} Variable acotada

Algunas variables numéricas solo pueden tomar valores dentro de ciertos límites.

Por ejemplo:

> una proporción entre `0` y `1`

> un porcentaje entre `0 %` y `100 %`
```

````

El rango de valores posibles de una variable será importante más adelante, cuando definamos modelos probabilísticos adecuados para distintos tipos de datos.

### 3.2. Según su rol dentro del problema de inferencia

Una clasificación completamente diferente se refiere al **rol que una variable cumple dentro de una pregunta o modelo**.

En muchos problemas distinguiremos entre una **variable de respuesta** y una o más **variables explicativas o predictoras**.

````{grid}
:gutter: 2

```{grid-item-card} Variable de respuesta
:text-align: center

Es la variable cuyo comportamiento queremos **describir, explicar o predecir** dentro del problema.

También puede denominarse variable **objetivo**.
```

```{grid-item-card} Variable explicativa o predictora
:text-align: center

Es una variable que utilizamos como información para estudiar cómo cambia o qué valores puede tomar la variable de respuesta.

En distintos contextos también puede aparecer el término **covariable**.
```

````

``````{card} Ejemplo: tránsito urbano

````{grid}

```{grid-item}
Queremos estimar el volumen de tránsito de una avenida a partir de características observadas en otras vías.

**Variable de respuesta**

> volumen de tránsito

**Variables explicativas o predictoras**

> ancho de calzada  
> densidad poblacional

El volumen de tránsito es aquello que queremos inferir, mientras que las otras variables aportan información para hacerlo.
```

```{grid-item}
![tráfico urbano](figuras/trafico_calles.jpg)
```

````

``````

``````{card} Ejemplo: resistencia del hormigón

Si estudiamos cómo varía la resistencia del hormigón en función de las características de la mezcla:

**Respuesta**

> resistencia a compresión

**Predictoras**

> relación agua/cemento  
> proporción de agregados  
> contenido de aditivo

La clasificación depende de la pregunta que queremos responder, no de una propiedad intrínseca de la variable.
``````

```{admonition} El rol de una variable depende de la pregunta
:class: tip

La temperatura podría ser una **variable de respuesta** si queremos predecir la temperatura máxima del próximo verano.

La misma temperatura podría actuar como **variable predictora** si queremos estudiar su asociación con la demanda eléctrica o con la probabilidad de inundación.

Por lo tanto, una variable no es "de respuesta" o "predictora" por naturaleza.
```

```{admonition} Predictora no significa causa
:class: important

El término **variable explicativa** o **predictora** no implica que modificar esa variable produciría necesariamente un cambio causal en la respuesta.

Una variable puede ser muy útil para predecir otra simplemente porque ambas están asociadas.

La diferencia entre asociación y causalidad depende de la **pregunta inferencial y de los supuestos del análisis**, no del nombre asignado a las columnas del conjunto de datos.
```

<!-- CITA SUGERIDA:
Agregar una referencia de regresión/aprendizaje estadístico para response/predictor.
Posible fuente: Introduction to Statistical Learning.
La advertencia predictor != causal puede enlazarse también al capítulo de introducción.
-->

### 3.3. Según cómo se obtiene la variable

Una tercera distinción útil consiste en preguntar si el valor de una variable fue **observado directamente** mediante un proceso de medición, o si fue **calculado a partir de otras observaciones**.

````{grid}
:gutter: 2

```{grid-item-card} Variable observada

Su valor proviene directamente del mecanismo de observación adoptado.

Por ejemplo:

> temperatura registrada por una estación

> aceleración registrada por un acelerómetro

> ancho de una fisura medido durante una inspección
```

```{grid-item-card} Variable derivada

Su valor se calcula o construye a partir de otros datos.

Por ejemplo:

> velocidad resultante calculada a partir de componentes

> máximo anual obtenido de una serie de viento

> relación agua/cemento calculada a partir de cantidades medidas
```

````

La frontera no siempre es absoluta. Una variable puede ser considerada "observada" dentro de un conjunto de datos aunque haya requerido procesamiento previo antes de llegar a nosotros. Lo importante es mantener clara la **trazabilidad**: saber qué valores provienen directamente de observaciones y cuáles fueron construidos mediante algún procedimiento.

``````{card} Ejemplo: velocidad máxima anual del viento

Una estación meteorológica puede registrar la velocidad del viento cada diez minutos.

Esas mediciones son observaciones directas de la variable velocidad para distintos instantes.

Si posteriormente calculamos:

\[
V_{\max,\,2025} = \max(V_1,V_2,\ldots,V_n),
\]

la **velocidad máxima anual** es una variable derivada construida a partir de todas las mediciones realizadas durante ese año.

Esta variable derivada puede luego convertirse en la variable de respuesta de un problema inferencial sobre vientos extremos.
``````

```{admonition} Derivada no significa menos válida
:class: note

Que una variable sea derivada no implica que tenga menor calidad o menor importancia.

En ingeniería, muchas de las cantidades que utilizamos se construyen deliberadamente a partir de observaciones más elementales: máximos, promedios, índices, razones, intensidades o indicadores de desempeño.

Lo importante es conocer **cómo fue definida y calculada**.
```

### 3.4. Las taxonomías son independientes

La manera más útil de integrar estas clasificaciones es aplicarlas simultáneamente a variables concretas.

````{tab-set}

```{tab-item} Resistencia del hormigón

Supongamos que estudiamos la resistencia en función de la composición de la mezcla.

| Criterio | Clasificación |
| --- | --- |
| Tipo de valores | **Numérica continua** |
| Rol en el problema | **Respuesta** |
| Forma de obtención | **Observada**, a través del ensayo |

Una sola variable recibe tres etiquetas diferentes porque cada una describe un aspecto distinto.
```

```{tab-item} Relación agua/cemento

En el mismo problema:

| Criterio | Clasificación |
| --- | --- |
| Tipo de valores | **Numérica continua** |
| Rol en el problema | **Predictora** |
| Forma de obtención | **Derivada**, a partir de cantidades de agua y cemento |

La relación agua/cemento puede ser calculada antes de incorporarse al conjunto de datos.
```

```{tab-item} Nivel de daño

En un relevamiento post-sismo:

| Criterio | Clasificación |
| --- | --- |
| Tipo de valores | **Categórica ordinal** |
| Rol en el problema | **Respuesta**, si queremos inferir daño |
| Forma de obtención | **Observada/clasificada**, según el procedimiento del relevamiento |

Si posteriormente construyéramos un índice numérico a partir de varias observaciones, ese índice sería una nueva variable derivada.
```

```{tab-item} Máximo anual del viento

En un estudio de extremos:

| Criterio | Clasificación |
| --- | --- |
| Tipo de valores | **Numérica continua** |
| Rol en el problema | **Respuesta** |
| Forma de obtención | **Derivada**, como máximo de una serie temporal |

La variable representa un resumen calculado a partir de muchas observaciones realizadas durante el año.
```

````

### Compruebe su comprensión

Considere un conjunto de datos de edificios inspeccionados después de un terremoto. Para cada edificio se dispone de:

> `material`, `numero_pisos`, `distorsion_maxima`, `nivel_dano`

Supongamos que queremos predecir el nivel de daño a partir de las otras variables.

````{tab-set}

```{tab-item} material

¿Cómo clasificaría `material`?

```{dropdown} Ver respuesta

**Según sus valores:** categórica nominal.

**Según su rol:** predictora.

**Según su origen:** probablemente observada o clasificada directamente durante el relevamiento.
```
```

```{tab-item} numero_pisos

¿Cómo clasificaría `numero_pisos`?

```{dropdown} Ver respuesta

**Según sus valores:** numérica discreta.

**Según su rol:** predictora.

**Según su origen:** observada o registrada directamente.
```
```

```{tab-item} distorsion_maxima

¿Cómo clasificaría `distorsion_maxima`?

```{dropdown} Ver respuesta

**Según sus valores:** numérica continua.

**Según su rol:** predictora en este problema.

**Según su origen:** podría ser observada directamente por instrumentación o derivada de otras mediciones, dependiendo de cómo fue producido el conjunto de datos.

Este último punto muestra que una clasificación correcta requiere conocer el **proceso de obtención**.
```
```

```{tab-item} nivel_dano

¿Cómo clasificaría `nivel_dano`?

```{dropdown} Ver respuesta

Si las categorías son, por ejemplo,

`sin daño < leve < moderado < severo < colapso`:

**Según sus valores:** categórica ordinal.

**Según su rol:** respuesta.

**Según su origen:** observada o clasificada mediante un procedimiento de inspección.
```
```

````

```{admonition} Idea central
:class: tip

**"Tipo de variable" no es una única etiqueta.**

Una variable puede describirse simultáneamente según:

- la naturaleza de los valores que puede tomar;
- el rol que cumple dentro de una pregunta inferencial;
- la manera en que sus valores fueron obtenidos.

Estas clasificaciones afectan distintas decisiones posteriores: cómo resumimos y visualizamos una variable, qué modelos podemos utilizar y cómo interpretamos los resultados.
```

La siguiente pregunta ya no se refiere a una variable individual, sino al **proceso mediante el cual obtenemos muchas observaciones**. En la próxima sección distinguiremos diferentes formas de generación y recolección de datos, en particular entre estudios experimentales y observacionales.
