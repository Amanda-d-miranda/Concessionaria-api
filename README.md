<div align="center">

<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f697.svg" width="250" alt="Carro">

# Concessionária

### Sistema de estoque de veículos no terminal, com preços de referência da **Tabela FIPE**
</div>
📖 Sobre o projeto

Projeto de estudo para praticar consumo de APIs em Python. O sistema controla o estoque de uma concessionária e usa a API FIPE para buscar marcas, modelos, anos e o valor de referência de cada veículo. Você define o preço de venda e o sistema mostra se ele está acima ou abaixo da FIPE.

💡 Não precisa de chave de API nem de conta. Basta ter internet para cadastrar veículos novos.

✨ Funcionalidades
	Recurso	Descrição
🆕	Cadastrar veículo	Escolhe marca, modelo e ano direto da API FIPE
💰	Valor FIPE automático	Busca o preço de referência do mês
📊	Comparação com a FIPE	Mostra a diferença percentual do seu preço de venda
📋	Ver estoque	Tabela com ID, veículo, FIPE, preço de venda e diferença
🤝	Registrar venda	Marca o veículo como vendido
📈	Relatório	Total em estoque, quantidade vendida e faturamento
🎨	Menu com degradê azul	Cores em 24 bits no terminal
🧪	Estoque de exemplo	Script que cria 7 carros fictícios para testar
🛠️ Tecnologias
Python 3.10+
requests para as chamadas HTTP
JSON para guardar o estoque localmente
API FIPE (documentação)
📁 Estrutura do projeto
concessionaria/
├── main.py            # Menu e fluxo do sistema
├── api.py             # Chamadas à API FIPE
├── storage.py         # Leitura e escrita do estoque.json
├── popular.py         # Cria 7 carros de exemplo
├── requirements.txt   # Dependências
├── .gitignore
└── estoque.json       # Criado automaticamente (não vai para o Git)
<details> <summary><b>🔎 O que cada arquivo faz</b></summary> <br>
Arquivo	Responsabilidade
main.py	Interface: menu, cores, entrada do usuário e cálculos de exibição
api.py	Funções listar_marcas, listar_modelos, listar_anos e consultar_veiculo
storage.py	Funções carregar e salvar que lidam com o JSON
popular.py	Sobrescreve o estoque com 7 veículos fictícios

Separar API, armazenamento e interface facilita trocar uma parte sem mexer nas outras. Por exemplo, trocar o JSON por SQLite mexe só no storage.py.

</details>
🚀 Instalação
1️⃣ Pré-requisitos

Confira a versão do Python (precisa ser 3.10 ou superior):

bash
python --version
2️⃣ Baixe o projeto
bash
git clone https://github.com/SEU-USUARIO/concessionaria.git
cd concessionaria
3️⃣ Crie o ambiente virtual
<details open> <summary><b>🪟 Windows</b></summary>
bash
python -m venv venv
venv\Scripts\activate

Se o PowerShell bloquear a ativação, rode uma vez: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

</details> <details> <summary><b>🐧 Linux / 🍎 Mac</b></summary>
bash
python3 -m venv venv
source venv/bin/activate
</details>

Quando der certo, aparece (venv) no começo da linha do terminal.

4️⃣ Instale as dependências
bash
pip install -r requirements.txt
5️⃣ (Opcional) Crie o estoque de exemplo
bash
python popular.py
7 veículos cadastrados com sucesso!

⚠️ O popular.py sobrescreve o estoque.json. Rode apenas na primeira vez.

🎮 Como usar

Inicie o sistema:

bash
python main.py

Você verá o menu:

=== CONCESSIONÁRIA ===

1) Cadastrar veículo
2) Ver estoque
3) Registrar venda
4) Relatório
0) Sair
Escolha:
<details> <summary><b>🆕 Opção 1: Cadastrar veículo</b></summary> <br>
Digite parte do nome da marca e escolha o número da lista.
Repita para o modelo.
Escolha o ano.
O sistema mostra o valor FIPE e pede o preço de venda.
Digite parte do nome (marca): honda
  [1] Honda
Número: 1
Digite parte do nome (modelo): city
  [1] CITY Sedan DX 1.5 Flex 16V Mec.
Número: 1

Anos disponíveis:
  [1] 2021 Gasolina
Número: 1

Honda CITY Sedan DX 1.5 Flex 16V Mec. 2021
Valor FIPE (outubro de 2026): R$ 77.687,00
Preço de venda: R$ 87687
Cadastrado! Preço +12.9% em relação à FIPE.

Dicas de digitação

O número pedido é o da lista na tela ([1], [2]...), não o código da marca.
No preço, digite só o valor. Estes formatos funcionam:
Digitado	Resultado
87687	R$ 87.687,00
87687,50	R$ 87.687,50
87.687,00	R$ 87.687,00
R$ 87.687,00	R$ 87.687,00
</details> <details> <summary><b>📋 Opção 2: Ver estoque</b></summary> <br>
ID  Veículo                                              FIPE         Venda    Dif.
-------------------------------------------------------------------------------------
1   Fiat Argo 1.3 Drive 2023                       R$ 72.500,00  R$ 76.900,00   +6.1%
4   Hyundai HB20 1.0 Comfort 2021                  R$ 61.200,00  R$ 59.900,00   -2.1%

