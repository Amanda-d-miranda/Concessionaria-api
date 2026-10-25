import json
from pathlib import Path

ARQUIVO = Path("estoque.json")


def carregar() -> list[dict]:
    if not ARQUIVO.exists():
        return []
    with open(ARQUIVO, encoding="utf-8") as f:
        return json.load(f)


def salvar(estoque: list[dict]) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=2)