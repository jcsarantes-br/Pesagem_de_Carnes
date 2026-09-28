# 🥩 Apuração de Peso Real — Carne Refrigerada

Programa em Python para **apuração de peso real** no recebimento de caixas contendo carne refrigerada, descontando pallet, caixas vazias e embalagens plásticas do peso total pesado na balança.

Interface colorida no terminal com relatório formatado e opção de exportação em `.txt`.

---

## 📋 Índice

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Como usar](#-como-usar)
- [Lógica de cálculo](#-lógica-de-cálculo)
- [Exemplo de uso](#-exemplo-de-uso)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Personalização](#-personalização)
- [Tecnologias](#-tecnologias)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 📖 Sobre o projeto

No recebimento de carne refrigerada, o **peso bruto** pesado na balança inclui diversos itens que **não são carne**:

- Pallet
- Caixas vazias
- Embalagens plásticas internas

Este programa faz o **desconto automático** de todos esses itens para entregar o **peso real de carne recebido** — tanto o total quanto por caixa.

---

## ✨ Funcionalidades

- ✅ Cálculo do **peso real total** e **peso real por caixa**
- ✅ Desconto de **pallet**, **caixas vazias** e **embalagens plásticas**
- ✅ **Interface colorida** no terminal (tupla de cores ANSI)
- ✅ **Validação de entrada** (aceita vírgula ou ponto decimal)
- ✅ **Relatório formatado** com bordas e alinhamento
- ✅ **Exportação para arquivo `.txt`**
- ✅ Repetição para **múltiplas apurações** sem reiniciar o programa

---

## 🔧 Pré-requisitos

- **Python 3.7+**
- Nenhuma biblioteca externa necessária (usa apenas `os` da biblioteca padrão)

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/jcsaratnes-br/apuracao-peso-carne.git
cd apuracao-peso-carne
```

### 2. Execute o programa

```bash
python apuracao.py
```

### 3. Siga as instruções no terminal

O programa vai solicitar, em ordem:

| Entrada | Descrição |
|---|---|
| Peso do pallet | Em kg |
| Peso de **uma** caixa vazia | Em kg |
| Quantidade de caixas | Inteiro |
| Peso de **uma** embalagem plástica | Em kg |
| Quantidade de plásticos **por caixa** | Inteiro |
| Peso total na balança | Em kg (pallet + caixas + carne + plásticos) |

Ao final, o programa exibe o **relatório de apuração** e pergunta se deseja salvar em `.txt`.

---

## 🧮 Lógica de cálculo

```
Peso Real Total = Peso na Balança
                − Peso do Pallet
                − (Peso Caixa Vazia × Qtd Caixas)
                − (Peso Plástico × Qtd Plástico por Caixa × Qtd Caixas)

Peso Real por Caixa = Peso Real Total ÷ Qtd Caixas
```

---

## 🖥️ Exemplo de uso

```
════════════════════════════════════════════════════════════
        APURAÇÃO DE PESO REAL - CARNE REFRIGERADA
════════════════════════════════════════════════════════════

▶ PESO DO PALLET (kg)
   Peso do pallet: 25.00

▶ CAIXAS VAZIAS
   Peso de UMA caixa vazia (kg): 1.20
   Quantidade de caixas: 50

▶ EMBALAGEM PLÁSTICA (padrão por caixa)
   Peso de UMA embalagem plástica (kg): 0.05
   Quantidade de plásticos POR caixa: 4

▶ PESAGEM NA BALANÇA
   Peso TOTAL na balança (kg): 1200.00

════════════════════════════════════════════════════════════
                  RELATÓRIO DE APURAÇÃO
════════════════════════════════════════════════════════════
Peso total na balança                            1200.00 kg
(−) Peso do pallet                                 25.00 kg
(−) Caixas vazias (50x)                            60.00 kg
(−) Plásticos (4x por caixa)                       10.00 kg
────────────────────────────────────────────────────────────
PESO REAL TOTAL DE CARNE                         1105.00 kg
PESO REAL POR CAIXA                                22.10 kg
════════════════════════════════════════════════════════════
```

---

## 📁 Estrutura do projeto

```
apuracao-peso-carne/
│
├── apuracao.py       # Programa principal
├── README.md         # Este arquivo
└── (gerado) *.txt    # Relatórios salvos pelo usuário
```

---

## 🎨 Personalização

### Cores do terminal

No topo do arquivo `apuracao.py` há a tupla de cores ANSI:

```python
CORES = (
    "\033[1;36m",   # 0 - Títulos
    "\033[1;33m",   # 1 - Rótulos
    "\033[1;32m",   # 2 - Resultados
)
```

Altere os códigos ANSI para mudar o tema. Referência rápida:

| Código | Cor |
|---|---|
| `\033[1;31m` | Vermelho |
| `\033[1;32m` | Verde |
| `\033[1;33m` | Amarelo |
| `\033[1;34m` | Azul |
| `\033[1;35m` | Magenta |
| `\033[1;36m` | Ciano |

> ⚠️ **Windows:** para as cores funcionarem corretamente, execute no **Windows Terminal** ou **PowerShell 7+**. No `cmd.exe` antigo as cores ANSI podem não renderizar.

---

## 🛠️ Tecnologias

- **Python 3**
- Biblioteca padrão: `os`
- Códigos ANSI para cores no terminal

---

## 👤 Autor

**Julio Cesar Sarantes**

- 🌐 Site pessoal: [juliosutti.com.br](https://juliosutti.com.br)
- 💼 LinkedIn: [linkedin.com/in/jcsarantes](https://www.linkedin.com/in/jcsarantes)
- 🐙 GitHub: [@jcsaratnes-br](https://github.com/jcsaratnes-br)
- 📧 E-mail: [jcsarantes@gmail.com](mailto:jcsarantes@gmail.com)

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!
