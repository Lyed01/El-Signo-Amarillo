label esc_18B_2B:

    scene edificio_frente with fade
    play ambient "engine_idle_fog.ogg" fadein 1.5

    "El motor del auto arranca con un rugido seco que rompe el silencio del amanecer."

    "Una neblina ligera cubre la calle, envolviendo los faroles y las fachadas dormidas de la ciudad."

    show tessie at right
    show scott at left

    "TESSIE y SCOTT aparecen, apresurados, con pocas pertenencias. Sus pasos resuenan sobre el empedrado húmedo."

    "Scott abre la puerta del auto; Tessie mira una última vez hacia las ventanas del estudio, donde la luz del sol empieza a filtrarse tímidamente."

    te "(en voz baja) Parece… que todo fue un sueño."

    sc "(serio, mientras enciende el motor) Entonces no miremos atrás."

    play sound "car_start.ogg"

    "El auto se pone en marcha."

    scene bg_car_depart_fog with dissolve

    "La cámara sigue el vehículo mientras se pierde entre la niebla matinal, dejando atrás el edificio, el estudio y el eco de todo lo que ocurrió entre sus paredes."

    "Por un momento, el aire parece calmo…"

    # Detalle del Signo Amarillo brillando
    show yellow_sign_glow at center with dissolve
    pause 1.0
    hide yellow_sign_glow with fade

    "En el asiento trasero, un destello dorado brilla fugazmente entre las sombras: el Signo Amarillo, grabado en la cubierta del libro, apenas visible."

    "El sonido del motor se aleja, fundiéndose con el viento."

    scene black with fade

    return
