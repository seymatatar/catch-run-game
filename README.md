# 🎮 Catch-Run Game

<p align="center">
  <a href="#-english">English</a> | 
  <a href="#-turkish">Turkish</a>
</p>

---

## 🕹️ [Click to Download for Windows (.zip)](https://github.com/seymatatar/catch-run-game/releases/download/v1.0.0/Catch-Run-Game-v1.0.zip)

---

## 🇺🇸 English

Catch-Run is an arcade-style survival game developed using Python, featuring hardware-accelerated graphics. This project was developed to experience the entire software lifecycle, from the initial idea phase to end-user deployment (executable).

### 🕹️ How to Play?
Catch-Run is a fast-paced game based on reflexes and strategic movement:
1. **Controls:** Use the **WASD** keys to control your **triangle**.
2. **Dodge:** Evade the **dangerous black squares** that spawn randomly but intelligently. The game gets harder every second, and the number of squares varies.
3. **Collect Points:** Survival isn't enough! You must "pop" the **safe targets** that appear on the screen to increase your score. Note that your speed changes based on whether your score increases or decreases.
4. **Area Management:** The spawn algorithm constantly checks the player's position, so you must move dynamically to create safe zones for yourself.
5. **Goal:** Survive as long as possible and achieve the highest score!

### 🚀 Technical Features
- **Graphics Engine:** GPU-based rendering using the `ModernGL` library.
- **Game Logic:** Event management and sound control provided by the `Pygame` framework.
- **Dynamic Spawn System:** The positions of enemies and safe zones are determined in real-time based on the player's current coordinates and screen calculations.
- **Collision Detection:** In-game interactions are managed with precise collision detection algorithms.
- **Deployment:** All library dependencies were compiled using `PyInstaller` to create a portable `.exe` file.

### 🛠️ Tech Stack
- **Language:** Python 3.13
- **Graphics:** ModernGL (Vertex & Fragment Shaders)
- **Multimedia:** Pygame (Sound & Event Loop)
- **Version Control:** Git & GitHub

### 📝 Engineering Notes
The development focused on the following areas:
1. **Spatial Calculation:** Mathematical models were used to ensure objects remain within screen boundaries and do not overlap.
2. **Optimization:** The rendering load was shifted from the CPU to the GPU for a fluid gaming experience.
3. **Audio:** 8-bit sound effects were integrated to support the retro-arcade atmosphere.

### 📜 Credits & License
- **Music:** Bensound - Benjamin Tissot (License Code: BMV1J1SSBKF8X8QR)
- **Sound Effects:** sfxr.me
- **License:** This project is provided under the **MIT License**.

---

## 🇹🇷 Turkish

Catch-Run, Python kullanılarak geliştirilmiş, donanım hızlandırmalı grafiklere sahip arcade tarzı bir hayatta kalma oyunudur. Bu proje, bir yazılımın fikir aşamasından son kullanıcı dağıtımına (executable) kadar olan tüm süreçlerini deneyimlemek amacıyla geliştirilmiştir.

### 🕹️ Nasıl Oynanır?
Catch-Run, reflekslerinize ve stratejik hareketlerinize dayanan hızlı tempolu bir oyundur:
1. **Kontrol:** Klavyenin **WASD** tuşlarını kullanarak bir **üçgeni** kontrol edersiniz.
2. **Kaçış:** Ekrana rastgele ama akıllıca spawn olan **tehlikeli siyah karelerden** kaçmalısınız. Her saniye oyun zorlaşır ve karelerin sayısı değişkendir.
3. **Puan Toplama:** Hayatta kalmak için sadece kaçmak yetmez! Ekranda beliren **güvenli (safe) hedefleri** "patlatarak" puanınızı artırmalısınız. Puanınızın durumuna göre hızınızın da değişeceğini unutmayın.
4. **Alan Yönetimi:** Spawn algoritması oyuncunun konumunu sürekli kontrol eder, bu yüzden güvenli alanlar oluşturmak için dinamik hareket etmelisiniz.
5. **Amaç:** En yüksek skoru yaparak en uzun süre hayatta kalmak!

### 🚀 Teknik Özellikler
- **Grafik Motoru:** `ModernGL` kütüphanesi kullanılarak GPU tabanlı render işlemleri gerçekleştirilmiştir.
- **Oyun Mantığı:** `Pygame` altyapısı ile etkinlik yönetimi ve ses kontrolü sağlanmıştır.
- **Dinamik Spawn Sistemi:** Düşman ve güvenli bölgelerin konumu, oyuncunun koordinatlarına ve ekran alan hesaplamalarına göre anlık belirlenir.
- **Çarpışma Algılama:** Hassas algoritmalar ile oyun içi etkileşimler yönetilir.
- **Dağıtım:** `PyInstaller` ile tüm bağımlılıklar derlenerek taşınabilir bir `.exe` haline getirilmiştir.

### 🛠️ Kullanılan Teknolojiler
- **Dil:** Python 3.13
- **Grafik:** ModernGL (Vertex & Fragment Shaders)
- **Multimedya:** Pygame (Sound & Event Loop)
- **Versiyon Kontrol:** Git & GitHub

### 📝 Mühendislik Notları
1. **Alan Hesaplama:** Nesnelerin ekran sınırları içerisinde kalması ve çakışmaması için matematiksel modeller kullanılmıştır.
2. **Optimizasyon:** Render yükü CPU'dan GPU'ya taşınarak akıcı bir deneyim hedeflenmiştir.
3. **Müzik ve Ses:** Atmosferi desteklemek amacıyla 8-bit ses efektleri entegre edilmiştir.

### 📜 Lisans ve Teşekkür
- **Müzik:** Bensound - Benjamin Tissot (Lisans Kodu: BMV1J1SSBKF8X8QR)
- **Ses Efektleri:** sfxr.me
- **Lisans:** Bu proje **MIT Lisansı** altında sunulmaktadır.

---

<p align="center">
  <img width="400" height="400" alt="catch-run-game" src="https://github.com/user-attachments/assets/400967c1-05e8-46cb-aea9-5202c7045ff8" />
</p>
