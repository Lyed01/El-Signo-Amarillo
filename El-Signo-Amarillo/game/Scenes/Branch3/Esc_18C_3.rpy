label esc_18C:

    scene lluvia_plaza with fade

    n "La lluvia caía con persistencia sobre la plaza vacía. Los faroles amarillos parpadeaban entre la bruma, y el sonido de los motores lejanos se confundía con el murmullo del viento."
    n "SCOTT permanecía frente a la puerta de la iglesia, la visión de TESSIE aún grabada en su mente. El agua le corría por el rostro, mezclándose con el sudor y la culpa."
    n "THOMAS lo observaba en silencio, los hombros encogidos bajo el abrigo mojado."

    show tho at left
    th "¿Y ahora, señor?"

    n "SCOTT no respondió. La imagen de TESSIE bajo la lluvia, con el símbolo brillando sobre su pecho, lo perseguía con una claridad insoportable."
    n "El tiempo pesaba. Cada segundo que dudaba podía ser demasiado tarde."
    n "THOMAS dio un paso atrás, inquieto."

    th "Yo no puedo seguirlo, señor. Ya he hecho demasiado. No me corresponde saber más."

    n "SCOTT lo miró apenas, comprendiendo sin necesidad de palabras."

    show sc1 at right
    sc "Entiendo."

    n "THOMAS asintió una última vez y se alejó bajo la lluvia, su figura desvaneciéndose entre la niebla."
    n "SCOTT quedó solo. La ciudad parecía observarlo, expectante."
    n "Frente a él, dos caminos se abrían, invisibles pero definidos por su conciencia."

    menu:
        "Ignorar la premonición":
            jump esc_18_op1

        "Ir al hospedaje de Tessie":
            jump esc_18_op2


# ----------- OPCIÓN 1: IGNORAR LA PREMONICIÓN -----------

label esc_18_op1:

    scene lluvia_calles with fade

    n "SCOTT levantó la vista hacia los tejados del distrito y exhaló con cansancio."

    sc "No puedo vivir con cada imagen que me muestra mi cabeza. Quizá… nada de esto sea real."

    n "Giró sobre sus pasos y comenzó a caminar hacia su departamento."
    n "El sonido de la lluvia acompañaba su resignación."
    n "Cada reflejo en los charcos parecía mirarlo pasar, como si la ciudad juzgara su elección."
    n "El aire olía a óxido, y las sombras lo siguieron en silencio hasta que su figura se perdió entre los callejones del régimen."

    return


# ----------- OPCIÓN 2: IR AL HOSPEDAJE DE TESSIE -----------

label esc_18_op2:

    scene lluvia_camino with fade

    n "SCOTT apretó los puños. La culpa y el miedo se mezclaban con una sensación de urgencia visceral."

    sc "Si hay una mínima posibilidad de que esté en peligro… no puedo quedarme quieto."

    n "Echó a andar bajo la lluvia."
    n "Los faroles temblaban sobre su cabeza, y el pavimento mojado reflejaba fragmentos de símbolos rotos que parecían seguirlo en silencio."
    n "A cada paso, la bruma se cerraba más, y la ciudad se convertía en un laberinto de luces amarillas y ecos metálicos."
    n "SCOTT caminaba rápido, casi sin pensar."
    n "Sabía que lo que lo impulsaba no era solo la premonición, sino la necesidad de redimirse antes de que fuera demasiado tarde."
    n "La noche lo engulló."

    scene black with fade
    n "CORTE A NEGRO."

    return