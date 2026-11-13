import mirdata

# GuitarSet'i data/raw/guitarset klasörüne indir
dataset = mirdata.initialize("guitarset", data_home="data/raw/guitarset")

print("Indirilebilir parcalar:", list(dataset.remotes.keys()))

# Sadece etiketler + mikrofon kaydi (~700 MB)
dataset.download(partial_download=["annotations", "audio_mic"])

print("Indirme bitti. Kontrol ediliyor...")
dataset.validate()
print("Toplam kayit sayisi:", len(dataset.track_ids))