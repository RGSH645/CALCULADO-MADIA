nome = input("Digiteco nome do aluno: ")

nota1 = float(input("Digite a primeira nota do aluno")) #Definimos a varial notal ela é do tipo float 
nota2 = float(input("Digite a segunda nota do aluno"))
nota3 = float(input("Degite a terceira nota do aluno"))

media = (nota1+nota2+nota3)/3 #estmos fazendo o calculo de media 

print(f"A media do aluno é: {media:.2f} ") #f significa fstring para eu conseguir colocar a variavel entre aspas"
#{media} colocar entre chaves para conseguir colocar a variavel media na string 
#:.2f significa quantas casas apos a virgula 
print(f"a media do aluno é: {media:.2f}")
 if media >=7:
     print("aprovado")
 else:
     print("Aprovado :(")
