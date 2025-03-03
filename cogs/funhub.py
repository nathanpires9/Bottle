import os, discord, asyncio, requests, time,random
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import cooldown
from discord.utils import get
import discord.utils 
from config import *





n = random.randint(0,10)
size = (n * '=')

class funhub(commands.Cog, name="funhub"):

    def __init__(self, bot):
        self.commands = bot
        self._cd = commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.user)

#---------------------------------------------------------------
    @commands.command(aliases=['av','AV','Av','avatar'])
    async def grab(self,ctx,member : discord.Member=None):

        if member == None:
            await ctx.send(f'__**AVATAR GRABBER**__\n\n**USER:** {ctx.message.author.mention}\n**Link:** {ctx.author.avatar.url}')
        else:
            await ctx.send(f'__**AVATAR GRABBER**__\n\n**USER:** {member.mention}\n**Link:** {member.avatar.url}\n')

#---------------------------------------------------------------    


#---------------------------------------------------------------

    @commands.command(aliases=["howgay","gay","rate"])
    async def howgayis(self, ctx,member : discord.Member=None):
        g = random.randint(0,100)

        if member == None:
            embed = discord.Embed(title="__**GAY MACHINE**__", description=f"{ctx.message.author}'s is {g}% gay", color=embed_color)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="__**GAY MACHINE**__", description=f"{member.mention}'s is {g}% gay", color=embed_color)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)


#---------------------------------------------------------------



#---------------------------------------------------------------

    @commands.command(aliases=["simprate","simp","ratesimp","simperate"])
    async def simpcheck(self, ctx,member : discord.Member=None):
        g = random.randint(0,100)

        if member == None:
            embed = discord.Embed(title="__**SIMP MACHINE**__", description=f"{ctx.message.author}'s is {g}% a simp", color=embed_color)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="__**SIMP MACHINE**__", description=f"{member.mention}'s is {g}% a simp", color=embed_color)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)


#---------------------------------------------------------------



#---------------------------------------------------------------

    @commands.command(aliases=["ADVICE","Advice","advices"])
    async def advice(self, ctx):
        api = 'https://api.adviceslip.com/advice'
        response = requests.get(api)
        resolve = response.json()
        advice_response = resolve["slip"]
        advice_string= advice_response["advice"]

        embed = discord.Embed(title="__**ADVICE Generator**__", description=f"Fear not i am here to help\nAdvice: {advice_string}", color=embed_color)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)


#---------------------------------------------------------------





#---------------------------------------------------------------

    @commands.command(aliases=["joke","Joke","tellmeajoke"])
    async def joker(self, ctx):
        api = 'https://official-joke-api.appspot.com/jokes/random'
        response = requests.get(api)
        resolve = response.json()
        setup = resolve["setup"]
        punch = resolve["punchline"]
        embed = discord.Embed(title="__**Joke Genearator**__", description=f"Question: {setup}\n\nPunchline: ||{punch}||", color=embed_color)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)




#---------------------------------------------------------------





#---------------------------------------------------------------


  




    @commands.command(aliases=["penis","PP","howbig"])
    async def pp(self, ctx,member : discord.Member=None):
        n = random.randint(0,20)
        size = (n * '=')
        if member == None:
            embed = discord.Embed(title="__**PENIS MACHINE**__", description=f"{ctx.message.author}'s Penis size\n8{size}>", color=embed_color)
            embed.set_footer(text=f'{name} Bot')
            await ctx.send(embed=embed)


        else:
            embed = discord.Embed(title="__**PENIS MACHINE**__", description=f"{member.mention}'s Penis size\n8{size}>", color=embed_color)
            embed.set_footer(text=f'{name} Bot')
            await ctx.send(embed=embed)



    # TOOLS COMMANDS
    @commands.command()
    async def insult(self,ctx,member : discord.Member=None):
        if member == None:
            url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
            response = requests.get(url).json()
            insult = response["insult"]
            embed = discord.Embed(title="__**Insult Generator**__", description=f"{ctx.message.author.mention} {insult}", color=embed_color)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)        

        else:
            url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
            response = requests.get(url).json()
            insult = response["insult"]
            embed = discord.Embed(title="__**insult Generator**__", description=f"{member.mention} {insult}", color=embed_color)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)





