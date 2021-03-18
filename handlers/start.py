from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

Haii Aku Pemutar Musik Telegram, Kamu Bisa Mendengarkan Musik Di Telegram!.

Silahkan Klik Tombol Dibawah Ini, Apabila Kurang Jelas Atau Masih Bingung Menggunakan Aku.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Click Me!", url="https://t.me/afterdaytoxic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/https://t.me/joinchat/Vgi-MRNFL3DER7E-"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/captionanakmuda"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
