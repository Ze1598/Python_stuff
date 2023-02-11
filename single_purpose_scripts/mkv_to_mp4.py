import os
import ffmpeg

start_dir = "C:\\Users\\ze179\\Desktop\\lock off\\mkv"

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print(f"Finished converting {mkv_file}")

for path, folder, files in os.walk(start_dir):
    for file in files:
        if file.endswith('.mkv'):
            print(f"Found file: {file}")
            convert_to_mp4(os.path.join(start_dir, file))
        else:
            pass
