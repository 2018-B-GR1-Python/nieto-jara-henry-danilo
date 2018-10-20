



def imprimir_nombre(**kwargs): ##key word arguments
    print("{kwargs['primer_nombre']} {kwargs['segundo_nombre']} "
          "{kwargs['apellido_paterno'[} {kwargs['apellido_materno']}")

imprimir_nombre(primer_nombre = "Henry",
                segundo_nombre = "Danilo",
                apellido_paterno = "Nieto",
                apellido_materno = "Jara")
