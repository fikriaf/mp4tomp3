import os
from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(mp4_file, mp3_file):
    try:
        # Memuat file video
        video = VideoFileClip(mp4_file)

        # Menyimpan sebagai MP3
        video.audio.write_audiofile(mp3_file)
        video.close()

        print(f"Berhasil mengonversi {mp4_file} menjadi {mp3_file}")
        return True  # Mengembalikan True jika konversi berhasil
    except Exception as e:
        print(f"Error saat mengonversi {mp4_file}: {e}")
        return False  # Mengembalikan False jika konversi gagal


def convert_all_mp4_to_mp3(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                mp4_path = os.path.join(root, file)
                mp3_path = (
                    os.path.splitext(mp4_path)[0] + ".mp3"
                )  # Mengganti ekstensi menjadi .mp3

                # Konversi dan hapus file MP4 jika berhasil
                if convert_mp4_to_mp3(mp4_path, mp3_path):
                    os.remove(mp4_path)
                    print(f"Dihapus: {mp4_path}")


# Contoh penggunaan
if __name__ == "__main__":
    directory_path = "C:\\Users\\Fikri\\Music\\"  # Ganti dengan path direktori Anda
    convert_all_mp4_to_mp3(directory_path)
