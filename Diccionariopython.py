meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "OE": "Jerga peruana: Una forma de iniciar conversación, similar a oye",
            "CAUSA": "Jerga peruana: Signfica amigo",
            "PE": "Jerga peruana: Lo mismo que decir pues"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No conozco esa palabra")
