import os
import requests
from api import listar_marcas, listar_modelos, listar_anos, consultar_veiculo
from storage import carregar, salvar
 
# Ativa suporte a cores no terminal do Windows
os.system("")
 
 
# ---------- Utilidades ----------
 
def moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
 
 
def ler_valor(texto: str) -> float:
    """Aceita '77687', '77687,50', '77.687,00' ou 'R$ 77.687,00'."""
    texto = texto.replace("R$", "").strip()
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    return float(texto)
 
 
def cor_rgb(r: int, g: int, b: int, texto: str) -> str:
    return f"\033[38;2;{r};{g};{b}m{texto}\033[0m"
 
 
def degrade_azul(linhas: list[str]) -> str:
    """Pinta cada linha com um tom de azul, do claro ao escuro."""
    total = len(linhas)
    resultado = []
    for i, linha in enumerate(linhas):
        t = i / max(total - 1, 1)      # 0.0 (topo) até 1.0 (fim)
        r = int(120 - 100 * t)         # 120 -> 20
        g = int(200 - 120 * t)         # 200 -> 80
        b = 255 - int(55 * t)          # 255 -> 200
        resultado.append(cor_rgb(r, g, b, linha))
    return "\n".join(resultado)
 
 
def escolher(itens: list[dict], rotulo: str, max_exibir: int = 15) -> str | None:
    """Filtra por texto e deixa o usuário escolher um item. Retorna o código."""
    filtro = input(f"Digite parte do nome ({rotulo}): ").strip().lower()
    filtrados = [i for i in itens if filtro in i["nome"].lower()][:max_exibir]
 
    if not filtrados:
        print("Nada encontrado.")
        return None
 
    for n, item in enumerate(filtrados, 1):
        print(f"  [{n}] {item['nome']}")
 
    escolha = input("Número: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(filtrados):
        return str(filtrados[int(escolha) - 1]["codigo"])
 
    print(f"Opção inválida. Digite um número de 1 a {len(filtrados)}.")
    return None
 
 
# ---------- Funções do sistema ----------
 
def cadastrar_veiculo() -> None:
    marca = escolher(listar_marcas(), "marca")
    if not marca:
        return
    modelo = escolher(listar_modelos(marca), "modelo")
    if not modelo:
        return
 
    anos = listar_anos(marca, modelo)
    print("\nAnos disponíveis:")
    for n, a in enumerate(anos, 1):
        print(f"  [{n}] {a['nome']}")
    escolha = input("Número: ").strip()
    if not escolha.isdigit() or not 1 <= int(escolha) <= len(anos):
        print(f"Opção inválida. Digite um número de 1 a {len(anos)}.")
        return
 
    veiculo = consultar_veiculo(marca, modelo, anos[int(escolha) - 1]["codigo"])
    print(f"\n{veiculo['marca']} {veiculo['modelo']} {veiculo['ano']}")
    print(f"Valor FIPE ({veiculo['referencia']}): {moeda(veiculo['valor_fipe'])}")
 
    try:
        preco = ler_valor(input("Preço de venda: R$ "))
    except ValueError:
        print("Valor inválido. Exemplo: 77687 ou 77.687,00")
        return
 
    estoque = carregar()
    veiculo["id"] = max((v["id"] for v in estoque), default=0) + 1
    veiculo["preco_venda"] = preco
    veiculo["vendido"] = False
    estoque.append(veiculo)
    salvar(estoque)
 
    diff = (preco / veiculo["valor_fipe"] - 1) * 100
    print(f"Cadastrado! Preço {diff:+.1f}% em relação à FIPE.")
 
 
def ver_estoque() -> None:
    disponiveis = [v for v in carregar() if not v["vendido"]]
    if not disponiveis:
        print("Estoque vazio.")
        return
 
    print(f"\n{'ID':<4}{'Veículo':<45}{'FIPE':>14}{'Venda':>14}{'Dif.':>8}")
    print("-" * 85)
    for v in disponiveis:
        diff = (v["preco_venda"] / v["valor_fipe"] - 1) * 100
        nome = f"{v['marca']} {v['modelo']} {v['ano']}"[:43]
        print(f"{v['id']:<4}{nome:<45}{moeda(v['valor_fipe']):>14}"
              f"{moeda(v['preco_venda']):>14}{diff:>+7.1f}%")
 
 
def registrar_venda() -> None:
    ver_estoque()
    escolha = input("\nID do veículo vendido: ").strip()
    estoque = carregar()
 
    for v in estoque:
        if str(v["id"]) == escolha and not v["vendido"]:
            v["vendido"] = True
            salvar(estoque)
            print(f"Venda registrada: {moeda(v['preco_venda'])}")
            return
    print("Veículo não encontrado.")
 
 
def relatorio() -> None:
    estoque = carregar()
    disponiveis = [v for v in estoque if not v["vendido"]]
    vendidos = [v for v in estoque if v["vendido"]]
 
    print("\n=== RELATÓRIO ===")
    print(f"Em estoque:  {len(disponiveis)} veículos "
          f"({moeda(sum(v['preco_venda'] for v in disponiveis))})")
    print(f"Vendidos:    {len(vendidos)} veículos")
    print(f"Faturamento: {moeda(sum(v['preco_venda'] for v in vendidos))}")
 
 
# ---------- Programa principal ----------
 
def main():
    titulo = "=== CONCESSIONÁRIA ==="
    menu = [
        "1) Cadastrar veículo",
        "2) Ver estoque",
        "3) Registrar venda",
        "4) Relatório",
        "0) Sair",
    ]
 
    print(cor_rgb(100, 180, 255, titulo))
    while True:
        print()
        print(degrade_azul(menu))
        opcao = input("Escolha: ").strip()
 
        try:
            if opcao == "1":
                cadastrar_veiculo()
            elif opcao == "2":
                ver_estoque()
            elif opcao == "3":
                registrar_venda()
            elif opcao == "4":
                relatorio()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except requests.exceptions.ConnectionError:
            print("Sem conexão com a internet.")
        except requests.exceptions.Timeout:
            print("A requisição demorou demais.")
        except requests.exceptions.HTTPError as e:
            print(f"Erro na API: {e}")
 
 
if __name__ == "__main__":
    main()