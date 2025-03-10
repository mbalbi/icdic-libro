---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Modelos, variables y parámetros

ESTO ES UNA PRUEBA!

Hypotheses may come from some more general theory, or may be more ad hoc,
based on intuition or guesswork about the way some phenomenon might work.
Experiments or observations of the phenomenon can be made, and the results com-
pared with the predictions of the hypothesis. This comparison allows one to test
the model and/or estimate any unknown parameters. Any mismatch between data
and model predictions, or other unpredicted ﬁndings in the data, may suggest ways
to revise or change the model. This process of learning about hypotheses from data
is scientiﬁc inference. Vaughan et al.

We might say that deductive reasoning concerns statements that are either
true or false, whereas inductive reasoning concerns statements whose truth value
is unknown, about which we are better to speak in terms of ‘degree of belief’ or
‘conﬁdence’. Vaughan et al.

There is another kind of non-deductive inference, called abduction, or inference to
the best explanation...
Again the conclusion is not unavoidable, other conclusions are valid. Perhaps
someone else ate the banana. But the original conclusion seems to be in some sense
the simplest of those allowed. This kind of reasoning, from observed data to an
explanation, is used all the time in science. Vaughan et al.

Scientiﬁc work employs all the above forms of reasoning. We use deductive rea-
soning to go from general theories to speciﬁc predictions about the data we could
observe, and non-deductive reasoning to go from our limited data to general con-
clusions about unobserved cases or theories. Vaughan et al.

Experimental and observational science is all about inductive reasoning, going
from a ﬁnite number of observations or results to a general conclusion about unobserved cases (induction), or a theory that explains them (abduction).


---
from https://bjlkeng.io/posts/hypothesis-testing/#id11:

The first big idea is that all data (or observations as statisticians like to say) have a "true" probability distribution 1. Of course, it is almost never possible to precisely define it because the real world rarely fits so nicely into the distributions we learn in stats class. However, the implications of this idea is that the "true" distribution and its parameters are fixed (i.e. not random) albeit unknown. The randomness comes in when you sample from this "true" distribution from which each datum is randomly drawn.

The second big idea is that statistical inference 2 (or as computer scientists call it "learning" 3) basically boils down to estimating this distribution directly by computing the distribution or density function 4, or indirectly by estimating derived metrics such as the mean or median of the distribution.

Give a sample X1,X2,…,Xn drawn from some (unknown) distribution F , how do we estimate F
 (or some properties of F
)?


---
En la introducción anterior mencionamos que el motivo principal por el que necesitamos de la ciencia de datos es porque nuestro conocimiento de los procesos que queremos modelar es incompleto, y requerimos de observaciones para poder caracterizar...

Como nos interesa responder preguntas sobre la población general y no solo sobre los datos observados, la inferencia estadística requiere la postulación de una serie de hipótesis simplificativas sobre esa población, traducidas matemáticamente en un "modelo de generación de datos". Toda inferencia que hagamos sobre la población general requiere que asumamos un determinado modelo, es decir, unas determinadas hipótesis, sobre cómo las observaciones podrían haber surgido. Si bien algunos modelos realizan más hipótesis que otros, todos los modelos tienen algún conjunto de especificaciones prescriptas por el modelador que estarán sujetas al escrutinio externo.

En este sentido, el problema de inferencia es un problema de construcción de un modelo de generación de datos. El proceso de construcción de modelos tiene tres grandes etapas:

1. Postulación de modelo: En base al EDA, y al conocimiento específico sobre un determinado problema en cuestión (por ejemplo, conocer la física del problema), se debe postular un conjunto de hipótesis sobre el proceso que generó los datos. En la estadística clásica, esto se refería a postular una familia de distribuciones para la población general de la cual fueron obtenidos los datos. Estas hipótesis se traducen, matemáticamente, en una familia de modelos (probabilísticos) que, creemos, pueden representar el **proceso de generación de datos**.

2. Inferencia del modelo: Una vez postuladas las hipótesis, podemos extraer de las observaciones toda la información necesaria para extraer los modelos más compatibles con los datos observados, dentro de todos los posibles por las hipótesis postuladas. 

3. Comparación y mejora del modelo: El modelo resultante puede utilizarse para realizar predicciones sobre nuevas potenciales observaciones. Comparar a estas con las observaciones que sí tenemos sirve como medida de lo útil que es el modelo como representación del mecanismo de generación de datos real. Esto se conoce como una medida de la **bondad de ajuste** del modelo propuesto, y sirve para poder comparar distintos modelos (hipótesis) entre sí.

```{figure} figuras/population_and_sample_and_model.png
:width: 150px
:alt: Información sobre el objetivo de la ciencia de datos
:name: fig-poblacion-2

EL modelo de generación de datos son las hipótesis simplificativas de la población general que realizamos para poder hacer inferencias sobre la misma

```

## Cómo se define un modelo?

The type of randomness described above is usually called random error (or measurement error) by physicists (the term error is used differently by statisticians6). Here, error does not mean a mistake as in the usual sense. To most scientists the ‘measurement error’ is an estimate of the repeatability of a measurement. If we take some data and use them to infer the speed of sound through air, what is the error on our measurement? If we repeat the entire experiment – under almost identical conditions – chances are the next measurements will be slightly different, by some unpredictable amount. As will further repeats. The ‘random error’ is a quantitative indication of how close repeated results will be. Data with small errors are said to have high precision – if we repeat the measurement the next value is likely to be very close to the previous value(s). Vaughan et al.


modelos paramétricos vs no-paramétricos (ver https://bjlkeng.io/posts/hypothesis-testing/#id11 o wasserman)

(The art of statistics - Spiegelhalter)
-Simple mathematical representations for associations (statisticians)
-Complex deterministic models based on scientific understanding of a physical process
-Complex algorithms used to make decisiones or predictions from large numbers of data (machine learning)


## Tipos de modelos

Modelos físicos, matemáticos o computacionales

Modelos determinísticos o probabilísticos

Modelos fenomenológicos o teóricos

## Modelos como representaciones de conocimiento e incertidumbres



It is the so-called 'normal' distribution that is abnormal in the sense that it has many unique properties not possessed by any other. -- E. T. Jaynes

## Variables, datos y parámetros

1. **Variables**: características (atributos) físicas medibles de los objetos de una población, y que presentan una variabilidad dentro de esa población. *Caracterizados con letras latinas mayúsculas ($X$,$Y$,...)*
2. **Datos**: Mediciones (observaciones) de variables. Un conjunto de datos es una "muestra". *Caracterizados con letras latinas minúsculas ($y_1$,$y_2$,...)*.
3. **Parámetros**: propiedades de una variable o un conjunto de datos.
    1. poblacionales: Propiedad de la distribución de probabilidad (o población) de una variable. Por ejemplo, la esperanza, el desvío estándar, el percentil. *Caracterizados con letras griegas ($\alpha$,$\theta$,...)*.
    2. muestrales: Propiedad de un conjunto de datos (de la muestra). Por ejemplo, el promedio, la dispersión, la proporción, etc. *Caracterizados con letras latinas minúsculas ($\alpha$,$\theta$,...)*.

GRAFICO DE MUESTRA Y POBLACIÓN con nomenclatura
