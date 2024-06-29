from pydub import AudioSegment
from pydub.utils import mediainfo


# Загрузите и конвертируйте аудиофайл
audio = AudioSegment.from_file("NOAA_08090929.mp3", format="mp3")

# Преобразование аудио в формат WAV
audio.export("NOAA_08090929.wav", format="wav")

print("Преобразование завершено. Файл .wav создан.")