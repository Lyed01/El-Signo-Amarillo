label esc_14B:

    scene estudio_scott_tarde with fade

    play ambience "viento.ogg" fadein 1.0

    # Tessie despidiéndose
    show tessie neutral at center
    "La bruma invade el estudio mientras el viento agita las persianas."
    "te" "Nos vemos, Scott…"
    "TESSIE se despide con un gesto breve, su silueta perdiéndose entre la niebla de la ciudad."

    hide tessie with dissolve

    # Scott queda solo
    show scott serio at center
    "SCOTT permanece en el estudio, respirando hondo, apoyado sobre la mesa donde el libro sigue escondido."
    "El silencio es pesado, cargado de tensión."

    # Thomas aparece
    show thomas neutral at right with dissolve

    "sc" "No quiero que nadie más se acerque a ese libro. ¿Entendés, Thomas? Es demasiado peligroso."

    "th" "Sí, señor. Nadie lo tocará."

    "El murmullo distante de la ciudad entra por las ventanas entreabiertas, mezclándose con el crujido de papeles y el eco de una amenaza silenciosa."

    # Punto final de la escena
    jump escena_15   # Cambiá esto por el siguiente label