import discord
from discord.ext import commands
import logging

log = logging.getLogger(__name__)


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

        try:
            await self.load_extension('bot.cogs.modmail')
        except Exception as e:
            log.exception('Failed to load extension %s.', e)
    
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.process_commands(message)

        
