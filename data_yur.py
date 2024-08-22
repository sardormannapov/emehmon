import pandas as pd

file_path = 'data.xlsx'

yur_ovir_ru = pd.read_excel(file_path, sheet_name='yur_ovir_ru')
yur_ovir_uz = pd.read_excel(file_path, sheet_name='yur_ovir_uz')
yur_emehmon_ru_data = pd.read_excel(file_path, sheet_name='yur_emehmon_ru')
yur_emehmon_uz_data = pd.read_excel(file_path, sheet_name='yur_emehmon_uz')
yur_turizm_ru_data = pd.read_excel(file_path, sheet_name='yur_turizm_ru')
yur_turizm_uz_data = pd.read_excel(file_path, sheet_name='yur_turizm_uz')



#------------------------------------------------
yur_emehmon_ru_pay = pd.read_excel(file_path, sheet_name='yur_emehmon_ru_pay')
yur_emehmon_ru_reg = pd.read_excel(file_path, sheet_name='yur_emehmon_ru_reg')
yur_emehmon_ru_control = pd.read_excel(file_path, sheet_name='yur_emehmon_ru_control')
yur_emehmon_ru_total_dogovor = pd.read_excel(file_path, sheet_name='yur_emehmon_ru_total_dogovor')
yur_emehmon_uz_pay = pd.read_excel(file_path, sheet_name='yur_emehmon_uz_pay')
yur_emehmon_uz_reg = pd.read_excel(file_path, sheet_name='yur_emehmon_uz_reg')
yur_emehmon_uz_control = pd.read_excel(file_path, sheet_name='yur_emehmon_uz_control')
yur_emehmon_uz_total_dogovor = pd.read_excel(file_path, sheet_name='yur_emehmon_uz_total_dogovor')

#------------------------------------------------

def remove_slash(value):
    if isinstance(value, str):
        return value.replace('/', '')
    return value

yur_ovir_ru_data = remove_slash(yur_ovir_ru)
yur_ovir_uz_data = remove_slash(yur_ovir_uz)
yur_emehmon_ru_data = remove_slash(yur_emehmon_ru_data)
yur_emehmon_uz_data = remove_slash(yur_emehmon_uz_data)
yur_turizm_ru_data = remove_slash(yur_turizm_ru_data)
yur_turizm_uz_data = remove_slash(yur_turizm_uz_data)

yur_emehmon_ru_pay_data = remove_slash(yur_emehmon_ru_pay)
yur_emehmon_ru_reg_data = remove_slash(yur_emehmon_ru_reg)
yur_emehmon_ru_control_data = remove_slash(yur_emehmon_ru_control)
yur_emehmon_ru_total_dogovor_data = remove_slash(yur_emehmon_ru_total_dogovor)
yur_emehmon_uz_pay_data = remove_slash(yur_emehmon_uz_pay)
yur_emehmon_uz_reg_data = remove_slash(yur_emehmon_uz_reg)
yur_emehmon_uz_control_data = remove_slash(yur_emehmon_uz_control)
yur_emehmon_uz_total_dogovor_data = remove_slash(yur_emehmon_uz_total_dogovor)

yur_ovir_ru = yur_ovir_ru_data.values.tolist()
yur_ovir_uz = yur_ovir_uz_data.values.tolist()
yur_emehmon_ru = yur_emehmon_ru_data.values.tolist()
yur_emehmon_uz = yur_emehmon_uz_data.values.tolist()
yur_turizm_ru = yur_turizm_ru_data.values.tolist()
yur_turizm_uz = yur_turizm_uz_data.values.tolist()

yur_emehmon_pay_ru = yur_emehmon_ru_pay_data.values.tolist()
yur_emehmon_reg_ru = yur_emehmon_ru_reg_data.values.tolist()
yur_emehmon_control_ru = yur_emehmon_ru_control_data.values.tolist()
yur_emehmon_total_dogovor_ru = yur_emehmon_ru_total_dogovor_data.values.tolist()
yur_emehmon_pay_uz = yur_emehmon_uz_pay_data.values.tolist()
yur_emehmon_reg_uz = yur_emehmon_uz_reg_data.values.tolist()
yur_emehmon_control_uz = yur_emehmon_uz_control_data.values.tolist()
yur_emehmon_total_dogovor_uz = yur_emehmon_uz_total_dogovor_data.values.tolist()
