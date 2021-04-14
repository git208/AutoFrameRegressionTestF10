import time


def form_data_format_body(dict):
    temp_str = f'----------------------------{hex(int(time.time() * 1000))}\n'
    for key, value in dict.items():
        temp_str = temp_str + f'Content-Disposition: form-data; name="{key}"\r\n{value}\n----------------------------{hex(int(time.time() * 1000))}\n'
    return temp_str[:-1] + '--'


def form_data_format_header():
    return {'Content-Type': f'multipart/form-data; boundary=--------------------------{hex(int(time.time() * 1000))}'}