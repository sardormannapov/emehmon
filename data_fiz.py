import pandas as pd

file_path = 'data.xlsx'

fiz_ovir_ru_data = pd.read_excel(file_path, sheet_name='fiz_ovir_ru')
fiz_ovir_uz_data = pd.read_excel(file_path, sheet_name='fiz_ovir_uz')
fiz_emehmon_ru_data = pd.read_excel(file_path, sheet_name='fiz_emehmon_ru')
fiz_emehmon_uz_data = pd.read_excel(file_path, sheet_name='fiz_emehmon_uz')

#------------------------------------------------
fiz_emehmon_ru_pay = pd.read_excel(file_path, sheet_name='fiz_emehmon_ru_pay')
fiz_emehmon_ru_reg = pd.read_excel(file_path, sheet_name='fiz_emehmon_ru_reg')
fiz_emehmon_ru_log = pd.read_excel(file_path, sheet_name='fiz_emehmon_ru_log')
fiz_emehmon_ru_cadastr = pd.read_excel(file_path, sheet_name='fiz_emehmon_ru_cadastr')
fiz_emehmon_uz_pay = pd.read_excel(file_path, sheet_name='fiz_emehmon_uz_pay')
fiz_emehmon_uz_reg = pd.read_excel(file_path, sheet_name='fiz_emehmon_uz_reg')
fiz_emehmon_uz_log = pd.read_excel(file_path, sheet_name='fiz_emehmon_uz_log')
fiz_emehmon_uz_cadastr = pd.read_excel(file_path, sheet_name='fiz_emehmon_uz_cadastr')

#------------------------------------------------


def remove_slash(value):
    if isinstance(value, str):
        return value.replace('/', '')
    return value

fiz_ovir_ru_data = remove_slash(fiz_ovir_ru_data)
fiz_ovir_uz_data = remove_slash(fiz_ovir_uz_data)
fiz_emehmon_ru_data = remove_slash(fiz_emehmon_ru_data)
fiz_emehmon_uz_data = remove_slash(fiz_emehmon_uz_data)

fiz_emehmon_ru_pay_data = remove_slash(fiz_emehmon_ru_pay)
fiz_emehmon_ru_reg_data = remove_slash(fiz_emehmon_ru_reg)
fiz_emehmon_ru_log_data = remove_slash(fiz_emehmon_ru_log)
fiz_emehmon_ru_cadastr_data = remove_slash(fiz_emehmon_ru_cadastr)
fiz_emehmon_uz_pay_data = remove_slash(fiz_emehmon_uz_pay)
fiz_emehmon_uz_reg_data = remove_slash(fiz_emehmon_uz_reg)
fiz_emehmon_uz_log_data = remove_slash(fiz_emehmon_uz_log)
fiz_emehmon_uz_cadastr_data = remove_slash(fiz_emehmon_uz_cadastr)



fiz_ovir_ru = fiz_ovir_ru_data.values.tolist()
fiz_ovir_uz = fiz_ovir_uz_data.values.tolist()
fiz_emehmon_ru = fiz_emehmon_ru_data.values.tolist()
fiz_emehmon_uz = fiz_emehmon_uz_data.values.tolist()
fiz_emehmon_pay_ru = fiz_emehmon_ru_pay_data.values.tolist()
fiz_emehmon_reg_ru = fiz_emehmon_ru_reg_data.values.tolist()
fiz_emehmon_log_ru = fiz_emehmon_ru_log_data.values.tolist()
fiz_emehmon_cadastr_ru = fiz_emehmon_ru_cadastr_data.values.tolist()
fiz_emehmon_pay_uz = fiz_emehmon_uz_pay_data.values.tolist()
fiz_emehmon_reg_uz = fiz_emehmon_uz_reg_data.values.tolist()
fiz_emehmon_log_uz = fiz_emehmon_uz_log_data.values.tolist()
fiz_emehmon_cadastr_uz = fiz_emehmon_uz_cadastr_data.values.tolist()




