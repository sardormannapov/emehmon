from telebot import TeleBot
from check_inn import check_inn
from keyboard import *
from localization.bot_lang import *
import config.config as c

token = "7131258522:AAE5LpzEvl7P8aT5us9HdXkpJa4Is0aMIrg"

admin_id = [668290718, 634660069]
OPERATOR_CHAT_ID = 634660069
bot = TeleBot(token)
user_langs = {}
previous_message_ids = {}
user_inns = {}
user_requests = {}
operator_chats = {}
chat_id_to_inn = {}
pending_media = {}





@bot.message_handler(commands=['answer_yur', 'photo_yur', 'document_yur', 'answer_fiz', 'photo_fiz', 'document_fiz'])
def reply_to_user(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    try:
        parts = message.text.split(' ', 2)
        if len(parts) < 2:
            bot.send_message(chat_id, format_yur_fiz[lang])
            return

        command, identifier = parts[:2]
        reply_message = parts[2] if len(parts) > 2 else None

        if command in ['/answer_yur', '/photo_yur', '/document_yur']:
            if identifier not in user_inns:
                bot.send_message(chat_id, not_found[lang])
                return

            user_chat_id = user_inns[identifier]
        else:
            try:
                user_id = int(identifier)
            except ValueError:
                bot.send_message(chat_id, format_yur_fiz[lang])
                return

            if user_id not in user_requests:
                bot.send_message(chat_id, not_found[lang])
                return

            user_chat_id = user_requests[user_id]

        if command in ['/answer_yur', '/answer_fiz']:
            if reply_message:
                bot.send_message(user_chat_id, reply_message)
                bot.send_message(chat_id, send_answer[lang])
            else:
                bot.send_message(chat_id, format_yur_fiz[lang])
        elif command in ['/photo_yur', '/photo_fiz']:
            pending_media[chat_id] = user_chat_id
            bot.send_message(chat_id, send_photo[lang])
        elif command in ['/document_yur', '/document_fiz']:
            pending_media[chat_id] = user_chat_id
            bot.send_message(chat_id, send_doc[lang])
        else:
            bot.send_message(chat_id, format_yur_fiz[lang])
    except Exception as e:
        bot.send_message(chat_id, format_yur_fiz[lang])
        print(f"Error: {e}")


@bot.message_handler(content_types=['photo', 'document'])
def handle_media(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if chat_id in pending_media:
        user_chat_id = pending_media.pop(chat_id)
        if message.content_type == 'photo':
            bot.send_photo(user_chat_id, message.photo[-1].file_id)
        elif message.content_type == 'document':
            bot.send_document(user_chat_id, message.document.file_id)
        bot.send_message(chat_id, send_answer[lang])
    else:
        if message.content_type == 'photo':
            bot.send_message(chat_id, err_photo_yur_fiz[lang])
        elif message.content_type == 'document':
            bot.send_message(chat_id, err_document_yur_fiz[lang])


@bot.message_handler(commands=["admin"])
def admin(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    print(admin_id)
    if chat_id in admin_id:
        ans_data = bot.send_message(chat_id, "Admin panelga xush kelibsiz!", reply_markup=admin_panel(lang))
        bot.register_next_step_handler(ans_data, admin_panel_menu)

    elif chat_id not in admin_id:
        bot.send_message(chat_id, "Siz admin emassiz")
        bot.register_next_step_handler(message, start)

def admin_panel_menu(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == admin_quest[lang]:
        file = open('data.xlsx', 'rb')
        doc = bot.send_document(chat_id, file)
        bot.reply_to(message, "Sovallari exel faylida yuboring!")
        bot.register_next_step_handler(doc, change_data)



def change_data(message):
    document = message.document
    if document:
        if document.mime_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                  'application/vnd.ms-excel']:
            file_info = bot.get_file(document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open('data.xlsx', 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, f"Document {document.file_name} saqlandi va yangilandi!")
            return start(message)

        else:
            bot.reply_to(message, "Пожалуйста, отправьте Excel файл.")
    else:
        bot.reply_to(message, "Ошибка: это не документ.")

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    if chat_id_to_inn:
        del chat_id_to_inn[chat_id]
    access = bot.send_message(chat_id, f"🤖 Assalomu alaykum!\nMen E-Mehmon tizimining qo'llab-quvvatlash botiman.\nQaysi tilda javob berishim kerak?\n\n"
                                       f"🤖 Здравствуйте!\nЯ бот поддержки системы E-Mehmon.\nНа каком языке вам отвечать?",
                              reply_markup=generate_lang())
    bot.register_next_step_handler(access, select_type)




def select_type(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == '🇺🇿UZ':
        lang = "uz"
        bot.send_message(chat_id, type_message[lang], reply_markup=generate_select_type_person(lang))
        bot.register_next_step_handler(message, select_type_person)
    if message.text == '🇷🇺RU':
        lang = "ru"
        bot.send_message(chat_id, type_message[lang], reply_markup=generate_select_type_person(lang))
        bot.register_next_step_handler(message, select_type_person)


    if message.text == '/start':
        return start(message)

    if message.text == '/admin':
        return admin(message)


    user_langs[chat_id] = lang


def select_type_person(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == select_type_yur[lang]:
        bot.send_message(chat_id, select_section[lang], reply_markup=generate_yur(lang))
        bot.register_next_step_handler(message, select_category_yur)

    if message.text == select_type_fiz[lang]:
        bot.send_message(chat_id, select_section[lang], reply_markup=generate_fiz(lang))
        bot.register_next_step_handler(message, select_category_fiz)


    if message.text in [select_language[lang], '/start']:
        return start(message)

    if message.text == '/admin':
        return admin(message)

#-----------------------------YUR------------------------------------------------------
def select_category_yur(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == quest_emehmon[lang]:
        bot.send_message(chat_id, quest_emehmon_yur[lang], reply_markup=generate_quest_yur_emehmon(0, lang))

    elif message.text == quest_ovir[lang]:
        bot.send_message(chat_id, quest_ovir_yur[lang], reply_markup=generate_quest_yur_ovir(0, lang))

    elif message.text == quest_tur[lang]:
        bot.send_message(chat_id, quest_tur_yur[lang], reply_markup=generate_quest_yur_tur(0, lang))

    if message.text == back[lang]:
        bot.send_message(chat_id, type_message[lang], reply_markup=generate_select_type_person(lang))
        bot.register_next_step_handler(message, select_type_person)


#------------------------EMEHMON YUR-----------------------------------------------------


@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonyur_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_emehmon(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)


#------------------------OVIR YUR-----------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('pageoviryur_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_ovir(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)


#------------------------TURIZM YUR-----------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('pageturyur_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_tur(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)


#-----------------------------FIZ------------------------------------------------------
def select_category_fiz(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == quest_emehmon[lang]:
        bot.send_message(chat_id, quest_emehmon_fiz[lang], reply_markup=generate_quest_fiz_emehmon(0, lang))

    elif message.text == quest_ovir[lang]:
        bot.send_message(chat_id, quest_ovir_fiz[lang], reply_markup=generate_quest_fiz_ovir(0, lang))

    if message.text == back[lang]:
        bot.send_message(chat_id, type_message[lang], reply_markup=generate_select_type_person(lang))
        bot.register_next_step_handler(message, select_type_person)

#------------------------EMEHMON FIZ-----------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonfiz_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_fiz_emehmon(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)


#------------------------OVIR FIZ-----------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('pageovirfiz_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_fiz_ovir(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)


#--------------------------FIZ pay category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('fiz_pay'))
def select_category_fiz_pay(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_fiz[lang], reply_markup=generate_quest_fiz_emehmon_pay(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonfizpay_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_fiz_emehmon_pay(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questionfizpay_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_fiz_pay(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------


#--------------------------FIZ reg category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('fiz_reg'))
def select_category_fiz_reg(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_fiz[lang], reply_markup=generate_quest_fiz_emehmon_reg(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonfizreg_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_fiz_emehmon_reg(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questionfizreg_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_fiz_reg(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------



#--------------------------FIZ log category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('fiz_log'))
def select_category_fiz_log(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_fiz[lang], reply_markup=generate_quest_fiz_emehmon_log(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonfizlog_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_fiz_emehmon_log(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questionfizlog_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_fiz_log(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------



#--------------------------FIZ cadastr category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('fiz_cadastr'))
def select_category_fiz_cadastr(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_fiz[lang], reply_markup=generate_quest_fiz_emehmon_cadastr(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonfizcadastr_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_fiz_emehmon_cadastr(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questionfizcadastr_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_fiz_cadastr(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------





#--------------------------YUR pay category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('yur_pay'))
def select_category_yur_pay(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_yur[lang], reply_markup=generate_quest_yur_emehmon_pay(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonyurpay_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_emehmon_pay(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questionpay_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_pay(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------


#--------------------------YUR reg category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('yur_reg'))
def select_category_yur_reg(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_yur[lang], reply_markup=generate_quest_yur_emehmon_reg(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonyurreg_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_emehmon_reg(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questionreg_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_reg(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------


#--------------------------YUR control category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('yur_control'))
def select_category_yur_control(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_yur[lang], reply_markup=generate_quest_yur_emehmon_control(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonyurcontrol_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_emehmon_control(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questioncontrol_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_control(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------


#--------------------------YUR total_dogovor category keyboard-----------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('yur_total_dogovor'))
def select_category_yur_total_dogovor(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, quest_emehmon_yur[lang], reply_markup=generate_quest_yur_emehmon_total_dogovor(0, lang))

@bot.callback_query_handler(func=lambda call: call.data.startswith('pageemehmonyurtotaldogovor_'))
def handle_pagination(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    page_number = int(call.data.split('_')[1])
    new_keyboard = generate_quest_yur_emehmon_total_dogovor(page_number, lang)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('questiontotaldogovor_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang_total_dogovor(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#------------------------------------------------------------------------


#---------------------------logic keyboard------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
def handle_main_menu(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass
    call_data = bot.send_message(call.message.chat.id, select_section[lang], reply_markup=generate_select_type_person(lang))
    if chat_id_to_inn:
        del chat_id_to_inn[user_id]

    bot.register_next_step_handler(call_data, select_type_person)

@bot.callback_query_handler(func=lambda call: call.data == 'back_menu_yur')
def handle_main_menu(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, quest_emehmon_yur[lang], reply_markup=generate_quest_yur_emehmon(0, lang))


@bot.callback_query_handler(func=lambda call: call.data == 'back_menu_fiz')
def handle_main_menu(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, quest_emehmon_fiz[lang], reply_markup=generate_quest_fiz_emehmon(0, lang))


#--------------------------------Question yur emehmon----------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('questionemehmonyur_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_lang(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id
#---------------------------------------------------------------------------------------------------


#--------------------------------Question yur ovir----------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('questionoviryur_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_ovir_lang(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#-----------------------------------------------------------------------------------------


#--------------------------------Question yur tur----------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('questionyurtur_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_tur_lang(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#-----------------------------------------------------------------------------------------



#--------------------------------Question fiz emehmon----------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('questionfizemehmon_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_emehmon_fiz_lang(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#-----------------------------------------------------------------------------------------


#--------------------------------Question fiz ovir----------------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('questionfizovir_'))
def handle_question(call):
    user_id = call.from_user.id
    lang = user_langs.get(user_id, "uz")
    if user_id in previous_message_ids:
        try:
            bot.delete_message(call.message.chat.id, previous_message_ids[user_id])
        except:
            pass

    _, page_number, question_index = call.data.split('_')
    page_number = int(page_number)
    question_index = int(question_index)
    question = pages_ovir_fiz_lang(lang)[page_number][question_index]
    answer = question[1]

    sent_message = bot.send_message(call.message.chat.id, answer)

    previous_message_ids[user_id] = sent_message.message_id

#-----------------------------------------------------------------------------------------

@bot.callback_query_handler(func=lambda call: call.data == 'connect_to_disp_fiz')
def handle_operator_answer(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    bot.send_message(call.message.chat.id, answer_load[lang])

    bot.send_message(OPERATOR_CHAT_ID, f"{user_id} {help_user[lang]}")
    user_requests[user_id] = chat_id
    operator_chats[chat_id] = OPERATOR_CHAT_ID




@bot.callback_query_handler(func=lambda call: call.data == 'connect_to_disp_yur')
def handle_operator_answer(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    msg = bot.send_message(chat_id, send_inn[lang])
    bot.register_next_step_handler(msg, process_inn_step)

def process_inn_step(message):
    inn_number = message.text
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    check = check_inn(inn_number)

    if check == 'true':
        user_id = message.from_user.id
        bot.send_message(chat_id, answer_load[lang])
        bot.send_message(OPERATOR_CHAT_ID, f"{inn_number} {help_user[lang]}")
        user_requests[user_id] = chat_id
        operator_chats[chat_id] = OPERATOR_CHAT_ID
        user_inns[inn_number] = chat_id
        chat_id_to_inn[chat_id] = inn_number

    elif inn_number.isdigit():
        bot.send_message(chat_id, invalid_data[lang])
        bot.register_next_step_handler(message, process_inn_step)

    elif inn_number.isalnum():
        return start(message)


@bot.message_handler(func=lambda message: message.chat.id in user_requests.values())
def handle_user_message(message):
    user_chat_id = message.chat.id
    lang = user_langs.get(user_chat_id, "uz")
    operator_chat_id = operator_chats[user_chat_id]

    if user_chat_id in chat_id_to_inn and user_chat_id in user_requests:
        inn_number = chat_id_to_inn[user_chat_id]
        bot.send_message(operator_chat_id, f"{user[lang]} {inn_number}: {message.text}")

    else:
        bot.send_message(operator_chat_id, f"{user[lang]} {message.from_user.id}: {message.text}")

@bot.message_handler(func=lambda message: message.chat.id == OPERATOR_CHAT_ID)
def handle_operator_message(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    try:
        command, user_id, reply_message = message.text.split(' ', 2)
        user_id = int(user_id)

        if user_id in user_requests:
            user_chat_id = user_requests[user_id]
            bot.send_message(user_chat_id, reply_message)
        else:
            bot.send_message(message.chat.id, not_found[lang])
    except ValueError:
        bot.send_message(message.chat.id, format_yur_fiz[lang])


bot.polling(none_stop=True)
