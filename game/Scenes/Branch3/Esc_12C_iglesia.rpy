label esc_12C_3: #iglesia

    # Comienza con la bruma exterior y el ambiente tenso
    scene bg plaza_iglesia with fade

    "La bruma matinal se espesaba sobre la plaza."
    "Las campanas lejanas resonaban con un eco hueco."
    "El aire olía a carbón y humedad."


    "SCOTT permanecía junto a THOMAS, ambos frente a la ventana, observando la plaza bajo la neblina."

    # Scott decides
    show sc1 at left
    sc "(voz baja, firme) Vamos a la iglesia."

    
    show tho at right
    th "(sorprendido) ¿A la iglesia, señor?"
    th "No creo que el régimen vea con buenos ojos que entremos sin permiso."

    sc "Precisamente por eso. Quiero ver qué esconden ahí dentro."

    "THOMAS lo miró con respeto y temor."
    "El aire parecía cargado de advertencias, pero obedeció sin más."

    # Salida del edificio
    scene bg sotano_iglesia with dissolve
    play sound audio.sfx_agente_escalera

    "Salieron al pasillo, descendiendo las escaleras del edificio."
    "El sonido de sus pasos se mezclaba con la lluvia fina que empezaba a caer sobre los adoquines."

    # Atrio de la iglesia
    scene bg atrio with fade

    "El atrio de la antigua iglesia se alzaba ante ellos como una herida abierta en la piedra."
    "Las banderas del régimen colgaban flácidas, mudas bajo la lluvia."

    "La puerta metálica, antes ornamentada, mostraba ahora el sello oficial grabado sobre el escudo:"
    "un ojo rodeado de laureles, símbolo de la vigilancia absoluta."

    # Abrir el portón
    play sound "metal_door_creak.ogg"

    "Scott empujó el portón."
    "El chirrido del metal reverberó en el interior, rompiendo el silencio."

    scene black with fade

    "CORTE A NEGRO."

    return