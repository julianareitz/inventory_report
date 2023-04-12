from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def get_oldest_manufacturing_date(cls, products):
        return min(product["data_de_fabricacao"] for product in products)

    @classmethod
    def get_nearest_expiration_date(cls, products):
        today = datetime.today().date()
        date_pattern = "%Y-%m-%d"
        nearest_expiration = min(
            [
                product["data_de_validade"]
                for product in products
                if datetime.strptime(
                    product["data_de_validade"], date_pattern
                ).date()
                > today
            ]
        )
        return nearest_expiration

    @classmethod
    def get_company_with_more_products(cls, products):
        return Counter(
            product["nome_da_empresa"] for product in products
        ).most_common()[0][0]

    @classmethod
    def generate(cls, products):
        oldest_manufacturing_date = cls.get_oldest_manufacturing_date(products)
        nearest_expiration_date = cls.get_nearest_expiration_date(products)
        company_with_more_products = cls.get_company_with_more_products(
            products
        )
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
