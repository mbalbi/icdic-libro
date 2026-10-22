## 4. ¿Cómo se obtienen los datos?

**Pregunta central — ¿Cómo llegan a existir las observaciones que terminan formando parte de nuestro conjunto de datos?**

Los datos que analizamos no aparecen de manera espontánea. Son el resultado de un conjunto de decisiones y condiciones que determinan **qué unidades observamos, qué variables registramos, bajo qué circunstancias y mediante qué mecanismo**.

Llamaremos de manera general **proceso generador de los datos** al conjunto de condiciones, mecanismos y decisiones que determinan qué observaciones terminan formando parte de un conjunto de datos.

Entender este proceso es fundamental para interpretar correctamente cualquier análisis posterior.

```{admonition} Idea central
:class: tip

Un conjunto de datos no es una colección neutral de valores.

Los datos dependen de:

- qué decidimos observar;
- qué unidades llegaron a ser observadas;
- bajo qué condiciones fueron observadas;
- qué mecanismo utilizamos para registrarlas.

Estas decisiones condicionan qué conclusiones podremos extraer posteriormente.
```

<!-- CITA SUGERIDA:
Agregar aquí una referencia general de estadística/data science sobre data-generating processes,
sampling y diseño de estudios.
-->

### 4.1. Estudios experimentales y observacionales

Una primera distinción fundamental se refiere a **cómo se generan las condiciones bajo las cuales observamos los datos**.

````{grid}
:gutter: 2

```{grid-item-card} Estudio experimental

Quien obtiene los datos **interviene deliberadamente sobre alguna condición del sistema** y observa la respuesta.

La intervención forma parte del proceso que genera las observaciones.
```

```{grid-item-card} Estudio observacional

Las variables se registran bajo condiciones que **no fueron asignadas deliberadamente** por quien realiza el análisis.

El sistema se observa tal como ocurre o como ocurrió.
```

````

#### Estudios experimentales

En un estudio experimental se modifica deliberadamente una o más condiciones del sistema para observar cómo responde.

Esto permite, dependiendo del diseño, seleccionar las condiciones de observación, controlar parte del entorno y decidir de antemano qué variables registrar.

``````{card} Ejemplo: resistencia del hormigón

````{grid}

```{grid-item}
Queremos estudiar cómo cambia la resistencia del hormigón al modificar la relación agua/cemento.

Podemos preparar mezclas con diferentes relaciones agua/cemento definidas previamente, fabricar probetas bajo condiciones controladas y medir luego su resistencia a compresión.

En este caso la relación agua/cemento no aparece simplemente como una característica existente en los datos: fue **modificada deliberadamente como parte del estudio**.
```

```{grid-item}
![mezclas de hormigón](figuras/hormigon_mezclas.jpg)
```

````

``````

Otro ejemplo sería un estudio geotécnico en el que se compactan muestras con diferentes energías prescritas y se mide posteriormente alguna propiedad de resistencia o deformabilidad.

#### Estudios observacionales

En un estudio observacional, las condiciones de interés no son asignadas deliberadamente por quien obtiene los datos. Las observaciones provienen de configuraciones que existen o de fenómenos que ocurren de manera natural.

````{tab-set}

```{tab-item} Viento

Una estación meteorológica registra velocidades de viento durante décadas.

No decidimos qué velocidad tendrá el viento cada día: observamos el fenómeno tal como ocurre.

→ **Estudio observacional**
```

```{tab-item} Tránsito

Medimos ancho de calzada, densidad poblacional y volumen de tránsito en avenidas existentes.

No asignamos deliberadamente a cada avenida un ancho o una densidad poblacional.

→ **Estudio observacional**
```

```{tab-item} Daño sísmico

Después de un terremoto inspeccionamos edificios y registramos tipología, número de pisos y nivel de daño.

No asignamos el movimiento sísmico ni las características de los edificios.

→ **Estudio observacional**
```

````

```{admonition} Experimental no significa necesariamente "laboratorio"
:class: note

Un experimento puede realizarse en laboratorio, en una obra, en una estructura real o incluso a escala urbana.

Lo que caracteriza al estudio experimental es la **intervención deliberada sobre alguna condición del sistema**, no el lugar físico donde se desarrolla.
```

