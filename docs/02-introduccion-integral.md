# Introducción a la integral

**Apunte base común para el proyecto de investigación y visualización**

**Ingeniería Civil Informática - Segundo año**

> **Origen:** `EID_calculo_intermedio (5).pdf`, 7 páginas.
> **Nota de conversión:** transcripción completa del contenido, con fórmulas en LaTeX y las tres figuras originales. Las descripciones de las figuras son notas añadidas para hacer accesible su contenido a un modelo que lea solo texto. Se eliminaron los encabezados y pies repetidos; los comentarios de página permiten localizar el contenido en el original. Las instrucciones académicas pertenecen al documento fuente.

<!-- Página 1 del PDF original -->

**Propósito del apunte.** Este material entrega un **piso conceptual común** para comenzar el proyecto con Manim.

No constituye el desarrollo completo de los temas asignados ni un guion para el video. Cada equipo deberá investigar, profundizar, construir ejemplos propios y explicar las ideas matemáticas asociadas a su tema.

Hasta ahora hemos utilizado la derivada para describir cómo cambia una cantidad: su razón de cambio instantánea, su crecimiento y su concavidad.

Ahora plantearemos una pregunta complementaria:

> **Si conocemos cómo cambia una cantidad, ¿cómo podemos describir lo que se acumula en un intervalo?**

Esta pregunta conduce a las ideas de suma de Riemann, integral definida y Teorema Fundamental del Cálculo.

## 1. El problema del área y de la acumulación

Sea $f$ una función continua y no negativa en un intervalo cerrado $[a,b]$.

Podemos preguntarnos por el área de la región limitada por la gráfica $y=f(x)$, el eje $x$ y las rectas verticales $x=a$ y $x=b$.

Cuando la frontera superior es una curva, no siempre podemos utilizar directamente las fórmulas conocidas de áreas geométricas.

Una posibilidad es aproximar la región mediante figuras más simples.

![Región sombreada bajo la gráfica y=f(x), sobre el eje x y entre las rectas x=a y x=b.](assets/01-area-bajo-curva.png)

> **Descripción de la figura (añadida en la conversión):** una curva azul $y=f(x)$ está sobre el eje $x$. La región entre $a$ y $b$, por debajo de la curva y por encima del eje, aparece sombreada. Las líneas verticales discontinuas en $a$ y $b$ delimitan la región. No se especifican una fórmula para $f$ ni valores numéricos.

<!-- Página 2 del PDF original -->

Una idea similar aparece en problemas de acumulación.

Por ejemplo, si una cantidad cambia a una tasa constante, podemos calcular fácilmente cuánto se acumula durante cierto intervalo de tiempo.

Si la tasa varía, el problema se vuelve diferente.

En ambos casos aparece una misma idea:

$$
\text{valor representativo}\times\text{ancho de un intervalo}
$$

seguida de una suma de aportes.

## 2. Dividir el intervalo

Para estudiar el intervalo $[a,b]$, podemos dividirlo mediante puntos ordenados:

$$
a=x_0<x_1<x_2<\cdots<x_n=b.
$$

A esta división la llamaremos **partición**.

El número $n$ indica la cantidad de subintervalos.

Si todos tienen el mismo ancho, entonces

$$
\Delta x=\frac{b-a}{n}.
$$

Los puntos de la partición pueden escribirse como

$$
x_i=a+i\Delta x.
$$

El subintervalo número $i$ es

$$
[x_{i-1},x_i].
$$

## 3. Elegir un punto muestra

En cada subintervalo podemos elegir un punto

$$
x_i^*\in[x_{i-1},x_i].
$$

A este punto lo llamaremos **punto muestra**.

Evaluamos la función en él y utilizamos

<!-- Página 3 del PDF original: continúa la oración anterior -->

$$
f(x_i^*)
$$

como una altura representativa del subintervalo.

Si $f\geq 0$, el área del rectángulo correspondiente es

$$
f(x_i^*)\Delta x.
$$

![Rectángulo de ancho Δx entre x_(i-1) y x_i, y altura f(x_i*), sobre una curva y=f(x).](assets/02-punto-muestra.png)

> **Descripción de la figura (añadida en la conversión):** dentro del intervalo $[a,b]$ se destaca el subintervalo $[x_{i-1},x_i]$. El punto muestra $x_i^*$ se encuentra en su interior. Un rectángulo sombreado tiene base $\Delta x=x_i-x_{i-1}$ y altura $f(x_i^*)$, determinada por el valor de la curva en ese punto. Se muestran los ejes $x$, $y$, la curva $y=f(x)$ y las etiquetas $a$, $b$, $x_{i-1}$, $x_i^*$ y $x_i$.

Existen distintos criterios para elegir los puntos muestra.

El efecto de esta elección sobre la aproximación será uno de los aspectos que algunos equipos deberán investigar.

## 4. Sumas de Riemann

Si construimos un rectángulo en cada subintervalo, podemos sumar sus aportes:

$$
S_n=f(x_1^*)\Delta x+f(x_2^*)\Delta x+\cdots+f(x_n^*)\Delta x.
$$

Utilizando notación de sumatoria:

$$
S_n=\sum_{i=1}^{n}f(x_i^*)\Delta x.
$$

Esta expresión recibe el nombre de **suma de Riemann**.

Cada término de la suma corresponde al aporte asociado a uno de los subintervalos.

