import requests
from translate import Translator  # ترجمه به فارسی
from bale import Bot, CallbackQuery, Message, Components, EventType, InlineKeyboard

# Enter token bale
bot = Bot(token="** Enter token **")

TxtWelcome = f"سلام اینجا میتونی تصاویر زیبای از ستارگان و کهکشان ها و ... را ببینی. \n" \
             f"برای دریافت تصاویر رویه شروع بزنید"


@bot.listen(EventType.MESSAGE)
async def start_shoo(message: Message):
    if message.content == "/start":
        await message.reply(
            TxtWelcome,
            components=Components(inline_keyboards=[[
                InlineKeyboard("شروع", callback_data="star")
            ]]

            )

        )


@bot.listen(EventType.CALLBACK)
async def Photo_shoo(call: CallbackQuery):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "** Enter token **",  # Enter token api = https://api-ninjas.com/api
        "count": 1  # Number of examples
    }

    response = requests.get(url, params=params)
    if call.data == "star":
        if response.status_code == 200:
            results = response.json()
            for result in results:
                ph = (result["url"])
                cap = (result["title"])
                translator = Translator(to_lang="fa")
                translation = translator.translate(cap)
                await bot.send_photo(
                    chat_id=call.from_user.chat_id,
                    photo=ph,
                    caption=translation
                )


bot.run()
