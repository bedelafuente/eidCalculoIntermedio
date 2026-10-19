# Guion del video del grupo 16

**Estado:** propuesta para grabar con las voces reales del equipo. El MP4 base
carece de narración y no constituye aún el video final de evaluación.

**Duración:** 5:00, incluidos presentación y créditos. El cronograma está definido
en `video_plan.py` y lo ejecuta `VideoGrupo16`, en `escenas/video_grupo16.py`.
Los tiempos siguientes son tiempos del montaje; los 40 s del viaje pertenecen al
modelo y se muestran comprimidos con factor 0,6.

Los nombres y la asignación de voces son una propuesta de montaje, no un registro
de participación ya efectuada. Cada integrante revisará su texto, lo explicará
con sus propias palabras y comprobará que cabe en su bloque. Se pueden ajustar
los tiempos del plan manteniendo el total entre 4 y 6 minutos y sincronizando
otra vez las animaciones.

| Tiempo | Bloque | Voz prevista | Evidencia principal |
| --- | --- | --- | --- |
| 0:00-0:20 | Presentación | Juan Ignacio Carrera | Integrantes, tema y pregunta |
| 0:20-0:55 | Conceptos | Juan Ignacio Carrera | Símbolos, unidades y condiciones |
| 0:55-1:15 | Datos del ejemplo | Juan Ignacio Carrera | Función, intervalo y supuestos |
| 1:15-1:45 | Viaje y contadores | Juan Ignacio Carrera | Posición, pausa, desplazamiento y distancia |
| 1:45-2:20 | Gráfica sincronizada | Benjamin De La Fuente | Velocidad con signo y movimiento |
| 2:20-2:55 | Sumas de Riemann | Benjamin De La Fuente | Partición, puntos medios y límite |
| 2:55-3:30 | Desplazamiento | Benjamin De La Fuente | Aportes +15, 0 y -15 m |
| 3:30-4:05 | Distancia | Benjamin Aliaga | Valor absoluto y suma de magnitudes |
| 4:05-4:40 | Respuesta y cierre | Benjamin Aliaga | Interpretación y comprobación |
| 4:40-5:00 | Créditos | Lectura visual | Fuentes, Manim, IA y verificación |

## 0:00-0:20. Presentación

**Narración, Juan Ignacio Carrera:**

«Somos Juan Ignacio Carrera, Benjamin De La Fuente y Benjamin Aliaga, del grupo
16 de Cálculo Intermedio. Nuestro tema es distancia recorrida y desplazamiento.
Responderemos: ¿por qué integrar velocidad puede dar un resultado distinto de la
distancia total recorrida? Lo veremos con un viaje de ida y regreso.»

**En pantalla:** los tres nombres, tema y pregunta completa.

## 0:20-0:55. Conceptos y condiciones

**Narración, Juan Ignacio Carrera:**

«La posición x de t indica dónde estamos sobre una recta. La velocidad v de t
incluye el sentido: positiva hacia la derecha y negativa hacia la izquierda.
Su valor absoluto es la rapidez. El desplazamiento, delta x, es posición final
menos posición inicial. La distancia D suma todo lo recorrido. Medimos posición
en metros, velocidad en metros por segundo y tiempo en segundos. Las letras a
y b indican los instantes inicial y final. Suponemos movimiento en una dimensión
y velocidad integrable.»

**Sincronización:** siete líneas aparecen progresivamente durante los primeros
21 s. Usar los 14 s restantes para terminar la explicación y hacer una pausa.

**Nota matemática:** la rapidez es no negativa. La distancia puede ser cero.
No se exige velocidad continua: el ejemplo es constante por tramos, acotado y
con un número finito de saltos, luego es integrable. La posición obtenida al
acumular esa velocidad es continua, aunque tenga esquinas.

## 0:55-1:15. Ejemplo principal

**Narración, Juan Ignacio Carrera:**

«La casa está en cero y la panadería a quince metros a la derecha. Durante los
primeros quince segundos viajamos a más un metro por segundo. Compramos durante
diez segundos, detenidos. Después regresamos a menos un metro por segundo hasta
el segundo cuarenta. Idealizamos los cambios de velocidad como instantáneos.»

