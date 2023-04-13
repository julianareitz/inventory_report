from inventory_report.reports.simple_report import SimpleReport

# from collections import Counter


class CompleteReport(SimpleReport):
    #     @classmethod
    # def get_companies_stock(cls, list):
    #     companies = dict()
    #     for i in list:
    #         for k, v in companies.items():
    #             companies.setdefault(k, set()).add(v)
    #     companies_stock = {k: len(v) for k, v in companies.items()}
    #     return companies_stock
    @classmethod
    def generate(cls, report) -> str:
        simple_report = super().generate(report)
        # print('simple report 1', simple_report)
        companies = [company["nome_da_empresa"] for company in report]
        print(companies)

        stock_report = "Produtos estocados por empresa: \n"

        for company in companies:
            stock_report += f"- {company}: {companies[1]}\n"
        # print(stock_report)

        return f"{simple_report}\n" f"{stock_report}"

        # print('Testando')


# PARAMETRO RECEBIDO
# [
#   {
#     "id": 1,
#     "nome_do_produto": "MESA",
#     "nome_da_empresa": "Forces of Nature",
#     "data_de_fabricacao": "2022-05-04",
#     "data_de_validade": "2023-02-09",
#     "numero_de_serie": "FR48",
#     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
#   }
# ]

# SAIDA ESPERADA
# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com mais produtos: NOME DA EMPRESA
# Produtos estocados por empresa:
# - Physicians Total Care, Inc.: QUANTIDADE
# - Newton Laboratories, Inc.: QUANTIDADE
# - Forces of Nature: QUANTIDADE
