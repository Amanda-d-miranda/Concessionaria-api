from storage import salvar


carros = [
    ("Fiat", "Argo 1.3 Drive", 2023, "Gasolina", "001478-6", 72500.0, 76900.0),
    ("Chevrolet", "Onix 1.0 LT", 2022, "Gasolina", "004485-5", 68900.0, 71500.0),
    ("Volkswagen", "Polo 1.0 TSI", 2023, "Gasolina", "005526-1", 89900.0, 93000.0),
    ("Hyundai", "HB20 1.0 Comfort", 2021, "Gasolina", "026003-1", 61200.0, 59900.0),
    ("Toyota", "Corolla 2.0 XEi", 2022, "Gasolina", "002187-1", 138000.0, 142500.0),
    ("Honda", "Civic 2.0 EX", 2020, "Gasolina", "014043-8", 105400.0, 108900.0),
    ("Jeep", "Compass 1.3 T270 Longitude", 2023, "Gasolina", "009237-6", 156000.0, 162000.0),
]

estoque = []
for i, (marca, modelo, ano, comb, cod, fipe, venda) in enumerate(carros, 1):
    estoque.append({
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "combustivel": comb,
        "codigo_fipe": cod,
        "valor_fipe": fipe,
        "referencia": "outubro de 2026",
        "id": i,
        "preco_venda": venda,
        "vendido": False,
    })

salvar(estoque)
print(f"{len(estoque)} veículos cadastrados com sucesso!")