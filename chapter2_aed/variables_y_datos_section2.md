## 2. Del fenómeno de interés al dato

**Pregunta central — ¿Cómo transformamos un fenómeno o propiedad del mundo real en un dato registrado?**

En la sección anterior distinguimos entre la **variable** que queremos observar y el **dato** que finalmente registramos. Esa relación no es automática: para transformar una característica del mundo real en datos necesitamos definir **cómo vamos a observarla**.

En algunos problemas la variable de interés puede medirse de manera bastante directa. En otros, el fenómeno que realmente nos interesa no puede observarse directamente y debemos representarlo mediante otra variable que sí podamos registrar.

De manera esquemática podemos pensar el proceso de observación como:

> **Fenómeno o propiedad de interés → variable observable → mecanismo de observación → dato**

Cuando la variable observable coincide esencialmente con aquello que nos interesa, el problema principal es la calidad del mecanismo de medición. Cuando no coincide, aparece además una segunda cuestión: **qué tan bien representa la variable observada al fenómeno de interés**.

````{grid}
:gutter: 2

```{grid-item-card} Variable medida directamente
:text-align: center

**Desplazamiento real**

↓

sensor

↓

**4.82 mm**
```

```{grid-item-card} Fenómeno representado por una variable
:text-align: center

**Daño estructural**

↓

deformación máxima

↓

sensor / inspección

↓

**dato registrado**
```

````

```{admonition} Dos preguntas diferentes
:class: tip

Al obtener datos conviene distinguir dos preguntas:

1. **¿Medimos adecuadamente la variable que decidimos observar?**
2. **¿La variable observada representa adecuadamente el fenómeno que realmente nos interesa?**

La primera pregunta se relaciona con el **error de medición**. La segunda, con la elección de la variable y el uso de **proxies**.
```

### 2.1. El proceso de observación

Un mecanismo de observación puede ser un instrumento físico, un ensayo de laboratorio, una clasificación realizada por una persona, un algoritmo de procesamiento o una combinación de estos.

Por ejemplo, en el ensayo de un bulón:

> **resistencia a tracción → ensayo mecánico → 438 MPa**

En un relevamiento post-sismo:

> **tipología estructural → inspección visual → “mampostería”**

En ambos casos existe un procedimiento mediante el cual una característica de la unidad de observación se transforma en un valor registrado.

```{admonition} Medir en un sentido amplio
:class: note

En este libro utilizaremos **medición** u **observación** en un sentido amplio. El mecanismo puede involucrar un instrumento físico, pero también una clasificación visual, una encuesta, una imagen satelital o un procedimiento computacional.

Lo importante es que exista algún proceso que transforme una característica del sistema real en información registrada.
```

Todo proceso de observación tiene limitaciones. En aplicaciones reales estas limitaciones pueden introducir errores, variabilidad o diferencias entre el fenómeno que queremos estudiar y la variable que efectivamente logramos registrar.

<!-- CITA SUGERIDA:
Agregar aquí una referencia formal sobre medición, error de medición e incertidumbre.
Posibles fuentes: International Vocabulary of Metrology (VIM) / NIST.
-->

### 2.2. Error en el proceso de medición

Supongamos primero que la variable que medimos coincide con la característica que realmente nos interesa. Incluso en ese caso, el dato registrado puede no coincidir exactamente con el valor de la variable debido a imperfecciones del mecanismo de medición.

``````{card} Medición de desplazamientos en una estructura

````{grid}

```{grid-item}
Queremos conocer el desplazamiento de un punto de un puente sometido a una determinada condición de carga.

La variable de interés es el **desplazamiento** y utilizamos un sensor para registrarlo. Si repitiésemos la medición varias veces bajo condiciones prácticamente iguales, podríamos obtener:

`4.81 mm`, `4.84 mm`, `4.79 mm`, `4.83 mm`, ...

La variable que queremos medir no cambió necesariamente en esa misma magnitud. Parte de las diferencias entre los datos puede provenir del propio mecanismo de medición.
```

```{grid-item}
**[IMAGEN A AGREGAR]**

Sensor de desplazamiento o sistema de monitoreo estructural.
```

````

``````

Podemos representar conceptualmente esta situación como:

> **valor de la variable + error de medición → dato registrado**

El error de medición puede contener componentes diferentes. Algunas generan fluctuaciones impredecibles entre mediciones repetidas; otras pueden desplazar sistemáticamente los valores registrados.

````{grid}
:gutter: 2

```{grid-item-card} Error aleatorio

Mediciones repetidas bajo condiciones similares producen valores ligeramente diferentes.

**Ejemplo:** ruido electrónico de un sensor.

El efecto cambia de una medición a otra y contribuye a la dispersión de los datos.
```

