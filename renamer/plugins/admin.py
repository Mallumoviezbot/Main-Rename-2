from pyrogram import Client as RenamerNs, filters
from ..tools.db.database import db
from renamer.config import Config



@RenamerNs.on_message(
    filters.private & filters.command("admin") & filters.user(Config.ADMINS)
)
async def admin(c, m):

    text = "Current admins of the bot:\n\n"
    admins = await db.get_users(Config.AUTH_USERS)
    for admn in admins:
        text += f"\t- {admn.mention}\n"

    text += "\nAvailable admin commands are:\n"
    text += (
        "\t- /unban_user\n\t- /broadcast\n\t- /banned_users\n\t- /ban_user\n\t- /status"
    )

    await m.reply_text(text, quote=True)
