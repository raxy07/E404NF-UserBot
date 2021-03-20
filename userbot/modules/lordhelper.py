""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lordhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Lord {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/liualvinas)"
        "\n[Repo](https://github.com/zora24/Lord-Userbot)"
        "\n[Instagram](Instagram.com/liualvinas_)")


@register(outgoing=True, pattern="^.lordvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Zora24/Lord-Userbot/Lord-Userbot/varshelper.txt)")


CMD_HELP.update({
    "lordhelper":
    "`.lordhelp`\
\nUsage: Bantuan Untuk Lord-Userbot.\
\n`.lordvar`\
\nUsage: Melihat Daftar Vars."
})
