label esc_27C_4:    #iglesia tessie DECISION

    scene bg estudioNoche with fade

    n "La habitación estaba en calma, iluminada apenas por la luz vacilante de la lámpara."
    n "El libro amarillo descansaba sobre la mesa, su presencia imponía una gravedad que llenaba el aire."
    n "Cada símbolo que Scott había visto en la iglesia seguía ardiendo en su mente."
    n "Fuera, la lluvia continuaba cayendo."
    n "El sonido se filtraba por la ventana como un eco persistente, mezclado con el rumor distante de motores y patrullas."
    n "Tessie lo observaba en silencio."
    n "Su rostro, iluminado por la lámpara, mezclaba determinación y miedo."

    te "Tenemos que volver a la iglesia. No podemos dejar esto sin comprobar."

    n "Scott permaneció quieto."
    n "Su mirada fija en el libro, los dedos apoyados sobre el borde de la mesa."
    n "Respiró hondo."
    n "La habitación parecía encogerse."
    n "El aire estaba tan denso que el zumbido de la lámpara sonaba como una advertencia."
    n "El pensamiento lo dividía en dos direcciones: si se quedaban, tal vez la seguridad de Tessie persistiría, pero a costa de ignorar un peligro que crecía con cada hora."
    n "Si volvían a la iglesia, el riesgo sería total, y algo en su interior le decía que ya no habría retorno."
    n "Scott levantó la vista."
    n "El reflejo dorado del libro le tembló en las pupilas."

    menu:
        "Ir a la iglesia":
            $ irJuntos = True
            jump escena_27_opcion_1
            
        "Quedarse":
            $ irJuntos = False
            jump escena_27_opcion_2
           


# ================================
# OPCIÓN 1 – IR A LA IGLESIA
# ================================

label escena_27_opcion_1:

    sc "(decidido) Está bien. Si tenemos que hacerlo, será ahora. Pero no daré un paso sin saber a qué nos enfrentamos."

    n "Tessie asintió, aliviada, aunque en su mirada brillaba una sombra de temor."
    n "Ambos comenzaron a prepararse en silencio, tomando abrigos, lámparas y los papeles que Scott había guardado."
    n "La ciudad los esperaba afuera, gris y vigilante, como un testigo que conocía su destino."
    n "La lluvia se volvió más intensa."
    n "El libro amarillo quedó sobre la mesa, abierto, sus símbolos brillando débilmente bajo la luz."

    return


# ================================
# OPCIÓN 2 – QUEDARSE
# ================================

label escena_27_opcion_2:

    n "Scott cerró los ojos, exhalando con lentitud."

    sc "No. No esta noche. Ya vimos demasiado."

    n "Tessie frunció el ceño, dolida pero sin discutir."

    te "¿Y si alguien más entra allí? ¿Si todo desaparece?"

    sc "(de forma firme) Entonces no seremos nosotros los que lo provoquemos."

    n "Se sentó junto a la mesa, la mirada perdida en el libro que ahora parecía observarlos."
    n "El silencio se instaló entre ambos."
    n "Solo la lluvia y el zumbido de la lámpara llenaban el cuarto con su insistencia."

    n "La cámara se aleja lentamente: Tessie de pie, Scott sentado, y entre ellos, el libro."
    n "Abierto, inmóvil, como si esperara una decisión distinta."

    scene black with fade

    return
