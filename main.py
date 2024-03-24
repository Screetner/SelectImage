# TODO : loop to show each image in the given directory then
# if user press y, move the image to the given directory if not go next image

import os
import shutil
import cv2


def move_image(image_path, destination_dir):
    filename = os.path.basename(image_path)
    shutil.move(image_path, os.path.join(destination_dir, filename))
    print(f"Image {filename} moved successfully.")


def main():
    # Specify the directory containing images
    source_dir = "./oak-1133"

    # Specify the directory to move images to
    destination_dir = "./dataset"

    # Check if directories exist
    if not os.path.isdir(source_dir):
        print("Source directory does not exist.")
        return
    if not os.path.isdir(destination_dir):
        print("Destination directory does not exist.")
        return

    # List all files in the source directory
    # List all files in the source directory
    image_files = [file for file in os.listdir(source_dir) if file.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    num_images = len(image_files)
    if num_images == 0:
        print("No images found in the source directory.")
        return

    # Initialize current index
    current_index = 0

    # Loop through each image
    while True:
        image_file = image_files[current_index]
        image_path = os.path.join(source_dir, image_file)
        # Read and display the image
        image = cv2.imread(image_path)
        resized_image = cv2.resize(image, (800, 600))
        cv2.imshow("Image", resized_image)
        key = cv2.waitKey(0)

        # If user presses 'y', move the image to the destination directory
        if key == ord('y'):
            move_image(image_path, destination_dir)
            image_files.pop(current_index)
            num_images -= 1
            if num_images == 0:
                print("All images processed.")
                break
        elif key == ord('q'):
            print("Exiting...")
            break
        elif key == ord('.'):
            current_index = (current_index + 1) % len(image_files)
        elif key == ord(','):
            current_index = (current_index - 1) % len(image_files)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
