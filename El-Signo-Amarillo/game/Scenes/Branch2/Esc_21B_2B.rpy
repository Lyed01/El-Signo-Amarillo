label esc_21B_2B:

    scene bg_road_sunset with fade
    play ambient "car_road_low.ogg" fadein 1.5

    "El sol comienza a ocultarse tras las colinas, tiñendo el horizonte de un rojo profundo."
    "El auto de SCOTT avanza lentamente por la carretera solitaria. El silencio entre ambos es pesado."

    show tessie car_passenger_reading at right
    show scott driving_concern at left

    te "(sin apartar la vista del libro) “...cuando los ojos del rey se abran, no habrá más aurora…”"
    te "(sonríe, nerviosa) Cada página parece escrita para asustar a quien la lee."

    sc "(con voz baja, distante) Deja de leer, Tessie… por favor."

    "TESSIE lo mira, sorprendida por el tono de su voz."
    "El coche continúa, pero algo en el ambiente cambia: el viento deja de soplar, el motor suena irregular."

    te "Scott… ¿qué pasa?"

    # Motor fallando
    play sound "engine_fail1.ogg"
    "El motor tose, se sacude… y se apaga."

    scene bg_road_stopped with dissolve
    stop ambient fadeout 2.0

    "El auto se detiene en medio del camino."
    "Silencio absoluto."

    show scott driving_alert at left
    sc "No… no debería haberse detenido."

    "SCOTT intenta girar la llave, pero el motor no responde."
    "El marcador de combustible parpadea erráticamente; las agujas tiemblan."

    te "¿Nos quedamos sin nafta?"

    sc "No… Esto no es normal."

    "El reloj del tablero se detiene."
    "Una brisa extraña atraviesa el interior del vehículo, aunque las ventanas están cerradas."

    show tessie car_passenger_scared at right
    "Tessie sostiene el libro con fuerza, sintiendo una vibración tenue."

    te "(voz apenas audible) Scott… escuchá."

    "No hay sonido alguno."
    "Ni pájaros, ni viento, ni motor."
    "Solo el eco lejano… de una página que se mueve sola."

    # Efecto visual del símbolo brillando
    show yellow_sign_flash at center with dissolve
    play sound "low_hum.ogg"
    pause 1.3
    hide yellow_sign_flash with fade

    "La cámara se acerca lentamente al símbolo grabado en la tapa del libro,"
    "que parece brillar con una luz enfermiza, palpitante."

    # --- FINAL ---
    scene black with fade

    "Y en el silencio absoluto de la carretera…"
    "algo más que el motor dejó de funcionar."

    "FIN – RUTA DEL SIGNO AMARILLO"

    return
