import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Context
from discord.ui import Button, View

import random
from datetime import datetime

class ModMail(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.hybrid_group()
    async def help(self, ctx: discord.Message):    

        if ctx.guild is None:
            embed = discord.Embed(title='ModMail', description='DM ``?help contact` to create a channel and contact moderation staff.', color=0x5e7bdd)
                
            await ctx.author.send(embed=embed)
        else:
            await ctx.send('DM `?help` for more info.')

    @help.command()
    async def contact(self, ctx: discord.Message):
        ticket_name = random.randint(1000, 9999)
        guild = self.bot.get_guild(1024690969100156989) # < - takes guild ID as a parameter.
        category = get(guild.categories, id=1035934640483094601) # < - takes category ID as a parameter.
    
        close_channel = Button(emoji='🔒', label='Close', style=discord.ButtonStyle.blurple)

        
        async def close_channel_callback(interaction: discord.Interaction):
            await interaction.channel.set_permissions(ctx.author,
                                                view_channel=False)
            await interaction.response.send_message(f'The channel has been closed by {interaction.user.mention}')

        close_channel.callback = close_channel_callback    
        
        if ctx.guild is None:
            channel = await guild.create_text_channel(name=ticket_name, category=category)
            channel_id = get(guild.channels, name=str(channel))
               
            if channel_id:
                ch_id = channel_id.id

            em1 = discord.Embed(title="Staff channel created", description=f'Here is your channel <#{ch_id}>', color=0x04d277, timestamp=datetime.utcnow())
            em1.set_thumbnail(url="https://user-images.githubusercontent.com/113610436/198890799-041e43ea-d7e9-46c1-bef1-c3180f24e0ef.png")
                
            em2 = discord.Embed(title='New ModMail Ticket', description='Please be patience, moderation staff will be there any time soon.\n'
                                'Tell us what do you need help about.', 
                                timestamp=datetime.utcnow(), color=0x5e7bdd)
            em2.add_field(name='User', value=f'{ctx.author.mention} (`{ctx.author.id}`)')
            em2.set_footer(icon_url=ctx.author.avatar, text=ctx.author.name)
            

            view = View()
            view.add_item(close_channel)
            embed1 = await channel.send(embed=em2, view=view)

            moderation_role = get(guild.roles, id=1024696145445924914)
            await channel.send(ctx.author.mention + " " + moderation_role.mention)
            await channel.set_permissions(ctx.author, 
                                          view_channel=True,
                                          read_messages=True)
            await ctx.author.send(embed=em1)
            
            embed3 = discord.Embed(title='Channel created', color=0x04d277, timestamp=datetime.utcnow())
            embed3.description = f'Channel {channel.mention} has been created by {ctx.author.mention} (`{ctx.author.id}`)'
            modlog_channel = self.bot.get_channel(1035981357333102613)

            await modlog_channel.send(embed=embed3)
        else:
            await ctx.send('DM `?help contact` in order to contact staff.')
    
    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    async def delete(self, ctx: Context):
        channel = ctx.channel
        guild = self.bot.get_guild(1024690969100156989)
        modlog_channel = self.bot.get_channel(1035981357333102613)
        modlog_category = get(guild.categories, id=1035934640483094601)

        embed = discord.Embed(title='Channel deleted', color=0xFF0000)
        embed.description = f'`Channel {channel.name}` has been deleted by {ctx.author.mention} (`{ctx.author.id}`)'
        embed.timestamp = datetime.utcnow()
         
        if ctx.channel.category is modlog_category:
            if ctx.channel != modlog_channel:
                await channel.delete()
                await modlog_channel.send(embed=embed)
            else:
                return
     


async def setup(bot):
    await bot.add_cog(ModMail(bot))
