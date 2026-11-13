# Polyphonic Guitar Transcription to Tablature

CENG 481 – Artificial Neural Networks  
Yusuf Çağlayan (202211016) · Eren Civil (202111081)

Gitar kaydını dinleyip tablatura (tel + perde) üreten bir CRNN modeli ve
playability-aware string/fret ataması.

## Kurulum

```bash
git clone https://github.com/<kullanici>/guitar-tab-transcription.git
cd guitar-tab-transcription
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Klasör yapısı

```
configs/          Ön işleme ve eğitim ayarları (YAML)
data/raw/         GuitarSet (git'e eklenmez)
data/processed/   Önceden hesaplanmış CQT ve etiketler (git'e eklenmez)
notebooks/        Keşif ve görselleştirme
scripts/          Çalıştırılabilir scriptler (indirme, ön işleme, eğitim)
src/data/         Dataset, CQT, etiket üretimi
src/models/       TabCNN, CRNN
src/eval/         Metrikler, playability ölçümleri
tests/            Sanity check'ler
```

## Yol haritası

- [ ] Hafta 1–2: Data pipeline (CQT, etiketler, player split) · Metrikler + Basic Pitch
- [ ] Hafta 3–4: TabCNN baseline · Tab export (MusicXML) → **uçtan uca çalışan sistem**
- [ ] Hafta 5–6: CRNN + onset head · Augmentation, telefon test seti
- [ ] Hafta 7–8: Playability loss · Hand-movement decoding
- [ ] Hafta 9–10: Demo, rapor, sunum
