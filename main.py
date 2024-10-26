import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True
import os
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

imagen = os.listdir('images')
@bot.command()
async def climatico (ctx):
    await ctx.send('El Cambio climatico es cuando altas temperaturas en la Tierra.Esto puede pasar por la quema de gasolina de los carros y muchas otras cosas malas que afectan al planeta Tierra')
    img_name = imagen[0]
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("https://www.bing.com/ck/a?!&&p=4b06646b4367167eJmltdHM9MTcyOTY0MTYwMCZpZ3VpZD0zNGYyYWY0OC1mMTdlLTYzMGYtM2UzMS1iYjY2ZjAyOTYyNjkmaW5zaWQ9NTI0OQ&ptn=3&ver=2&hsh=3&fclid=34f2af48-f17e-630f-3e31-bb66f0296269&psq=que+es+cambio+climatico&u=a1aHR0cHM6Ly93d3cubWl0ZWNvLmdvYi5lcy9lcy9jYW1iaW8tY2xpbWF0aWNvL3RlbWFzL2VsLXByb2Nlc28taW50ZXJuYWNpb25hbC1kZS1sdWNoYS1jb250cmEtZWwtY2FtYmlvLWNsaW1hdGljby9uYWNpb25lcy11bmlkYXMvY29wMjEvZWwtY2FtYmlvLWNsaW1hdGljby5odG1s&ntb=1")
imagen = os.listdir('images')
@bot. command()
async def consequencias (ctx):
    await ctx.send('Las consecuencias por todas las cosas que le hacemos a la tierra forma ciclones, huracanes, muerte o migracion de animales, etc...')
    img_name = imagen[1]
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("https://www.bing.com/ck/a?!&&p=2a3a50b2d8efbfacJmltdHM9MTcyOTY0MTYwMCZpZ3VpZD0zNGYyYWY0OC1mMTdlLTYzMGYtM2UzMS1iYjY2ZjAyOTYyNjkmaW5zaWQ9NTI0NA&ptn=3&ver=2&hsh=3&fclid=34f2af48-f17e-630f-3e31-bb66f0296269&psq=consecuencias+del+cambio+clim%c3%a1tico+y&u=a1aHR0cHM6Ly93d3cuZnVuZGFjaW9uYXF1YWUub3JnL3dpa2kvY2F1c2FzLXktY29uc2VjdWVuY2lhcy1jYW1iaW8tY2xpbWF0aWNvLw&ntb=1")
@bot.command()
async def ayudar (ctx):
    await ctx.send('Como podemos ayudar al medio ambiente tenemos que ajustarnos a una dieta que tenga vegetales, o cuidar nuestro consumo de energia para ayudar al medio ambiente. ')
    img_name = imagen[2]
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("https://www.bing.com/ck/a?!&&p=80b4c6729f0145c8JmltdHM9MTcyOTY0MTYwMCZpZ3VpZD0zNGYyYWY0OC1mMTdlLTYzMGYtM2UzMS1iYjY2ZjAyOTYyNjkmaW5zaWQ9NTE5Ng&ptn=3&ver=2&hsh=3&fclid=34f2af48-f17e-630f-3e31-bb66f0296269&psq=como+puedo+ayudar+en+el+cambio+climatico+&u=a1aHR0cHM6Ly93d3cudW5lcC5vcmcvZXMvbm90aWNpYXMteS1yZXBvcnRhamVzL3JlcG9ydGFqZXMvMTAtbWFuZXJhcy1lbi1xdWUtcHVlZGVzLWF5dWRhci1jb21iYXRpci1sYS1jcmlzaXMtY2xpbWF0aWNh&ntb=1" )
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))

    else:
     await ctx.send("Olvidaste subir la imagen :(")
bot.run("Token")
