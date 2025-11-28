label esc_2B:

# Entrar al recuerdo
    scene black 
    play sound audio.sfx_transicion

    # Narración inicial
    n "La luz gris del cielo se filtraba entre las ramas altas del bosque, dibujando líneas plateadas sobre el suelo húmedo."
    n "El aire olía a tierra mojada, a musgo viejo, a una calma que parecía no pertenecer al mundo real."

    scene bg calle_feliz 
    play ambience "bosque_viento.ogg" fadein 2.0

    show scott_nino at center
    with dissolve

    n "El pequeño Scott corría entre los árboles, riendo en silencio, como si temiera romper algún hechizo secreto."

    n "A su alrededor, el bosque parecía responder a cada movimiento suyo. Las ramas se arqueaban, las sombras danzaban, y el viento murmuraba un idioma antiguo."

    scott_nino "Ya casi los veo…"

    n "En un claro iluminado, figuras indefinidas parecían bailar: un ciervo con astas imposibles, una sombra que respiraba, un rostro hecho de hojas y niebla."

    n "Scott no sentía miedo. Solo una extraña familiaridad. Como si el bosque siempre hubiese sido su verdadero hogar."

    # Voz de la madre fuera de escena
    voice "madre_llamando.ogg"
    madre "¡Scott! ¡Es hora de volver!"

    n "El niño miró el claro una última vez. Las figuras se desvanecieron lentamente."

    scott_nino "Volveré…"

    hide scott_nino with dissolve

    n "Scott corrió hacia la voz de su madre, mientras la neblina del claro giraba un segundo más, como si escuchara su promesa."

    stop ambience fadeout 3.0
    scene black with fade

    n "El bosque quedó en silencio, guardando sus secretos."

    return