import subprocess

def edit_video(input_path, output_path, text):
    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vf", f"hflip,drawtext=text='{text}':x=10:y=50:fontsize=24:fontcolor=white",
        "-y",
        output_path
    ]
    subprocess.run(cmd)