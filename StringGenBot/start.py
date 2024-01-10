from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""۞¦ اهلا بـك عزيـزي  {msg.from_user.mention}
۞¦ فـي بـوت اسـتـخـراج الـجـلـسـات
۞¦ يمكنك استخراج الجلسات الـتالية
۞¦ بايروجرام للحسابات & بايروجرام للبوتات
۞¦ بـايـروجـرام مـيوزك احـدث إصـدار 
۞¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

۞¦ بواسطـة : [𐇮 ᯓ𓆩˹ َتــــٓــايــــٓــســــٓــون ،ِّّ⸙⛥َٰ⏤͟͟͞͞𓆃 𐇮](tg://user?id=6094482545) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📥 ⍆ اضغط لبدا استخراج كود ⍅ 📥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔱 𝚂𝙾𝚄𝚁𝙲𝙴 𝚅𝙴𝙽𝙾𝙼 🔱", url="https://t.me/one_1_X_bet"),
                    InlineKeyboardButton("𝚍𝚎𝚟 𝚝𝚊𝚢𝚜𝚘𝚗", user_id=6094482545)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
