# FSM.py
from enum import Enum, auto
from engine import EduEngine

class State(Enum):
    IDLE       = auto()
    CHOOSING   = auto()
    QUIZ       = auto()
    EVALUATION = auto()

class EduFSM:
    def __init__(self):
        self.nlp                  = EduEngine()
        self.state               = State.IDLE
        self.current_subject     = None
        self.current_question_idx = 0
        self.score                = 0
        self.response            = ""
        # Menyinkronkan variabel rumus ke objek sidebar app.py
        self.last_formula        = None

    def get_response(self):
        return self.response

    def get_menu_text(self):
        lines = "📚 **Ini beberapa topik seru yang siap kita ulik bareng:**\n\n"
        for key, data in self.nlp.course_data.items():
            lines += f"- {data['emoji']} **{key.capitalize()}** — *{data['desc']}*\n"
        lines += (
            "\n💡 **Cara ngobrol sama aku:**\n"
            "• Mau baca materi? Ketik aja: *'belajar fisika'* atau *'materi kimia'*\n"
            "• Mau langsung kuis? Ketik: *'kuis biologi'* atau *'soal sejarah'*\n"
            "• Mau mulai ulang dari awal? Cukup ketik *'reset'* kapan saja ya!"
        )
        return lines

    def _help_text(self):
        return (
            "🆘 **Butuh panduan cepat? Tenang, ini beberapa perintah yang bisa kamu pakai:**\n\n"
            "• Ketik **'menu'** → Buat intip semua pilihan mata pelajaran yang ada.\n"
            "• Ketik **'belajar [topik]'** → Kita bakal bahas teorinya dulu santai (Contoh: *belajar kimia*).\n"
            "• Ketik **'kuis [topik]'** → Langsung gas latihan soal tanpa basa-basi (Contoh: *kuis sejarah*).\n"
            "• Ketik **'reset'** → Mulai ulang sesi obrolan kita dari awal.\n\n"
            "Topik yang siap kita bahas saat ini: " + ", ".join(
                f"{v['emoji']} {k.capitalize()}" for k, v in self.nlp.course_data.items()
            )
        )

    def step(self, user_input=""):
        intent           = self.nlp.detect_intent(user_input)
        detected_subject = self.nlp.parse_subject(user_input)

        # ── Global interrupts (work from any state) ────────────────────────
        if intent == "RESET_SYSTEM" and self.state != State.IDLE:
            self.state                = State.IDLE
            self.current_subject      = None
            self.current_question_idx = 0
            self.score                = 0
            self.last_formula         = None

        if intent == "HELP":
            self.response = self._help_text()
            return

        # ==================================================================
        # STATE: IDLE
        # ==================================================================
        if self.state == State.IDLE:
            self.response = (
                "Sistem berhasil di-refresh! Halo, aku **RuangSobat** 👋\n\n"
                "Hari ini kamu mau nemenin aku bahas materi apa nih? Yuk, ketik **'menu'** buat lihat daftar topik seru yang udah aku siapkan!"
            )
            self.state = State.CHOOSING
            return

        # ==================================================================
        # STATE: CHOOSING
        # ==================================================================
        elif self.state == State.CHOOSING:
            if intent in ("ASK_MENU", "LEARN_MATERIAL", "START_QUIZ") or detected_subject:
                self.current_question_idx = 0
                self.score                = 0

            if detected_subject:
                self.current_subject = detected_subject

            # 1. Jika pengguna minta menu secara eksplisit
            if intent == "ASK_MENU":
                self.response = self.get_menu_text()

            # 2. Jika pengguna ingin kuis DAN subjeknya sudah terdeteksi
            elif self.current_subject and intent == "START_QUIZ":
                self.state                = State.QUIZ
                self.current_question_idx = 0
                self.score                = 0
                first_q = self.nlp.course_data[self.current_subject]["kuis"][0]["soal"]
                total   = len(self.nlp.course_data[self.current_subject]["kuis"])
                self.response = (
                    f"🚀 **Kuis {self.current_subject.capitalize()} resmi dimulai!**\n"
                    f"Ada total *{total} soal* yang harus kamu taklukkan. Tantangan diterima? 😎\n\n"
                    f"📝 **Soal 1 dari {total}:**\n"
                    f"{first_q}\n\n"
                    f"_*Langsung ketik jawabanmu di bawah ya, semangatt!*_"
                )

            # 3. FIX SOLUSI: Jika ketik "mau belajar" tapi BELUM sebut topik, panggil sapaan & langsung suguhkan menu
            elif intent == "LEARN_MATERIAL" and not self.current_subject:
                self.response = (
                    "Sip! Asyik banget hari ini kamu lagi semangat belajar. 😊\n"
                    "Kamu mau ulik materi apa nih? Silakan ketik langsung salah satu dari daftar di bawah ini ya:\n\n"
                ) + self.get_menu_text()

            # 4. Jika pengguna ingin belajar DAN subjek/topik sudah terdeteksi spesifik
            elif self.current_subject and (intent in ("LEARN_MATERIAL", "YES") or (detected_subject and intent != "START_QUIZ")):
                data   = self.nlp.course_data[self.current_subject]
                total  = len(data["kuis"])
                
                # Isi pembaruan teks rumus ke panel kiri secara otomatis
                self.last_formula = f"📘 **Fokus Utama {self.current_subject.capitalize()}:**\n\n{data['materi']}"
                
                self.response = (
                    f"Asyik, mari kita ulas materi **{self.current_subject.capitalize()}** bareng-bareng! {data['emoji']}\n\n"
                    f"Ini poin inti yang wajib banget kamu kantongi:\n"
                    f"👉 *{data['materi']}*\n\n"
                    f"✏️ *Oya, catatan ringkas di atas udah aku pin juga ya di Panel Belajar (sebelah kiri) biar kamu nggak lupa.*\n\n"
                    f"--- \n"
                    f"Gimana, teorinya aman? Aku udah nyiapin **{total} soal latihan** yang pas banget buat nguji pemahamanmu. "
                    f"Kalau kamu udah siap tempur, langsung ketik aja **'kuis {self.current_subject}'** ya! Yuk, kita lihat seberapa jago kamu! 🔥"
                )

            # 5. Jika minta kuis tapi subjeknya kosong
            elif intent == "START_QUIZ" and not self.current_subject:
                self.response = (
                    "📌 **Eh, sebentar!** Pilih dulu dong topiknya sebelum kita mulai kuisnya.\n"
                    "Coba ketik **'menu'** dulu yuk buat milih mapel yang kamu kuasai!"
                )

            # 6. Jika input tidak dikenali sama sekali
            elif intent == "UNKNOWN":
                suggestions = self.nlp.suggest_closest(user_input)
                if suggestions:
                    suggestion_list = ", ".join(f"**{s.capitalize()}**" for s in suggestions)
                    self.response = (
                        f"🤔 Hm, maksud kamu salah satu dari materi ini bukan: {suggestion_list}?\n\n"
                        "Coba ketik nama topiknya dengan lebih lengkap, atau ketik **'menu'** biar langsung milih dari daftar ya!"
                    )
                else:
                    self.response = (
                        "😅 Waduh, aku agak kurang nangkep nih maksud kalimatmu. Coba deh pakai cara ini:\n"
                        "• Ketik **'menu'** buat lihat daftar mapel.\n"
                        "• Ketik **'help'** kalau kamu butuh bantuan panduan lengkap."
                    )

            else:
                self.response = (
                    "Hmm, kalimatnya agak membingungkan nih. Coba ketik **'menu'** untuk lihat daftar materi, "
                    "atau **'help'** untuk intip panduan pakainya ya!"
                )

        # ==================================================================
        # STATE: QUIZ
        # ==================================================================
        elif self.state == State.QUIZ:
            soal_list = self.nlp.course_data[self.current_subject]["kuis"]
            idx       = self.current_question_idx
            total     = len(soal_list)
            kunci     = soal_list[idx]["kunci"]

            if user_input.lower().strip() == kunci.lower():
                self.score += 1
                feedback = "🎯 **Wih, jawabanmu BENAR!** Keren banget, pertahankan!"
            else:
                feedback = f"❌ **Aduh, masih kurang tepat nih!**\nJawaban yang bener itu: **{kunci}**"

            self.current_question_idx += 1
            idx_baru = self.current_question_idx

            if idx_baru < total:
                soal_next = soal_list[idx_baru]["soal"]
                self.response = (
                    f"{feedback}\n\n"
                    f"✍️ **Yuk lanjut ke Soal {idx_baru + 1} dari {total}:**\n"
                    f"{soal_next}"
                )
            else:
                self.state = State.EVALUATION
                self.step(user_input)

        # ==================================================================
        # STATE: EVALUATION
        # ==================================================================
        elif self.state == State.EVALUATION:
            total      = len(self.nlp.course_data[self.current_subject]["kuis"])
            nilai      = int((self.score / total) * 100)
            salah      = total - self.score

            if nilai == 100:
                predikat = "🏆 **SANGAR! Skor Sempurna!** Kamu beneran master di materi ini! Kebanggaan kelas nih!"
            elif nilai >= 80:
                predikat = "🥇 **Keren abis!** Hasil yang luar biasa. Sedikit lagi dapet nilai sempurna!"
            elif nilai >= 60:
                predikat = "🥈 **Not bad!** Hasilnya udah lumayan oke kok. Coba baca ulang materinya sekali lagi biar makin mantap!"
            else:
                predikat = "🥉 **Jangan berkecil hati ya!** Namanya juga proses belajar. Yuk latihan lagi, jangan pernah menyerah!"

            self.response = (
                f"🎉 **Hore! Kuis {self.current_subject.capitalize()} selesai juga!**\n\n"
                f"📊 **Ini dia rapor hasil latihanmu:**\n"
                f"• ✅ Jawaban Benar: **{self.score}** dari {total} soal\n"
                f"• ❌ Jawaban Salah: **{salah}** soal\n"
                f"• 🎯 Skor Akhir: **{nilai} / 100**\n\n"
                f"{predikat}\n\n"
                f"Mau lanjut belajar? Ketik **'menu'** buat cari petualangan di topik lain, "
                f"atau ketik **'kuis {self.current_subject}'** kalau penasaran mau ngulang kuis ini lagi!"
            )
            self.state = State.CHOOSING