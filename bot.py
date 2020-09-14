import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('I am Ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server . ')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server .')    


client.run('NzU1MTE2ODEzMTkyMjY1NzMw.X1-nVQ.5yGWftWnkUkBn_GwxBEQoFZiud4')
