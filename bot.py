import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready for use desu")
    print("Fuck me nyaaaa desuu")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello nyaa! I am Kage's personal pet. Nice to meet you.")
@bot.command()    
async def hi(ctx):
    await ctx.send("Fuck me nyaaaa desuu")

@bot.command()    
async def greet(ctx, member: discord.Member):
    await ctx.send(f'Hello {member.mention} desu! i am your slave desu! ||plz cum on me desu!!||')

@bot.event
async def on_member_join(member):
    # Mention the new member and send a welcome message
    welcome_channel_id = 863643976333262871 
    welcome_channel = member.guild.get_channel(863643976333262871)
    
    if welcome_channel:
        await welcome_channel.send(f'konichiwa{member.mention} desu! Welcome to the server! if you need anything dont ask kage because he is dum dum ask me instead desu ')

@bot.event
async def on_member_remove(member):
    goodbye_channel = member.guild.get_channel(863643976333262871)

    if goodbye_channel:
        await goodbye_channel.send(f'sayonara nigga{member.mention}')
    
@bot.command()
async def send_meme(ctx):
    meme_url = 'https://cdn.discordapp.com/attachments/479963532000231424/1145732113186963559/369602742_2014977578862842_7572931396998453032_n.png'
    await ctx.send(meme_url) 



bot.run('NTc5MDMxNjQ4NDYxNTIwODk2.GuX1Rt.F6zALNDtujYeeoFkkuo1ULrDlCBXp-5BZdYG7k')