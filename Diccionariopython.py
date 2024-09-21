import discord
import random
from bot_settings import settings
from bot_logic import gen_pass, gen_emodji_smile, gen_emodji_angry, gen_emodji_sad, flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hola!, has iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("hola, como has estado hoy?")
    if message.content.startswith("$hola amigo"):
        await message.channel.send("https://th.bing.com/th/id/OIP.1Won_QcQaiprPgZEPy52uwHaHH?rs=1&pid=ImgDetMain")
        await message.channel.send(f"Hola, bienvenid@, soy {client.user}")
    elif message.content.startswith('$bien'):
        await message.channel.send("me alegro, que tengas un lindo día")
    elif message.content.startswith('$adiós'):
        await message.channel.send("adiós, cúidate, no olvides regresar :)")
    elif message.content.startswith('$Genera una contraseña:'):
        x= random.randint(10, 20)
        await message.channel.send(f"Contraseña: {gen_pass(x)}")
    elif message.content.startswith('$¿Cómo estás?'):
        await message.channel.send("bien, y tú?")
    elif message.content.startswith('$cuál es tu aplicación favorita'):
        await message.channel.send("discord, me gusta que nostros los bots podamos ayudarlos aquí")
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji_smile())
    elif message.content.startswith('$angry'):
        await message.channel.send(gen_emodji_angry())
    elif message.content.startswith('$sad'):
        await message.channel.send(gen_emodji_sad())
    elif message.content.startswith('$coin'):
        image_url, message_text = flip_coin()
        await message.channel.send(message_text)
        await message.channel.send(image_url)
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('🤣'):
        await message.channel.send("😂")
    elif message.content.startswith('😎'):
        await message.channel.send("😎")
    elif message.content.startswith('$Tengo mucho sueño 🥱'):
        await message.channel.send("Hola, que puedo hacer para ayudarte 😴?")
    elif message.content.startswith('😑'):
        await message.channel.send("😐")
    elif message.content.startswith('😄'):
        await message.channel.send("😆")
    elif message.content.startswith('😨'):
        await message.channel.send("🤯")
    else:
        await message.channel.send("Aún no tengo programada esa función, lo siento :'v")

client.run("YOUR SECRET TOKEN")
