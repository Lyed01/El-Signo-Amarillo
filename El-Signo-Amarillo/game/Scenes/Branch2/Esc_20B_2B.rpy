label esc_20B_2B:

    scene bg auto with dissolve
    play ambient "car_road_low.ogg" fadein 1.5

    "El auto sigue su marcha lenta por la carretera."
    "El viento se cuela por la ventanilla entreabierta, levantando el polvo dorado del camino."

    show tessie car_passenger_reading at right
    show scott driving_focus at left

    "TESSIE hojea el libro con la despreocupación de quien encuentra un objeto viejo sin importancia."
    "Las páginas crujen al pasar; el sol se refleja en el borde amarillento del papel."

    te "(sonriendo levemente) Está lleno de símbolos raros… y frases en otro idioma. Escuchá esto, Scott:"
    
    te "(leyendo) “...bajo la mirada del rey, el sueño se disuelve y el cuerpo recuerda su verdadero nombre…”"

    "SCOTT, al volante, asiente distraído. Al principio no presta demasiada atención, pero su expresión se endurece poco a poco."

    te "(hojeando otra página) “...las ciudades se doblan sobre sí mismas, y los hombres olvidan su rostro…”"
    te "(pausa, divertida) Vaya poesía oscura, ¿no te parece?"

    show scott driving_concern at left
    sc "(suavemente) Déjame ver eso un momento, Tessie."

    "Ella sonríe y le pasa el libro sin sospecha."

    te "¿Lo reconocés?"

    show scott book_hold at left
    "SCOTT lo toma, observa las páginas abiertas y se queda inmóvil."
    "Sus dedos tiemblan apenas al rozar el símbolo en relieve de la portada."

    sc "(en voz baja, casi para sí) Sí… lo he visto antes."

    te "¿Dónde?"

    sc "(tras una pausa, sin apartar la vista del libro) En un sueño… o en algo que preferiría no recordar."

    "El ruido del motor parece apagarse bajo la tensión creciente."
    "El auto sigue avanzando, pero el paisaje fuera de la ventana se siente más lejano, más irreal."

    # Efecto sutil: distorsión visual para sugerir influencia del Signo Amarillo
    show yellow_sign_flash at center with dissolve
    pause 0.8
    hide yellow_sign_flash with fade

    return
