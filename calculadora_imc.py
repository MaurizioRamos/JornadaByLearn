def calcular_media (notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  return media

def verificar_aprovacao (media):
  if media >= 6:
    
    print ('O Aluno está Aprovado',)
  else:
    print ('O Aluno está reprovado')
...
notas = [0,2,9,7]
media = calcular_media(notas)
print ('O Aluno tirou:', media)
verificar_aprovacao (media)