import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from PrimeMusic import LOGGER, app, userbot
from PrimeMusic.core.call import Prime
from PrimeMusic.plugins import ALL_MODULES
from PrimeMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
        and not config.STRING6
        and not config.STRING7
        and not config.STRING8
        and not config.STRING9
        and not config.STRING10
    ):
        LOGGER("PrimeMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("PrimeMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PrimeMusic.plugins" + all_module)
    LOGGER("PrimeMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Prime.start()
    prime = await app.get_me()
    PrimeMusic = prime.username
    await userbot.one.send_message("primesupportgroup", f"@{PrimeMusic}")
    try:
        await Prime.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("PrimeMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Prime.decorators()
    LOGGER("PrimeMusic").info("Prime Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("PrimeMusic").info("Stopping Prime Music Bot! GoodBye")
