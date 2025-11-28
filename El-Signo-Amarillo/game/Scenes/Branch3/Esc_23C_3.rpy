label escena_23:

    scene estudio_scott_noche with fade

    n "La lluvia golpea las ventanas con la insistencia de un puño que no cesa."
    n "El agua corre por los vidrios empañados, filtrando destellos amarillos en el interior del estudio."
    n "SCOTT permanece arrodillado junto al cuerpo de TESSIE."
    n "Su rostro está en sombras."
    n "Las manos, empapadas y temblorosas, brillan bajo la luz vacilante de la lámpara."

    show sc1 at center
    sc "(voz apenas audible) Tessie..."

    n "Silencio."
    n "Solo la tormenta, arrastrando hojas y papeles contra los muros."
    n "El documento oficial sigue sobre la mesa, húmedo, con el sello en tinta roja aún visible:"
    n "una firma ilegible y la palabra 'Cumplido.'"

    n "SCOTT la observa, los ojos abiertos de par en par, como si esa palabra fuera su condena."
    n "Las manos le tiemblan."
    n "Aprieta el papel."
    n "Lo rompe."
    n "Lo desgarra."

    n "El estudio es un caos: frascos de pintura caídos, pinceles mezclados con fragmentos de vidrio,"
    n "el humo del cigarrillo extinguido flotando entre el olor a aguarrás y humedad."
    n "Cada objeto parece mirarlo. Acusarlo. Recordarle que llegó tarde."

    n "SCOTT levanta la cabeza. La respiración entrecortada."
    n "El cabello pegado a la frente."
    n "En su pecho, el dolor se mezcla con algo más. Un impulso que no sabe contener."
    n "Rabia. Desesperación. Impotencia."

    n "Golpea el suelo con el puño. Una, dos, tres veces."
    n "La madera cruje bajo el impacto."

    sc "(gritando, ronco) ¡No puede terminar así!"

    n "El eco de su grito se pierde entre los truenos."
    n "Pero algo en el estudio parece responder: la lámpara titila, y por un instante cree ver"
    n "el reflejo de un rostro blando y grisáceo en la ventana. El AGENTE. O su recuerdo."

    n "SCOTT se pone de pie, tambaleante, los ojos fijos en el abrigo del perchero."
    n "Sabe lo que hay dentro."
    n "El peso frío del revólver, todavía cargado, esperando como una promesa."

    n "Avanza, tropezando con pinceles y cristales rotos."
    n "Su respiración es un temblor constante."
    n "Mira el cuerpo de TESSIE una última vez."
    n "Una furia ciega lo recorre de pies a cabeza."
    n "La lluvia aumenta, golpeando los ventanales."
    n "La lámpara parpadea."
    n "SCOTT cierra los ojos. Aprieta los dientes."

    n "Dos caminos se abren ante él."
    n "Ambos lo arrastran hacia un destino sin retorno."

    menu:
        "Opcion A - Tomar venganza":
            jump opcionA

        "Opcion B - Sucumbir":
            jump opcionB


# ------------------------------
# RUTA A – TOMAR VENGANZA
# ------------------------------


label escena_23_venganza:

    scene estudio_scott_noche with fade

    n "SCOTT toma el revólver del abrigo."
    n "El metal brilla bajo la luz amarilla."
    n "Se coloca el broche en el pecho."
    n "Sale a la noche, la lluvia cubriéndolo como un manto, en busca del agente del atrio."

    return


# ------------------------------
# RUTA B – SUCUMBIR
# ------------------------------

label escena_23_sucumbir:

    scene estudio_scott_noche with dissolve

    n "SCOTT no se mueve."
    n "La rabia se disuelve en un temblor profundo."
    n "Cae de rodillas junto al cuerpo."
    n "La tormenta devora el sonido de su respiración."
    n "El estudio se apaga."
    n "Solo queda culpa y silencio."

    scene black with fade

    return
