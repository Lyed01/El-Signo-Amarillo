label branch_thomas_scene12:

    # Comienza con la bruma exterior y el ambiente tenso
    scene bg_plaza_bruma with fade
    play ambient "morning_mist.ogg" fadein 2.0

    "La bruma matinal se espesaba sobre la plaza."
    "Las campanas lejanas resonaban con un eco hueco."
    "El aire olía a carbón y humedad."

    show scott normal at left
    show thomas normal at right

    "SCOTT permanecía junto a THOMAS, ambos frente a la ventana, observando la plaza bajo la neblina."

    # Scott decides
    sc "(voz baja, firme) Vamos a la iglesia."

    th "(sorprendido) ¿A la iglesia, señor?"
    th "No creo que el régimen vea con buenos ojos que entremos sin permiso."

    show scott determined at left
    sc "Precisamente por eso. Quiero ver qué esconden ahí dentro."

    "THOMAS lo miró con respeto y temor."
    "El aire parecía cargado de advertencias, pero obedeció sin más."

    # Salida del edificio
    scene bg_stairs with dissolve
    play sound "steps_stairs.ogg"

    "Salieron al pasillo, descendiendo las escaleras del edificio."
    "El sonido de sus pasos se mezclaba con la lluvia fina que empezaba a caer sobre los adoquines."

    # Atrio de la iglesia
    scene bg_iglesia_atrio_bruma with fade
    play ambient "rain_light.ogg" fadein 1.5

    "El atrio de la antigua iglesia se alzaba ante ellos como una herida abierta en la piedra."
    "Las banderas del régimen colgaban flácidas, mudas bajo la lluvia."

    "La puerta metálica, antes ornamentada, mostraba ahora el sello oficial grabado sobre el escudo:"
    "un ojo rodeado de laureles, símbolo de la vigilancia absoluta."

    # Abrir el portón
    play sound "metal_door_creak.ogg"

    "Scott empujó el portón."
    "El chirrido del metal reverberó en el interior, rompiendo el silencio."

    scene black with slow_fade

    "CORTE A NEGRO."

    return