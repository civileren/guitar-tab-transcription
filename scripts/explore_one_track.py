import mirdata

dataset = mirdata.initialize("guitarset", data_home="data/raw/guitarset")
track = dataset.choice_track()  # rastgele bir kayit sec

print("Kayit adi:  ", track.track_id)
print("Oyuncu:     ", track.player_id)
print("Tur:        ", track.mode, "/", track.style)
print("Tempo:      ", track.tempo)
print("Ses dosyasi:", track.audio_mic_path)

print("\nHer telde kac nota var:")
for tel, notalar in track.notes.items():
    if notalar is None:
        print(f"  {tel} teli: 0 nota (hic calinmamis)")
    else:
        print(f"  {tel} teli: {len(notalar.intervals)} nota")