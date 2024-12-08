import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = '7630548242:AAF_B7OxnW-DJ_vBYekNrFp24jPIhX0-fnY'
bot = telebot.TeleBot(BOT_TOKEN)

LINKS = {
    "Ավտոպահեստամասեր": "https://www.list.am/category/22",
    "Ավտոաքսեսուարներ": "https://www.list.am/category/83",
    "Մեքենայի աուդիո և վիդեո համակարգ": "https://www.list.am/category/194",
    "Հեծանիվներ": "https://www.list.am/category/18",
    "Ավտոմեքենաներ արտերկրից": "https://www.list.am/category/399",
    "Մոտոպահեստամասեր և աքսեսուարներ": "https://www.list.am/category/190",
    "Ավտոբուսներ": "https://www.list.am/category/74",
    "Կվադրոցիկլեր և ձյունագնացներ": "https://www.list.am/category/197",
    "Ավտոմեքենաներ": "https://www.list.am/category/23",
    "Կոմերցիոն մեքենաների պահեստամասեր": "https://www.list.am/category/192",
    "Բեռնատարներ": "https://www.list.am/category/25",
    "Գազի սարքավորումներ": "https://www.list.am/category/237",
    "Գյուղատնտեսական տեխնիկա": "https://www.list.am/category/114",
    "Ավտոմեքենաներ աճուրդներից": "https://www.list.am/category/124",
    "Մոտոցիկլեր": "https://www.list.am/category/24",
    "Սկուտերներ և մոպեդներ": "https://www.list.am/category/198",
    "Ջրային տրանսպորտ": "https://www.list.am/category/196",
    "Անիվներ և անվադողեր": "https://www.list.am/category/115",
    "Անվահեծեր և անվադողի թասակներ": "https://www.list.am/category/238",
    "Վթարված մեքենաներ որպես պահեստամաս": "https://www.list.am/category/188",
    "Շինարարական և ծանր տեխնիկա": "https://www.list.am/category/191",
    "Ավտոէլեկտրոնիկա": "https://www.list.am/category/193",
    "Մարտկոցներ": "https://www.list.am/category/236",
    "Հեծանիվների պահեստամասեր և աքսեսուարներ": "https://www.list.am/category/189",
    "Ավտոտնակներ և կցանքներ": "https://www.list.am/category/195",
    "Մնացած ամեն ինչ տրանսպորտի համար": "https://www.list.am/category/28"
}

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "Բարև ձեզ, դուք գտնվում եք «List.am» տելեգրամյան ալիքում։\n"
        "Այս ալիքում դուք կարող եք նշել ձեր նախընտրած մեքենան կամ մեքենայի համար "
        "անհրաժեշտ դետալներ։ Ալիքը ձեզ կտրամադրի այն մեքենաները, որոնք արդի են "
        "հայկական շուկայում։"
    )
    bot.send_message(message.chat.id, welcome_text)
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Տրանսպորտ")
    button2 = KeyboardButton("Կապ մեզ հետ")
    markup.add(button1, button2)
    
    bot.send_message(message.chat.id, "Ընտրեք գործողություն:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Տրանսպորտ")
def transport_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(LINKS.keys()), 3):
        markup.add(*[KeyboardButton(button) for button in list(LINKS.keys())[i:i+3]])
    markup.add(KeyboardButton("🔙 Վերադառնալ գլխավոր ընտրացանկ"))
    bot.send_message(message.chat.id, "Ընտրեք բաժինը:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in LINKS.keys())
def send_link(message):
    link = LINKS[message.text]
    bot.send_message(message.chat.id, f"Ահա հղումը՝ {link}")

@bot.message_handler(func=lambda message: message.text == "🔙 Վերադառնալ գլխավոր ընտրացանկ")
def main_menu(message):
    start(message)


@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    bot.send_message(message.chat.id, "Ներեցեք, ես չեմ հասկանում այդ հրահանգը։")

if __name__ == "__main__":
    print("Bot is running...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Bot stopped due to an error: {e}")