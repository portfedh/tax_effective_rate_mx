from constantes import *

class TasaIsrPf():

    def __init__(self):
        self.introduccion()
        self.obtener_salario()
        self.obtener_valores()
        self.calcular_tasas()
        self.imprimir_resultado()
    
    def introduccion(self):
        print("\nCalculo de la tasa de impuesto de Persona Fisica")
        print("    - Usando la Tarifa ISR 2021: Mensual")
        print("    - Obtenida del Articulo 96 de la Ley ISR \n")
        print("Calculo mas conservador:")
        print("    - Sin ingresos excentos.")
        print("    - Sin deducciones autorizadas.\n")
        print("Ultima actualizacion: 12 Noviembre 2021 \n\n")

    def obtener_salario(self):
        self.salario_mensual = int(input("¿Cuál es tu salario bruto mensual?: "))

    def obtener_valores(self):
        if self.salario_mensual <= 0.01:
            print("Error: El salario anual es demasiado bajo")
            self.limite_inferior = 0
            self.porcentaje = 0
            self.cuota_fija = 0

        elif self.salario_mensual <= limite_superior_1:
            self.limite_inferior = 0.01
            self.porcentaje = porcentaje_1
            self.cuota_fija = cuota_1

        elif self.salario_mensual <= limite_superior_2:
            self.limite_inferior = limite_superior_1
            self.porcentaje = porcentaje_2
            self.cuota_fija = cuota_2

        elif self.salario_mensual <= limite_superior_3:
            self.limite_inferior = limite_superior_2
            self.porcentaje = porcentaje_3
            self.cuota_fija = cuota_3

        elif self.salario_mensual <= limite_superior_4:
            self.limite_inferior = limite_superior_3
            self.porcentaje = porcentaje_4
            self.cuota_fija = cuota_4

        elif self.salario_mensual <= limite_superior_5:
            self.limite_inferior = limite_superior_4
            self.porcentaje = porcentaje_5
            self.cuota_fija = cuota_5

        elif self.salario_mensual <= limite_superior_6:
            self.limite_inferior = limite_superior_5
            self.porcentaje = porcentaje_6
            self.cuota_fija = cuota_6

        elif self.salario_mensual <= limite_superior_7:
            self.limite_inferior = limite_superior_6
            self.porcentaje = porcentaje_7
            self.cuota_fija = cuota_7

        elif self.salario_mensual <= limite_superior_8:
            self.limite_inferior = limite_superior_7
            self.porcentaje = porcentaje_8
            self.cuota_fija = cuota_8

        elif self.salario_mensual <= limite_superior_9:
            self.limite_inferior = limite_superior_8
            self.porcentaje = porcentaje_9
            self.cuota_fija = cuota_9

        elif self.salario_mensual <= limite_superior_10:
            self.limite_inferior = limite_superior_9
            self.porcentaje = porcentaje_10
            self.cuota_fija = cuota_10
        else:
            self.limite_inferior = limite_superior_10
            self.porcentaje = porcentaje_11
            self.cuota_fija = cuota_11

    def calcular_tasas(self):
        self.excedente = self.salario_mensual - self.limite_inferior
        self.impuesto_marginal = self.excedente * self.porcentaje
        self.isr_causado = self.cuota_fija + self.impuesto_marginal
        self.tasa_efectiva = self.isr_causado/self.salario_mensual

    def imprimir_resultado(self):
        print("\nSalario Mensual: " + "$" + "{:,.2f}".format(self.salario_mensual))
        print("Salario Anual: " + "$" + "{:,.2f}".format(self.salario_mensual))
        print("Limite inferior: " + "$" + "{:,.2f}".format(self.limite_inferior))
        print("Cuota Fija: " + "$" + "{:,.2f}".format(self.cuota_fija))
        print("Tasa a Excedente: " + "{:,.2f}".format(self.porcentaje*100) + "%")
        print("Excedente: " + "$" + "{:,.2f}".format(self.excedente))
        print("Impuesto marginal: " + "$" + "{:,.2f}".format(self.impuesto_marginal))
        print("ISR Causado: " + "$" + "{:,.2f}".format(self.isr_causado))
        print("Tasa efectiva de impuestos: "
            + "{:,.2f}".format((self.tasa_efectiva)*100)
            + "%")


if __name__ == "__main__":
    oTasaIsr = TasaIsrPf()