#---------------------------------------------------------------
    @commands.command(aliases=["meme","MEME","Meme","memez"])
    async def memes(self,ctx):
        #No longer works (DEAD API)
        #url =f'https://some-random-api.ml/meme'
        url = "https://meme-api.com/gimme"
        response = requests.get(url)
        resolve = response.json()
        image= resolve["url"]
 
        embed = discord.Embed(title="__**Meme Generator**__", description = 'Here is your meme', color=embed_color)
        embed.set_image(url = image)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)
        
    
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.cooldown(10,60, commands.BucketType.user)
    @commands.command(aliases=["spam","say","repeat"])
    async def spammer(self,ctx, amnt: int, *, msg ):
        if isinstance(amnt, int) == True:
            if amnt > max_server_spam:
                await ctx.send(f"```Error, amount exceeds max amount!```")
                return
            else:
                await ctx.send(f"Sending '{msg}' {amnt} times")
                x = 0
                while x < int(amnt):
                    await ctx.send(msg)
                    x=x+1
                    await asyncio.sleep(2)

        else:
            await ctx.send(f"```Error, {amnt} is an invalid time duration```")
        
    
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.cooldown(60,1, commands.BucketType.user)
    @commands.command(aliases=["dmspam","dmraid","dms"])
    async def dm(self,ctx, member: discord.Member, amnt: int, *, msg ):
        if isinstance(amnt, int) == True:
            if amnt > max_dm_spam:
                await ctx.send(f"```Error, amount exceeds max amount!```")
                return
            else:
                
                try:

                    await ctx.send(f"Sending '{msg}' {amnt} times to {member.mention}")
                    x = 0
                    while x < int(amnt):
                        embed = discord.Embed(title="__**New Notification**__", description = f'**MESSAGE:**{msg}', color=embed_color)
                        embed.set_footer(text=f"Sent by {ctx.author.name}", icon_url=ctx.author.avatar)
                        await member.send(embed=embed)
                        x=x+1
                        await asyncio.sleep(2)

                except:
                    await member.send(f"```Error, Failed to send message to: {member.mention}```")

        else:
            await ctx.send(f"```Error, {amnt} is an invalid time duration```")
        
    
#---------------------------------------------------------------

#---------------------------------------------------------------
    @commands.command(aliases=["trivia","trivas","Triva"])
    async def TRIVA(self,ctx,diffculty=None):
        diff = diffculty.lower()
        if diffculty ==None:
            url ='https://opentdb.com/api.php?amount=1'      


        else:
            url =f'https://opentdb.com/api.php?amount=1&difficulty={diff}'
            response = requests.get(url)
            resolve = response.json()
            results= resolve["results"]
            diffculty_set = results["difficulty"]
            question = results["question"]
            correct_answer = results["correct_answer"]
            embed = discord.Embed(title="__**Trivia**__", description= f"**Question:**{question}\n**Answers:** ||{correct_answer} ||\nDiffculty: {diffculty_set}", color=embed_color)
            embed.set_footer(text=f'{name} Bot')
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

    
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.command(aliases=["funhelp","fun","funcmds"])
    async def Fun(self,ctx):
        embed = discord.Embed(title="__**Fun Commands**__", description= f"\n{prefix}gay <member> \n▸ **How gay are you or another discord server member**\n\n{prefix}pp <member>\n▸ **Reveals how big your or another discord server member pp is**\n\n{prefix}insult <member>\n▸ **Send a random generated insult to a you or another discord server member**\n\n{prefix}8ball\n▸ **Ask the magic 8ball any question you would like an answer for!**\n\n{prefix}joke\n▸ **Gernerates a random joke**\n\n{prefix}advice\n▸ **Generates random advice**\n\n{prefix}trivia <easy/medium/hard> (soon)\n▸ **Generates a random trivia question based on diffculty set**\n\n{prefix}meme\n▸ **Generate a random meme**\n\n{prefix}simpcheck <user>\n▸ **Checks if a user is a simp**\n\n{prefix}av <user>\n▸ **Snatches a users profile photo****\n\n{prefix}pp <member>\n▸ **Reveals how big your or another discord server member pp is**\n\n{prefix}insult <member>\n▸ **Send a random generated insult to a you or another discord server member**\n\n{prefix}8ball\n▸ **Ask the magic 8ball any question you would like an answer for!**\n\n{prefix}joke\n▸ **Gernerates a random joke**\n\n{prefix}advice\n▸ **Generates random advice**\n\n{prefix}trivia <easy/medium/hard> (soon)\n▸ **Generates a random trivia question based on diffculty set**\n\n{prefix}meme\n▸ **Generate a random meme**\n\n{prefix}simpcheck <user>\n▸ **Checks if a user is a simp**\n\n{prefix}spam <# of times> <msg>\n▸ **Repeatdly Send a message for x amount of times**\n\n{prefix}dm <@user> <# of times> <msg>\n▸ **Repeatdly Send a message for x amount of times in the dms**", color=embed_color)
        embed.set_footer(text=f'{name} Bot')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
    
#---------------------------------------------------------------

#---------------------------------------------------------------
    @commands.command(aliases=["8ball","8Ball","eightball"])
    async def ball(self,ctx,*,question):
        responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
        ]
        embed = discord.Embed(title="__**MAGIC 8BALL**__", description= f"**Question:** {question}\n**ANSWER:** {random.choice(responses)}", color=embed_color)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)
    
#---------------------------------------------------------------




async def setup(commands):
    await commands.add_cog(funhub(commands))
    print("cogs/funhub Loaded !")