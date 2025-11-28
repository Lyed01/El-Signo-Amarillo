default branch = 0
default subbranch = 0

# variables branch 1
default advertir = False
default noadvertir = False

#variables branch 2
default rechazoATessie = False
#default tessieIgnoraScott = False

#variables branch 3
default pathiglesia = False
default arma = False
default irtessie = False   
default irJuntos = False
default armasotano = False
default verganza = False
default tiraco = False

# Flag: whether Scott has his revolver (prevents NameError if unset)
default scott_tiene_revolver = False

label start:

    call esc_1

    if branch == 1:
        call escena_2_reprimir_recuerdos_branch1
    elif branch == 2:
        call bosque_breton_infancia
    elif branch == 3:
        call esc_2C

    call esc_3
    call esc_4
    call esc_5
    call esc_6

    if subbranch == 1:
        call esc_7A
        call esc_8A
        call esc_9A
        call esc_10A
        call esc_11A
        call esc_12A     
        # ======================================
        #       DECISIÓN DESPUÉS DE ESC_12A
        # ======================================
        if advertir:
            # RUTA A (original)
            call esc_13A
            call esc_14A
            call esc_15A
            call esc_16A
            call esc_17A
            call esc_18A
            call esc_19A
            call esc_20A
            call esc_21A
            call esc_22A
        elif noadvertir:
            # RUTA ALTERNATIVA A_1A
            call esc_13A_1A
            call esc_14A_1A
            call esc_15A_1A
            call esc_16A_1A
            call esc_17A_1A
            call esc_18A_1A
            call esc_19A_1A

    elif subbranch == 2:
        call esc_7B_2
        call esc_8B
        call esc_9B
        call esc_10B
        call esc_11B    
        call esc_12B_2
        call esc_13B
        call esc_14B
        call esc_15B
        call esc_16B

        if rechazoATessie:
            call esc_17B_2A
            call esc_18B_2A
            call esc_19B_2A
            call esc_20B_2A
        else:
            call esc_17B_2B
            call esc_18B_2B
            call esc_19B_2B
            call esc_20B_2B
            call esc_21B_2B

    elif subbranch == 21:
        call esc_7B_1
        call esc_8B
        call esc_9B
        call esc_10B
        call esc_11B
        call esc_12B_1
        call esc_16A
        call esc_17A
        call esc_18A
        call esc_19A
        call esc_20A
        call esc_21A
        call esc_22A         

    elif subbranch == 3:
        call esc_7C
        call esc_8C
        call esc_9C
        call esc_10C
        call esc_11C

        if pathiglesia == False: #noiglesia
            call esc_12C_1
            call esc_13C_1
            call esc_14C_1
            call esc_15C_1
            call esc_16C_1
            call esc_17C_1
            call esc_18C_1
            call esc_19C_1
            call esc_20C_1
            call esc_21C_1
            call esc_22C_1
            call esc_23C_1

            if choice23 == 1:
                call esc_24C_1A
                call esc_25C_1A
            else:
                call esc_24C_1B
                call esc_25C_1B
        else: #iglesia
            call esc_12C_3
            call esc_13C_3
            call esc_14C_3
            call esc_15C_3
            call esc_16C_3
            call esc_17C_3
            call esc_18C_3

            if irtessie:
                call esc_19C_4
                call esc_20C_4
                call esc_21C_4
                call esc_22C_4
                call esc_23C_4
                call esc_24C_4
                call esc_25C_4
                call esc_26C_4
                call esc_27C_4

                if irJuntos:
                    call esc_28C_4_1
                    call esc_29C_4_1
                    call esc_30C_4_1
                    call esc_31C_4_1
                    call esc_32C_4_1
                    call esc_33C_4_1

                    if armasotano: 
                        call esc_34C_4_1_2
                    else:
                        call esc_34C_4_1
                else:
                    call esc_28C_4_2
                    call esc_29C_4_2
                    call esc_30C_4_2
                    call esc_31C_4_2
            else:
                call esc_19C_3
                call esc_20C_3
                call esc_21C_3
                call esc_22C_3
                call esc_23C_3

                if verganza:
                    call esc_24C_3
                    call esc_25C_3
                    call esc_26C_3

                    if tiraco:
                        call esc_27C_3A
                        call esc_final28C_3A
                    else:
                        call esc_27C_3B
                        call esc_final28C_3B
                else:
                    call esc_24C_3_2