```{grid-item-card} Error sistemático

El procedimiento tiende a desplazar las mediciones en una dirección determinada.

**Ejemplo:** un sensor mal calibrado registra sistemáticamente valores 0.5 mm mayores que los reales.

Repetir muchas veces la medición no elimina necesariamente este problema.
```

````

```{admonition} Error aleatorio y variabilidad de la población
:class: important

El **error aleatorio de medición** no es lo mismo que la **variabilidad inherente de la población** discutida en la introducción.

Dos probetas pueden tener resistencias realmente diferentes aunque pudiéramos medirlas sin error. En cambio, si medimos varias veces una misma magnitud y obtenemos valores diferentes por limitaciones del instrumento, esa variabilidad proviene del proceso de medición.

En los datos reales, ambas fuentes pueden coexistir.
```

<!-- CITA SUGERIDA:
Referencia sobre random measurement error vs systematic measurement error/bias.
-->

#### Una demostración interactiva

El siguiente ejemplo permite modificar separadamente la magnitud del **ruido aleatorio** y del **sesgo sistemático** de un instrumento. La línea horizontal representa el valor real de la variable y los puntos representan mediciones repetidas.

```{code-cell} ipython3
:tags: [remove-input]

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets


def simular_mediciones(ruido=0.2, sesgo=0.0, n=30):
    rng = np.random.default_rng(42)
    valor_real = 10.0
    mediciones = valor_real + sesgo + rng.normal(0, ruido, n)

    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.scatter(np.arange(1, n + 1), mediciones)
    ax.axhline(valor_real, linestyle="--", label="Valor real")
    ax.axhline(mediciones.mean(), linestyle=":", label="Promedio medido")
    ax.set_xlabel("Medición")
    ax.set_ylabel("Valor registrado")
    ax.set_title("Mediciones repetidas de una misma variable")
    ax.legend()
    plt.show()


widgets.interact(
    simular_mediciones,
    ruido=widgets.FloatSlider(
        value=0.2, min=0.0, max=1.5, step=0.1,
        description="Ruido:"
    ),
    sesgo=widgets.FloatSlider(
        value=0.0, min=-2.0, max=2.0, step=0.1,
        description="Sesgo:"
    ),
    n=widgets.IntSlider(
        value=30, min=5, max=100, step=5,
        description="N:"
    ),
);
```

```{admonition} ¿Qué debería observar?
:class: note

Al aumentar el **ruido**, las mediciones se dispersan más alrededor de su valor medio. Al aumentar el **sesgo**, el conjunto de mediciones se desplaza sistemáticamente respecto del valor real. Aumentar el número de mediciones permite caracterizar mejor la distribución de los datos, pero no elimina por sí solo un sesgo sistemático.
```

### 2.3. Cuando lo observable no es exactamente lo que interesa

Existe un problema diferente al error de medición. Muchas veces el **fenómeno que realmente queremos estudiar no puede observarse directamente** o no posee una única medición natural.

En esos casos debemos decidir qué variable observable utilizaremos para representarlo.

| Fenómeno de interés | Posible variable observable |
| --- | --- |
| Daño de una estructura durante un sismo | Deformación máxima, ancho de fisuras o categoría visual de daño |
| Capacidad de carga de un suelo | Tensión alcanzada bajo un determinado criterio de deformación |
| Congestión de una vía | Velocidad media, tiempo de viaje o volumen de tránsito |
| Deterioro de un pavimento | Número, longitud o tipo de fisuras |
| Uso o cobertura del suelo | Respuesta espectral registrada por un sensor remoto |

A una variable utilizada como sustituto observable de una característica o fenómeno que no podemos medir directamente la llamaremos, en términos generales, **variable proxy**.

```{admonition} ¿Qué significa operacionalizar un fenómeno?
:class: note

Definir cómo un concepto o fenómeno de interés será representado mediante variables observables suele denominarse **operacionalización**.

En ingeniería hacemos esto constantemente. Conceptos como *daño*, *confort*, *congestión*, *deterioro* o *capacidad* deben traducirse a variables que podamos registrar antes de construir un conjunto de datos.
```

El uso de una variable proxy introduce una dificultad diferente a la del ruido instrumental. Incluso si el proxy se mide con enorme precisión, puede seguir siendo una representación incompleta del fenómeno que nos interesa.

````{grid}
:gutter: 2

```{grid-item-card} Error de medición

**Quiero conocer:** desplazamiento.

**Mido:** desplazamiento.

**Problema:** el sensor no lo registra perfectamente.

Una medición mejor puede reducir esta diferencia.
```

```{grid-item-card} Variable proxy

**Quiero conocer:** daño estructural.

**Mido:** deformación máxima.

**Problema:** la variable medida no es idéntica al fenómeno de interés.

Incluso una medición perfecta de la deformación no convierte a la deformación en una medida perfecta del daño.
```

