# =====================================================
# CHARACTERS.RPY — PERSONAJES PRINCIPALES (ESC. 1–6)
# Project: El Signo Amarillo (Visual Novel)
# =====================================================

# -----------------------------------------------------
# NARRADOR
# -----------------------------------------------------

define n = Character(
    None,                      # No se muestra nombre
    what_color = "#e6e6e6",    # Color del texto del narrador
    window_yalign = 0.85       # Ubicación del cuadro de texto
)


# -----------------------------------------------------
# PERSONAJES PRINCIPALES
# -----------------------------------------------------

define sc = Character(
    "Scott",
    color = "#ff0000",
    what_prefix = "«",
    what_suffix = "»"
)

define scott_nino = Character(
    "Scotty",
    color = "#a8c9ff",
    what_prefix = "«",
    what_suffix = "»"
)

define madre = Character(
    "Mama",
    color = "#efb1de",
    )

define modelo = Character(
    "Rosi",
    color = "#b42ee5", 
)

define soldado = Character(
    "soldado",
    color = "#490000",
)

define general = Character(
    "general",
    color = "#490000",
)

define te = Character(

    "Tessie",
    color = "#f5c2e7",
    )

define th = Character(
    "Thomas",
    color = "#a6d189",
)


# -----------------------------------------------------
# PERSONAJES SECUNDARIOS (abreviaturas usadas en escenas)
# -----------------------------------------------------

define md = Character(
    "Médico",
    color = "#c9d1ff",
)

define ag = Character(
    "Agente",
    color = "#d1c9c9",
)

define of = Character(
    "Oficial",
    color = "#d1d1c9",
)

define es = Character(
    "Espía",
    color = "#c9d1b5",
)


# -----------------------------------------------------
# OPCIONAL — PARA FUTUROS TEXTOS (Libro, documentos)
# -----------------------------------------------------

define doc = Character(
    None,
    what_color = "#f9ffb5",
    what_prefix = "«",
    what_suffix = "»"
)
