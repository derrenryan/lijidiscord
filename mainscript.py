# Discord Bot

#-------------------#

#Token: NTA5NjM4MDk1MzEwOTQ2MzA0.DsQtBQ.qH-a-L0_mTr4Rsh5z3NP79RQltE
#InviteLink: https://discordapp.com/api/oauth2/authorize?client_id=509638095310946304&permissions=8&scope=bot
#Secret: c1Olusmm6x05IDZRbNkVKTmpger_KdNg

#--------------------#

#NewSecreToken: 2SC4x5himYdqeZ3lxS-gKy3ycJY8EJRE
#NewClientID: 510775849692168223
Token =  'NTEwNzc1ODQ5NjkyMTY4MjIz.DshRAw.WBotEcMKLeQSnfnguccZErRKjy8d'
#NewInviteLink: https://discordapp.com/api/oauth2/authorize?client_id=510775849692168223&permissions=2146958839&scope=bot

#--------------------#

import discord
from discord.ext import commands
import random

prefix = "l!"

client=discord.Client()

#BotStart
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

#8ballCommand
@client.event
async def on_message(message):
	if message.content.startswith(prefix + "8ball"):
		ballmessage = random.choice(["Not Sure", "Maybe", "Who Knows?", "Yes!", "NO WAY!", "NO MEANS NO!"])
		await client.send_message(message.channel, ballmessage)

#PrefixCommand
@client.event
async def on_message(message):
	if message.content.startswith("@Liji#2480 What is your prefix?"):
		await client.send_message(message.channel, "It's " + prefix)

#WhoAreYou
@client.event
async def on_message(message):
	if message.content.startswith("@Liji#2480 Who are you?"):
		await client.send_message(message.channel, "Hello, I'm <@510775849692168223> Created by <@414839769311215617>. I'm a basic and simple bot.")

#@client.command()
#async def kick	

client.run(Token) 