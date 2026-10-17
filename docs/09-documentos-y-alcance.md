# Documentos originales y alcance de este avance

Revisión: 17 de octubre de 2026, zona America/Santiago.

## Repositorio identificado

La carpeta de trabajo es un clon Git cuyo remoto `origin` es
<https://github.com/bedelafuente/eidCalculoIntermedio.git>. El propietario indicado
por esa URL es **bedelafuente**. La configuración local de autor es **juan-xp**;
son datos distintos. El punto de partida de este avance es
`63340b53e2e9a254c9f776b79662915afaf3ff1b` en `main`.

El trabajo se desarrolla en **dev/grupo-16-video**, creada directamente desde
`main` en el commit indicado. No se mezcla con `main`.

La API de GitHub confirmó el 17 de octubre de 2026 que el repositorio tiene
visibilidad **pública**, rama predeterminada `main` y permiso de escritura para
la cuenta conectada.

## Identificación de los tres archivos

Los originales se leyeron desde la carpeta Downloads. Se extrajo su texto y se
revisaron visualmente las páginas del tema, los criterios del video y la pauta.
No se incorporan los PDF originales al repositorio, que ya excluye esos archivos.

| Archivo | Identificación | Páginas relevantes | Uso en este avance |
| --- | --- | --- | --- |
| `EID_calculo_intermedio (2).pdf` | Temas y preguntas centrales por grupo, MAT1188 | 6 de 7: solo apartado del grupo 16 | Tema, pregunta y requisitos del ejemplo |
| `EID_calculo_intermedio (3).pdf` | Evaluación Integrada de Desempeño, pauta común | 1, 2 y 4 de 4 | Video, fuentes, repositorio y documentación de entrega |
| `EID_calculo_intermedio (6).pdf` | Rúbrica de evaluación del EID | 1-3 de 4: escala de video y V1-V8 | Revisión del video, hasta 40 puntos |

Identificadores SHA-256 de los originales consultados:

```text
(2) 07077fcfab1fd5fa3473cf35f01a5f3dd3fedc5c527ed4757602bdd748ee2ab5
(3) ce9df3c9f3377cc77e77a1fc126bf69aef69e8f696040e8673f6555be875f395
(6) f83283a560b9b5512dfd1381cb4059ce4f5079500414c441aac86d7ddcd0f4b4
```

La rúbrica y la pauta ya tenían transcripciones en `03-rubrica-evaluacion.md` y
`01-pauta-proyecto.md`. El apunte `02-introduccion-integral.md` también estaba en
el repositorio y declara proceder de otro PDF, `(5)`, no de uno de los tres
adjuntos de esta solicitud. Se usa esa transcripción como apunte base; no se
afirma haber revisado ahora su PDF original.

Los tres enlaces a figuras de esa transcripción apuntan a archivos ausentes en
el clon. La revisión del apunte se limita a su texto; las figuras del video se
generan con Manim y no dependen de esos archivos.

## Grupo 16

**Tema:** distancia recorrida y desplazamiento.

**Pregunta central:** ¿Por qué integrar velocidad puede dar un resultado distinto
de la distancia total recorrida?

El apartado exige movimiento en una dimensión con cambio de signo de velocidad,
distinción entre desplazamiento y distancia, y conexión con acumulación con signo
y acumulación de magnitudes positivas. No se incluyen los temas de los grupos
que aparecen antes o después en la página.

## Aplicación de los documentos

La solicitud del usuario define el alcance: preparar el video del grupo 16 y
publicar el progreso en una rama separada. Las instrucciones académicas de los
PDF se utilizan como requisitos del producto dentro de ese alcance.

Se revisa **solo el componente de video V1-V8**, con escala 0, 0,5 o 1 por
indicador. D1-D6 corresponden a defensa oral y no se utilizan para calificar ni
ampliar este trabajo. No se asigna una nota anticipada: un guion o un render sin
voces no acredita una explicación narrada.

Requisitos concretos de la pauta que afectan al video:

- MP4 entre 4 y 6 minutos, incluyendo presentación y créditos.
- Tres integrantes, cada uno con explicación matemática sustantiva y voz propia,
  identificado por nombre. No basta con saludar o leer créditos.
- Tema y pregunta central, teoría, ejemplo propio, Manim Community, respuesta y
  créditos legibles; lenguaje accesible sin técnicas de integración previas.
- Al menos dos fuentes matemáticas complementarias, apunte, documentación oficial
  de Manim, recursos adaptados y declaración de IA con verificación.
- Repositorio público reproducible y ficha PDF con datos, duración, enlace y SHA
  de la versión que realmente corresponda al video final.
- Archivos finales: `MAT1188_EID_G16_2026.mp4` y `MAT1188_EID_G16_2026.pdf`.
- La pauta fija la entrega final el **18 de octubre de 2026 a las 23:59**.

El código de ética es una entrega independiente indicada por la pauta, con plazo
del 6 de octubre. Este avance no acredita su entrega ni aceptación firmada. No
se inventan firmas, cuentas de GitHub ni participaciones efectivamente realizadas.
Tampoco se realiza una entrega a Blackboard desde este repositorio.
