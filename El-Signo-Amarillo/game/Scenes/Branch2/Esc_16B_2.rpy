label esc_16B:

    scene estudio_scott_manana with fade

    "El silencio tras la confesión de TESSIE aún cuelga en el aire, pesado y expectante."

    "TESSIE da un paso más cerca de SCOTT, su voz baja pero decidida:"

    te "Scott… y si nos fuéramos… a otro país. Juntos."

    "SCOTT la observa, sorprendido, con los ojos fijos en ella, evaluando la propuesta que suena a sueño y a peligro al mismo tiempo."

    "La luz matinal entra por las ventanas, iluminando sus rostros mientras el estudio parece estrecharse a su alrededor, atrapando la tensión de una decisión que cambiaría todo."

    menu:
        "Quedarse":
            $ rechazoATessie = True

        "Irse con Tessie":
            $ rechazoATessie = False

    return
    # Aquí irán las dos opciones de Scott (Aceptar / Rechazar)
    # Puedo agregarlas cuando me digas.
    # jump escena_17  # Temporal