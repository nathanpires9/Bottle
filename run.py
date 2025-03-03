try:
    from config import *

except:
    print('Failed to load config file')



try:
    import os, discord, asyncio, requests, time, sys, youtube_dl, traceback
    from datetime import datetime, timezone
    from discord.ext import commands, tasks
    from discord import Intents
    
except:
    print('Failed to 1 or more import(s)\nAttempting to install them')
    os.system('pip3 install discord.py')
    os.system('pip3 install requests')
    os.system('pip3 install asyncio')
    os.system('pip3 install datetime')
    os.system('pip3 install yt_dlp')
    os.system('pip3 install pynacl')
    os.system('pip3 install audioop-lts') # If python3 > 3.12 version required
    os.system('pip3 install pydub') # For cliphub

    import os, discord, asyncio, requests, time, sys, youtube_dl, traceback
    from datetime import datetime, timezone
    from discord.ext import commands, tasks
    from discord import Intents


intents =  Intents.all()



bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=intents)
bot.remove_command("help") # REMOVING SINCE WE WROTE OUR OWN CLEANER ONE
bot.launch_time = datetime.now(timezone.utc)


def cls():
    os.system("cls || clear")

@tasks.loop(seconds=3)
async def change_status():
    for x in status:
        await bot.change_presence(activity=discord.Game(x))
        await asyncio.sleep(2)


@bot.event
async def on_ready():
    change_status.start()
    today = date.today()
    #Month abbreviation, day  and year
    start = today.strftime("%b-%d-%Y")
    cls()

    # Retrive bots amount of servers
    total_server = len(bot.guilds)
    print(f"{name} is online\nUsername: {bot.user.name}\nID: {bot.user.id}\nServer Count: {total_server}")

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        message = f'Welcome {member.mention} to {guild}, enjoy your stay!'
        await guild.system_channel.send(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        msg = f'```Error, Command Not Found! Type {prefix}help for a list of commands```'
        await ctx.send(msg)

    elif isinstance(error, commands.MissingRequiredArgument):
        msg = f'```Error, missing required arugment```'
        await ctx.send(msg)

    elif isinstance(error, commands.MissingRole):
        msg = f'```Error, missing required role```'
        await ctx.send(msg)

    elif isinstance(error, commands.NSFWChannelRequired):
        msg = f'```Error, This is **not a nsfw** channel```'

    elif isinstance(error, commands.MissingPermissions):
        msg = f'```Error, missing required permissions```'
        await ctx.send(msg)
    elif isinstance(error, commands.CommandOnCooldown):
        msg = f'```Error, Command is on cooldown! Please wait {round(error.retry_after, 2)}s```'
        await ctx.send(msg)

@bot.event
async def on_message(message):
    upper = message.content.upper()  # UPPER SO IT STILL CATCHES BLACKLISTS
    user_id = message.author.id
    channel = bot.get_channel(log_channel_id)  # CURRENT CHANNEL
    channel2 = bot.get_channel(message.channel.id)  # CHANNEL TO LOG TO ( Changed in config.py )
    
    #If someone just pings the bot tell them the prefix
    if message.content == f"<@{bot.user.id}>":
        embed = discord.Embed(title=f"__**{name} Prefix**__", description=f"My prefix is currently set to: **{prefix}**",color=embed_color)
        embed.set_footer(text=f"Requested by {message.author.name}", icon_url=message.author.avatar)
        await channel2.send(embed=embed)

    for word in blacklisted:
        if upper.find(word) != -1:
            if message.author == bot.user:
                await bot.process_commands(message)
                return

            elif user_id in whitelisted:
                await bot.process_commands(message)
                return


            else:
                await message.channel.purge(limit=1)
                await channel.send(f'Blacklisted word from {message.author} message: {message.content}')
                await channel2.send(f'Your message contains 1 or more blacklisted word(s) {message.author.mention}')
                await bot.process_commands(message)
    await bot.process_commands(message)
#~~~~~~~~~~~~~~~~~~ EVENTS ~~~~~~~~~~~~~~~~~~~



@bot.command(aliases=["PING", "Ping", "pong", "PONG", "Pong"])
async def ping(ctx):
    embed = discord.Embed(title=f"__**{name} Latency**__", description=f"Pong {round(bot.latency * 1000)}ms :ping_pong:",color=embed_color)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.message.author.avatar)
    await ctx.send(embed=embed)
    


@bot.command(aliases=["uptimes","UPTIME","UPTIMES"])
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(title=f"__**{name} Bot Uptime**__", description=f"Elapsed for {days}d, {hours}h, {minutes}m, {seconds}s", color=embed_color)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)



#Loading commands from the cogs new Version2 way
async def load():
    initial_extensions = ["cogs.modhub","cogs.funhub"]
    if __name__ == "__main__":
        for extension in initial_extensions:
            try:
                await bot.load_extension(extension)
            except Exception as e:
                print(f"Failed to load extension {extension}", file=sys.stderr)
                await asyncio.sleep(2)
                cls()
                traceback.print_exc()

#client connect
async def main():
    async with bot:
        await load()
        await bot.start(token)



asyncio.run(main()) # Login to the bot


