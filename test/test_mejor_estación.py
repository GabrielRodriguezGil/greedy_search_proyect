from src.buscar_mejor_estacion import buscar_mejor_estacion
import pytest


# Primero definimos los estados donde queremos ser escuchados
estados_solicitados = set(["id", "mo", "ks", "ar", "co", "sd", "wy", "nv", "or"])


# Estaciones de radio y estados que cubren


@pytest.mark.mejor_estacion
def test_mejor_estacion():
    estaciones = {}
    estaciones["kone"] = set(["id", "nv", "ut"])
    estaciones["ktwo"] = set(["wa", "id", "mt"])
    estaciones["kfive"] = set(["ca", "az"])

    estados_cubiertos = ["wa", "id", "nv"]

    assert buscar_mejor_estacion(estaciones, estados_cubiertos) == (2, "kfive")
