from pydub import AudioSegment
#import simpleaudio as sa

audio = AudioSegment.from_file('lagu.mp3')

# Mengonversi ke WAV (opsional, jika formatnya bukan WAV)
#audio.export('result.wav', format='wav')

# Memutar audio
# wave_obj = sa.WaveObject.from_wave_file('result.wav')
# play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
# play_obj.wait_done()

#pemotongan
#clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
#clipped_audio.export('clipped_result.mp3', format='mp3')

#penggabungan
# combined_audio = audio + clipped_audio
# combined_audio.export('combined_result.mp3', format='mp3')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')