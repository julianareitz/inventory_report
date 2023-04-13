from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id_product = 1
    product_name = "Nupoca Cacau"
    product_brand = "Mãe Terra"
    product_manufacturing_date = "01/02/2023"
    product_expiration_date = "01/06/2023"
    product_serial_or_batch_number = "GDSOGK0845341"
    product_preservation_directions = (
        "Conservar em local fresco, seco e ao abrigo do sol"
    )

    product = Product(
        id_product,
        product_name,
        product_brand,
        product_manufacturing_date,
        product_expiration_date,
        product_serial_or_batch_number,
        product_preservation_directions,
    )
    assert product.id == 1
    assert product.nome_do_produto == product_name
    assert product.nome_da_empresa == product_brand
    assert product.data_de_fabricacao == product_manufacturing_date
    assert product.data_de_validade == product_expiration_date
    assert product.numero_de_serie == product_serial_or_batch_number
    assert (
        product.instrucoes_de_armazenamento == product_preservation_directions
    )
