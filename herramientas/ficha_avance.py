"""Genera una ficha PDF de avance, marcada como borrador y sin afirmar entrega.

Ejecutar: python -m herramientas.ficha_avance
Dependencia opcional: requirements-documentos.txt.
"""

import argparse
from pathlib import Path
import re
import subprocess
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak,
)

from video_plan import CURSO, GRUPO, INTEGRANTES, PREGUNTA, DURACION_TOTAL


REPO = "https://github.com/bedelafuente/eidCalculoIntermedio"
RAMA = "dev/grupo-16-video"
RAIZ = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sha", help="Commit de código de 40 caracteres; por defecto HEAD")
    parser.add_argument("--salida", type=Path,
                        default=RAIZ / "output/pdf/MAT1188_EID_G16_2026_borrador.pdf")
    args = parser.parse_args()
    sha = args.sha or subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=RAIZ, text=True,
    ).strip()
    if not re.fullmatch(r"[0-9a-fA-F]{40}", sha):
        parser.error("El SHA debe tener 40 caracteres hexadecimales.")
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle("TituloFicha", parent=styles["Title"],
                              fontSize=21, leading=25, textColor=colors.HexColor("#163351")))
    styles.add(ParagraphStyle("Aviso", parent=styles["Normal"],
                              fontSize=11, leading=15, textColor=colors.HexColor("#8A2E20"),
                              spaceAfter=12))
    styles["Normal"].fontSize = 10
    styles["Normal"].leading = 14
    styles["Normal"].spaceAfter = 8
    styles["Heading2"].textColor = colors.HexColor("#163351")
    styles["Heading2"].spaceBefore = 12
    styles["Heading2"].spaceAfter = 8
    styles.add(ParagraphStyle("Pie", parent=styles["Normal"], fontSize=8,
                              leading=10, alignment=TA_CENTER))

    def p(texto, estilo="Normal"):
        return Paragraph(texto, styles[estilo])

    def enlace(etiqueta, url):
        return f'<link href="{escape(url, {chr(34): "&quot;"})}" color="#225F91">{escape(etiqueta)}</link>'

    story = [p("Evaluación Integrada de Desempeño", "TituloFicha"),
             p("Ficha de avance - Grupo 16", "Heading2"),
             p("BORRADOR: el video base no tiene narración. Esta ficha no acredita "
               "la participación oral, la entrega final ni el cumplimiento completo de la rúbrica.", "Aviso")]
    datos = [
        ("Asignatura", f"{CURSO} - Cálculo Intermedio"),
        ("Grupo / año", f"{GRUPO} / 2026"),
        ("Integrantes", "<br/>".join(escape(n) for n in INTEGRANTES)),
        ("Cuentas de GitHub", "Pendientes de confirmación por el equipo"),
        ("Tema", "Distancia recorrida y desplazamiento"),
        ("Duración de la base", f"{DURACION_TOTAL // 60}:00 minutos; duración final pendiente de verificar"),
        ("Rama", RAMA),
    ]
    tabla = Table([[p(f"<b>{a}</b>"), p(b)] for a, b in datos],
                  colWidths=[43 * mm, 125 * mm], hAlign="LEFT")
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EDF3F8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCD8E3")),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#CCD8E3")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
    ]))
    story += [tabla, p("Pregunta central", "Heading2"), p(escape(PREGUNTA)),
              p("Resultado del ejemplo", "Heading2"),
              p("Ida de 15 m, pausa de 10 s y regreso de 15 m. En 40 s de tiempo "
                "modelado: desplazamiento = 15 + 0 - 15 = 0 m; distancia = "
                "15 + 0 + 15 = 30 m. La integral de velocidad acumula con signo; "
                "la de rapidez acumula magnitudes no negativas."),
              p("Repositorio y versión del código", "Heading2"),
              p(enlace(REPO, REPO)), p(f"SHA del código de este avance: <b>{sha}</b>"),
              p("La ficha final debe registrar el SHA del código que corresponda al MP4 "
                "narrado. Este SHA identifica el avance, no una entrega académica final."),
              PageBreak(), p("Fuentes y documentación", "TituloFicha")]
    fuentes = [
        ("Gilbert Strang y Edwin Jed Herman (2016). Calculus Volume 1. OpenStax. "
         "Secciones 5.2 (integral definida) y 5.4 (cambio neto).",
         "https://openstax.org/books/calculus-volume-1/pages/5-4-integration-formulas-and-the-net-change-theorem"),
        ("Grant Sanderson, 3Blue1Brown (2017). Integration and the fundamental "
         "theorem of calculus. Adaptación textual: Kurt Bruns.",
         "https://www.3blue1brown.com/lessons/integration/"),
        ("Manim Community (documentación continua). Versión utilizada: 0.22.0.",
         "https://docs.manim.community/en/stable/"),
    ]
    for texto, url in fuentes:
        story += [p(escape(texto)), p(enlace("Consultar fuente: " + url.split("/")[2], url))]
    story += [
        p("Apunte base del curso: Introducción a la integral, s. f.; autoría no "
          "identificada en la transcripción. Registro: docs/02-introduccion-integral.md."),
        p("Referencias completas: " + enlace("docs/06-fuentes.md", REPO + "/blob/" + sha + "/docs/06-fuentes.md")),
        p("Declaración de IA y verificación", "Heading2"),
        p("Asistente de programación de OpenAI: apoyo en guion, plan temporal, "
          "escenas, documentación y comprobaciones. NotebookLM figura como apoyo "
          "de estudio previo en el registro del proyecto; el equipo debe confirmar "
          "sus usos efectivos. No se han generado voces de los estudiantes."),
        p("Se contrastaron las relaciones matemáticas con fuentes identificadas, "
          "se calcularon áreas y posiciones, se ejecutaron las ocho pruebas del "
          "modelo y se revisaron fotogramas del render. El equipo aún debe revisar "
          "la narración real, el audio y la versión final."),
        p("Cómo localizar los respaldos", "Heading2"),
    ]
    for ruta in ("docs/10-guion-video.md", "docs/11-revision-video.md", "docs/12-estado-del-avance.md"):
        story.append(p(enlace(ruta, REPO + "/blob/" + sha + "/" + ruta)))
    story += [p("Antes de entregar", "Heading2"),
              p("Confirmar cuentas de GitHub; grabar las tres voces propias; sincronizar "
                "y comprobar audio; verificar MP4 de 4 a 6 minutos; completar ficha "
                "final y nombres MAT1188_EID_G16_2026; comprobar acceso público; "
                "cargar MP4 y ficha por separado en Blackboard. La entrega/aceptación "
                "del PDF de ética independiente debe confirmarla el equipo.")]

    def pie(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#657789"))
        canvas.drawString(20 * mm, 12 * mm, "Grupo 16 - Ficha de avance, pendiente de narración")
        canvas.drawRightString(190 * mm, 12 * mm, f"Página {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(args.salida), pagesize=(210*mm, 297*mm),
                            rightMargin=20*mm, leftMargin=20*mm,
                            topMargin=17*mm, bottomMargin=20*mm,
                            title="EID MAT1188 - Grupo 16 - Ficha de avance", author="Grupo 16")
    doc.build(story, onFirstPage=pie, onLaterPages=pie)
    print(args.salida)


if __name__ == "__main__":
    main()
