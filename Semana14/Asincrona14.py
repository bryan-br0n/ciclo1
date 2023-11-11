Nombres = [{'nombres': "Bryan Edenilson ", 'Apellidos': "Quintanilla Alberto", 'Edad': "22"},
           {'nombres': "Ale Alexa"}]

onlyname = []
respuesta = input("que nombre buscas")

for persona in Nombres:
    onlyname.append(persona['nombres'])
    print(persona['nombres'])
   