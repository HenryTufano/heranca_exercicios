from classeingresso import Ingresso
p=Ingresso()
class VIP(Ingresso):
    def __init__(self,valor,adicional):
        v=valor+adicional
        p.ImprimeValor(v)
