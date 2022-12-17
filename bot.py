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

        await self.process_commands(message)

        



bot = ModMailBot()
bot.remove_command('help')
bot.run()                      
