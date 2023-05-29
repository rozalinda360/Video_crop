# video_cropping
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def crop_video(input_folder, start_time, end_time):
    output_folder = os.path.join(input_folder,"output")
    os.makedirs(output_folder,exist_ok=True)

    for video in os.listdir(input_folder):
        input_path = os.path.join(input_folder, video)
        if os.path.isfile(input_path):
            file_name, file_extension = os.path.splitext(video)
            output_filename = file_name + "_cropped" + file_extension
            output_path = os.path.join(output_folder, output_filename)
            ffmpeg_extract_subclip(input_path, start_time, end_time, targetname=output_path)
        else:
            print("failed to crop videos")

        
input_video = input('Enter the folder containing the videos: ')
start_time =0  # Start time in seconds
end_time =60

crop_video(input_video, start_time, end_time)
