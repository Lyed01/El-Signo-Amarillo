label esc_17:

    scene atrio_iglesia_lluvia with fade
    play sound "audio/lluvia_suave.ogg"

    # Ascenso desde el sótano
    n "El eco de los pasos del funcionario aún flotaba en el aire cuando Scott ascendió por la escalera del sótano."
    n "La linterna de Thomas temblaba a su espalda."
    n "La luz de los vitrales rotos proyectaba figuras amarillentas sobre las losas húmedas, formas que se movían con lentitud, como si tuvieran voluntad propia."

    # Branch: Scott tiene el revólver o no
    if scott_tiene_revolver:
        n "Scott llevaba el revólver en la mano."
    else:
        n "Scott llevaba el vacío en el bolsillo, según la decisión tomada."

    n "Cada paso aumentaba la sensación de que algo invisible lo seguía desde las sombras."

    # Llegada al atrio
    n "Al llegar al atrio, una corriente de aire helado le rozó la nuca."
    n "Cerró los ojos un instante."
    n "Entonces lo vio."

    # Visión de Tessie
    scene vision_tessie with dissolve
    n "Una visión fugaz lo atravesó: Tessie, sola, bajo la lluvia, la ropa empapada, el rostro vuelto hacia un punto que él no podía ver."
    n "Sobre su pecho brillaba un símbolo dorado, idéntico al descubierto en los vitrales."
    n "La imagen se desvaneció tan rápido como había llegado."

    scene atrio_iglesia_lluvia with dissolve

    n "Scott quedó inmóvil, el corazón acelerado, la mente repitiendo el destello como una advertencia."

    # Diálogo de Scott
    sc "Tessie…"

    n "El miedo se mezcló con la culpa. La había dejado sola."
    n "Y ahora esa visión lo empujaba a creer que todo lo que habían desenterrado podía alcanzarla."

    # Thomas observa
    n "En el umbral, Thomas observaba a su patrón, intuyendo que algo lo había sacudido."

    # Salida al exterior
    scene exterior_lluvia_iglesia with fade

    n "Scott salió al exterior."
    n "La lluvia lo golpeó de lleno."
    n "La ciudad se extendía frente a él, gris, empapada, silenciosa."
    n "Cada farol proyectaba una sombra distinta, cada charco reflejaba una forma que parecía moverse."

    n "Scott miró hacia ambos lados de la calle. La premonición seguía viva en su mente."

    sc "No puedo perder tiempo… Tengo que volver."

    n "La cámara se aleja mientras él desciende los escalones del atrio."
    n "Thomas lo sigue con paso inseguro, la lluvia cayendo sobre ambos, mientras la bruma de la ciudad los engulle lentamente."
    n "El futuro de Tessie —y el suyo— pendían ahora de una sola decisión."

    return