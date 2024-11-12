def syt_chas_cek(value):
    return float(value)/24, float(value)/86400
def chas_syt_cek(value):
    return float(value)*24, float(value)/3600
def cek_syt_chas(value):
    return float(value)*86400, float(value)*3600
