import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1/carros"


def _get(caminho: str):
    resposta = requests.get(f"{BASE_URL}{caminho}", timeout=10)
    resposta.raise_for_status()
    return resposta.json()


def listar_marcas() -> list[dict]:
    return _get("/marcas")


def listar_modelos(marca: str) -> list[dict]:
    return _get(f"/marcas/{marca}/modelos")["modelos"]


def listar_anos(marca: str, modelo: str) -> list[dict]:
    return _get(f"/marcas/{marca}/modelos/{modelo}/anos")


def consultar_veiculo(marca: str, modelo: str, ano: str) -> dict:
    dados = _get(f"/marcas/{marca}/modelos/{modelo}/anos/{ano}")
    return {
        "marca": dados["Marca"],
        "modelo": dados["Modelo"],
        "ano": dados["AnoModelo"],
        "combustivel": dados["Combustivel"],
        "codigo_fipe": dados["CodigoFipe"],
        "valor_fipe": converter_valor(dados["Valor"]),
        "referencia": dados["MesReferencia"],
    }


def converter_valor(texto: str) -> float:
    """Converte 'R$ 52.340,00' em 52340.0"""
    return float(texto.replace("R$", "").replace(".", "").replace(",", ".").strip())