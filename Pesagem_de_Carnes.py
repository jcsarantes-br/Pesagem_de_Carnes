# ============================================================
#   APURAÇÃO DE PESO REAL - CARNE REFRIGERADA
# ============================================================

import os

# ---------- TUPLA DE CORES (máximo 3 cores) ----------
# Índices: 0=Título, 1=Rótulos, 2=Destaque/Resultado
CORES = (
    "\033[1;36m",   # 0 - Ciano brilhante (títulos)
    "\033[1;33m",   # 1 - Amarelo brilhante (rótulos)
    "\033[1;32m",   # 2 - Verde brilhante (resultados)
)
RESET = "\033[0m"
NEGRITO = "\033[1m"


# ---------- FUNÇÕES AUXILIARES ----------
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def linha(char="═", tam=60, cor=0):
    print(CORES[cor] + char * tam + RESET)


def titulo(texto):
    linha("═", 60, 0)
    print(CORES[0] + NEGRITO + texto.center(60) + RESET)
    linha("═", 60, 0)


def pedir_float(msg):
    """Lê um número float positivo, com validação."""
    while True:
        try:
            valor = float(input(CORES[1] + msg + RESET).replace(",", "."))
            if valor < 0:
                print("\033[1;31m✖ Valor não pode ser negativo. Tente novamente.\033[0m")
                continue
            return valor
        except ValueError:
            print("\033[1;31m✖ Entrada inválida. Digite um número (ex: 12.50).\033[0m")


def pedir_int(msg):
    """Lê um número inteiro positivo, com validação."""
    while True:
        try:
            valor = int(input(CORES[1] + msg + RESET))
            if valor < 0:
                print("\033[1;31m✖ Valor não pode ser negativo. Tente novamente.\033[0m")
                continue
            return valor
        except ValueError:
            print("\033[1;31m✖ Entrada inválida. Digite um número inteiro.\033[0m")


# ---------- PROGRAMA PRINCIPAL ----------
def main():
    limpar_tela()
    titulo("APURAÇÃO DE PESO REAL - CARNE REFRIGERADA")

    # --- Peso do pallet (definido uma vez) ---
    print(CORES[1] + "\n▶ PESO DO PALLET (kg)" + RESET)
    peso_pallet = pedir_float("   Peso do pallet: ")

    # --- Peso da caixa vazia (definido uma vez) ---
    print(CORES[1] + "\n▶ CAIXAS VAZIAS" + RESET)
    peso_caixa_vazia = pedir_float("   Peso de UMA caixa vazia (kg): ")
    qtd_caixas = pedir_int("   Quantidade de caixas: ")

    # --- Embalagem plástica (padrão definido apenas uma vez) ---
    print(CORES[1] + "\n▶ EMBALAGEM PLÁSTICA (padrão por caixa)" + RESET)
    peso_plastico_unit = pedir_float("   Peso de UMA embalagem plástica (kg): ")
    qtd_plastico_por_caixa = pedir_int("   Quantidade de plásticos POR caixa: ")

    # --- Peso total na balança ---
    print(CORES[1] + "\n▶ PESAGEM NA BALANÇA" + RESET)
    peso_balanca = pedir_float("   Peso TOTAL na balança (pallet + caixas + carne + plásticos) (kg): ")

    # ---------- CÁLCULOS ----------
    peso_total_caixas_vazias = peso_caixa_vazia * qtd_caixas
    peso_total_plasticos     = peso_plastico_unit * qtd_plastico_por_caixa * qtd_caixas

    peso_real_total = peso_balanca - peso_pallet - peso_total_caixas_vazias - peso_total_plasticos
    peso_real_por_caixa = peso_real_total / qtd_caixas if qtd_caixas > 0 else 0

    # ---------- RELATÓRIO ----------
    print()
    linha("═", 60, 2)
    print(CORES[2] + NEGRITO + "RELATÓRIO DE APURAÇÃO".center(60) + RESET)
    linha("═", 60, 2)

    def item(rotulo, valor, unidade="kg"):
        print(f"{CORES[1]}{rotulo:<45}{RESET}{CORES[2]}{valor:>10.2f} {unidade}{RESET}")

    item("Peso total na balança",              peso_balanca)
    item("(−) Peso do pallet",                 peso_pallet)
    item(f"(−) Caixas vazias ({qtd_caixas}x)", peso_total_caixas_vazias)
    item(f"(−) Plásticos ({qtd_plastico_por_caixa}x por caixa)",
         peso_total_plasticos)

    linha("─", 60, 1)

    item("PESO REAL TOTAL DE CARNE",           peso_real_total)
    item("PESO REAL POR CAIXA",                peso_real_por_caixa)

    linha("═", 60, 2)

    # ---------- SALVAR EM TXT ----------
    salvar = input(CORES[1] + "\nDeseja salvar o relatório em .txt? (s/n): " + RESET).strip().lower()
    if salvar == "s":
        nome = input(CORES[1] + "Nome do arquivo (sem extensão): " + RESET).strip() or "apuracao"
        with open(f"{nome}.txt", "w", encoding="utf-8") as f:
            f.write("RELATÓRIO DE APURAÇÃO - CARNE REFRIGERADA\n")
            f.write("=" * 50 + "\n")
            f.write(f"Peso total na balança........: {peso_balanca:>10.2f} kg\n")
            f.write(f"Peso do pallet................: {peso_pallet:>10.2f} kg\n")
            f.write(f"Caixas vazias ({qtd_caixas}x)........: {peso_total_caixas_vazias:>10.2f} kg\n")
            f.write(f"Plásticos.....................: {peso_total_plasticos:>10.2f} kg\n")
            f.write("-" * 50 + "\n")
            f.write(f"PESO REAL TOTAL...............: {peso_real_total:>10.2f} kg\n")
            f.write(f"PESO REAL POR CAIXA...........: {peso_real_por_caixa:>10.2f} kg\n")
        print(CORES[2] + f"\n✔ Arquivo '{nome}.txt' salvo com sucesso!" + RESET)


if __name__ == "__main__":
    while True:
        main()
        print()
        cont = input(CORES[1] + "Deseja fazer outra apuração? (s/n): " + RESET).strip().lower()
        if cont != "s":
            print(CORES[2] + "\n✔ Programa encerrado. Até logo!\n" + RESET)
            break
        limpar_tela()