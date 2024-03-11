#Ejercicio 1
VariableSaludo  = "Hola"
VariableNumero  = 1
VariableLista   = ["Naia","Iván","Astrid","Max"]
VariableBoolean = True

#Ejercicio 2
VariableTresPrimerasLetras  = VariableSaludo[:3]
#Comprobación de que está bien
print(VariableTresPrimerasLetras)

#Ejercicio 3
print(VariableLista.index("Naia"))

#Ejercicio 4
VariableNumero  += 10
#Comprobación de que está bien
print(VariableNumero)

#Ejercicio 5
print(VariableLista.index("Max"))

#Ejercicio 6
names = 'harry,alex,susie,jared,gail,conner'
lista = names.split()
#Comprobación de que está bien
print(lista)

#Ejercicio 7
VariablePrimeraLetraDeMiString = VariableSaludo[:1]
#Comprobación de que está bien
print(VariablePrimeraLetraDeMiString)
VariableSaludoEnMayusculas = VariableSaludo.upper()
#Comprobación de que está bien
print(VariableSaludoEnMayusculas)
VariableSaludoMayusculasYOriginal = VariableSaludo.upper() + VariableSaludo[1:]
#Comprobación de que está bien
print(VariableSaludoMayusculasYOriginal)

#Ejercicio 8
print(f"My number variable is: {VariableNumero}")

#Ejercicio 9
print('hello world')

#Ejercicio Extra 
String = "Hola"
IndexWord = String.index("Hola")
StringReplace = String.replace("Hola","adiós")
print(StringReplace)