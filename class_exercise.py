class Circulo:
    def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio

    def calc_area(self):
        area = (self.raio*self.raio)*3.14
        return area
    def calc_diametro(self):
        diametro = self.raio*2
        return diametro
    def calc_comprimento(self):
        comprimento = 2*3.14*self.raio
        return comprimento
    def muda_posicao(self):
        insere_x = int(input("Insira a nova posição do eixo X:"))
        insere_y = int(input("Insira a nova posição do eixo Y:"))
        self.x = insere_x
        self.y = insere_y
        return f"Novas coordenadas:{self.x, self.y}"

if __name__ == '__main__':
    circulo1 = Circulo(2,3,10)
    print(circulo1.calc_area())
    print(circulo1.calc_diametro())
    print(circulo1.calc_comprimento())
    print(circulo1.muda_posicao())
