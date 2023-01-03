import asyncio

import os
import logging

from dotenv import load_dotenv

from bot.bot import ModMail

load_dotenv('secrets.env')
TOKEN = os.getenv("TOKEN")

log = logging.getLogger(__name__)


async def run_bot():
    async with ModMail() as bot:
        bot.remove_command('help')
        await bot.start(TOKEN)
        

def main():
    asyncio.run(run_bot())
    


if __name__ == '__main__':
    main()
