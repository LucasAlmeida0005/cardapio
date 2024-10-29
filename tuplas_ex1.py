estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5} 
cardapio = { 
'x-burguer': ['pao', 'hamburguer'], 
'x-salada': ['pao', 'hamburguer', 'tomate'], 
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'], 
'x-egg': ['pao', 'hamburguer', 'ovo'], 
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo'] 
} 
validador = 0
print("Cardápio:")
for lanche, ingredientes in cardapio.items():
  print(f"\n{lanche}\ningredientes:",end=" ")
  i = 0
  while i != len(ingredientes):
    print(ingredientes[i],end=",")
    i = i+1
  print("\n")
x = 0
while x != 1:
   pedido = input("Oque deseja pedir? (0 para sair)")
   if pedido == 'x-burguer' or pedido == 'x-salada' or pedido == 'x-bacon' or pedido == 'x-egg' or pedido == 'x-tudo' :

         if pedido == 'x-burguer':
            for i, qt in estoque.items():
               if qt > 0 and i == 'pao':
                  validador = 1
               if validador == 1:
                  if qt > 0 and i == 'hamburguer':
                     estoque["hamburguer"] += -1
                     estoque["pao"] += -1
                     validador = 1
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif qt == 0:
                  print(f"Infelizmente acabou o {i}.")
         elif pedido == 'x-salada':
            for i, qt in estoque.items():
               if qt > 0 and i == 'pao':
                  validador = 1
               if validador == 1:
                  if qt > 0 and i == 'hamburguer':
                     validador = 2
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 2:
                  if qt > 0 and i == 'tomate':
                     estoque["hamburguer"] += -1
                     estoque["pao"] += -1
                     estoque["tomate"] += -1
                     validador = 1
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif qt == 0:
                  print(f"Infelizmente acabou o {i}.")
         elif pedido == 'x-bacon':
            for i, qt in estoque.items():
               if qt > 0 and i == 'pao':
                  validador = 1
               if validador == 1:
                  if qt > 0 and i == 'hamburguer':
                     validador = 2
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 2:
                  if qt > 0 and i == 'tomate':
                     validador = 3
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 3:
                  if qt > 0 and i == 'bacon':
                     estoque["hamburguer"] += -1
                     estoque["pao"] += -1
                     estoque["tomate"] += -1
                     estoque["bacon"] += -1
                     validador = 1
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif qt == 0:
                  print(f"Infelizmente acabou o {i}.")
         elif pedido == 'x-egg':
            for i, qt in estoque.items():
               if qt > 0 and i == 'pao':
                  validador = 1
               if validador == 1:
                  if qt > 0 and i == 'hamburguer':
                     validador = 2
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 2:
                  if qt > 0 and i == 'ovo':
                     estoque["hamburguer"] += -1
                     estoque["pao"] += -1
                     estoque["ovo"] += -1
                     validador = 1
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif qt == 0:
                  print(f"Infelizmente acabou o {i}.")
         elif pedido == 'x-tudo':
            for i, qt in estoque.items():
               if qt > 0 and i == 'pao':
                  validador = 1
               if validador == 1:
                  if qt > 0 and i == 'hamburguer':
                     validador = 2
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 2:
                  if qt > 0 and i == 'tomate':
                     validador = 3
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 3:
                  if qt > 0 and i == 'bacon':
                     validador = 4
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif validador == 4:
                  if qt > 0 and i == 'ovo':
                     estoque["hamburguer"] += -1
                     estoque["pao"] += -1
                     estoque["tomate"] += -1
                     estoque["bacon"] += -1
                     estoque['ovo'] += -1
                     validador = 1
                  elif qt == 0:
                     validador = 0
                     print(f"Infelizmente acabou o {i}.")
               elif qt == 0:
                  print(f"Infelizmente acabou o {i}.")
         if validador == 1:
            print(f"Um {pedido} saindo no capricho!")
         print(estoque)
      # else:
      #    print("Obrigado por comer no restaurante boca feliz!")
      #    x = 1
   elif pedido == '0':
      print("Obrigado pela visita!")
      x = 1
   else:
      print("Você digitou um lanche que não está no cardápio!")
