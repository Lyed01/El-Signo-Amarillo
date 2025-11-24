label esc_20B_2A:

    scene bg campo_fusilacion with fade
    play ambient "wind.ogg" fadein 2.0

    "La neblina cubre el campo como una sábana húmeda. El aire es frío, cortante, casi inmóvil."

    show scott_tied at center
    "En el centro, SCOTT está de pie frente a un muro descascarado, las manos atadas. Su camisa blanca está oscurecida por el rocío."

    "A lo lejos, los pasos acompasados de un pelotón se acercan."
    play sound "march.ogg"

    "El sonido metálico de los fusiles rompe el silencio, marcando los últimos segundos."

    "SCOTT mira hacia el horizonte. Apenas hay luz, solo una línea tenue donde comienza a aclarar el cielo."

    "Por un instante, cierra los ojos. Tal vez recuerde su estudio… la textura del óleo en sus dedos…"
    "O tal vez imagine a Tessie leyendo esta noticia."

    scene black with fade
    play sound audio.sfx_disparos
    scene bg campo_fusilacion with fade
    "El estruendo corta el amanecer."
    "Las aves levantan vuelo desde los muros."
    "El humo de la pólvora se disipa lentamente."

    hide scott_tied
    show scott_body at center

    "Cuando la bruma vuelve a cubrir el patio, el cuerpo de SCOTT yace inmóvil, recostado contra la pared."

    scene black with fade
    "Solo queda el silencio. El mismo que acompañó a Scott desde su estudio hasta este final inevitable."

    return