**Datos para respaldar el cálculo:**

$$
v(t)=\begin{cases}
1,&0\le t<15,\\
0,&15\le t<25,\\
-1,&25\le t<40,\\
0,&t=40.
\end{cases}
$$

Los valores numéricos de $v$ están en m/s y $t$ en s. Asignar un valor en un
instante aislado no altera las integrales. La derecha es el sentido positivo.
El ejemplo no pretende reproducir aceleraciones reales de un auto.

## 1:15-1:45. Viaje y dos contadores

**Narración, Juan Ignacio Carrera, alineada con el clip existente:**

- **1:15-1:17:** «¿Volver al inicio significa recorrer cero metros?»
- **1:17-1:26:** «En la ida avanzamos quince metros. El desplazamiento y la
  distancia aumentan juntos.»
- **1:26-1:32:** «Durante la compra pasa el tiempo, pero no sumamos recorrido.»
- **1:32-1:41:** «Al regresar disminuye el desplazamiento. La distancia sigue
  aumentando porque seguimos recorriendo metros.»
- **1:41-1:45:** «Volvimos al origen: desplazamiento cero y distancia total de
  treinta metros.»

**Verificación del reloj:** 2 s de presentación, 9 s de ida, 6 s de compra, 9 s
de regreso y 4 s de cierre. Mismo factor temporal para los tres tramos.

## 1:45-2:20. Gráfica velocidad-tiempo

**Narración, Benjamin De La Fuente:**

«Soy Benjamin De La Fuente. En esta gráfica, el eje horizontal es tiempo en
segundos; el vertical es velocidad en metros por segundo, no posición. El punto
verde y el auto usan el mismo reloj. El tramo superior corresponde a la ida.
El tramo sobre el eje indica la compra: el tiempo avanza y el auto sigue quieto.
El tramo inferior indica el regreso. Velocidad negativa significa cambiar de
sentido, no perder distancia. Las líneas horizontales representan velocidades
constantes.»

**Sincronización:** 1:45-1:48 introducción; 1:48-1:57 ida; 1:57-2:03 compra;
2:03-2:12 regreso; 2:12-2:20 interpretación. No hay líneas diagonales que inventen
aceleraciones entre tramos. Extremos abiertos y cerrados muestran los valores de
la función; en t=40 se muestra v=0.

## 2:20-2:55. De sumas de Riemann a integral

**Narración, Benjamin De La Fuente:**

«En cada intervalo pequeño, velocidad por duración aproxima un cambio de
posición. Dividimos los cuarenta segundos en n intervalos iguales, de ancho
delta t igual a cuarenta dividido por n. Elegimos el punto medio, t sub i
estrella. Sigma significa sumar esos aportes. Mostramos ocho, dieciséis y treinta
y dos intervalos. Al refinar la partición, delta t tiende a cero y obtenemos la
integral. Aquí los cortes coinciden con las velocidades constantes, por eso las
sumas ya son exactas.»

**En pantalla:** n=8 de 2:20 a 2:28; n=16 de 2:28 a 2:36; n=32 de 2:36 a 2:44;
aclaración de exactitud desde 2:44 hasta 2:55. Los rectángulos de altura cero
durante la compra no tienen área visible.

**Notas y símbolos:** $\Delta t=40/n$; $t_i^*$ es el punto medio del subintervalo;
$\Sigma$ suma sus aportes. El símbolo $\int$ denota la acumulación límite;
los límites 0 y 40 son segundos y $dt$ indica integración respecto del tiempo.
No se suman áreas negativas geométricas: se suman aportes orientados.

$$
\sum_{i=1}^{n}v(t_i^*)\Delta t\longrightarrow\int_0^{40}v(t)\,dt.
$$

Para n=8,16,32, las fronteras 15 y 25 pertenecen a la partición. La suma de
anchos en la ida es 15, en la compra 10 y en el regreso 15. Por tanto, todas esas
sumas con signo son 0 m; con rapidez son 30 m. La exactitud de este modelo no
demuestra exactitud de rectángulos finitos para velocidades variables generales.

