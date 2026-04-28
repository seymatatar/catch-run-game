## 🕹️ [Oyunu İndirmek İçin Tıklayın (Windows .zip)](https://github.com/seymatatar/catch-run-game/releases/download/v1.0.0/Catch-Run-Game-v1.0.zip)

# Catch-Run Game 🎮
Catch-Run, Python kullanılarak geliştirilmiş, donanım hızlandırmalı grafiklere sahip arcade tarzı bir hayatta kalma oyunudur. Bu proje, bir yazılımın fikir aşamasından son kullanıcı dağıtımına (executable) kadar olan tüm süreçlerini deneyimlemek amacıyla geliştirilmiştir.

## 🕹️ Nasıl Oynanır? (Gameplay)
Catch-Run, reflekslerinize ve stratejik hareketlerinize dayanan hızlı tempolu bir oyundur:
1. **Kontrol:** Klavyenin WASD tuşlarını kullanarak bir **üçgeni** kontrol edersiniz.
2. **Kaçış:** Ekrana rastgele ama akıllıca spawn olan **tehlikeli siyah karelerden** kaçmalısınız. Her saniye oyun zorlaşır ve karelerin sayısı değişkendir.
3. **Puan Toplama:** Hayatta kalmak için sadece kaçmak yetmez! Ekranda beliren **güvenli (safe) hedefleri** "patlatarak" puanınızı artırmalısınız.Unutmayın puanınızın artıp azalma durumuna göre hızınız da değişir.
4. **Alan Yönetimi:** Spawn algoritması oyuncunun bulunduğu konumu sürekli kontrol eder, bu yüzden kendinize kaçacak güvenli alanlar (safe zones) oluşturmak için dinamik hareket etmelisiniz.
5. **Amaç:** En yüksek skoru yaparak en uzun süre hayatta kalmak!

   
## 🚀 Teknik Özellikler
- **Grafik Motoru:** `ModernGL` kütüphanesi kullanılarak GPU tabanlı render işlemleri gerçekleştirilmiştir.
- **Oyun Mantığı:** `Pygame` altyapısı ile etkinlik yönetimi ve ses kontrolü sağlanmıştır.
- **Dinamik Spawn Sistemi:** Düşman ve güvenli bölgelerin konumu, oyuncunun mevcut koordinatlarına ve ekran alan hesaplamalarına göre anlık olarak belirlenir.
- **Collision Detection:** Hassas çarpışma algılama algoritmaları ile oyun içi etkileşimler yönetilir.
- **Deployment:** `PyInstaller` ile tüm kütüphane bağımlılıkları derlenerek taşınabilir bir `.exe` haline getirilmiştir.


## 🛠️ Kullanılan Teknolojiler
- **Dil:** Python 3.13
- **Grafik:** ModernGL (Vertex & Fragment Shaders)
- **Multimedya:** Pygame (Sound & Event Loop)
- **Versiyon Kontrol:** Git & GitHub

## 📝 Mühendislik Notları
Proje geliştirilirken özellikle şu alanlara odaklanılmıştır:
1. **Alan Hesaplama:** Nesnelerin ekran sınırları içerisinde kalması ve birbirleriyle çakışmaması için matematiksel modeller kullanılmıştır.
2. **Optimizasyon:** Render yükü CPU'dan GPU'ya taşınarak akıcı bir oyun deneyimi hedeflenmiştir.
3. **Müzik ve Ses:** Oyun içi atmosferi desteklemek amacıyla telif haklarına uygun 8-bit ses efektleri entegre edilmiştir.

## 📜 Lisans (Credits)
- **Müzik:** Bensound - Benjamin Tissot (Lisans Kodu: BMV1J1SSBKF8X8QR)
- **Ses Efektleri:** sfxr.me
  
<img width="400" height="400" alt="catch-run-game" src="https://github.com/user-attachments/assets/400967c1-05e8-46cb-aea9-5202c7045ff8" />
