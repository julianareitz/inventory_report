from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "CADEIRA",
        "Forces of Nature",
        "2022-04-04",
        "2023-02-09",
        "FR48",
        "Conservar em local fresco",
    )
    assert product.id == 1
    assert product.nome_do_produto == "CADEIRA"
    assert product.nome_da_empresa == "Forces of Nature"
    assert product.data_de_fabricacao == "2022-04-04"
    assert product.data_de_validade == "2023-02-09"
    assert product.numero_de_serie == "FR48"
    assert product.instrucoes_de_armazenamento == "Conservar em local fresco"
