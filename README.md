# Polyphonic Guitar Transcription to Tablature

CENG 481 – Artificial Neural Networks
Yusuf Çağlayan (202211016) · Eren Civil (202111081)

## Proje Tanımı

Bu proje, polifonik gitar kayıtlarını otomatik olarak tablatüre dönüştüren bir sistem geliştirmeyi amaçlamaktadır. Ses kaydı Constant-Q Transform (CQT) ile zaman-frekans temsiline çevrilir ve bir CRNN (Convolutional Recurrent Neural Network) modeli, her zaman diliminde hangi telde hangi perdenin çalındığını tahmin eder.

Standart nota transkripsiyonundan farklı olarak gitarda aynı nota birden fazla tel ve perde kombinasyonuyla çalınabilir. Bu nedenle sistem, tel/perde atamasında çalınabilirliği (playability) de göz önünde bulundurarak gerçekçi ve elle çalınabilir tablatürler üretmeyi hedefler. Model, GuitarSet veri seti üzerinde eğitilip değerlendirilmektedir.   