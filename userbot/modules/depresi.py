from datetime import datetime
import time
from random import choice, randint

from telethon.events import StopPropagation
from telethon.tl.functions.account import UpdateProfileRequest

from userbot import (  # noqa pylint: disable=unused-import isort:skip
    AFKREASON,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    ALIVE_NAME,
    COUNT_MSG,
    ISAFK,
    PM_AUTO_BAN,
    USERS,
    PM_AUTO_BAN,
    bot,
)
from userbot.events import register

# ========================= CONSTANTS ============================
AFKSTR = [
    f"**𝗠𝗮𝗮𝗳 {ALIVE_NAME} 𝗦𝗲𝗱𝗮𝗻𝗴 𝗗𝗘𝗣𝗥𝗘𝗦𝗜 **",
    f"**𝗠𝗮𝗮𝗳 {ALIVE_NAME} 𝗦𝗲𝗱𝗮𝗻𝗴 𝗗𝗘𝗣𝗥𝗘𝗦𝗜!\n 𝗧𝘂𝗻𝗴𝗴𝘂 𝗔𝗷𝗮 𝗦𝗮𝗺𝗽𝗮𝗶 𝗗𝗶𝗮 𝗕𝗲𝗿𝗵𝗲𝗻𝘁𝗶 𝗗𝗘𝗣𝗥𝗘𝗦𝗜**",
    f"**𝗠𝗮𝗮𝗳 {ALIVE_NAME} 𝗦𝗲𝗱𝗮𝗻𝗴 𝗗𝗘𝗣𝗥𝗘𝗦𝗜!\n 𝗧𝘂𝗻𝗴𝗴𝘂𝗹𝗮𝗵 𝗦𝗮𝗺𝗽𝗲 𝗗𝗶𝗮 𝗚𝗮 𝗗𝗘𝗣𝗥𝗘𝗦𝗜!**",
    f"**𝗠𝗮𝗮𝗳 {ALIVE_NAME} 𝗦𝗲𝗱𝗮𝗻𝗴 𝗗𝗘𝗣𝗥𝗘𝗦𝗜!**",
]


global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
afk_start = {}

# =================================================================


@register(outgoing=True, pattern="^.depresi(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text  # pylint:disable=E0602
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"**⚠️**\n**𝗗 𝗘 𝗣 𝗥 𝗘 𝗦 𝗜  !**\
        \n𝗞𝗮𝗿𝗲𝗻𝗮 : `{string}`")
    else:
        await afk_e.edit("**𝗗 𝗘 𝗣 𝗥 𝗘 𝗦 𝗜  !**\n**𝗦𝗲𝗱𝗮𝗻𝗴 𝗗𝗘𝗣𝗥𝗘𝗦𝗜**")
    if user.last_name:
        await afk_e.client(UpdateProfileRequest(first_name=user.first_name, last_name=user.last_name + "ᴬᴶᴳ"))
    else:
        await afk_e.client(UpdateProfileRequest(first_name=user.first_name, last_name="ᴬᴶᴳ"))
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\n**𝚂𝚎𝚍𝚊𝚗𝚐 𝙰𝙵𝙺!**")
    ISAFK = True
    afk_time = datetime.now()  # pylint:disable=E0602
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    last = user.last_name
    if last and last.endswith("ᴬᴶᴳ"):
        last1 = last[:-12]
    else:
        last1 = ""
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("**𝗜 𝗔𝗠 𝗕𝗔𝗖𝗞!!!**")
        time.sleep(3)
        await msg.delete()
        await notafk.client(UpdateProfileRequest(first_name=user.first_name, last_name=last1))
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "Anda Mendapatkan " + str(COUNT_MSG) + " 𝙱𝚊𝚌𝚘𝚝𝚊𝚗 𝙳𝚊𝚛𝚒 " +
                str(len(USERS)) + "𝗕𝗔𝗖𝗢𝗧𝗔𝗡 𝗬𝗔𝗡𝗚 𝗔𝗡𝗗𝗔 𝗧𝗘𝗥𝗜𝗠𝗔!",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " 𝗠𝗘𝗡𝗚𝗜𝗥𝗜𝗠𝗨 " + "**" + str(USERS[i]) + " 𝗣𝗘𝗦𝗔𝗡**",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**𝗧𝗘𝗥𝗔𝗞𝗛𝗜𝗥 𝗗𝗜𝗟𝗜𝗛𝗔𝗧!**"
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**KEMARIN**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"⚠️ {afk_since} 𝗗 𝗘 𝗣 𝗥 𝗘 𝗦 𝗜  !\
                        \n𝗞𝗮𝗿𝗲𝗻𝗮 `{AFKREASON}`")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(f"⚠️ {afk_since} 𝗗 𝗘 𝗣 𝗥 𝗘 𝗦 𝗜  !\
                            \n𝗞𝗮𝗿𝗲𝗻𝗮 `{AFKREASON}`")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "𝙱𝚎𝚕𝚞𝚖 𝙻𝚊𝚖𝚊"
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Kemarin**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}` **𝙹𝚊𝚖** `{int(minutes)}` **𝙼𝚎𝚗𝚒𝚝**"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}` **𝙼𝚎𝚗𝚒𝚝** `{int(seconds)}` **𝙳𝚎𝚝𝚒𝚔**"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"**DEPRESI** `{afk_since}` **YANG LALU**.\
                        \n**𝗞𝗮𝗿𝗲𝗻𝗮** `{AFKREASON}`")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(f"**DEPRESI** {afk_since} **YANG LALU.**\
                            \n**𝗞𝗮𝗿𝗲𝗻𝗮** `{AFKREASON}`")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


CMD_HELP.update({
    "afk":
    "`.afk` ; `.depresi` [Alasan]\
\nUsage: Lakukan ketika ingin OFF/DEPRESI.\nSiapapun Yang Balas, Tag, Atau Chat Kamu \
Mereka Akan Tau Alasan Kamu OFF.\n\nAFK Bisa Dilakukan Dan Dibatalkan Dimanapun.\
"
})