```{admonition} Observacional no significa "sin diseño"
:class: note

Un estudio observacional puede estar cuidadosamente planificado.

Podemos decidir qué estaciones instalar, qué edificios inspeccionar, durante cuánto tiempo observar o con qué frecuencia registrar datos, aunque no controlemos las condiciones naturales o sociales que generan las variables de interés.
```

```{admonition} Experimentos y preguntas causales
:class: important

Los estudios experimentales pueden proporcionar condiciones particularmente favorables para estudiar efectos causales porque permiten controlar deliberadamente una intervención.

Sin embargo, la posibilidad de interpretar un resultado causalmente depende del **diseño y de los supuestos del análisis**, no solamente de que los datos hayan sido obtenidos en un experimento.

De manera análoga, encontrar una asociación en datos observacionales no implica por sí solo una relación causal.
```

<!-- CITA SUGERIDA:
Referencia de estadística introductoria para experimental vs observational.
Si se desea ampliar la última admonición, referenciar más adelante un texto de inferencia causal.
-->

### 4.2. Datos primarios y secundarios

Otra clasificación independiente se refiere a **quién generó originalmente los datos y con qué propósito**.

````{grid}
:gutter: 2

```{grid-item-card} Datos primarios

Son recolectados específicamente como parte del estudio o proyecto que estamos realizando.

**Ejemplos**

Instrumentar un puente, realizar ensayos de laboratorio o efectuar un conteo de tránsito diseñado para nuestro análisis.
```

```{grid-item-card} Datos secundarios

Fueron recolectados previamente por otra persona, organismo o sistema, posiblemente con un objetivo diferente al nuestro.

**Ejemplos**

Registros meteorológicos históricos, censos, inventarios de infraestructura, imágenes satelitales o bases de datos públicas.
```

````

La distinción entre datos primarios y secundarios no indica por sí sola su calidad. Un conjunto de datos secundarios puede haber sido producido mediante procedimientos extremadamente rigurosos, mientras que un conjunto primario puede contener problemas importantes.

La diferencia está en cuánto control tuvimos sobre su generación.

``````{card} Ejemplo: viento para el diseño de un puente

Para estudiar el viento en el sitio de un nuevo puente podemos:

````{grid}

```{grid-item-card} Generar datos primarios

Instalar una estación meteorológica en el emplazamiento y comenzar a registrar nuestras propias observaciones.
```

```{grid-item-card} Utilizar datos secundarios

Obtener varias décadas de registros de una estación operada por el servicio meteorológico nacional.
```

````

Ambas estrategias pueden ser útiles. Sin embargo, al utilizar datos secundarios heredamos decisiones sobre localización, frecuencia de medición, instrumentos, mantenimiento, períodos faltantes y criterios de procesamiento que no fueron definidos específicamente para nuestro problema.
``````

```{admonition} Los datos existentes también fueron medidos
:class: important

Recibir un archivo, descargar una base de datos o consultar una API no elimina el proceso de observación que produjo los datos.

Para interpretarlos correctamente necesitamos conocer, cuando sea posible:

**qué se observó, sobre qué unidades, mediante qué procedimiento, cuándo y bajo qué condiciones**.
```

### 4.3. Mecanismos y fuentes de observación

La clasificación experimental/observacional describe **cómo se generan las condiciones del estudio**. La clasificación primario/secundario describe **quién produjo originalmente los datos**.

Una tercera cuestión es diferente: **¿mediante qué mecanismo o fuente se registran las observaciones?**

````{tab-set}

```{tab-item} Instrumentos y ensayos

Muchas variables se registran mediante dispositivos o procedimientos específicamente diseñados para medirlas.

Algunos ejemplos de ingeniería civil son estaciones meteorológicas, acelerómetros, extensómetros, celdas de carga, piezómetros, estaciones hidrométricas y equipos de ensayo de laboratorio.

````{grid}

```{grid-item-card} Ejemplo
**Variable:** aceleración estructural

**Mecanismo:** acelerómetro

**Dato:** registro de aceleración en un instante determinado
```

```{grid-item-card} Aspectos a considerar
Resolución, calibración, frecuencia de muestreo, mantenimiento, ruido y procedimiento de instalación.
```

````

**[IMAGEN A AGREGAR]**

Instrumentación de una estructura o ensayo de laboratorio.
```

```{tab-item} Observación remota

Algunos fenómenos se observan a distancia mediante sensores instalados en satélites, aeronaves, drones o sistemas de radar.

Ejemplos frecuentes incluyen imágenes satelitales, radar meteorológico y LiDAR.

````{grid}

```{grid-item-card} Ejemplo
**Fenómeno:** cobertura del suelo

