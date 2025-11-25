label esc_19B_2B:

    scene bg calle_noche with fade
    play ambient "wind_car_road.ogg" fadein 1.5

    "El sol se hunde lentamente detrás de los campos dorados."
    "El auto de SCOTT avanza por una carretera vacía, flanqueada por árboles que parecen observarlos en silencio."

    show sc1 at left
    show te1 at right

    "Dentro, el aire es espeso, cargado de cansancio y expectativa."

    "TESSIE, apoyada contra la ventanilla, deja escapar un suspiro. Busca algo en el asiento trasero y encuentra un libro cubierto de polvo, con la portada desvanecida."

    te "(confundida) Scott… ¿habías traído esto?"

    sc "(levantando la vista, distraído) ¿El qué?"

    "TESSIE sostiene el libro a la luz del sol. La portada está desvanecida."

    te "(leyendo apenas) No tiene título… parece antiguo."

    "TESSIE levanta un poco más el libro. En la tapa se distingue un relieve tenue, un símbolo que parece moverse bajo la superficie."

    sc "…No… no lo recuerdo. ¿Dónde lo encontraste?"

    te "Estaba junto al bolso."

    "Sin esperar respuesta, TESSIE abre el libro."

    play sound audio.theme_main

    "El papel amarillento exhala un polvo fino."

    "Sus ojos recorren las primeras líneas. Su expresión cambia: primero curiosidad… luego un desconcierto helado."

    te "(leyendo en voz baja) “El que contempla el Signo Amarillo queda ligado al destino del rey que no muere…”"

    # Efecto visual del Signo Amarillo brillando
    show yellow_sign_glow at center with dissolve
    pause 1.2
    hide yellow_sign_glow with fade

    "Un escalofrío atraviesa el interior del auto, aunque ninguna de las ventanas esté abierta."

    return
