from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def company_stock(cls, products):
        stock = {}
        for product in products:
            if product["nome_da_empresa"] not in stock:
                stock[product["nome_da_empresa"]] = 0
            stock[product["nome_da_empresa"]] += 1
        return stock

    @classmethod
    def get_companies_stock(cls, products):
        stock = cls.company_stock(products)

        # stock_report = "Produtos estocados por empresa:\n"
        stock_report = ""

        for product in stock.items():
            stock_report += f"- {product[0]}: {product[1]}\n"
        return stock_report

    # @classmethod
    # def generate(cls, products) -> str:
    #     simple_report = super().generate(products)
    #     print('simple report 1', simple_report)
    #     return f"{simple_report}\n" f"{cls.get_companies_stock}"

    # print('Testando')

    @classmethod
    def generate(cls, products):
        oldest_manufacturing_date = cls.oldest_manufacturing_date(products)
        nearest_expiration_date = cls.nearest_expiration_date(products)
        company_with_more_products = cls.company_with_more_products(products)
        get_companies_stock = cls.get_companies_stock(products)
        return f"""Data de fabricação mais antiga: {oldest_manufacturing_date}
Data de validade mais próxima: {nearest_expiration_date}
Empresa com mais produtos: {company_with_more_products}
Produtos estocados por empresa:\n{get_companies_stock}"""


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
