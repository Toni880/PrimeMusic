import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )
        self.six = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING6),
            no_updates=True,
        )
        self.seven = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING7),
            no_updates=True,
        )
        self.eight = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING8),
            no_updates=True,
        )
        self.nine = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING9),
            no_updates=True,
        )
        self.ten = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING10),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("PrimeSupportChannel")
                await self.one.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Started as {self.one.name}"
            )
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("PrimeSupportChannel")
                await self.two.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Two Started as {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("PrimeSupportChannel")
                await self.three.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("PrimeSupportChannel")
                await self.four.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("PrimeSupportChannel")
                await self.five.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.name}"
            )
        if config.STRING6:
            await self.six.start()
            try:
                await self.six.join_chat("PrimeSupportChannel")
                await self.six.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(6)
            try:
                await self.six.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 6 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.six.get_me()
            self.six.username = get_me.username
            self.six.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.six.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.six.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Six Started as {self.six.name}"
            )
        if config.STRING7:
            await self.seven.start()
            try:
                await self.seven.join_chat("PrimeSupportChannel")
                await self.seven.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(7)
            try:
                await self.seven.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 7 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.seven.get_me()
            self.seven.username = get_me.username
            self.seven.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.seven.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.seven.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Seven Started as {self.seven.name}"
            )
        if config.STRING8:
            await self.eight.start()
            try:
                await self.eight.join_chat("PrimeSupportChannel")
                await self.eight.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(8)
            try:
                await self.eight.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 8 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.eight.get_me()
            self.eight.username = get_me.username
            self.eight.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.eight.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.eight.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Eight Started as {self.eight.name}"
            )
        if config.STRING9:
            await self.nine.start()
            try:
                await self.nine.join_chat("PrimeSupportChannel")
                await self.nine.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(9)
            try:
                await self.nine.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 9 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.nine.get_me()
            self.nine.username = get_me.username
            self.nine.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.nine.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.nine.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Nine Started as {self.nine.name}"
            )
        if config.STRING10:
            await self.ten.start()
            try:
                await self.ten.join_chat("PrimeSupportChannel")
                await self.ten.join_chat("PrimeSupportGroup")
            except:
                pass
            assistants.append(9)
            try:
                await self.ten.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 10 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.ten.get_me()
            self.ten.username = get_me.username
            self.ten.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.ten.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.ten.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Ten Started as {self.ten.name}"
            )
