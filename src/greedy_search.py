from buscar_mejor_estacion import buscar_mejor_estacion

estaciones = {
    key: value
    for key, value in [
        ("kone", {"id", "nv", "ut"}),
        ("ktwo", {"wa", "id", "mt"}),
        ("kthree", {"or", "nv", "ca"}),
        ("kfour", {"nv", "ut"}),
        ("kfive", {"ca", "az"}),
        ("ksix", {"nm", "tx", "ok"}),
        ("kseven", {"ok", "ks", "co"}),
        ("keight", {"ks", "co", "ne"}),
        ("knine", {"ne", "sd", "wy"}),
        ("kten", {"nd", "ia"}),
        ("keleven", {"mn", "mo", "ar"}),
        ("ktwelve", {"la"}),
        ("kthirteen", {"mo", "ar"}),
    ]
}


def greedy_search(estaciones, estados_solicitados):
    estaciones_restantes = estaciones.copy()
    estados_cubiertos = set()
    estaciones_usadas = []

    mayor_num_cubierto = []
    num_estados_cubiertos = []

    while estados_cubiertos < estados_solicitados:
        num_cobertura, mejor_estacion = buscar_mejor_estacion(
            estaciones_restantes, estados_cubiertos
        )

        if mejor_estacion:
            estados_cubiertos |= estaciones_restantes[mejor_estacion]
            estaciones_usadas.append(mejor_estacion)
            mayor_num_cubierto.append(num_cobertura)
            num_estados_cubiertos.append(len(estados_cubiertos))
            del estaciones_restantes[mejor_estacion]

    print(
        estados_cubiertos,
        estaciones_usadas,
        mayor_num_cubierto,
        num_estados_cubiertos,
    )

    return (
        estados_cubiertos,
        estaciones_usadas,
        mayor_num_cubierto,
        num_estados_cubiertos,
    )


todos_los_estados = set(
    [
        "id",
        "nv",
        "ut",
        "wa",
        "mt",
        "or",
        "ca",
        "az",
        "nm",
        "tx",
        "ok",
        "ks",
        "co",
        "ne",
        "sd",
        "wy",
        "nd",
        "ia",
        "mn",
        "mo",
        "ar",
        "la",
    ]
)


greedy_search(estaciones, todos_los_estados)
