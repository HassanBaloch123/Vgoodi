import random
android_versions = ["4.4.4", "5.0.2", "6.0.1", "7.1.1", "8.0.0", "9", "10", "11", "12"]
model_devices = ["Nexus 5", "Galaxy S7", "Pixel 2", "OnePlus 6T", "Galaxy Note 10", "Pixel 6 Pro", "Galaxy S21", "OnePlus 9 Pro", "Xperia 1 III", "Mi 11 Ultra"]
build_devices = ["KTU84P", "LRX22G", "MMB29K", "N4F26I", "PPR1.180610.011", "RP1A.200720.012", "RQ3A.210705.001", "RP1A.201005.001.A1", "A1000_11_OTA_028_all_200702221", "N2G48B"]
versi_chromes = ["86.0.4240.75", "89.0.4389.82", "93.0.4577.63", "97.0.4692.99", "99.0.4844.51", "102.0.4476.86"]
languages = ["en_US", "fr_FR", "de_DE", "it_IT", "es_ES", "pt_BR", "zh_CN", "ru_RU", "ja_JP", "ar_SA"]
versi_apps = ["336.0.0.20.117", "356.0.0.9.116", "402.0.0.0.7", "425.0.0.24.120", "464.0.0.7.120", "503.0.0.22.120", "521.0.0.28.220"]
simcards = ["310260", "310410", "310120", "310030", "310070", "310590", "310900", "311030", "310260", "310170"]
merk_devices = ["samsung", "motorola", "xiaomi", "nokia", "lg", "oppo", "vivo", "realme", "lenovo", "asus"]
brand_devices = ["SM-N960U", "XT1962-4", "M2003J15SC", "TA-1105", "LM-Q730", "CPH2201", "V2061A", "RMX3366", "K13a40", "ZC554KL"]
cpu_devices = ["SM8150", "SM8250", "MT6768", "SM7125", "SM8250", "SM7325", "SM6115", "SM4250", "SM4350", "SM6125"]
large_devices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

android_version = random.choice(android_versions)
model_device = random.choice(model_devices)
build_device = random.choice(build_devices)
versi_chrome = random.choice(versi_chromes)
language = random.choice(languages)
versi_app = random.choice(versi_apps)
simcard = random.choice(simcards)
merk_device = random.choice(merk_devices)
brand_device = random.choice(brand_devices)
cpu_device = random.choice(cpu_devices)
large_device = random.choice(large_devices)

user_agent = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/Messenger;FBAV/{versi_chrome};FBPN/com.facebook.orca;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/{large_device};]"

print(user_agent)
