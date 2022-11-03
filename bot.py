import discord
from lib.point import Farquaad
from io import BytesIO


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
fq = Farquaad('farquad.jpg', 'impact.ttf')

keyword = 'fq '

with open('token', 'r') as f:
    token = f.read()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.content.startswith(keyword):
        img = fq.add_text(message.content[len(keyword):])
        output = BytesIO()
        img.save(output, format="jpeg")
        output.seek(0)
        await message.channel.send(file=discord.File(output,
                                                     f'{message.content[len(keyword):].replace(" ", "")}.jpeg'))

client.run(token)
