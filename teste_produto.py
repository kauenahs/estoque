from produto import Produto

p1 = Produto()
p1.nome = "macarrão parafuso"
p1.quantidade = 5

p2 = Produto()
p2.nome = "molho de tomate"
p2.quantidade = 3

print(f"{p1.nome}: {p1.quantidade} un")
print(f"{p2.nome}; {p2.quantidade} un")

def situacao(self):
    if self.quantidade == 0:
        return "Em falta"
    elif self.quantidade < 8:
        return "Repor"
    else:
        return "Ok"