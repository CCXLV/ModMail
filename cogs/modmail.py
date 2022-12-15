"""
MIT License

Copyright (c) 2022 CCXLV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands
from discord.utils import get

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

        if ctx.guild is None:
            channel = await guild.create_text_channel(name=ticket_name, category=category)
            channel_id = get(guild.channels, name=str(channel))
               
            if channel_id:
                ch_id = channel_id.id

            em1 = discord.Embed(title="Staff channel created", description=f'Here is your channel <#{ch_id}>', color=0x04d277, timestamp=datetime.utcnow())
            em1.set_thumbnail(url="https://user-images.githubusercontent.com/113610436/198890799-041e43ea-d7e9-46c1-bef1-c3180f24e0ef.png")
                
            em2 = discord.Embed(title='ModMail channel', description='Please be patience, moderation staff will be there any time soon.\nTell us what do you need help about.', color=0x5e7bdd)
                
                
            embed1 = await channel.send(embed=em2)

            moderation_role = get(guild.roles, id=1024696145445924914)
            await channel.send(ctx.author.mention + " " + moderation_role.mention)
            await channel.set_permissions(ctx.author, 
                                          view_channel=True,
                                          read_messages=True)
            await ctx.author.send(embed=em1)
        else:
            await ctx.send('DM ``?help contact`` in order to contact staff.')
    
     


async def setup(bot):
    await bot.add_cog(ModMail(bot))