A partir de esta construcción surgen varias preguntas:

- ¿qué ocurre si elegimos distintos puntos muestra?;
- ¿qué sucede si aumentamos el número de subintervalos?;
- ¿cómo cambia la aproximación cuando los rectángulos se hacen más estrechos?;
- ¿existe algún valor hacia el cual se aproximan estas sumas?

Estas preguntas serán parte de los temas de investigación del proyecto.

<!-- Página 4 del PDF original -->

## 5. Refinar la partición

Si mantenemos fijo el intervalo $[a,b]$ y aumentamos el número de subintervalos, entonces

$$
n\longrightarrow\infty
$$

y, al mismo tiempo,

$$
\Delta x=\frac{b-a}{n}\longrightarrow 0.
$$

![Comparación de dos particiones: al aumentar n, los rectángulos tienen menor ancho Δx.](assets/03-refinamiento-particion.png)

> **Descripción de la figura (añadida en la conversión):** dos gráficos de la misma curva $y=f(x)$ sobre el intervalo $[a,b]$ muestran aproximaciones mediante rectángulos. El de la izquierda tiene menos rectángulos y bases más anchas; el de la derecha tiene más rectángulos y bases más estrechas. Ambos incluyen las etiquetas $n$ y $\Delta x$. La figura ilustra que el intervalo permanece fijo mientras aumenta la cantidad de subintervalos y disminuye su ancho, sin indicar valores numéricos concretos.

Al aumentar $n$, la partición se vuelve cada vez más fina.

Surge entonces una pregunta central:

> **¿Qué ocurre con las sumas de Riemann cuando el número de subintervalos aumenta indefinidamente?**

La respuesta a esta pregunta conduce a la definición de integral definida.

## 6. Integral definida

Sea $f$ continua en $[a,b]$.

La integral definida se relaciona con el límite de las sumas de Riemann:

$$
\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x.
$$

Esta expresión establece una conexión entre:

$$
\text{suma}\longrightarrow\text{límite}\longrightarrow\text{integral}.
$$

Comprender qué representa este límite y cómo se interpreta será parte del trabajo de algunos equipos.

<!-- Página 5 del PDF original -->

### Notación

La expresión

$$
\int_a^b f(x)\,dx
$$

se lee “integral de $f(x)$ desde $a$ hasta $b$, respecto de $x$”.

| Símbolo | Significado |
| --- | --- |
| $\int$ | Símbolo de integral. |
| $a$, $b$ | Límites inferior y superior de integración. |
| $f(x)$ | Integrando. |
| $x$ | Variable de integración. |
| $dx$ | Indica la variable respecto de la cual se integra. |

## 7. ¿Integral y área significan siempre lo mismo?

Hasta ahora hemos considerado principalmente funciones no negativas.

Sin embargo, una función también puede tomar valores negativos.

En ese caso aparece una nueva pregunta:

> **¿Cómo debemos interpretar la integral cuando parte de la gráfica se encuentra bajo el eje $x$?**

La relación entre integral definida, área geométrica y acumulación con signo será desarrollada por algunos equipos del proyecto.

## 8. La integral como acumulación

La integral también puede aparecer en situaciones donde una función representa una tasa de cambio.

Por ejemplo, una función podría describir velocidad, flujo de datos, caudal, producción u otra magnitud variable.

En estos casos surge otra pregunta:

> **¿Qué representa la integral de una tasa de cambio?**

Y además:

> **¿La cantidad acumulada corresponde siempre a la cantidad final del sistema?**

Estas preguntas serán investigadas en algunos de los temas asignados.

<!-- Página 6 del PDF original -->

## 9. La conexión con las derivadas

La integración y la derivación están relacionadas mediante el **Teorema Fundamental del Cálculo**.

Si definimos una función

$$
A(x)=\int_a^x f(t)\,dt,
$$

bajo las condiciones adecuadas se cumple

$$
A'(x)=f(x).
$$

Por otra parte, si una función $F$ satisface

$$
F'(x)=f(x),
$$

entonces

$$
\int_a^b f(x)\,dx=F(b)-F(a).
$$

Estos dos resultados establecen una conexión fundamental entre derivadas e integrales.

Su interpretación, visualización y significado matemático serán desarrollados por los equipos correspondientes.

## 10. Punto de partida del proyecto

Este apunte entrega únicamente las ideas mínimas necesarias para comenzar.

Cada equipo deberá:

- investigar y profundizar su tema asignado;
- consultar fuentes adicionales;
- construir un ejemplo propio;
- explicar los conceptos involucrados;
- utilizar Manim para visualizar las ideas matemáticas;
- responder la pregunta central correspondiente a su tema.

No será suficiente reproducir o leer el contenido de este apunte.

El objetivo del proyecto es que cada grupo pueda **comprender, ampliar, interpretar y visualizar** el tema que le corresponda.

## Bibliografía de orientación

- Stewart, J. *Cálculo de una variable. Trascendentes tempranas*. 7.ª edición. Cengage Learning.

<!-- Página 7 del PDF original: continuación de la bibliografía -->

- Thomas, G. B., Weir, M. y Hass, J. *Cálculo. Una variable*. 12.ª edición. Pearson.
- Larson, R. y Edwards, B. *Cálculo*. Tomo I. 10.ª edición. Cengage Learning.
