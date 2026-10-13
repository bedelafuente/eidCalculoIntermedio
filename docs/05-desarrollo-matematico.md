# Desarrollo matemático: viaje en auto a la panadería

## 1. Pregunta central

¿Por qué integrar velocidad puede dar un resultado distinto de la distancia total recorrida?

Estudiaremos un auto que sale de su casa, se dirige a una panadería y vuelve al punto de partida. El movimiento ocurre sobre una recta. Este es un modelo didáctico simplificado, no una descripción detallada de un viaje real.

## 2. Datos y supuestos

- La casa está en la posición $x=0\ \text{m}$.
- La panadería está en $x=15\ \text{m}$.
- Elegimos como sentido positivo el que va de la casa hacia la panadería, a la derecha.
- El auto viaja a $+1\ \text{m/s}$ durante 15 segundos.
- Permanece detenido durante 10 segundos mientras se realiza la compra.
- Regresa a $-1\ \text{m/s}$ durante 15 segundos y se detiene al llegar a casa.
- El tiempo total observado es de 40 segundos.

Idealizamos los cambios de velocidad como instantáneos. Un auto real necesita tiempo para acelerar y frenar. Al comenzar la observación, el auto ya tiene velocidad de $1\ \text{m/s}$; estar en la posición cero no significa estar en reposo.

## 3. Velocidad y gráfica velocidad-tiempo

Con $t$ medido en segundos, la velocidad es:

$$
v(t)=
\begin{cases}
1\ \text{m/s}, & 0\le t<15,\\
0\ \text{m/s}, & 15\le t<25,\\
-1\ \text{m/s}, & 25\le t<40,\\
0\ \text{m/s}, & t=40.
\end{cases}
$$

La velocidad es cero al llegar y detenerse en $t=40$. Los valores asignados en instantes aislados de cambio no alteran las integrales. Esta función es constante por tramos y tiene un número finito de discontinuidades, por lo que es integrable en el intervalo estudiado.

En la gráfica, el eje horizontal representa el **tiempo $t$ en segundos** y el vertical representa la **velocidad $v$ en metros por segundo**. No representa la posición del auto.

| Etapa | Intervalo de tiempo | Nivel horizontal de la gráfica |
| --- | --- | --- |
| Ida | De 0 a 15 s | $v=+1\ \text{m/s}$ |
| Compra | De 15 a 25 s | $v=0\ \text{m/s}$ |
| Regreso | De 25 a 40 s | $v=-1\ \text{m/s}$ |

Los tramos son horizontales, no diagonales: la velocidad permanece constante en cada etapa. Los saltos representan los cambios instantáneos idealizados; no son intervalos de tiempo adicionales.

## 4. De la acumulación a la integral

En un intervalo donde la velocidad es constante, el cambio de posición es:

$$
\Delta x=v\,\Delta t.
$$

Si la velocidad varía, podemos aproximar el cambio de posición en intervalos pequeños mediante $v(t_i^*)\Delta t_i$ y sumar los aportes. Al hacer que el ancho máximo de esos intervalos tienda a cero, las sumas de Riemann dan la integral:

$$
x(b)-x(a)=\int_a^b v(t)\,dt.
$$

El signo de la velocidad conserva el sentido de cada aporte. Para acumular distancia utilizamos la rapidez $|v(t)|$:

$$
D=\int_a^b |v(t)|\,dt.
$$

En nuestro modelo, separar la suma en los tres tramos permite calcular exactamente los aportes con rectángulos. Sus unidades son:

$$
\frac{\text{m}}{\text{s}}\cdot\text{s}=\text{m}.
$$

## 5. Integral de la velocidad: desplazamiento

Por la aditividad de la integral respecto del intervalo:

$$
\Delta x=\int_0^{40}v(t)\,dt
=\int_0^{15}1\,dt+\int_{15}^{25}0\,dt+\int_{25}^{40}(-1)\,dt.
$$

En los cálculos siguientes usamos los valores numéricos de la velocidad en m/s y del tiempo en segundos; los resultados se expresan en metros.

**Ida:**

$$
\Delta x_1=[t]_0^{15}=15-0=15\ \text{m}.
$$

**Compra:**

$$
\Delta x_2=0(25-15)=0\ \text{m}.
$$

**Regreso:**

$$
\Delta x_3=[-t]_{25}^{40}=-40-(-25)=-15\ \text{m}.
$$

La notación $[F(t)]_a^b$ significa $F(b)-F(a)$. Por tanto:

$$
\boxed{\Delta x=15+0-15=0\ \text{m}.}
$$

El auto termina en la misma posición donde comenzó. Un desplazamiento cero no significa que permaneció quieto.