Mostra apenas os veículos ainda não vendidos.

</details> <details> <summary><b>🤝 Opção 3: Registrar venda</b></summary> <br>

O sistema lista o estoque e pede o ID do veículo vendido. Ele é marcado como vendido e passa a contar no faturamento.

</details> <details> <summary><b>📈 Opção 4: Relatório</b></summary> <br>
=== RELATÓRIO ===
Em estoque:  6 veículos (R$ 640.200,00)
Vendidos:    1 veículos
Faturamento: R$ 76.900,00
</details>
⚙️ Como funciona
👤 Usuário
main.pymenu e interface
api.pyrequisições HTTP
🌐 API FIPE
storage.py
📄 estoque.json

Fluxo do cadastro

storage.py
API FIPE
api.py
main.py
Usuário
storage.py
API FIPE
api.py
main.py
Usuário
Escolhe "Cadastrar"
listar_marcas()
GET /marcas
lista de marcas
Seleciona marca, modelo e ano
consultar_veiculo()
GET /marcas/.../anos/...
valor FIPE
Mostra valor e pede preço de venda
Informa o preço
salvar(estoque)
<details> <summary><b>📦 Formato de um veículo no <code>estoque.json</code></b></summary>
json
{
  "id": 1,
  "marca": "Honda",
  "modelo": "CITY Sedan DX 1.5 Flex 16V Mec.",
  "ano": 2021,
  "combustivel": "Gasolina",
  "codigo_fipe": "014043-8",
  "valor_fipe": 77687.0,
  "referencia": "outubro de 2026",
  "preco_venda": 87687.0,
  "vendido": false
}
</details>
🧯 Problemas comuns
<details> <summary><b>❌ <code>ModuleNotFoundError: No module named 'requests'</code></b></summary> <br>

A biblioteca não foi instalada no ambiente ativo.

bash
python -m pip install requests
</details> <details> <summary><b>❌ O programa roda e não mostra nada</b></summary> <br>
Confira se o main.py termina com if __name__ == "__main__": main().
Confira se o arquivo foi salvo (Ctrl+S).
No VS Code, o botão ▶ executa o arquivo que está aberto na tela.
</details> <details> <summary><b>❌ Digitei um número e o menu voltou sem avisar</b></summary> <br>

O número deve ser o da lista exibida ([1], [2]...). Se só aparece [1], digite 1.

</details> <details> <summary><b>❌ "Valor inválido" no preço de venda</b></summary> <br>

Digite apenas o número, sem repetir o texto "Preço de venda: R$". Exemplos: 87687 ou 87.687,00.

</details> <details> <summary><b>❌ Erro 429 (Too Many Requests)</b></summary> <br>

A API gratuita tem limite diário de requisições. Espere um tempo ou use um token gratuito, conforme a documentação da API.

</details> <details> <summary><b>❌ "Estoque vazio" mesmo depois de cadastrar</b></summary> <br>

O estoque.json é criado na pasta de onde você executa o comando. Rode sempre de dentro da pasta do projeto:

bash
cd concessionaria
python main.py
</details> <details> <summary><b>❌ Cores aparecem como <code>←[38;2;...</code></b></summary> <br>

O terminal não suporta cores ANSI. Use o terminal do VS Code, o Windows Terminal, ou confirme que o main.py tem os.system("") no topo.

</details>
🗺️ Roadmap
 Cadastro de veículos pela API FIPE
 Comparação do preço de venda com a FIPE
 Registro de vendas e relatório
 Menu com degradê de azul
 Script de estoque de exemplo
 Cadastro manual (sem depender da API)
 Suporte a motos e caminhões
 Cadastro de clientes vinculado às vendas
 Cálculo de comissão do vendedor
 Cache das consultas à API
 Trocar JSON por SQLite
 API própria com FastAPI
 Interface web (Flask ou Streamlit)
 Gráficos de vendas com matplotlib
🔐 Boas práticas de versionamento

O .gitignore já impede o envio de:

venv/ e venvcls/ (ambientes virtuais)
__pycache__/ (cache do Python)
estoque.json (dados locais)
.env (chaves e tokens, caso passe a usar)

Nunca coloque tokens, senhas ou dados reais de clientes em arquivos versionados.

🤝 Contribuindo
Faça um fork do projeto
Crie uma branch: git checkout -b minha-melhoria
Faça o commit: git commit -m "Adiciona minha melhoria"
Envie: git push origin minha-melhoria
Abra um Pull Request
⚠️ Aviso

Os valores do popular.py são fictícios, criados só para testes. Os valores FIPE obtidos pela opção de cadastro vêm de uma API de terceiros e podem mudar ou ficar indisponíveis. Este é um projeto de estudo e não deve ser usado como referência oficial de preços.

<div align="center">

Feito com 🐍 Python e muito café ☕

⭐ Se o projeto te ajudou, deixe uma estrela no repositório!
</div>
