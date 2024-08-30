import os
os.environ["PATH"] += os.pathsep + "/path/to/ffmpeg/bin"
from pydub.playback import play
from pydub import AudioSegment
AudioSegment.ffmpeg = "/path/to/ffmpeg"


def manipulate_audio(input_path, output_path):
    try:

            # Memuat file audio
            audio = AudioSegment.from_file(input_path)
            print("✅ Audio berhasil dimuat")

            # Direktori output
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                print(f"✅ Direktori '{output_dir}' berhasil dibuat")

            # Operasi Pemotongan dengan validasi durasi
            if len(audio) > 10000:
                clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
                clipped_audio.export(os.path.join(output_dir, 'clipped_result.mp3'), format='mp3')
                print("✅ Pemotongan berhasil")
            else:
                raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

            # Operasi Penggabungan dengan validasi durasi
            combined_audio = audio + clipped_audio
            combined_audio.export(os.path.join(output_dir, 'combined_result.mp3'), format='mp3')
            print("✅ Penggabungan berhasil")

            # Operasi Konversi Format
            audio.export(os.path.join(output_dir, 'result.wav'), format='wav')
            print("✅ Konversi format berhasil")

            # Operasi Pengaturan Volume dengan validasi
            if audio.dBFS < -10:
                louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
                louder_audio.export(os.path.join(output_dir, 'louder_result.mp3'), format='mp3')
                print("✅ Pengaturan volume berhasil")
            else:
                raise ValueError("Volume audio sudah terlalu tinggi")

            # Operasi Pemutaran Audio
            print("🔊 Memutar audio hasil manipulasi...")
            play(louder_audio)

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('audio/example.mp3', 'audio/result.mp3')