**Variable registrada:** respuesta espectral

**Mecanismo:** sensor satelital
```

```{grid-item-card} Aspectos a considerar
Resolución espacial y temporal, calibración, condiciones atmosféricas, procesamiento y relación entre la señal medida y el fenómeno de interés.
```

````

![clasificación de imágenes satelitales](figuras/imagen_satelital_LU.jpg)
```

```{tab-item} Relevamientos humanos

En muchos conjuntos de datos el mecanismo de observación incluye la interpretación o clasificación realizada por una persona.

Por ejemplo:

- inspección post-sismo de edificios;
- relevamiento visual de pavimentos;
- inventario de infraestructura;
- clasificación manual de imágenes;
- encuestas.

````{grid}

```{grid-item-card} Ejemplo
**Variable:** nivel de daño

**Mecanismo:** inspección según un protocolo de clasificación

**Dato:** `daño moderado`
```

```{grid-item-card} Aspectos a considerar
Definición de categorías, consistencia entre observadores, capacitación, subjetividad y documentación del procedimiento.
```

````

**[IMAGEN A AGREGAR]**

Relevamiento de daño estructural o inspección de pavimento.
```

```{tab-item} Sistemas y registros existentes

Algunos datos se generan de manera continua como parte del funcionamiento habitual de organizaciones o infraestructuras.

Por ejemplo:

- sistemas automáticos de gestión de tránsito;
- registros administrativos;
- bases de mantenimiento;
- sistemas de transporte;
- redes de sensores;
- bases de datos de organismos públicos.

En estos casos el conjunto de datos puede no haber sido creado originalmente con fines científicos o estadísticos.

````{grid}

```{grid-item-card} Ejemplo
**Variable:** volumen de tránsito

**Fuente:** sistema automático de conteo vehicular

**Dato:** número de vehículos registrados por intervalo
```

```{grid-item-card} Aspectos a considerar
Cambios de sistema, períodos faltantes, definiciones administrativas, cobertura y objetivo original de la recolección.
```

````

```

````

```{admonition} Estas clasificaciones responden preguntas diferentes
:class: tip

Un mismo conjunto de datos puede ser simultáneamente:

> **observacional + secundario + obtenido mediante sensores**

Por ejemplo, una serie histórica descargada de una red meteorológica pública.

En cambio, una campaña de monitoreo que instalamos específicamente en un puente puede ser:

> **observacional + primaria + obtenida mediante sensores**

Las clasificaciones no compiten entre sí: describen distintas dimensiones del proceso generador de los datos.
```

### 4.4. ¿Qué observaciones terminan formando parte del dataset?

Aun después de definir qué variables registrar y mediante qué mecanismos observarlas, queda una pregunta fundamental:

> **¿Por qué observamos estas unidades y no otras?**

En el capítulo anterior distinguimos entre **muestra** y **población**. El proceso mediante el cual determinadas unidades terminan formando parte de la muestra también es parte del proceso generador de los datos.

A veces podemos decidir deliberadamente qué unidades observar. En otros casos solamente disponemos de aquellas observaciones que fueron registradas por un sistema existente, que pudieron ser medidas o que cumplieron ciertos criterios administrativos o prácticos.

``````{card} Ejemplo: relevamiento después de un sismo

Supongamos que queremos estudiar el nivel de daño de todos los edificios de una ciudad después de un terremoto.

Si nuestro conjunto contiene únicamente edificios cuyos propietarios reportaron daños, las unidades observadas pueden diferir sistemáticamente de los edificios que nunca fueron reportados.

Por lo tanto, aunque las mediciones realizadas sobre cada estructura sean correctas, la **muestra disponible puede no representar de la misma manera a toda la población de edificios**.
``````

```{admonition} La selección de las unidades también importa
:class: important

La calidad de un conjunto de datos no depende únicamente de la precisión de cada medición.

También debemos preguntarnos:

> **¿Qué mecanismo determinó qué unidades fueron observadas y cuáles quedaron fuera del conjunto de datos?**

Más adelante estudiaremos con mayor detalle cómo estas diferencias pueden afectar la inferencia.
```

<!-- CITA SUGERIDA:
Agregar una referencia general sobre sampling/selection bias cuando se desarrolle formalmente.
En esta sección basta con sembrar el concepto.
-->

