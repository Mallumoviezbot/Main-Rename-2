from pyrogram import Client as RenamerNs, filters
from ..tools.db.database import db
from renamer.config import Config


@RenamerNs.on_message(
    filters.private & filters.command("status") & filters.user(Config.ADMINS)
)
async def sts(c, m):
    total_users = await db.total_users_count()
    text = f"Total user(s) till date: {total_users}"
    await m.reply_text(text=text, quote=True)
