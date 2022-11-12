import discord
from discord.ext import commands
from discord.utils import get

import random
from datetime import datetime

class ModMail(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        ticket_name = random.randint(1000, 9999)
        guild = self.client.get_guild(1024690969100156989)
        category = get(guild.categories, id=1035934640483094601)

        if message.guild is None:
            if message.content == "!help":
                em = discord.Embed(title="ModMail", description="Type ``!contact staff`` to create a channel and contact moderation staff", color=0x5e7bdd)
                
                await message.author.send(embed=em)

            elif message.content.startswith("!contact staff"):
                channel = await guild.create_text_channel(name=ticket_name, category=category)
                channel_id = get(guild.channels, name=str(channel))
               
                if channel_id:
                    ch_id = channel_id.id

                em1 = discord.Embed(title="Staff channel created", description=f"Here is your channel <#{ch_id}>", color=0x04d277, timestamp=datetime.utcnow())
                em1.set_thumbnail(url="https://user-images.githubusercontent.com/113610436/198890799-041e43ea-d7e9-46c1-bef1-c3180f24e0ef.png")
                
                em2 = discord.Embed(title="ModMail channel", description="Please be patience, moderation staff will be there any time soon.\nTell us what do you need help about.", color=0x5e7bdd)
                
                
                embed1 = await channel.send(embed=em2)

                moderation_role = get(guild.roles, id=1024696145445924914)
                await channel.send(message.author.mention + " " + moderation_role.mention)
                await channel.set_permissions(message.author, 
                                            view_channel=True,
                                            read_messages=True)
                await message.author.send(embed=em1)


        await self.client.process_commands(message)


async def setup(bot):
    await bot.add_cog(ModMail(bot))
