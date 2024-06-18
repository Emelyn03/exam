sistema = "S"

while sistema == "S": 
  estudiante = {"Nombre" : "", "Matricula" : ""}

  estudiante["Nombre"] = input("Ingrese el nombre del estudiante: ")
  estudiante["Matricula"] = input("Ingrese su matricula: ")
  print(estudiante)

  nota1 = int(input("Ingrese la primera nota: "))
  nota2 = int(input("Ingrese la segunda nota: "))
  nota3 = int(input("Ingrese la tercera nota: "))
  nota4 = int(input("Ingrese la cuarta nota: "))

  notas = []
  notas.append(nota1)
  notas.append(nota2)
  notas.append(nota3)
  notas.append(nota4)
  if notas[0] < 0 or notas[1] > 100 or notas[1] < 0 or notas[1] > 100 or notas[2] < 0 or notas[2] > 100 or notas[3] < 0 or notas[3] > 100:
    print("Las notas deben ser mayores o iguales a 0 y menores o iguales a 100")
    break
  else:
    promedio_notas = sum(notas)/len(notas )



    print("El promedio de ", estudiante["Nombre"], " es de ", promedio_notas)
  sistema = input("Desea hacer lo mismo con otro estudiante? (S/N): ")