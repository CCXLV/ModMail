import discord
from discord.ext import commands
from discord.utils import get
import random
from datetime import datetime



intents = discord.Intents.all()
client = commands.Bot(command_prefix="", intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="your DMs"))
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    channel_name_random = random.randint(1000, 9999) 
    guild = client.get_guild(YOUR GUILD ID) 
    category = get(guild.categories, name="YOUR CATEGORY NAME")



    
    if message.guild is None: 
        if message.content == "!help":
            em = discord.Embed(title="ModMail", description="Type ``!contact staff`` to create a channel and contact moderation staff", timestamp=datetime.utcnow())
            
            await message.author.send(embed=em)
        elif message.content.startswith("!contact staff"): 
            channel = await guild.create_text_channel(name=channel_name_random, category=category)  
            channel_name = get(guild.channels, name=str(channel)) 
            if channel_name:  
                channel_id = channel_name.id 

            em1 = discord.Embed(title="Staff channel created", description=f"Here is your channel <#{channel_id}>.", color=0x04d277)
   
            em2 = discord.Embed(title="ModMail channel", description="Please be patience, moderation staff will be there any time soon.\nTell us what do you need help about.")
            
            
            await channel.send(embed=em2)
            await channel.send(message.author.mention)
            await channel.set_permissions(message.author,   
                                        view_channel=True ,
                                        read_messages=True)
            await message.author.send(embed=em1)
