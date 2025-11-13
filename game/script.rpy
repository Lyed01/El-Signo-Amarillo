# =====================================================
# script_prologo.rpy — Control general del prólogo
# =====================================================

# Variable global para guardar la rama
default branch = 0

label start:

    # Inicia en la primera escena
    call esc_1

    # Según lo que eligió Scott recordar:
    if branch == 1:
        call esc_2A
    elif branch == 2:
        call esc_2B
    elif branch == 3:
        call esc_2C

    # Continúa el flujo del prólogo
    call esc_3
    call esc_4
    call esc_5

    n "Fin del prólogo."

    return
