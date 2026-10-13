# Prompt para el video de estudio de NotebookLM

Este es el prompt propuesto en la conversación para generar un video explicativo de apoyo al estudio. Después de recibirlo, el usuario indicó haber visto el video. No se verificó si se hicieron cambios al pegarlo en NotebookLM.

**Contexto:** utiliza el ejemplo inicial $v(t)=t-2$ entre 0 y 4 segundos (desplazamiento de 0 m y distancia de 4 m). El ejemplo final del proyecto es el viaje a la panadería, con 40 segundos de duración y 30 m de distancia, documentado en [05-desarrollo-matematico.md](05-desarrollo-matematico.md). Se conserva el prompt original para documentar el apoyo de IA, no como guion final.

## Texto del prompt

```text
Crea un video explicativo y didáctico en español, de 4 a 6 minutos, para estudiantes de segundo año de Ingeniería Civil Informática que están comenzando a estudiar integrales.

Usa los documentos adjuntos como base. El objetivo es comprender y responder esta pregunta:

¿Por qué integrar velocidad puede dar un resultado distinto de la distancia total recorrida?

Explica con lenguaje sencillo, ejemplos visuales y un desarrollo progresivo. Define cada símbolo antes de utilizarlo y conecta las fórmulas con el movimiento. Evita asumir conocimientos de técnicas de integración.

Sigue esta estructura:

1. PREGUNTA INICIAL
Presenta esta situación: “Si sales de un punto, avanzas y luego regresas al mismo lugar, ¿tu recorrido fue cero?”.
Utilízala para introducir la diferencia entre desplazamiento y distancia recorrida.

2. CONCEPTOS
Explica:
- Posición: ubicación en una recta respecto de un origen.
- Velocidad: cómo cambia la posición con el tiempo.
- Velocidad positiva o negativa: indica el sentido del movimiento, no que el móvil vaya más rápido o más lento.
- Rapidez: valor absoluto de la velocidad.
- Desplazamiento: posición final menos posición inicial.
- Distancia total: suma de todo lo recorrido, sin cancelar movimientos en sentidos opuestos.

3. EJEMPLO PRINCIPAL
Considera un móvil con:
v(t) = t − 2, para 0 ≤ t ≤ 4.
El tiempo se mide en segundos, la velocidad en metros por segundo y la posición inicial es x(0) = 0 metros.

Muestra que:
- Entre 0 y 2 segundos, la velocidad es negativa.
- En t = 2 segundos, la velocidad es cero y el móvil cambia de sentido.
- Entre 2 y 4 segundos, la velocidad es positiva.

Presenta una gráfica velocidad-tiempo y un móvil sobre una recta. Si los muestras simultáneamente, sincroniza sus movimientos. La posición correspondiente es x(t) = t²/2 − 2t: parte en 0, llega a −2 metros y vuelve a 0. No animes el movimiento con rapidez constante.

4. CÁLCULO VISUAL
Calcula los resultados usando áreas de triángulos, sin depender de antiderivadas:
- Primer triángulo: base de 2 segundos y altura de 2 m/s; área geométrica de 2 metros y aporte al desplazamiento de −2 metros.
- Segundo triángulo: las mismas dimensiones; aporte al desplazamiento de +2 metros.
- Desplazamiento total: −2 + 2 = 0 metros.
- Distancia total: 2 + 2 = 4 metros.

Aclara que las áreas geométricas son positivas; el signo corresponde al aporte de la integral.

5. CONEXIÓN CON LA INTEGRAL
Introduce:
Desplazamiento = ∫₀⁴ v(t) dt = 0 m.
Distancia total = ∫₀⁴ |v(t)| dt = 4 m.

Explica intuitivamente las sumas de Riemann: en un intervalo pequeño, velocidad × duración aproxima el cambio de posición. Al sumar esos aportes y refinar la partición se obtiene la integral.

Muestra cómo el valor absoluto refleja sobre el eje horizontal la parte negativa de la gráfica de velocidad. Así, los aportes a la distancia son positivos.

Aclara que:
- Una integral de velocidad igual a cero no significa que el móvil permaneció quieto.
- La integral de velocidad entrega el desplazamiento; para obtener la posición final se suma la posición inicial.
- La distancia total no es, en general, el valor absoluto del desplazamiento.

6. CIERRE Y COMPROBACIÓN
Responde directamente la pregunta central.
Luego pregunta: “Si el móvil solamente se mueve en sentido negativo, ¿coinciden su desplazamiento y su distancia?”.
Explica que el desplazamiento es negativo y la distancia positiva; coinciden en magnitud.

Indicaciones visuales:
- Usa ejes, unidades y etiquetas legibles.
- Diferencia con colores los aportes negativos y positivos, acompañados de signos y texto.
- Presenta una idea por escena y sincroniza la explicación con lo mostrado.
- Incluye pausas breves para pensar.
- Termina con una comparación clara: desplazamiento = 0 m; distancia = 4 m.

Fidelidad a las fuentes:
No inventes referencias ni atribuciones. Distingue el ejemplo propuesto de los ejemplos de los documentos y utiliza solamente las fuentes disponibles para los créditos.
```
