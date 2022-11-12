import discord
from discord.ext import commands
import logging

log = logging.getLogger(__name__)


extensions = (
    'cogs.modmail',
)

class ModMailBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="?",
            intents=intents,
            status=discord.Status.online,
            activity=discord.Activity(type=discord.ActivityType.listening, name="your DMs")
        )

    async def setup_hook(self) -> None:
        print("ModMail Bot is running")

        for extension in extensions:
            try:
                await self.load_extension(extension)
            except Exception as e:
                log.exception('Failed to load extension %s.', extension)
    
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.guild is None:
            if message.content != None:
                if message.content != "!help":
                    if message.content != "!contact staff":

                        return await message.author.send("Type *!help* to contact staff")
        
        await self.process_commands(message)

        



client = ModMailBot()
client.remove_command("help")
client.run('MTAzNzc5NjE4NjM5MzkzNjAyMg.GJWrHw.t-eFqUQy1FphC229m4uamM-597gS4_72FWUEjg')                      