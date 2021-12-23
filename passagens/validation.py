def origem_destino_iguais(origem, destino, lista_erros):
    """[Valida se origem e destino são iguais]


    Args:

        origem ([str]): [Valor do campo origem da viagem]

        destino ([str]): [Valor do campo destino]

        lista_erros ([dict]): [lista que contem os erros das validações]
    """

    if origem == destino:

        lista_erros['destino'] = 'Origem e destino não podem ser iguais'


def campo_com_numero(valor_campo, nome_campo, lista_erros):
    """[Valida se os campos tem números]


    Args:

        valor_campo ([str]): [Valor do campo a ser validado]

        nome_campo ([str]): [Nome do campo a ser validado]

        lista_erros ([dict]): [Lista que contem os erros das validações]
    """

    if any(char.isdigit() for char in valor_campo):

        lista_erros['nome_campo'] = 'Não inclua números nesse campo'


def data_ida_maior_data_volta(data_ida, data_volta, lista_erros):
    """[Valida se data de ida é maior que data de volta]


    Args:

        data_ida ([str]): [Valor do campo data_ida]

        data_volta ([str]): [Valor do campo data_volta]

        lista_erros ([dict]): [Lista que contem os erros das validações]
    """

    if data_ida > data_volta:

        lista_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida'


def data_ida_menor_data_hoje(data_ida, data_hoje, lista_erros):
    """[Valida se data de ida é menor que data de hoje]

    Args:
        data_ida ([str]): [Valor do campo data_ida]
        data_hoje ([str]): [Valor do campo data_pesquisa]
        lista_erros ([dict]): [Lista que contem os erros das validações]
    """
    if data_ida < data_hoje:
        lista_erros['data_ida'] = 'Data de ida não pode ser menor que a data de hoje'
