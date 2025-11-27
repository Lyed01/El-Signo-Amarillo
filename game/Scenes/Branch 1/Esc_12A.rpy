label esc_12A:

    scene bg estudioNoche with fade

    n "El reloj marcaba las once. La lluvia seguía golpeando los cristales con un ritmo constante, y el humo del cigarrillo de Scott se mezclaba con el olor húmedo del aceite y el yeso. El estudio estaba en penumbra, solo iluminado por la lámpara sobre el caballete, que proyectaba sombras alargadas sobre las paredes."

    n "Tessie permanecía sentada en silencio, las rodillas juntas, mirando el lienzo inconcluso. Su rostro estaba pálido, la mirada perdida entre los trazos amarillos que parecían brillar débilmente bajo la luz artificial."

    show te1 at left

    te "—No deja de mirarme, Scott. Aunque cierre los ojos, lo veo. Aunque intento no pensarlo, siento que está ahí, detrás de los muros, esperándome."

    n "Él se detuvo, observándola. Había algo en su tono que lo estremecía, una mezcla de miedo y fascinación que reconocía demasiado bien."
    show sc1 at right
    sc "—Tessie. Tenés que dejar de pensar en él. Esa gente… esas presencias… se alimentan de lo que les damos. Si les temés, crecen. Si los recordás, vuelven."

    n "Ella levantó la cabeza lentamente."

    te "—¿Está diciendo que… que no es un hombre?"

    n "Scott vaciló. Su instinto de artista, su memoria de soldado y su razón se cruzaban como cables a punto de cortocircuitar."

    sc "—No lo sé. Pero lo que sea, no obedece las leyes de los hombres."

    n "Tessie se incorporó. La luz temblaba sobre su rostro, acentuando el brillo húmedo de sus ojos."

    te "—Entonces deberíamos hacer algo. Avisar a alguien, salir de aquí, irnos de la ciudad…"

    sc "—¿Y adónde iríamos? No hay lugares sin vigilancia. No hay esquinas sin ojos. Lo que viste en el atrio no pertenece solo a este barrio, Tessie. Está en todas partes."

    n "Ella lo miró con desesperación."

    te "—¿Por qué no me lo dijo antes? ¡Sabe lo que es y me lo ocultó!"

    n "Scott levantó la voz, aunque no era enojo sino un temor contenido."

    sc "—Porque no hay nada que puedas hacer. ¡Escuchame, Tessie! No lo nombres, no lo busques. No lo mires más. Fingí que no existe."

    n "El silencio cayó abruptamente. Afuera, el trueno hizo vibrar los vidrios. Tessie lo observó con incredulidad y dolor."

    te "—¿Eso es todo? ¿Olvidar? ¿Hacer de cuenta que no pasa nada mientras esa cosa me observa cada noche?"

    n "Scott se acercó un paso."

    sc "—No quiero que termines como los demás. Algunos intentaron enfrentarlo. Desaparecieron, o peor. Quedaron vacíos, como si algo les hubiera arrancado la voluntad."

    n "Tessie lo miró en silencio. Su respiración era agitada, sus manos temblaban."

    te "—No puedo prometerle que no lo recordaré. Pero intentaré no mirarlo."

    n "Scott asintió, y su expresión se suavizó apenas."

    sc "—Eso es suficiente. Mañana no vengas. Quedate en casa unos días. Descansá."

    te "—¿Y usted?"

    n "Él apartó la mirada hacia la ventana, donde el reflejo de la lámpara dibujaba sombras distorsionadas."

    sc "—Yo tengo que quedarme. Alguien tiene que seguir mirando."

    n "La lluvia redobló su ritmo. Tessie dio un paso hacia él, como queriendo abrazarlo, pero se contuvo. La distancia entre ambos parecía llenarse de un silencio denso, casi tangible."

    te "—Prométame que no irá a buscarlo."

    n "Scott no respondió. Solo encendió otro cigarrillo y dejó que el humo lo envolviera."

    n "Ella comprendió entonces que la advertencia no era solo para ella, sino también para él."

    n "Afuera, en el atrio, un relámpago iluminó fugazmente la figura del agente. Estaba en el mismo lugar de siempre, pero esta vez, su cabeza parecía girada hacia la ventana del estudio."

    n "Y aunque Scott no lo miró directamente, supo que lo había oído."

    # ============================================
    #        BLOQUE DE DECISIÓN AGREGADO
    # ============================================

    menu:
        "Advertir a Tessie sobre el peligro (RUTA A)":
            $ advertir = True
            $ noadvertir = False

        "No advertirla, dejar que siga investigando (RUTA A_1A)":
            $ advertir = False
            $ noadvertir = True

    return
