import cv2
import glob
from PIL import Image

def main():
    print("Welcome to the Video2Gif maker.\nPut this script into the video file before running!\n")
    video_file_name = input("Enter the converting video file name: ")
    mp4_file = video_file_name + ".mp4"
    mp4_converter(mp4_file)
    gif_maker(video_file_name,"output")

def mp4_converter(file):
    print("Your mp4 is converting...")
    still_reading, image = cv2.VideoCapture(file).read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"output/frame_{frame_count:03d}.jpg", image)
        # read next image
        still_reading, image = cv2.VideoCapture(file).read()
        frame_count += 1

    return "Your mp4 file is converted to frames"

def gif_maker(file_name,frame_folder):
    images = glob.glob(f"{frame_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frame_one = frames[0]
    frame_one.save(file_name+".gif", format="GIF", append_images=frames,
                   save_all=True, duration=50, loop=0)

if __name__ == "__main__":
    main()