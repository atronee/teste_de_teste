ingredientes={"massa":dict(), "molho":dict(), "cobertura":dict(), "queijo":dict()}
def cadastrar_ingrediente(tipo, ingrediente, valor):
    """Cadastrar Ingrediente
    :param tipo: tipo de ingrediente
    :type tipo: string
    :param ingrediente: ingrediente
    :type ingrediemte: string
    :param valor: valor do ingrediente
    :type valor: float
    :return: dicionário com os ingredientes
    :return type: dict

    >>> cadastrar_ingrediente("massa", "trigo", 19.34)
    {'massa': {'trigo': 19.34}, 'molho': {}, 'cobertura': {}, 'queijo': {}}
    >>> cadastrar_ingrediente("molho", "tomate", 5)
    {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {}, 'queijo': {}}
    >>> cadastrar_ingrediente("cobertura", "pepperoni", 5)
    {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {}}
    >>> cadastrar_ingrediente("queijo", "gorgonzola", 2)
    {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {'pepperoni': 5}, 'queijo': {'gorgonzola': 2}}
    """
    ingredientes[tipo][ingrediente]=valor
    return ingredientes


def montar_pizzza_valor(massa, molho, queijo, cobertura):
    """Montar pizza e retornar valor
    :param massa: massa escolhida
    :type massa: string
    :param molho: molho escolhido
    :type molho: string
    :param queijo: queijo escolhido
    :type queijo: string
    :param cobertura: cobertura escolhida
    :type cobertura: string
    :return: preço da pizza
    :return type: float
    
    >>> montar_pizzza_valor("trigo", "tomate", "gorgonzola", "pepperoni")
    31.34
    """
    valor = 0
    valor+=ingredientes["massa"][massa]
    valor+=ingredientes["molho"][molho]
    valor+=ingredientes["queijo"][queijo]
    valor+=ingredientes["cobertura"][cobertura]

    return valor

def remover_ingrediente(tipo,ingrediente):
    """Remove ingrediente do inventário
    :param tipo: tipo do ingrediente
    :type tipo: string
    :param ingrediente: ingrediente
    :type ingrediente: string
    :return: dicionário com os ingredientes
    :return type: dict

    >>> remover_ingrediente("cobertura", "pepperoni")
    {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {}, 'queijo': {'gorgonzola': 2}}
    """
    ingredientes[tipo].pop(ingrediente)
    return ingredientes

def listar_ingredientes(tipo):
    """Lista ingredientes e seus preços
    :param tipo: tipo do ingrediente
    :type tipo: string
    :return: dicionário dos ingredientes desse tipo e seus respectivos preços
    :return type: dict

    >>> listar_ingredientes("massa")
    {'trigo': 19.34}
    """
    tipo_ingrediente=ingredientes[tipo]
    return tipo_ingrediente


if __name__ =="__main__":
    import doctest
    doctest.testmod(verbose=True)
