label esc_16C_3:

    scene black with fade

    n "La penumbra del sótano permanecía suspendida, solo interrumpida por el eco de los pasos del funcionario que se alejaban por la escalera."
    n "La linterna de THOMAS temblaba en su mano, su luz oscilante recorriendo los lienzos, los diarios antiguos, los símbolos dorados sobre la piedra."
    n "Entre los escombros, un reflejo metálico atrajo la mirada de SCOTT."
    n "Se inclinó. Sus dedos tocaron algo frío y pesado."
    n "Un revólver antiguo, limpio de polvo, reposaba entre los restos de una caja rota."
    n "Scott lo levantó. El metal reflejaba un destello tenue, casi solemne."

    show tho at left
    th "¿Qué hacemos con esto, señor?"

    n "Scott permaneció inmóvil. El arma pesaba más de lo que parecía."
    n "El silencio del sótano se volvió denso, expectante."
    n "SCOTT cerró los ojos un instante."
    n "La decisión lo atravesaba más allá del gesto físico: cada elección arrastraba un futuro distinto."
    n "La ciudad vigilada, los símbolos prohibidos, la fragilidad de Tessie… todo se entrelazaba con ese objeto frío."

    # --- MENÚ DE DECISIÓN ---
    menu:
        "Tomar el arma":
            jump esc_16_opcion_tomar

        "Dejar el arma":
            jump esc_16_opcion_dejar


# ----------------------
# RUTA: TOMAR EL ARMA
# ----------------------
label esc_16_opcion_tomar:

    n "Scott apretó los dedos alrededor del revólver."

    show sc1 at left
    sc "La tomo."

    n "Su respiración era tensa, pero su mirada permanecía fija, decidida."
    n "THOMAS asintió sin palabras."
    n "Por un instante, la penumbra pareció retroceder ante la resolución."
    n "Cada sombra del sótano se volvió menos amenazante, pero una nueva tensión se instaló."
    n "Ahora portaban un medio de defensa, y también una responsabilidad."
    n "Scott sabía que el arma cambiaría el curso de todo lo que viniera después."
    n "La urgencia y la premonición se mezclaban en su pecho."

    scene black with fade
    return


# ----------------------
# RUTA: DEJAR EL ARMA
# ----------------------
label esc_16_opcion_dejar:

    n "Scott dejó el revólver en la caja."

    show sc1 at left
    sc "No lo necesito."

    show tho at right
    th "¿Está seguro, señor?"

    sc "Sí. No quiero que esto cambie quién soy… ni lo que debo hacer."

    n "Thomas guardó silencio."
    n "El sótano parecía escucharlos."
    n "La oscuridad se mantuvo inmóvil, como si aprobara la elección."
    n "Scott sintió una mezcla de alivio y vulnerabilidad."
    n "No tener un arma lo hacía más humano, pero también más expuesto."
    n "La sensación de peligro era más nítida, más cercana."

    scene black with fade
    return