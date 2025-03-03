import discord, os, random, time, asyncio 
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
import discord.utils 
from config import *








class modhub(commands.Cog, name="modhub"):

    def __init__(self, bot):
        self.commands = bot
#---------------------------------------------------------------
    @commands.command(aliases=[" purge","delete","PURGE"," PURGE"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount):
        await ctx.channel.purge(limit=int((int(amount) + 1))) # to delete their purge request plus the actual message
        await ctx.send(f"Success, Purged {amount} messages.")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
#---------------------------------------------------------------

#---------------------------------------------------------------    
    @commands.command(aliases=["wipe","bomb","purgeall","Nuke","Wipe","rip"])
    @commands.has_permissions(manage_messages=True)
    async def nuke(self, ctx):
        await ctx.channel.purge(limit=999999)
        await ctx.send(f'{ctx.message.author.mention} has wiped the chat https://imgur.com/LIyGeCR')
        asyncio.sleep(5)
        await ctx.channel.purge(limit=1)
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.command()
    #@commands.has_permissions(kick_members=True)
    async def joined(self,ctx, member: discord.Member):
        joined_date = member.joined_at.strftime("%B %d, %Y at %I:%M %p")  # Format date
        embed = discord.Embed(title=f"__**{member.name}'s Join Info**__", description=f"\n", color=embed_color)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="**Joined On**", value=f"▸ `{joined_date}`")
        await ctx.send(embed=embed)
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Um... you just yeeted {member.mention} out of the server... rip all beacuse of "{reason}"')
#---------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'RIP... {member.mention} is banned from the server, Reason: "{reason}"') 

#---------------------------------------------------------------

#---------------------------------------------------------------
    @commands.command(aliases=["Helpme","HELP","Help","help"])
    async def helpme(self,ctx):
        embed = discord.Embed(title=f"__**{name} HELP MENU**__", description= f"\n", color=embed_color)
        embed.set_footer(text=f'{name} Bot')
        embed.add_field(name="**MOD  COMMANDS**", value=f"▸ {prefix}modhelp")
        embed.add_field(name="**FUN COMMANDS**", value=f"▸ {prefix}funhelp")
        await ctx.send(embed=embed)
    
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self,ctx,member : discord.Member):
        add = ctx.guild.get_role(muted_role_id)
        await member.remove_roles(add)
        await ctx.send(f'{member.mention} **SPEAK!** :loudspeaker:\n')
#---------------------------------------------------------------


#---------------------------------------------------------------
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx,member : discord.Member):
        add = ctx.guild.get_role(muted_role_id)
        await member.add_roles(add)
        await ctx.send(f'{member.mention} has been muted \nhttp://gph.is/2l0ZeVc')
#---------------------------------------------------------------
        


#---------------------------------------------------------------
    @commands.command(aliases=["WARN","Warn","WARNS"])
    @commands.has_permissions(kick_members=True)
    async def warn(self,ctx,member : discord.Member,*,reason=None):
        await ctx.send(f'{member.mention} **Be WARNED!** :loudspeaker: **REASON**:{reason}\n')
        dm =f'ctx.message.author'   
        channel = bot.get_channel(ctx.channel.id)
        await channel.send(f'Infraction: {member} Reason: {reason} \nAdmin: {dm}')
#---------------------------------------------------------------



#---------------------------------------------------------------
    @commands.command(aliases=["modhelp","moderation","modcmds"])
    #@commands.has_role(Admin_role)
    async def mod(self,ctx):
        embed = discord.Embed(title="__**Admin Commands**__", description= f"\n{prefix}ban\n▸ **Ban a user from the discord server**\n\n{prefix}kick\n▸ **Kicks a user from the discord**\n\n{prefix}purge <amount>\n▸ **Deletes a selected amount of messages from the current channel**\n\n{prefix}nuke\n▸ **Clears all messages in current channel**\n\n{prefix}warn <USER>\n▸ **Warns a discord member**\n\n{prefix}uptime\n▸ **Fetches the bot's current uptime**\n\n{prefix}joined <user>\n▸ **Fetches the users joined date**", color=embed_color)
        embed.set_footer(text=f'{name} Bot')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
    
#---------------------------------------------------------------

        
async def setup(commands):
    await commands.add_cog(modhub(commands))
    print("cogs/modhub Loaded !")