## 6. Integral de la rapidez: distancia recorrida

La rapidez es el valor absoluto de la velocidad. Durante el regreso, $|-1|=1$, de modo que ese tramo también aporta positivamente:

$$
D=\int_0^{40}|v(t)|\,dt
=\int_0^{15}1\,dt+\int_{15}^{25}0\,dt+\int_{25}^{40}1\,dt.
$$

$$
D=(15-0)+0+(40-25).
$$

$$
\boxed{D=15+0+15=30\ \text{m}.}
$$

En la gráfica de velocidad, las dos regiones tienen área geométrica de 15 m cada una. El rectángulo inferior aporta negativamente al desplazamiento, pero positivamente a la distancia. En la gráfica de rapidez, ese rectángulo aparece reflejado por encima del eje horizontal.

No debemos tomar el valor absoluto después de sumar los aportes con signo:

$$
\left|\int_0^{40}v(t)\,dt\right|=0\ \text{m}
\quad\text{mientras que}\quad
\int_0^{40}|v(t)|\,dt=30\ \text{m}.
$$

## 7. Posición para animar el auto

La posición inicial es $x(0)=0$. La posición se obtiene acumulando velocidad desde ese instante:

$$
x(t)=x(0)+\int_0^t v(u)\,du.
$$

Aquí $u$ es la variable de integración y $t$ indica hasta qué instante acumulamos. Usando valores numéricos de tiempo en segundos y posición en metros:

$$
x(t)=
\begin{cases}
t, & 0\le t<15,\\
15, & 15\le t<25,\\
15-(t-25)=40-t, & 25\le t\le40.
\end{cases}
$$

La posición es continua: el auto no salta de lugar al cambiar de velocidad. En el interior de cada tramo, su derivada coincide con la velocidad; en los instantes de cambio el modelo tiene esquinas y la derivada no existe.

| Tiempo | Posición | Interpretación |
| --- | --- | --- |
| $0\ \text{s}$ | $0\ \text{m}$ | Está en casa y comienza la observación. |
| $15\ \text{s}$ | $15\ \text{m}$ | Llega a la panadería. |
| $25\ \text{s}$ | $15\ \text{m}$ | Termina la compra e inicia el regreso. |
| $40\ \text{s}$ | $0\ \text{m}$ | Llega a casa. |

Para un contador de distancia acumulada en la animación:

$$
D(t)=
\begin{cases}
t, & 0\le t<15,\\
15, & 15\le t<25,\\
15+(t-25)=t-10, & 25\le t\le40.
\end{cases}
$$

En el regreso, la posición disminuye mientras la distancia acumulada aumenta. Como la posición inicial es cero, el desplazamiento acumulado coincide numéricamente con $x(t)$ en este ejemplo.

## 8. Qué debe mostrar la animación

1. Una recta de posiciones con la casa en 0 m y la panadería en 15 m.
2. El auto moviéndose según $x(t)$, con una pausa durante la compra.
3. Una gráfica velocidad-tiempo sincronizada con el mismo reloj.
4. El área positiva que se acumula durante la ida y el aporte negativo del regreso.
5. Dos contadores separados: desplazamiento acumulado y distancia acumulada.
6. Un cierre con desplazamiento de 0 m y distancia recorrida de 30 m.

Si se comprime el tiempo para el video, todas las representaciones deben usar la misma escala temporal. Los 40 segundos corresponden al recorrido modelado, no a la duración total exigida del video.

## 9. Respuesta a la pregunta central

Integrar velocidad acumula cambios de posición con signo. Los 15 m de ida y los 15 m de regreso se compensan porque tienen sentidos opuestos. Integrar rapidez acumula magnitudes no negativas, por lo que ambos trayectos suman. Así, el auto puede recorrer 30 m y tener un desplazamiento final de 0 m.

## 10. Verificación y documentación pendiente

- Comprobación geométrica: cada rectángulo tiene base de 15 s y altura de 1 m/s, por lo que su área geométrica es 15 m.
- Comprobación por posiciones: $x(40)-x(0)=0-0=0\ \text{m}$.
- Comprobación del recorrido: $|15-0|+|0-15|=30\ \text{m}$.
- Este desarrollo fue redactado con apoyo de IA a partir del ejemplo acordado en la conversación. El equipo debe revisarlo, comprenderlo e incorporar el apoyo a su declaración de IA, junto con los usos previos de NotebookLM y las verificaciones que efectivamente realice.
- Queda pendiente incorporar al registro de fuentes las dos fuentes matemáticas complementarias exigidas y la documentación oficial de Manim. Este documento no sustituye esas referencias ni el guion narrado del video.
