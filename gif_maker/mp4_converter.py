import cv2

def convert_mp4_to_jpgs(path):
    still_reading, image = cv2.VideoCapture(path).read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"output/frame_{frame_count:03d}.jpg", image)
        # read next image
        still_reading, image = cv2.VideoCapture(path).read()
        frame_count += 1
if __name__ == "__main__":
    convert_mp4_to_jpgs("camfitool.mp4")