## 2:55-3:30. Integral de velocidad

**Narración, Benjamin De La Fuente:**

«En el primer tramo, un metro por segundo durante quince segundos aporta más
quince metros. La compra aporta cero por diez: cero metros. En el regreso,
menos un metro por segundo durante quince segundos aporta menos quince metros.
Cada región tiene área geométrica positiva de quince metros, pero la región
inferior contribuye con signo negativo. La integral entre cero y cuarenta suma
esos aportes: quince más cero menos quince da cero metros de desplazamiento.
Las unidades son metros por segundo multiplicados por segundos.»

**Sincronización:** aporte de ida 2:55-3:03; compra 3:03-3:10; regreso
3:10-3:18; suma final 3:18-3:30.

$$
\Delta x=\int_0^{15}1\,dt+\int_{15}^{25}0\,dt
+\int_{25}^{40}(-1)\,dt=15+0-15=0\ \mathrm{m}.
$$

Se calculan rectángulos base por altura, sin requerir técnicas de antiderivadas.
El resultado también es $x(40)-x(0)=0-0=0$.

## 3:30-4:05. Integral de rapidez

**Narración, Benjamin Aliaga:**

«Soy Benjamin Aliaga. Para medir distancia usamos la rapidez, valor absoluto de
la velocidad. El tramo de menos uno se convierte en más uno: lo reflejamos sobre
el eje horizontal. La ida suma quince metros, la pausa cero y el regreso otros
quince. Así, la integral de la rapidez da treinta metros. El valor absoluto debe
aplicarse antes de acumular: el valor absoluto del desplazamiento es cero, y no
recupera los treinta metros recorridos. La integral indica acumulación respecto
del tiempo, representada por dt.»

**Sincronización:** recordar signo 3:30-3:36; reflexión 3:36-3:39; observar
rapidez hasta 3:43; cálculo y comparación 3:43-4:05. Durante la reflexión se está
transformando una gráfica en otra, no representando un nuevo movimiento del auto.

$$
D=\int_0^{40}|v(t)|\,dt=1(15)+0(10)+1(15)=30\ \mathrm{m},
\qquad \left|\int_0^{40}v(t)\,dt\right|=0\ \mathrm{m}.
$$

## 4:05-4:40. Respuesta y comprobación

**Narración, Benjamin Aliaga:**

«Integrar velocidad puede dar un resultado distinto porque acumula cambios de
posición con signo: ida y regreso se compensan. La distancia acumula magnitudes
no negativas. Volvimos a casa, por eso el desplazamiento es cero, aunque
recorrimos treinta metros. Eso no significa estar quietos. Si solo viajamos
en sentido negativo, el desplazamiento es negativo y la distancia coincide con
su magnitud. Finalmente, para obtener la posición final sumamos la posición
inicial a la integral de velocidad.»

**Sincronización:** la variación de sentido negativo y la fórmula de posición
aparecen desde 4:21. Pausar brevemente después de la pregunta implícita.

**Comprobación adicional:** en movimiento monótono negativo, con recorrido no
nulo, $\Delta x<0$ y $D=-\Delta x=|\Delta x|$. Siempre
$|\int v|\le\int|v|$. No se afirma que distancia y desplazamiento siempre sean
distintos: con velocidad no negativa coinciden, y con velocidad no positiva
coinciden en magnitud.

## 4:40-5:00. Créditos legibles

No es necesaria narración nueva. Mantener la tarjeta completa 20 s; incluye las
dos fuentes matemáticas consultadas, apunte base, Manim, apoyos de IA, modo de
verificación y ruta a las referencias completas. Los gráficos y dibujos se
construyen con código propio del proyecto; no se reutilizan capturas ni audio
de los videos de referencia.

Las referencias completas y las limitaciones del registro de IA están en
[06-fuentes.md](06-fuentes.md). Antes de entregar, confirmar cuentas, grabar las
voces, revisar sincronización y mezcla, y generar la ficha con el SHA elegido.