### 4.5. Integrando el proceso generador de los datos

Podemos resumir el recorrido conceptual desarrollado hasta ahora de la siguiente manera:

> **Pregunta de interés**  
> ↓  
> **Población y unidades de observación**  
> ↓  
> **Variables de interés**  
> ↓  
> **Diseño de obtención de datos**  
> ↓  
> **Selección de las unidades observadas**  
> ↓  
> **Mecanismo de observación**  
> ↓  
> **Datos registrados**

Cada una de estas etapas puede afectar el significado y la calidad de las observaciones finales.

```{admonition} Imagen sugerida
:class: note

Transformar el esquema anterior en una figura vertical u horizontal que funcione como síntesis de las Secciones 1–4.

Podría diferenciar visualmente:

- decisiones conceptuales: pregunta, población, variables;
- decisiones de diseño: experimental/observacional, selección;
- mecanismo físico/operacional: instrumento, inspección, sensor;
- resultado: datos.
```

### Compruebe su comprensión

#### ¿Experimental u observacional?

````{tab-set}

```{tab-item} Caso 1

Una estación registra velocidades de viento durante 30 años.

```{dropdown} Ver respuesta
**Observacional.**

Las velocidades de viento no fueron asignadas deliberadamente por quien recolecta los datos.
```
```

```{tab-item} Caso 2

Se fabrican probetas con cuatro relaciones agua/cemento definidas previamente y luego se mide su resistencia.

```{dropdown} Ver respuesta
**Experimental.**

La relación agua/cemento fue modificada deliberadamente como parte del estudio.
```
```

```{tab-item} Caso 3

Se mide el tránsito en avenidas existentes que poseen diferentes anchos de calzada.

```{dropdown} Ver respuesta
**Observacional.**

Los anchos no fueron asignados deliberadamente por quien realiza el estudio.
```
```

```{tab-item} Caso 4

Durante una prueba piloto se modifica deliberadamente la programación de un semáforo y se mide la longitud de las colas antes y después del cambio.

```{dropdown} Ver respuesta
**Experimental.**

La programación semafórica fue intervenida deliberadamente y se observa la respuesta del sistema.
```
```

````

#### Reconstruya el proceso generador

Supongamos que recibimos el siguiente conjunto de datos de edificios inspeccionados después de un terremoto:

| building_id | material | floors | damage_level | PGA |
| --- | --- | ---: | --- | ---: |
| B001 | mampostería | 2 | severo | 0.41 |
| B002 | hormigón | 8 | leve | 0.32 |
| B003 | mampostería | 3 | moderado | 0.38 |

Antes de analizarlo, podríamos preguntar:

```{dropdown} ¿Cuál es la unidad de observación?

Cada **edificio inspeccionado**.
```

```{dropdown} ¿Qué variables parecen provenir de inspección directa?

`material`, `floors` y `damage_level` podrían haber sido registrados durante el relevamiento de cada edificio.

Para saberlo con certeza necesitaríamos consultar la documentación del conjunto de datos.
```

```{dropdown} ¿De dónde podría provenir PGA?

La aceleración máxima del suelo (`PGA`) podría provenir de una estación sísmica, un modelo espacial, un mapa interpolado u otra fuente externa.

No deberíamos asumir su origen solamente a partir del nombre de la columna.
```

```{dropdown} ¿El estudio parece experimental u observacional?

**Observacional.**

No existe indicio de que las características de los edificios o el movimiento sísmico hayan sido asignados deliberadamente.
```

```{dropdown} ¿Qué otra pregunta necesitamos hacer antes de generalizar a todos los edificios?

Necesitamos conocer **cómo fueron seleccionados los edificios inspeccionados**.

Si solamente se inspeccionaron edificios reportados como dañados, por ejemplo, la muestra podría diferir sistemáticamente de la población completa.
```

```{admonition} Idea central
:class: tip

Antes de analizar un dataset conviene preguntarse:

**¿Cómo llegaron estos datos a existir?**

Comprender su proceso de generación nos permite interpretar correctamente qué representan las observaciones y qué inferencias pueden sostener.
```

En la siguiente sección cambiaremos de escala. Dejaremos de pensar en observaciones individuales y estudiaremos **cómo muchas observaciones se organizan en conjuntos de datos, qué estructuras pueden adoptar y cómo esas estructuras se almacenan en distintos formatos**.
