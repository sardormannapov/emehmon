from telebot import types
from data_yur import *
from data_fiz import *
from localization.keyboard_lang import *


def generate_lang():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_uz = types.KeyboardButton(text="🇺🇿UZ")
    btn_ru = types.KeyboardButton(text="🇷🇺RU")
    keyboard.row(btn_uz, btn_ru)
    return keyboard


def generate_select_type_person(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_y = types.KeyboardButton(text=select_type_yur[lang])
    btn_j = types.KeyboardButton(text=select_type_fiz[lang])
    select_lang = types.KeyboardButton(text=select_language[lang])
    keyboard.row(btn_y, btn_j)
    keyboard.row(select_lang)
    return keyboard



def generate_yur(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_qs1 = types.KeyboardButton(quest_emehmon[lang])
    btn_qs2 = types.KeyboardButton(quest_ovir[lang])
    btn_qs3 = types.KeyboardButton(quest_tur[lang])
    btn_back = types.KeyboardButton(back[lang])
    keyboard.row(btn_qs1, btn_qs2)
    keyboard.row(btn_qs3)
    keyboard.row(btn_back)
    return keyboard


def generate_fiz(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_qs1 = types.KeyboardButton(quest_emehmon[lang])
    btn_qs2 = types.KeyboardButton(quest_ovir[lang])
    btn_back = types.KeyboardButton(back[lang])
    keyboard.row(btn_qs1, btn_qs2)
    keyboard.row(btn_back)
    return keyboard

#------------------------------------FIZ pay category keyboard-----------------------
def divide_into_pages_fiz_pay(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_fiz_pay(lang):
    if lang == "uz":
        return divide_into_pages_fiz_pay(fiz_emehmon_pay_uz, 3)

    if lang == "ru":
        return divide_into_pages_fiz_pay(fiz_emehmon_pay_ru, 3)

def generate_quest_fiz_emehmon_pay(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_fiz_pay(lang)[page_number]
    total_pages = len(pages_emehmon_lang_fiz_pay(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionfizpay_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonfizpay_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonfizpay_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_fiz"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_fiz"))
    return keyboard

#--------------------------------------------------------------------------------



#------------------------------------FIZ reg category keyboard-----------------------
def divide_into_pages_fiz_reg(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_fiz_reg(lang):
    if lang == "uz":
        return divide_into_pages_fiz_reg(fiz_emehmon_reg_uz, 3)

    if lang == "ru":
        return divide_into_pages_fiz_reg(fiz_emehmon_reg_ru, 3)

def generate_quest_fiz_emehmon_reg(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_fiz_reg(lang)[page_number]
    total_pages = len(pages_emehmon_lang_fiz_reg(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionfizreg_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonfizreg_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonfizreg_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_fiz"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_fiz"))
    return keyboard

#--------------------------------------------------------------------------------



#------------------------------------FIZ log category keyboard-----------------------
def divide_into_pages_fiz_log(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_fiz_log(lang):
    if lang == "uz":
        return divide_into_pages_fiz_log(fiz_emehmon_log_uz, 3)

    if lang == "ru":
        return divide_into_pages_fiz_log(fiz_emehmon_log_ru, 3)

def generate_quest_fiz_emehmon_log(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_fiz_log(lang)[page_number]
    total_pages = len(pages_emehmon_lang_fiz_log(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionfizlog_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonfizlog_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonfizlog_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_fiz"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_fiz"))
    return keyboard

#--------------------------------------------------------------------------------





#------------------------------------FIZ cadastr category keyboard-----------------------
def divide_into_pages_fiz_cadastr(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_fiz_cadastr(lang):
    if lang == "uz":
        return divide_into_pages_fiz_cadastr(fiz_emehmon_cadastr_uz, 3)

    if lang == "ru":
        return divide_into_pages_fiz_cadastr(fiz_emehmon_cadastr_ru, 3)

def generate_quest_fiz_emehmon_cadastr(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_fiz_cadastr(lang)[page_number]
    total_pages = len(pages_emehmon_lang_fiz_cadastr(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionfizcadastr_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonfizcadastr_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonfizcadastr_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_fiz"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_fiz"))
    return keyboard

#--------------------------------------------------------------------------------






#------------------------------------YUR pay category keyboard-----------------------
def divide_into_pages_yur_pay(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_pay(lang):
    if lang == "uz":
        return divide_into_pages_yur_pay(yur_emehmon_pay_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur_pay(yur_emehmon_pay_ru, 3)

def generate_quest_yur_emehmon_pay(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_pay(lang)[page_number]
    total_pages = len(pages_emehmon_lang_pay(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionpay_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonyurpay_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonyurpay_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_yur"))
    return keyboard

#--------------------------------------------------------------------------------



#------------------------------------YUR reg category keyboard-----------------------
def divide_into_pages_yur_reg(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_reg(lang):
    if lang == "uz":
        return divide_into_pages_yur_reg(yur_emehmon_reg_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur_reg(yur_emehmon_reg_ru, 3)

def generate_quest_yur_emehmon_reg(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_reg(lang)[page_number]
    total_pages = len(pages_emehmon_lang_reg(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionreg_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonyurreg_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonyurreg_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_yur"))
    return keyboard

#--------------------------------------------------------------------------------


#------------------------------------YUR control category keyboard-----------------------
def divide_into_pages_yur_control(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_control(lang):
    if lang == "uz":
        return divide_into_pages_yur_control(yur_emehmon_control_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur_control(yur_emehmon_control_ru, 3)

def generate_quest_yur_emehmon_control(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_control(lang)[page_number]
    total_pages = len(pages_emehmon_lang_control(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questioncontrol_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonyurcontrol_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonyurcontrol_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_yur"))
    return keyboard

#--------------------------------------------------------------------------------



#------------------------------------YUR total dogovor category keyboard-----------------------
def divide_into_pages_yur_total_dogovor(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang_total_dogovor(lang):
    if lang == "uz":
        return divide_into_pages_yur_total_dogovor(yur_emehmon_total_dogovor_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur_total_dogovor(yur_emehmon_total_dogovor_ru, 3)

def generate_quest_yur_emehmon_total_dogovor(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang_total_dogovor(lang)[page_number]
    total_pages = len(pages_emehmon_lang_total_dogovor(lang))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questiontotaldogovor_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonyurtotaldogovor_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonyurtotaldogovor_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))
    keyboard.add(types.InlineKeyboardButton(text=back[lang], callback_data="back_menu_yur"))
    return keyboard

#--------------------------------------------------------------------------------






#------------------------------------YUR--------------------------------------------
def divide_into_pages_yur(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_lang(lang):
    if lang == "uz":
        return divide_into_pages_yur(yur_emehmon_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur(yur_emehmon_ru, 3)


def generate_quest_yur_emehmon(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_lang(lang)[page_number]
    total_pages = len(pages_emehmon_lang(lang))
    keyboard.add(types.InlineKeyboardButton(text=yur_fiz_pay[lang], callback_data="yur_pay"))
    keyboard.add(types.InlineKeyboardButton(text=yur_fiz_reg[lang], callback_data="yur_reg"))
    keyboard.add(types.InlineKeyboardButton(text=yur_control[lang], callback_data="yur_control"))
    keyboard.add(types.InlineKeyboardButton(text=yur_total_dogovor[lang], callback_data="yur_total_dogovor"))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionemehmonyur_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonyur_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonyur_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))
    keyboard.add(types.InlineKeyboardButton(text=back_to_main[lang], callback_data="main_menu"))
    return keyboard


def pages_ovir_lang(lang):
    if lang == "uz":
        return divide_into_pages_yur(yur_ovir_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur(yur_ovir_ru, 3)


def generate_quest_yur_ovir(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_ovir_lang(lang)[page_number]
    total_pages = len(pages_ovir_lang(lang))

    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionoviryur_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageoviryur_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageoviryur_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))
    keyboard.add(types.InlineKeyboardButton(text=back_to_main[lang], callback_data="main_menu"))

    return keyboard


def pages_tur_lang(lang):
    if lang == "uz":
        return divide_into_pages_yur(yur_turizm_uz, 3)

    if lang == "ru":
        return divide_into_pages_yur(yur_turizm_ru, 3)


def generate_quest_yur_tur(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_tur_lang(lang)[page_number]
    total_pages = len(pages_tur_lang(lang))

    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionyurtur_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageturyur_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageturyur_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_yur"))

    keyboard.add(types.InlineKeyboardButton(text=back_to_main[lang], callback_data="main_menu"))

    return keyboard



#------------------------------------FIZ--------------------------------------------
def divide_into_pages_fiz(data, items_per_page):
    return [data[i:i + items_per_page] for i in range(0, len(data), items_per_page)]


def pages_emehmon_fiz_lang(lang):
    if lang == "uz":
        return divide_into_pages_fiz(fiz_emehmon_uz, 3)

    if lang == "ru":
        return divide_into_pages_fiz(fiz_emehmon_ru, 3)


def generate_quest_fiz_emehmon(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_emehmon_fiz_lang(lang)[page_number]
    total_pages = len(pages_emehmon_fiz_lang(lang))
    keyboard.add(types.InlineKeyboardButton(text=yur_fiz_pay[lang], callback_data="fiz_pay"))
    keyboard.add(types.InlineKeyboardButton(text=yur_fiz_reg[lang], callback_data="fiz_reg"))
    keyboard.add(types.InlineKeyboardButton(text=fiz_log[lang], callback_data="fiz_log"))
    keyboard.add(types.InlineKeyboardButton(text=fiz_cadastr[lang], callback_data="fiz_cadastr"))
    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionfizemehmon_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageemehmonfiz_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageemehmonfiz_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_fiz"))

    keyboard.add(types.InlineKeyboardButton(text=back_to_main[lang], callback_data="main_menu"))

    return keyboard


def pages_ovir_fiz_lang(lang):
    if lang == "uz":
        return divide_into_pages_fiz(fiz_ovir_uz, 3)

    if lang == "ru":
        return divide_into_pages_fiz(fiz_ovir_ru, 3)


def generate_quest_fiz_ovir(page_number=0, lang=""):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    page = pages_ovir_fiz_lang(lang)[page_number]
    total_pages = len(pages_ovir_fiz_lang(lang))

    for i, question in enumerate(page):
        quest_uz = question[0]
        callback_data = f"questionfizovir_{page_number}_{i}"
        keyboard.add(types.InlineKeyboardButton(text=quest_uz, callback_data=callback_data))

    nav_buttons = []

    if page_number > 0:
        nav_buttons.append(types.InlineKeyboardButton(text=prev[lang], callback_data=f"pageovirfiz_{page_number - 1}"))

    if page_number < total_pages - 1:
        nav_buttons.append(types.InlineKeyboardButton(text=next[lang], callback_data=f"pageovirfiz_{page_number + 1}"))

    keyboard.add(*nav_buttons)
    keyboard.add(types.InlineKeyboardButton(text=connect_to_disp[lang], callback_data="connect_to_disp_fiz"))
    keyboard.add(types.InlineKeyboardButton(text=back_to_main[lang], callback_data="main_menu"))
    return keyboard



def admin_panel(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_change_answ = types.KeyboardButton(admin_quest[lang])
    keyboard.row(btn_change_answ)
    return keyboard




