````

```{admonition} Una variable perfectamente medida puede ser una mala variable para la pregunta
:class: important

La calidad de los datos no depende solamente de la precisión del instrumento.

Podemos medir una variable con muy poco error y, aun así, obtener información poco útil si esa variable no representa adecuadamente el fenómeno necesario para responder nuestra pregunta.
```

### 2.4. Un ejemplo completo: imágenes satelitales y uso del suelo

El ejemplo de clasificación de imágenes satelitales discutido en la introducción muestra cómo las distintas etapas del proceso de observación pueden aparecer simultáneamente.

Supongamos que queremos caracterizar el **uso o cobertura del suelo** de una cuenca. Las categorías que nos interesan pueden ser, por ejemplo, agua, vegetación, suelo desnudo o superficie urbana.

Un satélite no observa directamente esas etiquetas. El sensor registra energía electromagnética en diferentes bandas espectrales. Después de distintas etapas de procesamiento, esos valores se utilizan para inferir las categorías de interés.

Podemos representar el proceso de manera simplificada como:

> **uso/cobertura del suelo**  
> ↓  
> **respuesta espectral de la superficie**  
> ↓  
> **sensor satelital**  
> ↓  
> **valores digitales de las bandas**  
> ↓  
> **procesamiento e inferencia**  
> ↓  
> **categoría estimada de uso del suelo**

``````{card} ¿Dónde aparecen las distintas fuentes de imperfección?

````{grid}

```{grid-item}
**Representación del fenómeno**

Una categoría como "área urbana" no es idéntica a la respuesta espectral que recibe el sensor. Distintas superficies pueden producir respuestas similares y una misma categoría puede presentar gran variabilidad.

**Proceso de medición**

El sensor posee resolución finita y sus registros pueden estar afectados por calibración, condiciones atmosféricas, geometría de observación y otras fuentes de error.

**Inferencia**

Finalmente utilizamos los valores medidos para inferir una categoría que no fue observada directamente.
```

```{grid-item}
![clasificación de imágenes satelitales](figuras/imagen_satelital_LU.jpg)
```

````

``````

Este mismo esquema aparece en muchos problemas de ingeniería: los datos que analizamos son el resultado final de una cadena de decisiones sobre **qué queremos representar, qué variable podemos observar y cómo la registramos**.

```{admonition} Imagen sugerida
:class: note

Agregar una figura conceptual de tres niveles:

**Fenómeno real** → **Variable observable** → **Dato**

y señalar visualmente los dos posibles desacoples:

1. fenómeno ↔ variable observable;
2. variable ↔ dato registrado.
```

### Compruebe su comprensión

Clasifique el principal problema presente en cada situación como **error aleatorio de medición**, **error sistemático** o **uso de una variable proxy**.

````{tab-set}

```{tab-item} Caso 1

Un sensor de temperatura registra repetidamente valores que fluctúan alrededor de la temperatura real.

```{dropdown} Ver respuesta
**Error aleatorio de medición.**

La variable de interés es la temperatura y el instrumento intenta medir directamente esa misma variable, pero las lecturas fluctúan entre mediciones.
```
```

```{tab-item} Caso 2

Después de una calibración incorrecta, un sensor registra siempre aproximadamente `0.8 °C` por encima de la temperatura real.

```{dropdown} Ver respuesta
**Error sistemático.**

La medición está desplazada de manera persistente en una dirección.
```
```

```{tab-item} Caso 3

Para representar la congestión de una avenida se utiliza la velocidad media de los vehículos.

```{dropdown} Ver respuesta
**Variable proxy.**

La congestión es el fenómeno de interés. La velocidad media es una variable observable elegida para representar ese fenómeno.
```
```

```{tab-item} Caso 4

El daño sísmico de una estructura se caracteriza únicamente mediante la máxima distorsión entre pisos.

```{dropdown} Ver respuesta
**Variable proxy.**

La distorsión puede medirse con gran precisión y aun así representar solamente una parte del concepto más amplio de daño estructural.
```
```

````

```{admonition} Idea central
:class: tip

Cuando realizamos inferencia no razonamos directamente a partir de la realidad, sino a partir de **datos generados por un proceso de observación**.

Por eso, la validez de un análisis depende no solamente de cuántos datos tenemos, sino también de **qué variables fueron observadas, qué tan bien representan el fenómeno de interés y cómo fueron obtenidas**.
```

En la siguiente sección clasificaremos las variables de acuerdo con el tipo de valores que pueden tomar. Esta clasificación será importante porque determina qué operaciones, visualizaciones y métodos estadísticos tienen sentido para cada variable.
