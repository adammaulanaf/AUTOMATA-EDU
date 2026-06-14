import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN MELEBAR PENUH (WIDE)
# ==========================================
st.set_page_config(
    page_title="Dunia Belajar Sobat Cilik 🎓", 
    page_icon="🎈", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Inisialisasi status halaman aktif agar bisa berpindah menu
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "Beranda"

# Inisialisasi skor bintang pemain jika belum ada
if "bintang_skor" not in st.session_state:
    st.session_state.bintang_skor = 0

# ==========================================
# 2. DATA HUB MATA PELAJARAN & GAME INTERAKTIF
# ==========================================
matkul_data = {
    "Berhitung Seru": {
        "emoji": "🧮", 
        "desc": "Belajar tambah-tambahan, perkalian kilat, dan tebak angka ajaib lewat game seru!",
        "materi": (
            "• **Penjumlahan Ajaib:** Yuk bantu Milo si kelinci menghitung wortelnya! $2 + 3 = 5$ wortel manis! 🥕\n\n"
            "• **Tebak Bangun Datar:** Bentuk pizza itu lingkaran, kalau atap rumah itu segitiga, dan buku tulis itu persegi panjang! 🍕🏠📖\n\n"
            "• **Perkalian Kilat Jari:** Perkalian angka 9 itu ajaib lho! Coba lipat jari keempatmu dari kiri, taraaa! $4 \\times 9 = 36$! 🖐️✨\n\n"
            "• **Mengenal Jam & Waktu:** Jarum pendek menunjukkan jam, jarum panjang menunjukkan menit. 🎒⏰"
        ),
        "pertanyaan": "Milo si kelinci punya 4 wortel, lalu diberi lagi oleh ibunya 5 wortel. Berapa jumlah wortel Milo sekarang?",
        "pilihan": ["7 Wortel", "8 Wortel", "9 Wortel", "10 Wortel"],
        "jawaban_benar": "9 Wortel",
        "pesan_sukses": "Hebat! Kamu pinter berhitung! 🥕 Tambah 10 Bintang! ✨"
    },
    "Penjelajah Dunia (IPA)": {
        "emoji": "🦁", 
        "desc": "Mengenal hewan purba, sistem tata surya, dan rahasia tumbuhan ajaib di sekitar kita.",
        "materi": (
            "• **Dunia Hewan:** Herbivora (Sapi 🐄), Karnivora (Singa 🦁), dan Omnivora (Ayam 🐓)!\n\n"
            "• **Sistem Tata Surya:** Bumi kita adalah planet ketiga yang berputar mengelilingi Matahari. Planet bercincin indah namanya Saturnus! 🌍🪐☀️\n\n"
            "• **Bagian Tumbuhan:** Akar mencari air, batang menopang, daun memasak makanan (fotosintesis), dan bunga menjadi buah! 🌳🍎\n\n"
            "• **Wujud Benda:** Ada benda padat (es batu 🧊), cair (air susu 🥛), dan gas (balon 🎈)."
        ),
        "pertanyaan": "Planet di tata surya kita yang terkenal memiliki cincin raksasa yang sangat indah adalah...",
        "pilihan": ["Merkurius", "Mars", "Saturnus", "Bumi"],
        "jawaban_benar": "Saturnus",
        "pesan_sukses": "Luar biasa, sang Penjelajah Antariksa! 🪐 Tambah 10 Bintang! ✨"
    },
    "Bahasa & Cerita": {
        "emoji": "📚", 
        "desc": "Membaca dongeng petualangan nusantara, menyusun kalimat sakti, dan kuis kosakata.",
        "materi": (
            "• **Membaca Dongeng:** Kisah Kancil yang cerdik mengelabui Buaya yang sedang kelaparan di sungai. 🐊\n\n"
            "• **Tiga Kata Sakti:** Selalu gunakan kata 'Tolong', 'Maaf', 'Terima Kerja', dan 'Terima Kasih'! 🌟\n\n"
            "• **Struktur Kalimat (SPOK):** Contoh: Budi (S) membaca (P) buku (O) di kelas (K). 📝\n\n"
            "• **Puisi Anak Indah:** Belajar membaca puisi dengan ekspresi penuh penjiwaan. 🌅"
        ),
        "pertanyaan": "Kata sakti apa yang harus kita ucapkan setelah kita diberikan bantuan oleh orang lain?",
        "pilihan": ["Tolong", "Terima Kasih", "Permisi", "Maaf"],
        "jawaban_benar": "Terima Kasih",
        "pesan_sukses": "Setuju! Kamu anak yang sopan dan baik budi! 💖 Tambah 10 Bintang! ✨"
    },
    "Kreatif Digital": {
        "emoji": "🎨", 
        "desc": "Belajar menggambar pixel di komputer, logika blok warna, dan teknologi masa depan.",
        "materi": (
            "• **Mewarnai Pixel:** Gambar digital di komputer terbentuk dari kotak-kotak kecil bernama pixel. 👾\n\n"
            "• **Logika Robot:** Perintah arah berturut-turut (Maju -> Belok Kanan) agar robot berjalan lancar. 🤖\n\n"
            "• **Internet Sehat:** Internet adalah jendela dunia, gunakan didampingi orang tua! 💻👨‍👩‍👧\n\n"
            "• **Bikin Animasi Sederhana:** Menggabungkan gambar agar terlihat bergerak hidup! 🎬"
        ),
        "pertanyaan": "Kotak-kotak kecil berwarna yang menyusun sebuah gambar di dalam layar komputer disebut...",
        "pilihan": ["Pixel", "Kotak game", "Baterai", "Robot"],
        "jawaban_benar": "Pixel",
        "pesan_sukses": "Keren! Calon Programmer masa depan nih! 👾 Tambah 10 Bintang! ✨"
    },
    "English Adventure": {
        "emoji": "🔤",
        "desc": "Petualangan seru belajar bahasa internasional, mengeja benda, dan bernyanyi lagu Inggris!",
        "materi": (
            "• **Animal Names:** Kucing itu *Cat* 🐱, anjing itu *Dog* 🐶, gajah itu *Elephant* 🐘!\n\n"
            "• **Daily Greetings:** Ucapkan *'Good Morning'* di pagi hari dan *'Good Night'* sebelum tidur! ☀️🌙\n\n"
            "• **Magic Colors:** Merah itu *Red* 🔴, Biru itu *Blue* 🔵, Kuning itu *Yellow* 🟡, Hijau itu *Green* 🟢.\n\n"
            "• **Counting 1 to 10:** *One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten!* 🖐️🖐️"
        ),
        "pertanyaan": "What is the English word for 'Kucing'? 🐱",
        "pilihan": ["Dog", "Bird", "Cat", "Elephant"],
        "jawaban_benar": "Cat",
        "pesan_sukses": "Excellent! Your English is very good! 🐱 Tambah 10 Bintang! ✨"
    },
    "Sinau Basa Jawa": {
        "emoji": "🤠",
        "desc": "Kenalan karo sato kewan, ngetung angka, lan sinau unggah-ungguh basa sing jempolan!",
        "materi": (
            "• **Arane Anak Kewan:** Anak pitik arane *Kuthuk* 🐥, anak gajah arane *Bledug* 🐘.\n\n"
            "• **Ngoko lan Krama:** Awake dhewe nggunakake *Mangan* 🍱, yen Bapak/Ibu nggunakake *Dhahar* 👴👵.\n\n"
            "• **Ngetung Siji Tekan Sopo:** Siji (Satunggal), Loro (Kalih), Telu (Tiga), Papat (Sekawan), Limo (Gangsal).\n\n"
            "• **Tembang Dolanan:** Nyanyi bareng *'Gundhul Gundhul Pacul'* utawa *'Mentok Mentok'*. 🎶"
        ),
        "pertanyaan": "Ing basa Jawa, arane utawa jenenge anak pitik sing isih cilik lan lucu yaiku...",
        "pilihan": ["Bledug", "Kuthuk", "Cemeng", "Pedhet"],
        "jawaban_benar": "Kuthuk",
        "pesan_sukses": "Jan jempolan tenan! Pintar banget boso Jowone! 🐥 Tambah 10 Bintang! ✨"
    },
    "Kapten PJOK (Olahraga)": {
        "emoji": "⚽",
        "desc": "Biar badan sehat, kuat, dan lincah! Yuk pelajari trik senam, lari cepat, dan oper bola!",
        "materi": (
            "• **Gerak Lokomotor:** Gerakan berpindah tempat, contoh melompat dan berlari! 🏃‍♂️\n\n"
            "• **Gerak Non-Lokomotor:** Olahraga di tempat, contoh memutar lengan dan menekuk lutut! 🤸\n\n"
            "• **Makanan Sehat:** Menu seimbang 4 Sehat 5 Sempurna + segelas Susu hangat! 🥛🍏\n\n"
            "• **Olahraga Beregu:** Bermain sepak bola ⚽ harus kompak bekerja sama dengan tim!"
        ),
        "pertanyaan": "Gerakan olahraga yang membuat tubuh kita berpindah dari satu tempat ke tempat lain disebut gerak...",
        "pilihan": ["Lokomotor", "Non-lokomotor", "Diam di tempat", "Tidur nyenyak"],
        "jawaban_benar": "Lokomotor",
        "pesan_sukses": "Hup! Dua! Tiga! Badanmu sehat dan kuat seperti kapten! ⚽ Tambah 10 Bintang! ✨"
    },
    "Detektif Sejarah (IPS)": {
        "emoji": "🗺️",
        "desc": "Membaca peta harta karun Indonesia, mengenal pahlawan hebat, dan budaya sabang sampai merauke.",
        "materi": (
            "• **Cinta Mata Uang Rupiah:** Mengenal Rupiah (Rp). Belajar hemat dengan menabung! 🪙🐖\n\n"
            "• **Rumah Adat Nusantara:** Rumah Gadang (Sumatra Barat), Rumah Honai bulat (Papua). 🏠\n\n"
            "• **Membaca Arah Peta:** Atas (Utara ⬆️), bawah (Selatan ⬇️), kanan (Timur ➡️), kiri (Barat ⬅️).\n\n"
            "• **Pahlawan Nasional:** Meneladani kegigihan Jenderal Sudirman dan Ibu Kartini! 🇮🇩"
        ),
        "pertanyaan": "Rumah adat tradisional yang berbentuk bulat, tidak memiliki jendela, dan berasal dari Papua bernama...",
        "pilihan": ["Rumah Gadang", "Rumah Joglo", "Rumah Honai", "Rumah Limas"],
        "jawaban_benar": "Rumah Honai",
        "pesan_sukses": "Hebat, Detektif! Kamu berhasil memecahkan teka-teki peta! 🏠 Tambah 10 Bintang! ✨"
    },
    "Sahabat Pancasila (PPKN)": {
        "emoji": "🦅",
        "desc": "Belajar jadi anak baik, menghormati teman, dan mengamalkan nilai luhur Garuda Pancasila.",
        "materi": (
            "• **Semangat Gotong Royong:** Membantu Ibu, membersihkan kelas bersama sahabat! 🧹🌱\n\n"
            "• **Sila Kedua Pancasila:** Simbol Rantai Emas ⛓️, artinya saling menyayangi sesama manusia.\n\n"
            "• **Simbol Negara:** Dasar Pancasila, lambang Burung Garuda 🦅, bendera Merah Putih 🇮🇩.\n\n"
            "• **Aturan di Rumah & Sekolah:** Merapikan tempat tidur 🛏️ dan mendengarkan guru! 🏫"
        ),
        "pertanyaan": "Apakah simbol dari Sila Kedua Pancasila yang mengajarkan kita untuk saling menyayangi?",
        "pilihan": ["Pohon Beringin", "Kepala Banteng", "Rantai Emas", "Padi dan Kapas"],
        "jawaban_benar": "Rantai Emas",
        "pesan_sukses": "Garuda Pancasila! Kamu anak baik yang berjiwa sosial tinggi! ⛓️ Tambah 10 Bintang! ✨"
    }
}

# Menyusun teks panduan materi untuk ingatan dasar Piko
konteks_materi_web = ""
for nama_mapel, isi in matkul_data.items():
    konteks_materi_web += f"\n- Mapel {nama_mapel}: {isi['desc']} Konten dasar: {isi['materi']}"

# Management State Aplikasi
if 'selected_matkul' not in st.session_state:
    st.session_state.selected_matkul = list(matkul_data.keys())[0]

# State untuk membuka/menutup jendela Chatbot Piko Melayang
if 'buka_chat_piko' not in st.session_state:
    st.session_state.buka_chat_piko = False

# State Penyimpanan Memori Chat
if 'riwayat_chat' not in st.session_state:
    st.session_state.riwayat_chat = [
        {"role": "assistant", "content": "Hai! Aku Piko 🤖 Asisten Pintarmu! Sekarang pilihanku sudah makin lengkap lho, ada Bahasa Jawa, Inggris, Olahraga, IPS, sampai PPKN! Yuk tanya apa saja ke aku! 🎒✨"}
    ]

# ==========================================
# 3. STYLING CSS KUSTOM (DIPERBAIKI AGAR TIDAK TERPOTONG)
# ==========================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght=500;700&display=swap');

        [data-testid="stHeader"] { display: none; }
        
        html, body, [data-testid="stAppViewContainer"], .stMarkdown {
            font-family: 'Quicksand', sans-serif;
            background-color: #FFFDE7; 
        }
        
        .navbar-bg {
            background: linear-gradient(135deg, #FFEB3B, #FFF176);
            padding: 10px 3%; border-bottom: 4px solid #FBC02D;
            margin-bottom: 30px; border-radius: 0 0 20px 20px;
        }

        .logo-text {
            font-family: 'Fredoka One', cursive; color: #E65100;
            font-size: 24px; margin-top: 5px;
        }
        
        div.stButton > button[key^="nav_"] {
            background: transparent !important; color: #5D4037 !important;
            font-weight: 700 !important; font-size: 16px !important;
            border: none !important; box-shadow: none !important;
            transition: all 0.2s ease !important;
        }
        div.stButton > button[key^="nav_"]:hover { color: #E65100 !important; transform: scale(1.1); }

        .hero-banner {
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), 
                              url('https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?q=80&w=1374&auto=format&fit=crop');
            background-size: cover; background-position: center; height: 260px; 
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            color: white; text-align: center; padding: 20px; border-radius: 30px; margin-bottom: 40px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1); border: 5px solid #FFA000;
        }
        .hero-title { font-family: 'Fredoka One', cursive; font-size: 40px; text-shadow: 3px 3px 0px rgba(0,0,0,0.4); margin-bottom: 10px; }
        .hero-subtitle { font-size: 18px; font-weight: bold; text-shadow: 1px 1px 5px rgba(0,0,0,0.6); max-width: 700px; }

        /* PERBAIKAN DI SINI: Ditambahkan padding-bottom dan menghapus min-height kaku agar tombol tidak melorot keluar kartu */
        .matkul-card {
            background: white; padding: 25px; padding-bottom: 15px; border-radius: 25px; box-shadow: 0 8px 0px #E0E0E0;
            border: 3px solid #CFD8DC; text-align: center; margin-bottom: 5px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .matkul-card:hover { transform: translateY(-10px) scale(1.03); box-shadow: 0 15px 0px #B0BEC5; border-color: #00E676; }
        .matkul-card h2 { font-size: 45px; margin: 0 0 10px 0; }
        .matkul-card h4 { font-family: 'Fredoka One', cursive; color: #263238; font-size: 20px; margin: 0 0 8px 0; }

        /* Style tombol hijau bawaan */
        .stButton>button {
            background: linear-gradient(145deg, #00E676, #00C853) !important; color: white !important;
            border-radius: 20px !important; border: none !important;
            font-family: 'Fredoka One', cursive !important; font-size: 16px !important;
            box-shadow: 0 5px 0px #006020 !important; transition: all 0.1s ease !important; padding: 10px 20px !important;
        }
        .stButton>button:hover { transform: translateY(3px) !important; box-shadow: 0 2px 0px #006020 !important; color: white !important; }

        [data-testid="stChatMessage"]:nth-child(even) {
            background-color: #FF8A80 !important; border-radius: 25px 25px 4px 25px !important;
            border: 3px solid #FF5252; padding: 12px; color: #FFFFFF !important; font-weight: bold;
        }
        [data-testid="stChatMessage"]:nth-child(odd) {
            background-color: #80D8FF !important; border-radius: 25px 25px 25px 4px !important;
            border: 3px solid #40C4FF; padding: 12px; color: #004D40 !important; font-weight: bold;
        }

        .chatbot-container-css {
            position: fixed; bottom: 25px; right: 25px; z-index: 99999;
            display: flex; flex-direction: column; align-items: flex-end;
        }
        
        .score-board {
            background: linear-gradient(135deg, #FF9100, #FF6D00);
            color: white; padding: 15px; border-radius: 20px;
            font-family: 'Fredoka One', cursive; text-align: center;
            font-size: 22px; box-shadow: 0 6px 0px #B26A00; margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 4. RENDER TOP NAVBAR
# ==========================================
st.markdown('<div class="navbar-bg">', unsafe_allow_html=True)
col_logo, col_space, col1, col2, col3 = st.columns([5, 2, 2.5, 2.5, 3])

with col_logo:
    st.markdown('<div class="logo-text">🚀 SOBAT CILIK ACADEMY</div>', unsafe_allow_html=True)

with col1:
    if st.button("BERANDA", key="nav_beranda", use_container_width=True):
        st.session_state.halaman_aktif = "Beranda"
        st.rerun()

with col2:
    if st.button("PILIH GAME", key="nav_game", use_container_width=True):
        st.session_state.halaman_aktif = "Pilih Game"
        st.rerun()

with col3:
    if st.button("RANGKUMAN MATERI", key="nav_juara", use_container_width=True):
        st.session_state.halaman_aktif = "Juara Kelas"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# 5. LOGIKA FILTER PERPINDAHAN HALAMAN MENU
# ==========================================

# --- HALAMAN 1: BERANDA ---
if st.session_state.halaman_aktif == "Beranda":
    st.markdown("""
        <div class="hero-banner">
            <div class="hero-title">✨ TAMAN BERMAIN & BELAJAR ✨</div>
            <div class="hero-subtitle">Kumpulkan bintang nilaimu, baca cerita seru, dan ikuti kuis berhadiah lencana keren! 👑🏆</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="score-board">⭐ Total Bintang Prestasimu: {st.session_state.bintang_skor} Bintang! ⭐</div>', unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #E65100; font-family: \"Fredoka One\", cursive;'>Selamat Datang di Beranda Utama! 👋</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #5D4037; font-size: 18px; font-weight: bold;'>Yuk, klik menu 🎮 PILIH GAME di atas untuk mulai bermain kuis dan mengumpulkan hadiah bintang bersama Piko!</p>", unsafe_allow_html=True)


# --- HALAMAN 2: PILIH GAME (RE-DESIGNED FIX) ---
elif st.session_state.halaman_aktif == "Pilih Game":
    st.markdown(f'<div class="score-board">⭐ Kantong Bintangmu: {st.session_state.bintang_skor} Bintang ⭐</div>', unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #E65100; font-family: \"Fredoka One\", cursive;'>🎮 Pilih Petualangan Belajarmu!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #5D4037; font-weight: bold; font-size: 18px; margin-bottom: 35px;'>Klik tombol hijau di bawah kartu untuk membuka Arena Bermain!</p>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, (name, info) in enumerate(matkul_data.items()):
        with cols[idx % 3]: 
            # Kartu Putih HTML
            st.markdown(f"""
                <div class="matkul-card">
                    <h2>{info['emoji']}</h2>
                    <h4>{name}</h4>
                    <p style="margin:0; color:#5D4037; font-size:14px; font-weight:500; line-height:1.4;">{info['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # PERBAIKAN: Tombol dipisahkan dengan kontainer kecil agar posisinya stabil di luar grid HTML kaku dan 100% aman diklik!
            with st.container():
                if st.button("Mainkan Yuk! ➔", use_container_width=True, key=f"btn_{idx}"):
                    st.session_state.selected_matkul = name
                    st.rerun()
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br><hr style='border: 2px dashed #FBC02D;'><br>", unsafe_allow_html=True)

    # =============== ARENA PERMAINAN AKTIF ===============
    selected = st.session_state.selected_matkul
    game_now = matkul_data[selected]
    
    st.markdown(f"<h3 style='color:#E65100; font-family:\"Fredoka One\", cursive; text-align:center;'>🎯 ARENA GAME: Pelajaran {selected} {game_now['emoji']}</h3>", unsafe_allow_html=True)

    belajar_col1, belajar_col2 = st.columns([1, 1], gap="large")
    
    with belajar_col1:
        st.markdown("<div style='background-color:#E8F5E9; padding:12px 20px; border-left: 6px solid #4CAF50; border-radius:15px; margin-bottom:15px;'><h5 style='margin:0; color:#2E7D32; font-family: \"Fredoka One\", cursive;'>📜 Lembar Kisi-Kisi Catatan</h5></div>", unsafe_allow_html=True)
        st.info(game_now["materi"])

    with belajar_col2:
        st.markdown("<div style='background-color:#E1F5FE; padding:12px 20px; border-left: 6px solid #0288D1; border-radius:15px; margin-bottom:15px;'><h5 style='margin:0; color:#01579B; font-family: \"Fredoka One\", cursive;'>🎮 Kuis Tantangan Seru</h5></div>", unsafe_allow_html=True)
        
        st.write(f"**Pertanyaan:** {game_now['pertanyaan']}")
        pilihan_user = st.radio("Pilih jawaban yang menurutmu benar ya:", game_now["pilihan"], key=f"quiz_radio_{selected}")
        
        if st.button("Kirim Jawaban 🚀", key=f"submit_quiz_{selected}"):
            if pilihan_user == game_now["jawaban_benar"]:
                st.balloons()
                st.success(game_now["pesan_sukses"])
                st.session_state.bintang_skor += 10
            else:
                st.error("Yaaa, jawabannya belum tepat. Coba baca 'Lembar Kisi-Kisi' di sebelah kiri dan tebak lagi! Kamu pasti bisa! 💪🌟")


# --- HALAMAN 3: RANGKUMAN MATERI ---
elif st.session_state.halaman_aktif == "Juara Kelas":
    st.markdown("<h2 style='text-align: center; color: #E65100; font-family: \"Fredoka One\", cursive;'>📚 Ensiklopedia Catatan Pintar</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #5D4037; font-weight: bold; font-size: 18px; margin-bottom: 35px;'>Semua rangkuman isi materi mapel berkumpul di sini untuk kamu pelajari ulang! 🌟</p>", unsafe_allow_html=True)
    
    for name, info in matkul_data.items():
        with st.container():
            with st.expander(f"{info['emoji']} Pembahasan Lengkap: {name}", expanded=False):
                col_materi_kiri, col_materi_kanan = st.columns([2, 1])
                
                with col_materi_kiri:
                    st.markdown(f"<h4 style='color: #E65100;'>📌 Inti Pelajaran</h4>", unsafe_allow_html=True)
                    st.info(info["materi"])
                    
                with col_materi_kanan:
                    st.markdown(f"<h4 style='color: #2E7D32;'>💡 Sekilas Info</h4>", unsafe_allow_html=True)
                    st.success(f"**Deskripsi:**\n{info['desc']}")
                    if st.button(f"Mainkan Game {info['emoji']}", key=f"rangkum_{name}", use_container_width=True):
                        st.session_state.selected_matkul = name
                        st.session_state.halaman_aktif = "Pilih Game"
                        st.rerun()
            st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
            
    st.snow()


# ==========================================
# 6. LOGIKA MAHLUK PIKO (VERSI CHATBOT SIDEBAR)
# ==========================================
st.markdown('<div class="chatbot-container-css">', unsafe_allow_html=True)
with st.container():
    col_kosong, col_tombol = st.columns([8, 2])
    with col_tombol:
        if st.button("🤖\nPIKO", key="piko_floating_avatar", use_container_width=True):
            st.session_state.buka_chat_piko = not st.session_state.buka_chat_piko
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.buka_chat_piko:
    with st.sidebar:
        st.markdown("<h2 style='font-family:\"Fredoka One\", cursive; color:#E65100;'>🤖 Robot Piko AI</h2>", unsafe_allow_html=True)
        st.write("Tanyakan materi sekolah atau game apa saja ke Piko!")
        
        if st.button("🧹 Bersihkan Riwayat Chat", use_container_width=True):
            st.session_state.riwayat_chat = []
            st.rerun()
            
        st.write("---")
        
        for msg in st.session_state.riwayat_chat:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                
        tanya_anak = st.chat_input("Tanya Piko di sini ya...")
        
        if tanya_anak:
            st.session_state.riwayat_chat.append({"role": "user", "content": tanya_anak})
            tanya_lower = tanya_anak.lower()
            jawaban_piko = ""
            
            try:
                from g4f.client import Client
                client = Client()
                
                prompt_sistem = (
                    "Kamu adalah Piko, sebuah chatbot AI pintar berwujud robot kecil yang ceria di website 'Sobat Cilik Academy'. "
                    "Tugas utamamu adalah menjawab semua pertanyaan anak-anak usia Sekolah Dasar (SD).\n\n"
                    f"Berikut adalah materi utama yang ada di website ini: {konteks_materi_web}\n\n"
                    "Aturan merespon:\n"
                    "1. Jawab secara SPONTAN, cerdas, kreatif, dan ramah anak.\n"
                    "2. Gunakan sapaan seperti 'Sobat Cilik' atau 'Teman Pintar'.\n"
                    "3. Tambahkan banyak emoji seru (🧮, 🦁, 🪐, 🚀, 🎨) agar anak gembira."
                )
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    stream=False,
                    messages=[
                        {"role": "system", "content": prompt_sistem},
                        {"role": "user", "content": tanya_anak}
                    ]
                )
                jawaban_piko = response.choices[0].message.content
                
                if not jawaban_piko or "invalid" in jawaban_piko.lower() or "auth" in jawaban_piko.lower():
                    raise ValueError("Respons API tidak valid")
                    
            except Exception:
                if any(x in tanya_lower for x in ["jawa", "basa jawa"]):
                    jawaban_piko = "🤠 **Matur nuwun sanget, Teman Pintar!** Sinau basa Jawa iku pancen seru! Ayo tebak, yen anak gajah kuwi jenenge opo? Jawabane yaiku *Bledug*! Lucu banget ya! 🐘"
                elif any(x in tanya_lower for x in ["inggris", "english"]):
                    jawaban_piko = "🔤 *Hello little adventurer!* Di game **English Adventure**, kita bisa bernyanyi bareng! Ingat ya, kalau kucing itu *Cat* 🐱 dan anjing itu *Dog* 🐶. *Keep it up!*"
                elif any(x in tanya_lower for x in ["pjok", "olahraga", "sehat"]):
                    jawaban_piko = "⚽ **Hup! Dua! Tiga! Semangat, Sobat Cilik!** Ingat kata Kapten PJOK, selain melompat dan berlari (gerak lokomotor), tubuh sehat kita juga butuh susu hangat! 🥛"
                elif any(x in tanya_lower for x in ["ips", "sejarah", "peta"]):
                    jawaban_piko = "🗺️ **Wah, sang Detektif Sejarah beraksi!** Tahu tidak, rumah adat Sumatra Barat yang mirip tanduk kerbau itu namanya Rumah Gadang! Keren sekali budaya Indonesia! 🏠"
                elif any(x in tanya_lower for x in ["ppkn", "pancasila", "garuda"]):
                    jawaban_piko = "🦅 **Garuda Pancasila!** Lambang Sila Kedua adalah Rantai Emas ⛓️. Artinya kita sesama sahabat tidak boleh bertengkar dan harus selalu gotong royong! 🧹"
                elif any(x in tanya_lower for x in ["kuis", "tebak", "game", "main"]):
                    jawaban_piko = "... Piko punya tebak-tebakan nih! *'Aku punya sayap tapi aku bukan burung, aku punya baling-baling di kepala. Siapakah aku?'* 🚁"
                elif "helikopter" in tanya_lower:
                    jawaban_piko = "🎉 **YEYYY BENAR!** Kamu hebat banget, jawabannya adalah Helikopter! 🚁 Kamu dapat tambahan bintang virtual dari Piko! ⭐"
                elif "mapel" in tanya_lower or "belajar" in tanya_lower:
                    jawaban_piko = "🎒 **Wah, pilihan mapel di game melimpah ruah!** Ada Matematika 🧮, IPA 🦁, B. Jawa 🤠, English 🔤, PJOK ⚽, IPS 🗺️, dan PPKN 🦅! Klik tombol kartu game di tengah layarmu untuk memainkannya!"
                else:
                    jawaban_piko = "Wah, pertanyaan hebat! 🚀 Coba tanyakan materi seru atau petunjuk bermain game ke Piko yuk, biar Piko bantu temani belajar dengan gembira! ⚡🤖"
            
            st.session_state.riwayat_chat.append({"role": "assistant", "content": jawaban_piko})
            st.rerun()