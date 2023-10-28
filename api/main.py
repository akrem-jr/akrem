import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
from decouple import config

TOKEN = config("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
COMMANDS = {
     "silver": "silver membership \n(Learn and earn program)",
    "gold": "Gold Membership",
    "vip": "Platinum Membership"
}


@bot.message_handler(commands=['start'])
def start(message):
     chat_id = message.chat.id
     start_bot(chat_id, message.chat.first_name)
     show_menu(message.chat.id)


def show_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    plan_button = types.KeyboardButton('plan🎁')
    status_button = types.KeyboardButton('Contact Admin')

    markup.add(plan_button, status_button)
    bot.send_message(chat_id," Check out our exciting membership plans and start your journey to success today!\n\n\t\t\t👇👇👇", reply_markup=markup)
    

def start_bot(chat_id, username):
    
    welcome_message = f"Welcome, {username}!"
    bot.send_message(chat_id, welcome_message)
    

@bot.message_handler(func=lambda message: message.text == 'Contact Admin')
def contact_admin(message):
    bot.send_message(message.chat.id, "https://t.me/layne19")
  


@bot.message_handler(func=lambda message: message.text == 'plan🎁')
def join_channel(message):
    show_commands(message.chat.id)
@bot.callback_query_handler(func=lambda call: True)
def button(call):
    command = call.data
    chat_id = call.message.chat.id

    
    if command == 'vip':
        bot.send_message(chat_id, 'You selected Platinum Membership.')
        vip_menu(chat_id)
    elif command == 'silver':
        bot.send_message(chat_id, 'You selected Silver Membership.')
        silver_menu(chat_id)
    elif command == 'gold':
        bot.send_message(chat_id, 'You selected Gold Membership.')
        gold_menu(chat_id)
    elif command == 'option_silver1':
        
        option_silver1(call)
    elif command == 'option_silver2':
        bot.send_message(chat_id, ' https://t.me/L4xsupport/3 ')
        option_silver2(call)
    elif command == 'option_gold1':
          option_gold1(call)
    elif command == 'back_option_vip1':
        vip_menu(chat_id)
    elif command == 'back_option_silver1':
        silver_menu(chat_id)
    elif command == 'back_option_gold1':
        gold_menu(chat_id)
    elif command == 'option1_1':
        bot.send_message(chat_id, ' Please Send screenshot to confirm \n\n @layne19')
    elif command == 'back':
        show_commands(chat_id)

def show_commands(chat_id):
    keyboard = []
    for cmd, desc in COMMANDS.items():
        keyboard.append([InlineKeyboardButton(desc, callback_data=cmd)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=chat_id,
        text="Please Choose Our Plan: ",
        reply_markup=reply_markup
    )
def gold_menu(chat_id):
    keyboard = [
         [InlineKeyboardButton('For payment 💳', callback_data='option_gold1')],
        [InlineKeyboardButton('⬅️Back', callback_data='back')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=chat_id,
        text="""L4X VIP  Gold Membership 
📌High win Rate Forex Signal 
📌London session and NY session live stream  Trade 
📌1-3 Signal per Day 
📌Free access  L4X VIP silver 

 subscription 100$ per monthly""",
        reply_markup=reply_markup
    )


@bot.callback_query_handler(func=lambda call: call.data == 'option1')
def option_gold1(call):
    keyboard = [
        [InlineKeyboardButton('⬅️Back', callback_data='back_option_gold1')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=call.message.chat.id,
        text="please contact \n\n @layne19",
        reply_markup=reply_markup
    )
def vip_menu(chat_id):
    keyboard = [
         [InlineKeyboardButton('⬅️Back', callback_data='back')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=chat_id,
        text="Platinum Membership Coming Soon...",
        reply_markup=reply_markup
    )
def silver_menu(chat_id):
    keyboard = [
        [InlineKeyboardButton('Done ✅', callback_data='option_silver1')],
        [InlineKeyboardButton('🎦How to change partner 🎦', callback_data='option_silver2')],
        [InlineKeyboardButton('⬅️Back', callback_data='back')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=chat_id,
        text="ወደ L4X Silver VIP Learn and Earn Program \n\n1 ምዝገባ ነጻ ነው (Free Registration) \n\n2 የ EXNESS አካዉንት\n\n3 ከ 50$ በላይ Deposit \n\nየ Enxess አካዉንት ከሌሎት ከ እዚ በታች ባለው ሊንክ ይክፈቱ \n\nhttps://one.exness-track.com/a/k66q9ywpdp \n\nካሎት ደሞ ለ Enxess ወደ እኛ IB program እንዲቀይርሎት ያሳውቁ ለማሳወቅ ከፈለጉ በ ቀላሉ Live Chat በማረግ መቀየር ይችላሉ፤ \n\nPartner code k66q9ywpdp \n\nPartner Link https://one.exness-track.com/a/k66q9ywpdp \n\nእርዳታችን የሚያስፈልጎት ከሆነ ይፃፉልን። ",
        reply_markup=reply_markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'option1')
def option_silver1(call):
    keyboard = [
        [InlineKeyboardButton('⬅️Back', callback_data='back_option_silver1')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=call.message.chat.id,
        text="Please Send screenshot to confirm \n\n @layne19",
        reply_markup=reply_markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'option2')
def option_silver2(call):
    keyboard = [
        [InlineKeyboardButton('⬅️Back', callback_data='back_option_silver1')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=call.message.chat.id,
        text=" partner ከቀየራቹ ቡሀላ አዲስ የ MT4 ወይም ደሞ የ MT5 አካዉንት መክፈት አለባቹ ከዛን ከ በፊቱ አካዉንታቹ ወደ አዲሱ ያላቹን Balance  አስተላልፉ",
        reply_markup=reply_markup
    )
    
@bot.callback_query_handler(func=lambda call: call.data == 'back_option_vip1')
def back_option_vip1(call):
    show_commands(call.message.chat.id)
    
    
@bot.callback_query_handler(func=lambda call: call.data == 'back_option_silver1')
def back_option_silver1(call):
    show_commands(call.message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == 'back_option_gold1')
def back_option_gold1(call):
    show_commands(call.message.chat.id)

if __name__ == "__main__":
    print("running the code .....")
    bot.polling()