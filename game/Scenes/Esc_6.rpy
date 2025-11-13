label esc_6:

    scene bg estudio_noche with fade

    n "El humo flota pesado sobre la mesa."
    n "El aire huele a aguarrás y miedo."
    n "La pintura, todavía húmeda, refleja un brillo enfermo bajo la luz del farol."

    n "Tessie aparta la cabeza y apoya las manos sobre la mesa."
    n "Tiembla. Sus ojos húmedos relucen a la luz tenue."
    n "La respiración se acelera, entrecortada."

    te "¡No puedo…! Siento que algo terrible va a pasar…"

    n "Scott permanece quieto, observándola con atención."
    n "Cada gesto, cada espasmo de sus manos, es un reflejo de terror genuino."
    n "La tensión del estudio se hace física; el silencio, insoportable."

    sc "(voz baja) Tranquila, Tessie…"

    n "Ella niega con la cabeza. El cigarrillo cae al suelo y deja una brasa que se apaga lentamente."

    te "No puedo respirar… No puedo…"

    n "Scott se levanta, da un paso hacia ella."
    n "El crujido del piso rompe el silencio."
    n "Su sombra se proyecta sobre la pared, deformada, como si el estudio mismo los observara."

    n "Tessie se encoge, temblando."
    n "El sonido lejano de una sirena del régimen corta el aire."

    n "Scott comprende que debe actuar antes de que la ansiedad la consuma."

    # Corte a negro
    scene black with fade

    # ============================
    # MENU DE CALMA — DESBLOQUEADO SEGÚN BRANCH
    # ============================

    n "¿Cómo debería Scott calmarla?"

    menu:

        # ------ BRANCH 1 ------
        "Recomendar a Tessie salir de la ciudad unos días. (BRANCH 1)" if branch == 1:
            $ decision_6 = "salir_ciudad"
            jump post_esc6

        # ------ BRANCH 2.1 ------
        "Invitarla a tomarse un tiempo junto a la ventana, con algo de tabaco. (BRANCH 2.1)" if branch == 21:
            $ decision_6 = "ventana_tabaco"
            jump post_esc6

        # ------ BRANCH 2 ------
        "Recomendarle pasar unos días en el campo; transmitirle serenidad y apoyo. (BRANCH 2)" if branch == 2:
            $ decision_6 = "campo_serenidad"
            jump post_esc6

        # ------ BRANCH 3 ------
        "Contarle la historia de un país sin represión. (BRANCH 3)" if branch == 3:
            $ decision_6 = "historia_pais"
            jump post_esc6

    return


# =====================================
# SECCIÓN POST-DECISIÓN / PUENTE DRAMÁTICO
# (Recomendado: cambia esto como quieras)
# =====================================

label post_esc6:

    if decision_6 == "salir_ciudad":
        n "Scott, con voz contenida, le sugiere a Tessie que abandone la ciudad unos días..."
        # (Podés expandir después)

    elif decision_6 == "ventana_tabaco":
        n "Scott la guía hacia la ventana, dejándole un cigarrillo para estabilizar el temblor..."
        # (Podés expandir después)

    elif decision_6 == "campo_serenidad":
        n "Scott le habla con calma y le propone unos días en el campo, lejos del gris y las patrullas..."
        # (Podés expandir después)

    elif decision_6 == "historia_pais":
        n "Scott respira hondo y empieza a hablarle de un país sin represión, casi como si lo hubiera visto..."
        # (Podés expandir después)

    return
