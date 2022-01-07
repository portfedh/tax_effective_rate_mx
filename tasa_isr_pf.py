
# Introduccion
print("\nCalculo de la tasa de impuesto de Persona Fisica")
print("    - Usando la Tarifa ISR 2021: Anual")
print("    - Obtenida del Articulo 96 de la Ley ISR \n")

print("Calculo mas conservador:")
print("    - Sin ingresos excentos.")
print("    - Sin deducciones autorizadas.\n")

print("Ultima actualizacion: 2 Junio 2021 \n\n")

# Constantes
limite1 = 7735
limite2 = 65651.07
limite3 = 115375.90
limite4 = 134119.41
limite5 = 160577.65
limite6 = 323862
limite7 = 510451
limite8 = 974535.03
limite9 = 299380.04
limite10 = 3898140.12

cuota_fija1 = 0
cuota_fija2 = 148.51
cuota_fija3 = 3855.14
cuota_fija4 = 9265.20
cuota_fija5 = 12264.16
cuota_fija6 = 17005.47
cuota_fija7 = 51883.01
cuota_fija8 = 95768.74
cuota_fija9 = 234993.95
cuota_fija10 = 338944.34
cuota_fija11 = 1222522.76

porcentaje_excedente1 = .0192
porcentaje_excedente2 = .0640
porcentaje_excedente3 = .1088
porcentaje_excedente4 = .1600
porcentaje_excedente5 = .1792
porcentaje_excedente6 = .2136
porcentaje_excedente7 = .2352
porcentaje_excedente8 = .3000
porcentaje_excedente9 = .3200
porcentaje_excedente10 = .3400
porcentaje_excedente11 = 0.3560


# Inputs
# salario_bruto_anual = float(input("¿Cuál es tu Salario Bruto Mensual?: "))
salario_bruto_mensual = int(input("¿Cuál es tu Salario Bruto Mensual?: "))


# Procesing
salario_bruto_anual = salario_bruto_mensual * 12

if salario_bruto_anual < 1:
    print("Error: El salario anual es demasiado bajo")
    limite_inferior = 0
    porcentaje_excedente = 0
    cuota_fija = 0

elif salario_bruto_anual <= limite1:
    limite_inferior = 0
    porcentaje_excedente = porcentaje_excedente1
    cuota_fija = cuota_fija1

elif salario_bruto_anual <= limite2:
    limite_inferior = limite1
    porcentaje_excedente = porcentaje_excedente2
    cuota_fija = cuota_fija2

elif salario_bruto_anual <= limite3:
    limite_inferior = limite2
    porcentaje_excedente = porcentaje_excedente3
    cuota_fija = cuota_fija3

elif salario_bruto_anual <= limite4:
    limite_inferior = limite3
    porcentaje_excedente = porcentaje_excedente4
    cuota_fija = cuota_fija4

elif salario_bruto_anual <= limite5:
    limite_inferior = limite4
    porcentaje_excedente = porcentaje_excedente5
    cuota_fija = cuota_fija5

elif salario_bruto_anual <= limite6:
    limite_inferior = limite5
    porcentaje_excedente = porcentaje_excedente6
    cuota_fija = cuota_fija6

elif salario_bruto_anual <= limite7:
    limite_inferior = limite6
    porcentaje_excedente = porcentaje_excedente7
    cuota_fija = cuota_fija7

elif salario_bruto_anual <= limite8:
    limite_inferior = limite7
    porcentaje_excedente = porcentaje_excedente8
    cuota_fija = cuota_fija8

elif salario_bruto_anual <= limite9:
    limite_inferior = limite8
    porcentaje_excedente = porcentaje_excedente9
    cuota_fija = cuota_fija9

elif salario_bruto_anual <= limite10:
    limite_inferior = limite9
    porcentaje_excedente = porcentaje_excedente10
    cuota_fija = cuota_fija10

else:
    limite_inferior = limite10
    porcentaje_excedente = porcentaje_excedente11
    cuota_fija = cuota_fija11


# Calculo
excedente = salario_bruto_anual - limite_inferior
impuesto_marginal = excedente * porcentaje_excedente
isr_causado = cuota_fija + impuesto_marginal
tasa_efectiva = isr_causado/salario_bruto_anual

# Output
print("\nSalario Mensual: " + "$" + "{:,.2f}".format(salario_bruto_mensual))
print("Salario Anual: " + "$" + "{:,.2f}".format(salario_bruto_anual))
print("Limite inferior: " + "$" + "{:,.2f}".format(limite_inferior))
print("Cuota Fija: " + "$" + "{:,.2f}".format(cuota_fija))
print("Tasa a Excedente: " + "{:,.2f}".format(porcentaje_excedente*100) + "%")
print("Excedente: " + "$" + "{:,.2f}".format(excedente))
print("Impuesto marginal: " + "$" + "{:,.2f}".format(impuesto_marginal))
print("ISR Causado: " + "$" + "{:,.2f}".format(isr_causado))
print("Tasa efectiva de impuestos: "
      + "{:,.2f}".format((isr_causado/salario_bruto_anual)*100)
      + "%")
