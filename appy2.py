import streamlit as st
import pandas as pd
import urllib.parse

# Configuración de la página web
st.set_page_config(page_title="Catálogo de Sublimados", page_icon="📱", layout="wide")

# Función corregida usando el endpoint de miniaturas de Google Drive
def obtener_url_imagen_drive(url_drive):
    try:
        if "file/d/" in url_drive:
            id_archivo = url_drive.split("file/d/")[1].split("/")[0]
            return f"https://drive.google.com/thumbnail?id={id_archivo}&sz=w600"
    except Exception:
        pass
    return url_drive

# 1. Base de datos con la información exacta de tu enlace
@st.cache_data
def cargar_datos():
    datos = [
        # Animal nocturno
        {"Colección": "Animal nocturno", "Modelo": "Oso", "URL": "https://drive.google.com/file/d/1BZCRfRa1hrJvFdh_al0wnpOACBZHWQuo/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Aguila", "URL": "https://drive.google.com/file/d/195Xdr1J3-EZe_ARYQA-KRVhh8gPozoHZ/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "León", "URL": "https://drive.google.com/file/d/18jWpnDPiU3WsDga3-5MDMCILvrG_lU7g/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Buho", "URL": "https://drive.google.com/file/d/1wG6dwNlQB1nW8nq6vmn5v-MXqx7_SYfm/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Serpiente", "URL": "https://drive.google.com/file/d/1mQG5akzWGS4Pwwe_lJ3VIu1BEVZIt0W-/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Puma", "URL": "https://drive.google.com/file/d/17d7VGoPzU-VBmqxB8CXQjnT8GKcsropI/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Elefante", "URL": "https://drive.google.com/file/d/1n1QpDz6J6PNgcdVVAJldfZ3xA7SuZmle/view?usp=drivesdk"},
        # Angel Armado
        {"Colección": "Angel Armado", "Modelo": "Venado", "URL": "https://drive.google.com/file/d/1rnyExjeEGQmoaHT6Noo_6ZTeMuS88F1H/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado IIII", "URL": "https://drive.google.com/file/d/1hG4i-2fq539uY5CwHVNC9EO9X-ECnpVp/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VIIII", "URL": "https://drive.google.com/file/d/1BLm6Dtb5XJsqVbYL2P_JPQQ7Q9VII_oC/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VIII", "URL": "https://drive.google.com/file/d/1JwICILHiG6OLb8WNqajhYhwpianfZuhA/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VII", "URL": "https://drive.google.com/file/d/1FNPf8xcL0xVyLXSlR7rgBCO6ph2s28V7/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VI", "URL": "https://drive.google.com/file/d/10bU3Uyr5Wm6hi-zRwsqxlHvOVJn8MAgD/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado V", "URL": "https://drive.google.com/file/d/1CJB2gZ9inD23jNJI9_EldfijA5wDKTtc/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado III", "URL": "https://drive.google.com/file/d/1DfpEVIGhuKnpPiuvfkIlHLDPHZXMdLzK/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado II", "URL": "https://drive.google.com/file/d/1HXv4R9Zb8V96XwJKD-x4qGkkiBfcgA5Q/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado I", "URL": "https://drive.google.com/file/d/12irI1nOr37XgYRWjbt-oXPq01t-1IgYV/view?usp=drivesdk"},
        # Animal
        {"Colección": "Animal", "Modelo": "Animal XIIII", "URL": "https://drive.google.com/file/d/1FGqbTtYZutDDqp9sDV0hKqBkJKOVxrDy/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal XIII", "URL": "https://drive.google.com/file/d/1c1gLcwG9qOAGUb9SfVjxInW6asxVBzMi/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal XII", "URL": "https://drive.google.com/file/d/1jEXB2_87uqj8FebKoQrdauknF6W2SLp8/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal XI", "URL": "https://drive.google.com/file/d/1iPKySoH_HDW-zGqlkb8ojqjQfMu81t8T/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal X", "URL": "https://drive.google.com/file/d/1SOSbtDXAW3jDJGpRDWesy4ISmYL3KXGq/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VIIII", "URL": "https://drive.google.com/file/d/1bFVja4a6eh6lHzEljdGU0nA_ffkWYWcz/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VIII", "URL": "https://drive.google.com/file/d/1YsVM6CGYpg7GfmoZuCwW995xRUB8YYqv/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VII", "URL": "https://drive.google.com/file/d/1yEi3o6_F2WjCEX-VHy3zKjsY73FUYyt9/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VI", "URL": "https://drive.google.com/file/d/1IcFRfv2R8wGKkQZkM6CvQwbZKIMoZWmk/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal V", "URL": "https://drive.google.com/file/d/1EuB64sR_nt2wke-RBXjbLsN1BLBikg_1/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal IIII", "URL": "https://drive.google.com/file/d/1W2YURhKfbdHn9Omfv9de-s6hFMtgQeaG/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal III", "URL": "https://drive.google.com/file/d/1aVibEqqODWd1wT1nhFH4Hmxf7YWqhMDx/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal II", "URL": "https://drive.google.com/file/d/1OSGV9RMzBawEEAiMR9C2rblquQ8BSPjz/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal I", "URL": "https://drive.google.com/file/d/1_wtreCfVsDf7M6ECCn7-CtdNRZsQTfAQ/view?usp=drivesdk"},
        # Magic
        {"Colección": "Magic", "Modelo": "Magic 12", "URL": "https://drive.google.com/file/d/1FVnzuujx9NHqy2R8hmlIylonYZ3sf8FN/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 11", "URL": "https://drive.google.com/file/d/12CiaMVD0wbptPNXh1lkuG-OhYEAp42jA/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 10", "URL": "https://drive.google.com/file/d/1Pf1mwYEFF2POB-jN7Mv4LoptrYoJwNDM/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 09", "URL": "https://drive.google.com/file/d/10FSWfmVs1bwl5v-FRc-_OqbgFeKjrPUc/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 08", "URL": "https://drive.google.com/file/d/1f9A72TJAelagydaxYRoQzpjXgbrLASZ8/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 07", "URL": "https://drive.google.com/file/d/18xuTEXCvRo_eTRp6diOUsyjwGT60lvZD/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 06", "URL": "https://drive.google.com/file/d/18Pg0NlTpn2GoXrdFp4uFe9NhdXIy-Atm/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 05", "URL": "https://drive.google.com/file/d/1Nlq3e5NkBPYnL0Y-qdsgYF0fZ2Y-5pHZ/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 04", "URL": "https://drive.google.com/file/d/1gHPn-xeEw13Tn1X2tGHKRkBPxwk5Z6Fa/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 03", "URL": "https://drive.google.com/file/d/1ojcDZvWWUvDjgVsktvB2ewrOOCAoc18X/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 02", "URL": "https://drive.google.com/file/d/156kpRWHII4Z1qf6iAd1vo26nG3pQqL9Z/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 01", "URL": "https://drive.google.com/file/d/137qwFVsBDfZgCHUsQz6xOjRg2rsdbdrr/view?usp=drivesdk"},
        # Mago de oz
        {"Colección": "Mago de oz", "Modelo": "Oz 09", "URL": "https://drive.google.com/file/d/1ukW-YOPQv6kji5INlQX5MXmGwe6TJUDx/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 08", "URL": "https://drive.google.com/file/d/1otDrujGGeENCUm55QQO0xvnseNgNYyV_/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 07", "URL": "https://drive.google.com/file/d/1-1IBqhlAfnvE8R5yNQ7zJkC11-mTZddV/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 06", "URL": "https://drive.google.com/file/d/1SMIukNG9LrqR06T5SQm0zNTFcdiC1ehd/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 05", "URL": "https://drive.google.com/file/d/1SUYLubYzefH2qVSZGcLX5PJ_ZiloRjwm/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 04", "URL": "https://drive.google.com/file/d/14ROBQC-Iu7OhxyIIS-bm4hHaVnemEVvC/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 03", "URL": "https://drive.google.com/file/d/1CCED0WJksAGU3Y_Is-wzMlFpE03T9rLt/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 02", "URL": "https://drive.google.com/file/d/1Knqd2ZanLMrWrSAYsUi6RuKAMniSCMEz/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Oz 01", "URL": "https://drive.google.com/file/d/1cvblxBS6tlg6XcO9FM_XzkgzWcPIsAmC/view?usp=drivesdk"},
        # Warzone
        {"Colección": "Warzone", "Modelo": "Warzone 09", "URL": "https://drive.google.com/file/d/1bAEGB19CnZp-Gj0eRQSfR_tBNtHDGIAT/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 08", "URL": "https://drive.google.com/file/d/1yweg0LF2DpUfB68ZhXr02wWOXqt9wa4j/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 07", "URL": "https://drive.google.com/file/d/1u2cpIIMxyEizFHffHg5aaW6f9Y09BvAf/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 06", "URL": "https://drive.google.com/file/d/1JyMqTilwO4ICy94Bs6Qm-ImjFDb74Y6r/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 05", "URL": "https://drive.google.com/file/d/1LcBNHUCxi4mzWIS5btY_aUVk4zhyLtb6/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 04", "URL": "https://drive.google.com/file/d/1z1p1Kd5milonsEUh-h6-d1KZHMmn6WcR/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 03", "URL": "https://drive.google.com/file/d/1ej-rFK-JzOJgJTN22Lh7DS79Zkd-TQnj/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 02", "URL": "https://drive.google.com/file/d/1GNSV2cJJYMGMg8SbbOMlm8GoO3lUGVoc/view?usp=drivesdk"},
        {"Colección": "Warzone", "Modelo": "Warzone 01", "URL": "https://drive.google.com/file/d/1nhJFjJvLlF3RRn5xELS-ReaYjc30V-9N/view?usp=drivesdk"},
        # Bob
        {"Colección": "Bob", "Modelo": "Bob 21", "URL": "https://drive.google.com/file/d/1hAyvBK6C8SOY2-tmhYaJ1ybm7Zh2dddl/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 20", "URL": "https://drive.google.com/file/d/141UQiP3krCC7YNeWCIjI6C34UO4Cura0/view?usp=drivesdk"},   
        {"Colección": "Bob", "Modelo": "Bob 19", "URL": "https://drive.google.com/file/d/1T-d37U0IjaFztqbidimcpvur1iOLcVvI/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 18", "URL": "https://drive.google.com/file/d/1KH3hjPiD7gP2AfJrOGmokUAQxWKDmUD-/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 17", "URL": "https://drive.google.com/file/d/1l8Yjujl3V7JcyWNgtsWzZGZxT46-Tyhg/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 16", "URL": "https://drive.google.com/file/d/1lfDAl89Ul-Mru4rM00ZRZ-8HJwMXqgEz/view?usp=drivesdk"},   
        {"Colección": "Bob", "Modelo": "Bob 15", "URL": "https://drive.google.com/file/d/1rxesH6x-d8bXP3Ljvf6sLxmqFWz9AyO6/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 14", "URL": "https://drive.google.com/file/d/1b61hUhjfCxPAYHl8NCc1_p2bTtQo_tvF/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 13", "URL": "https://drive.google.com/file/d/1llkA_XH3vYFhnJ5m7R2JsyM5pfNn_bH4/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 12", "URL": "https://drive.google.com/file/d/1aDb14U8jb-Z-2HmQ0EvEMR3OAiKpXAR1/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 11", "URL": "https://drive.google.com/file/d/1ehuu9hHX6JGEgHBB2t_JoeUNrWjettPX/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 10", "URL": "https://drive.google.com/file/d/13XrFrcsQSvS9cK7k4r9eEfCbiBdK6-A3/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 09", "URL": "https://drive.google.com/file/d/1Y_70n_Qwdp6yTCP3E_SS-sc0EoejL_8r/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 08", "URL": "https://drive.google.com/file/d/1K3ZtE27VXZA6KJ4AcS_tkh6gYvOJAubS/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 07", "URL": "https://drive.google.com/file/d/1IymsSxzDsOLyaUApc_WfsV8sgBGHJIM_/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 06", "URL": "https://drive.google.com/file/d/1MpfFJQmwwVTQFnYEaWkV_eK5hfEW2TkU/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 04", "URL": "https://drive.google.com/file/d/1Gz6tDAVwLfHFZ3xh5NZLole0r02VXlLA/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 03", "URL": "https://drive.google.com/file/d/1BfmcB8VvNGoCLlnxz9ypxKd2a5N3qcg8/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 02", "URL": "https://drive.google.com/file/d/1VnmXayZXTtIua-5TQYAiUns_bEFQ_HjM/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Bob 01", "URL": "https://drive.google.com/file/d/1sxrTMKRXxr2A3TQkOjPSIfoRyJzRA1SH/view?usp=drivesdk"},
        # Catlien
        {"Colección": "Catlien", "Modelo": "Catlien 14", "URL": "https://drive.google.com/file/d/1rlNhW0ruBfm8M9Z1-tq6BDMixN8L1dpY/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 13", "URL": "https://drive.google.com/file/d/11VvJK580YPbjJ7elhZUzfcRXHwmzpg7w/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 12", "URL": "https://drive.google.com/file/d/18N8-C8RF6mo4G3ho7emYH4k0HpZiu_ot/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 11", "URL": "https://drive.google.com/file/d/1FzPfyGJMvSts1sI3m2tQo4zNo7AOyp7Y/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 10", "URL": "https://drive.google.com/file/d/18t2z5maFhAm1PEg6jCMlu17BYcT-frp6/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 09", "URL": "https://drive.google.com/file/d/1IZaL7dAFdjRcUsFPcsu6wtPYS7qcatRA/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 08", "URL": "https://drive.google.com/file/d/1JBRAIxRcGi2L24fpVzy-t4IFDmsWalhg/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 07", "URL": "https://drive.google.com/file/d/1ngVOPCo2vBDcusRmYEICfKkVthmBZD7e/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 06", "URL": "https://drive.google.com/file/d/1cIqZY1cwrHcBw1Lepk5URf-PoAIcrlrL/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 05", "URL": "https://drive.google.com/file/d/1BCOIwpffSdRBDYqyI5TlSgRpaSHVz6Fd/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 04", "URL": "https://drive.google.com/file/d/1XkZUYBAYGJ2Uq30bvx-twMgVPXLYPJBk/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 03", "URL": "https://drive.google.com/file/d/1ysYSVghA7johQpq46dWsACnkpSMwOXel/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 02", "URL": "https://drive.google.com/file/d/1_SwyF4leSy-VXUrm8_PTZyoTPbck6YGt/view?usp=drivesdk"},
        {"Colección": "Catlien", "Modelo": "Catlien 01", "URL": "https://drive.google.com/file/d/1Zg4dlwuLwnOHV--QNVJH0ZUrmfBfsiFK/view?usp=drivesdk"},
        # Barrio
        {"Colección": "Barrio", "Modelo": "Barrio 10", "URL": "https://drive.google.com/file/d/1AVOfG67rQ4yqHV2QyDcx2s916HUiC2Zs/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 09", "URL": "https://drive.google.com/file/d/1v1EOXLDZTClLvtqxH-3Kw7PoOZBJO8yj/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 08", "URL": "https://drive.google.com/file/d/1JwiZYhWj1inLTW5I1Rv7AbEgLv4y9Yy8/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 07", "URL": "https://drive.google.com/file/d/1DNw-9TR6tK1S6UWpB0q5keiVMffn_U2i/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 06", "URL": "https://drive.google.com/file/d/1JwJRFiKyaD68C1xUIVfINvn7s5cUKggJ/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 05", "URL": "https://drive.google.com/file/d/1IrB2vFbkuNAGvzaQWjKAo7i4IXWDNnwF/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 04", "URL": "https://drive.google.com/file/d/1qIC7vulWeNesp9bahd4g60WTQSBQmK3w/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 03", "URL": "https://drive.google.com/file/d/1kMatonh74s2fOtgM8VGb17xk051RjPpy/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 02", "URL": "https://drive.google.com/file/d/1SfdxvNnje2QIKS-_OYWl0ZyjChHBbTY_/view?usp=drivesdk"},
        {"Colección": "Barrio", "Modelo": "Barrio 01", "URL": "https://drive.google.com/file/d/1uiXmdylNx1JnysDUYIx9R25kuRfG6jx-/view?usp=drivesdk"},
        # Sinfonía
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 11", "URL": "https://drive.google.com/file/d/1459nTFxAoasZBKugVtrlves6zzvtTWS7/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 10", "URL": "https://drive.google.com/file/d/17z6TDyOgFyd01sK9WDYRixr9eUAwUb7z/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 09", "URL": "https://drive.google.com/file/d/1FjMt12DQjejkHHL1_OI-Ifn1gPAkFFSe/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 08", "URL": "https://drive.google.com/file/d/1FIU5ykiY3oIpIFT-u3_lHeiJeWvnRcS6/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 07", "URL": "https://drive.google.com/file/d/1rRIV6WTxHjFKB-mb0HinCHzxez4q9ct3/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 06", "URL": "https://drive.google.com/file/d/1AtMAcGaMn_S3odvm_atM72uPA8S-0rL7/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 05", "URL": "https://drive.google.com/file/d/1Q2Nm3Hu37wUZeoO0dDB1bwsIoJfFhIjk/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 04", "URL": "https://drive.google.com/file/d/1uhw-WblVLvVuZ1q0H8OuPwLbYMKAi10b/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 03", "URL": "https://drive.google.com/file/d/1HE9ziyod581DaHtCky_-fZiWS-4selaj/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 02", "URL": "https://drive.google.com/file/d/1d1ixWEHb0rqbZB4J1DzMV8lJZ-G63kD8/view?usp=drivesdk"},
        {"Colección": "Sinfonía del cine", "Modelo": "Sinfonía 01", "URL": "https://drive.google.com/file/d/1eKXuFJn_dJO3ubZhrs-nOqh3Y37xn3Ti/view?usp=drivesdk"},
        # Virtual colection
        {"Colección": "Virtual colection", "Modelo": "Virtual 10", "URL": "https://drive.google.com/file/d/1JF_ZHDmGnrDyw-CpdNBTcco0ZR5aDklE/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 09", "URL": "https://drive.google.com/file/d/1NrwD-NqBdFq1h621SlAK5jvGs-qBS0s6/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 08", "URL": "https://drive.google.com/file/d/1iAyjsEcIUQ7AAkXrbsYX3HPqyorQnvBd/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 07", "URL": "https://drive.google.com/file/d/1YWrxEYlIqvGUoIJq7QLqQJmqfVU3wcQR/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 06", "URL": "https://drive.google.com/file/d/1eM1mHlKYB3iGGfukGfE0_wN-HFxObGoY/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 05", "URL": "https://drive.google.com/file/d/1Sv4cjKV4NrXeHSBCO3znd4MLUFuVhV1M/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 04", "URL": "https://drive.google.com/file/d/1HcysDNmyqR8UDZIdF9BwQwIZilywDadW/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 03", "URL": "https://drive.google.com/file/d/1itNS5lJ8X69zpOVFrv849slTARC_flCU/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 02", "URL": "https://drive.google.com/file/d/1c8GR9r5LrgAY3kWLbjJGeWrc9qhiQp4l/view?usp=drivesdk"},
        {"Colección": "Virtual colection", "Modelo": "Virtual 01", "URL": "https://drive.google.com/file/d/1n_wv-VKuPLAgHtQ5EZH8obpA_p6D_TEy/view?usp=drivesdk"},
        # Explora
        {"Colección": "Explora", "Modelo": "Explora 09", "URL": "https://drive.google.com/file/d/16LQdupJp5Ytqfn0woJ4xRUxt6zWPcS_I/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 08", "URL": "https://drive.google.com/file/d/1a6CAB65wK5UuKkS60A7uSiXvGG0VJTPf/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 07", "URL": "https://drive.google.com/file/d/1pfG8jlwmwPH4qqpAMp40m152hLRe1BNW/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 06", "URL": "https://drive.google.com/file/d/10KgSfgXqY_2Ec2io8vqazhyNgG4HMvJI/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 05", "URL": "https://drive.google.com/file/d/1O2GI1Q5RE0BZRbJI1NbRBRkRA62_NdoZ/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 04", "URL": "https://drive.google.com/file/d/1l1wDXvBZzieCsXGNd95qiLSEjH10YZvc/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 03", "URL": "https://drive.google.com/file/d/1Hz6a9QEYV6E58AuV3DP-lqRA9-wMjoeG/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 02", "URL": "https://drive.google.com/file/d/1DhWqEMgTAh11zDjpdyB2tpKKffqZdGG7/view?usp=drivesdk"},
        {"Colección": "Explora", "Modelo": "Explora 01", "URL": "https://drive.google.com/file/d/1sG9CCd_qjJ5ocRBFPXcK0M-edreFOmyN/view?usp=drivesdk"},
        # Frases
        {"Colección": "Frases", "Modelo": "Frases 17", "URL": "https://drive.google.com/file/d/1To7DiFa6x-ICw0scHpQRsAA-TEqXDnTg/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 16", "URL": "https://drive.google.com/file/d/1xUdAzNBDe06xHek7QCm9xHUDthxBSNFY/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 15", "URL": "https://drive.google.com/file/d/1_mQ0d7AlIVkHvHWPwVlFD2gDE4coLg1K/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 14", "URL": "https://drive.google.com/file/d/1bdqcd_Hmei2rUdj-QldJATEMqMY-Uy0N/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 13", "URL": "https://drive.google.com/file/d/1m8vm00OEJglenHwtLzOl-TIAW0av4lpp/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 12", "URL": "https://drive.google.com/file/d/1uJogk--CrpjpWXza6HvjctC2HoTx4qKw/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 11", "URL": "https://drive.google.com/file/d/1R85sSVOLSyEwahkKpzCtGsIxVuCVO9mP/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 10", "URL": "https://drive.google.com/file/d/1-G8BOAF0n8Pr02Y34x6p_WXMmK7LKt5C/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 09", "URL": "https://drive.google.com/file/d/1n0bfRImd8iIu_Hsf8XQ_8B-vcgdW9NBA/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 08", "URL": "https://drive.google.com/file/d/1yaTcEIefQLko_nhjv5vmU3UJd681sf3M/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 07", "URL": "https://drive.google.com/file/d/11PM6QheG0yO8IR_usOHRJM4fFjiyoJ3e/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 06", "URL": "https://drive.google.com/file/d/17f2ugLc-NImKDyta9J-dXM4Lb6ZWFan3/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 05", "URL": "https://drive.google.com/file/d/12tGaqq3YzaE7SuUS2dXMENSU_NH4BjPI/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 04", "URL": "https://drive.google.com/file/d/1PUHbZq3pe1aesp_kHXy3elrXdqlbwLLw/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 03", "URL": "https://drive.google.com/file/d/1j6y4m4V8BneAJsQlNnVdZ9B_Tizr-duR/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 02", "URL": "https://drive.google.com/file/d/1fDsOMfKXG--iLOVv0S7Jqo5iQQ2zvG4p/view?usp=drivesdk"},
        {"Colección": "Frases", "Modelo": "Frases 01", "URL": "https://drive.google.com/file/d/1yvzVo_SAiYAxZE3OGeBWI6goALwqebxV/view?usp=drivesdk"},
        # Chino
        {"Colección": "Chino", "Modelo": "Chino 6", "URL": "https://drive.google.com/file/d/1vYI4zrYzM_jAUWJKYlNisRIjhJze_vkx/view?usp=drivesdk"},
        {"Colección": "Chino", "Modelo": "Chino 5", "URL": "https://drive.google.com/file/d/145vDg8vmOF89sVDvMWLlDe9B5IXJfnPX/view?usp=drivesdk"},
        {"Colección": "Chino", "Modelo": "Chino 4", "URL": "https://drive.google.com/file/d/167HwyPd1fr9uXLmUrDw44dYq7QQDYFH7/view?usp=drivesdk"},
        {"Colección": "Chino", "Modelo": "Chino 3", "URL": "https://drive.google.com/file/d/1NSZeELFG623HgJ2Y6iAC1gdETUyt3yRV/view?usp=drivesdk"},
        {"Colección": "Chino", "Modelo": "Chino 2", "URL": "https://drive.google.com/file/d/142Lz8ua5mXC33QPZS3Ip5W9KbGjeWd7x/view?usp=drivesdk"},
        {"Colección": "Chino", "Modelo": "Chino 1", "URL": "https://drive.google.com/file/d/12Au9rYBzo82HfhSPmmTGvr94ba46I-nt/view?usp=drivesdk"},
        # Gótico
        {"Colección": "Gótico ", "Modelo": "Gótico 20", "URL": "https://drive.google.com/file/d/1LcmsWxpeTatbPLSMe9zPjvkuYgZbed7X/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 19", "URL": "https://drive.google.com/file/d/1RgBeVD1AJLGquv3j9SI9Non1jm-k_hGG/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 18", "URL": "https://drive.google.com/file/d/1CYJD9wd23BhmwLEkWfZeu-cOFywed4SB/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 17", "URL": "https://drive.google.com/file/d/1ojZM1LXbmun8Z6XvSaxwPOZ8fn6t2Y76/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 16", "URL": "https://drive.google.com/file/d/1bzShAC5vc-XzLrCi5TonhgRzEj2d2H6F/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 15", "URL": "https://drive.google.com/file/d/12BAMQnZy-_KWUEvlOHnO_xWB1V1jBUdp/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 14", "URL": "https://drive.google.com/file/d/1zeCGB77JxX5fRjmJECrK-X-Ne3PFzdcC/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 13", "URL": "https://drive.google.com/file/d/1anJoC4cOXhqDfxpwvwP6l5r5tdJsoRie/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 12", "URL": "https://drive.google.com/file/d/1wDdfer7xqPs7JGLufM35GhbH5TcSmt8e/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 11", "URL": "https://drive.google.com/file/d/1NVzYqIgzhJ7olRoYacQvTnlUAvEkj-kK/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 10", "URL": "https://drive.google.com/file/d/1M9aCfFbAw_Pt6ocBSi-p1MO7i5ga-Zi_/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 09", "URL": "https://drive.google.com/file/d/1NdacEUDhZhCziOzgaSBYBpF_8H2etb5A/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 08", "URL": "https://drive.google.com/file/d/1j-Stze-MTBcq4c_sx4spggVgpiaXaRl1/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 07", "URL": "https://drive.google.com/file/d/1zg1SFOansrLCN0Xo4rq1rkg-xFF5eDjN/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 06", "URL": "https://drive.google.com/file/d/1xOZihfxKtcUnilYjSEkU_ATr7pwZkvsV/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 05", "URL": "https://drive.google.com/file/d/11rBocQ3ilvS0bbd2Dwqg6RUN84-VyEDl/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 04", "URL": "https://drive.google.com/file/d/1vo8QorRbKb93xMuby7FQajsJx52Jcxz2/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 03", "URL": "https://drive.google.com/file/d/1AYx48gTz0pesNh5FpLmGJrf6Fw8xVCgs/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 02", "URL": "https://drive.google.com/file/d/14ktjdxynOpAYKEppQwZlZeGABNUmd0b_/view?usp=drivesdk"},
        {"Colección": "Gótico ", "Modelo": "Gótico 01", "URL": "https://drive.google.com/file/d/1jLIwczs1DilXVPO91IYu2Ux8fxyyLKRE/view?usp=drivesdk"},
        # HH
        {"Colección": "HIP-HOP", "Modelo": "HH 10", "URL": "https://drive.google.com/file/d/1GNe-Slo8JuhfOxJamBMDyNXEN0ZepqWd/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 09", "URL": "https://drive.google.com/file/d/1IR7f6zVlAIHyPSZmNhwEmq-Mq-T322-I/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 08", "URL": "https://drive.google.com/file/d/1AA5vRF_czavYgNHYSZMGOLUaS80SIdwu/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 07", "URL": "https://drive.google.com/file/d/1ApiYFDSprGRpCw10VkvomvjVtTzLU85K/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 06", "URL": "https://drive.google.com/file/d/1JyBz6-mBf-UN0D7jI29K7omCOOpWafjX/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 05", "URL": "https://drive.google.com/file/d/11mmVKwOeMfaPwYcUys3AsP07AjJJdkva/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 04", "URL": "https://drive.google.com/file/d/117hNli68aReELPI3X_BjCoFD6uYZLVwj/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 03", "URL": "https://drive.google.com/file/d/1aA8X8sDLNZUFOnDmhQPZHIK_KhAmj23j/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 02", "URL": "https://drive.google.com/file/d/1VbTUj7RbATrNbqy69ooTyuV5dIouGwFH/view?usp=drivesdk"},
        {"Colección": "HIP-HOP", "Modelo": "HH 01", "URL": "https://drive.google.com/file/d/114SlJ4mabNCdbYDXyfCUP4h5hCQihuRC/view?usp=drivesdk"},
                # Mítico
        {"Colección": "Mitico", "Modelo": "Mítico 08", "URL": "https://drive.google.com/file/d/1HT9fZmHHjFV0SS7u2ayr0KkoESDst5Ha/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 07", "URL": "https://drive.google.com/file/d/1evMqWBepqJpoN5Jsj69A88wiEDxNu2eB/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 06", "URL": "https://drive.google.com/file/d/1UZWS2zMPS4AaTY5W1sk8oWD-zTfT3U8s/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 05", "URL": "https://drive.google.com/file/d/1UyNCZW5xxcDntdWcneS9aHpHh-UosgTJ/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 04", "URL": "https://drive.google.com/file/d/1H7JGJanWnIUUlctwwKDxQCImVjbGkL07/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 03", "URL": "https://drive.google.com/file/d/1-t3NacABMgmwiM_1E_30zlaR950QrERm/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 02", "URL": "https://drive.google.com/file/d/1Sn4ojz8oHi6udCY2Ppnkr94yIRsDmjSl/view?usp=drivesdk"},
        {"Colección": "Mitico", "Modelo": "Mítico 01", "URL": "https://drive.google.com/file/d/1e4TR3OOhAmjU-2JLgmD1Z5Kvln60dARM/view?usp=drivesdk"},
        # Azteca
        {"Colección": "Azteca", "Modelo": "Runa", "URL": "https://drive.google.com/file/d/1B283VwYrsFbyFBm5_hIZ6QRJhw3BU1uB/view?usp=drivesdk"},
        {"Colección": "Azteca", "Modelo": "Ritual", "URL": "https://drive.google.com/file/d/1ZObOBlOAEXu2DEhNRohEMF_joSqE-bLt/view?usp=drivesdk"},
        {"Colección": "Azteca", "Modelo": "Azteca", "URL": "https://drive.google.com/file/d/1wGxJGFBGrzeLJNj5z1hhvKWfEWAtq-EK/view?usp=drivesdk"},
        {"Colección": "Azteca", "Modelo": "Quetzalcoatl", "URL": "https://drive.google.com/file/d/1eUOYu30Fw3Tp690aAjiURD2jxIcYaL9B/view?usp=drivesdk"},
        {"Colección": "Azteca", "Modelo": "Huitzilopochtli", "URL": "https://drive.google.com/file/d/1LBwZZ2ervENCYW5XFAmSg_16MpaBBhDf/view?usp=drivesdk"},
        # Rasta
        {"Colección": "Rasta", "Modelo": "Rasta 04", "URL": "https://drive.google.com/file/d/1wqC7v3_5G7UkE71lg7mKlMr4z9o-SBj1/view?usp=drivesdk"}, 
        {"Colección": "Rasta", "Modelo": "Rasta 03", "URL": "https://drive.google.com/file/d/1wcEI7GZrwn6Eb8mjEwok-J3OPwwZ1CR9/view?usp=drivesdk"},
        {"Colección": "Rasta", "Modelo": "Rasta 02", "URL": "https://drive.google.com/file/d/1xuIlJzvFqP2xikTapk7ruDG1HWsHeThS/view?usp=drivesdk"},
        {"Colección": "Rasta", "Modelo": "Rasta 01", "URL": "https://drive.google.com/file/d/1t6apRPldk1mr1TB_jEvHtEb0pz4FMyiM/view?usp=drivesdk"},
        # Psycodelic
        {"Colección": "Psy", "Modelo": "Psy 05", "URL": "https://drive.google.com/file/d/1L9KJ9IFjK5uD1mgkbuCHzuUCZfDBHUnw/view?usp=drivesdk"},
        {"Colección": "Psy", "Modelo": "Psy 04", "URL": "https://drive.google.com/file/d/1VMM8e_YXKiZGTHbZsFeLzL-Z_r0uCvTS/view?usp=drivesdk"},
        {"Colección": "Psy", "Modelo": "Psy 03", "URL": "https://drive.google.com/file/d/16_IlcfYuRiIQv5ckkpIM2tGDuf73Qggq/view?usp=drivesdk"},
        {"Colección": "Psy", "Modelo": "Psy 02", "URL": "https://drive.google.com/file/d/1QcdemBtzq4zC8QFmcrtdt_5vmJpTA0Dm/view?usp=drivesdk"},
        {"Colección": "Psy", "Modelo": "Psy 01", "URL": "https://drive.google.com/file/d/1lV7F7e7rnlnvJZcL-uipp050GEYl2w_A/view?usp=drivesdk"},
        # Amiri
        {"Colección": "Amiri", "Modelo": "Amiri VI", "URL": "https://drive.google.com/file/d/1HFM2iIF81o-iUU_uUOllmuDg1E3jNuSP/view?usp=drivesdk"},
        {"Colección": "Amiri", "Modelo": "Amiri V", "URL": "https://drive.google.com/file/d/1UlP7dK8pfKUHS5yTEO45qoXeL28SB7gn/view?usp=drivesdk"},
        {"Colección": "Amiri", "Modelo": "Amiri IV", "URL": "https://drive.google.com/file/d/1Tprtw4hQK69sEaLUuUGwv13t-vGnMDZv/view?usp=drivesdk"},
        {"Colección": "Amiri", "Modelo": "Amiri III", "URL": "https://drive.google.com/file/d/1Jt3vfBcWiAdro0L-hTjIFmRmEDXMmk99/view?usp=drivesdk"},
        {"Colección": "Amiri", "Modelo": "Amiri II", "URL": "https://drive.google.com/file/d/1_lSQEmgNWcHW0oscEDlLUaqK6ixWhMP8/view?usp=drivesdk"},
        {"Colección": "Amiri", "Modelo": "Amiri I", "URL": "https://drive.google.com/file/d/1fg88GfmNTBYoqMnWmrZ0fRuAR_79UZZo/view?usp=drivesdk"},
        # Secretos de la naturaleza
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 11", "URL": "https://drive.google.com/file/d/1zsETwWwvv9HbVAmSIvAUYZP3cPWVokCX/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 10", "URL": "https://drive.google.com/file/d/1zbSM-RU6UGd2YDwwOLM6pDCrrjBGG8uN/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 09", "URL": "https://drive.google.com/file/d/1t30QRQLA-b8Ga6d7eW5iNa19gWAf2CJj/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 08", "URL": "https://drive.google.com/file/d/1aOc2-YpqFXc3M2Brj9jlsAemkD5ZAiij/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 07", "URL": "https://drive.google.com/file/d/1tf5FIW4RtoDigna5zqmPJNMdchL7i_6y/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 06", "URL": "https://drive.google.com/file/d/1y9YThfTQ8zlAiF6A43g_ftUXDB0KdQHx/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 05", "URL": "https://drive.google.com/file/d/1z72uDBAlkQWO-uaS_czzOk_Af746V0-P/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 04", "URL": "https://drive.google.com/file/d/10JyWxrXvETOn2MXFL6D5lhks0kfdDyQY/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 03", "URL": "https://drive.google.com/file/d/1Uklgv6FtzPxRfTx4CbFSxs1pklTii65q/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 02", "URL": "https://drive.google.com/file/d/15o3Cne_DCfEc-atQIn4Z64mHIOcPFupt/view?usp=drivesdk"},
        {"Colección": "Secretos de la naturaleza", "Modelo": "Secretos 01", "URL": "https://drive.google.com/file/d/17eiFYcllPoY4bokdmkg-AYRylIb6TCh4/view?usp=drivesdk"},
        # Varios
        {"Colección": "varios", "Modelo": "Balón", "URL": "https://drive.google.com/file/d/1Hqvwl6pKZvr7pd8PlZ611JUknkZ-U6Ji/view?usp=drivesdk"},
        {"Colección": "varios", "Modelo": "Fut", "URL": "https://drive.google.com/file/d/1oHrCq_U3I5-Pym6zeiutnA0elQ46aSwi/view?usp=drivesdk"},
        {"Colección": "varios", "Modelo": "Gol", "URL": "https://drive.google.com/file/d/19MaElY7FoWDDP9IqkNROmlcsicC335Pw/view?usp=drivesdk"},
        {"Colección": "varios", "Modelo": "Filosofía", "URL": "https://drive.google.com/file/d/1qUZDk6msLsBUGGOKTaRnXDZgms0__EXG/view?usp=drivesdk"},
    ]
    return pd.DataFrame(datos)

df_catalogo = cargar_datos()

# Número corregido incluyendo el código de país de México (+52) y sin espacios ni símbolos
TELEFONO_WHATSAPP = "525629088870"

if "carrito" not in st.session_state:
    st.session_state.carrito = {}

# Función para limpiar el pedido borrando tanto el carrito como las claves de los inputs
def limpiar_pedido():
    # Eliminamos las llaves guardadas por los st.number_input
    for key in list(st.session_state.keys()):
        if key.startswith("input_"):
            st.session_state[key] = 0.0
    # Limpiamos el carrito principal
    st.session_state.carrito = {}

st.title("📱 Catálogo de Sublimados Interactivos")
st.write("Selecciona tus modelos de la lista, define los metros que necesitas y envía tu pedido directo por WhatsApp.")

# --- DISEÑO EN COLUMNAS ---
col_izquierda, col_derecha = st.columns([2, 1])

with col_izquierda:
    st.header("✨ Modelos Disponibles")
    
    colecciones = ["Todas"] + list(df_catalogo["Colección"].unique())
    coleccion_seleccionada = st.selectbox("Filtrar por Colección:", colecciones)
    
    if coleccion_seleccionada != "Todas":
        df_filtrado = df_catalogo[df_catalogo["Colección"] == coleccion_seleccionada]
    else:
        df_filtrado = df_catalogo

    for index, fila in df_filtrado.iterrows():
        key_id = f"{fila['Colección']}_{fila['Modelo']}"
        
        with st.container(border=True):
            col_img, col_info, col_accion = st.columns([1.2, 1.8, 1])
            
            with col_img:
                url_directa = obtener_url_imagen_drive(fila['URL'])
                st.image(url_directa, use_container_width=True)
                
            with col_info:
                st.subheader(f"{fila['Modelo']}")
                st.caption(f"Colección: {fila['Colección']}")
                
            with col_accion:
                registro_actual = st.session_state.carrito.get(key_id, 0.0)
                if isinstance(registro_actual, dict):
                    valor_actual = float(registro_actual.get("Metros", 0.0))
                else:
                    valor_actual = float(registro_actual)
                
                metros = st.number_input(
                    "Metros:", 
                    min_value=0.0, 
                    max_value=500.0, 
                    value=valor_actual, 
                    step=0.5, 
                    key=f"input_{key_id}"
                )
                
                if metros > 0:
                    st.session_state.carrito[key_id] = {
                        "Colección": fila["Colección"],
                        "Modelo": fila["Modelo"],
                        "Metros": metros
                    }
                elif key_id in st.session_state.carrito and metros == 0:
                    del st.session_state.carrito[key_id]

with col_derecha:
    st.header("🛒 Tu Pedido")
    
    if not st.session_state.carrito:
        st.info("Sin modelos seleccionados. Ajusta los metros en el panel izquierdo.")
    else:
        resumen_datos = []
        texto_whatsapp = "¡Hola! Quisiera realizar un pedido con el siguiente detalle:\n\n"
        total_metros = 0
        
        for k, v in st.session_state.carrito.items():
            resumen_datos.append({
                "Modelo": v["Modelo"],
                "Colección": v["Colección"],
                "Metros": f"{v['Metros']} m"
            })
            texto_whatsapp += f"• *{v['Colección']} - {v['Modelo']}*: {v['Metros']} metros\n"
            total_metros += v["Metros"]
            
        df_resumen = pd.DataFrame(resumen_datos)
        st.table(df_resumen)
        
        st.metric(label="Total Metros Seleccionados", value=f"{total_metros} m")
        
        # Usamos on_click llamando a la función que limpia todo correctamente
        st.button("Limpiar todo el Pedido", on_click=limpiar_pedido)
            
        st.write("---")
        
        # Codificación correcta del texto para la URL
        texto_codificado = urllib.parse.quote(texto_whatsapp)
        enlace_wa = f"https://wa.me/{TELEFONO_WHATSAPP}?text={texto_codificado}"
        
        # Implementación nativa de Streamlit
        st.link_button(
            "🚀 Solicitar pedido por WhatsApp", 
            enlace_wa, 
            use_container_width=True
        )
