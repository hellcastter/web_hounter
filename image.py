import cv2
import os
import shutil
import sys

input_dir = "./original_images/"
output_dir = "./img/"

if not os.path.exists(input_dir):
    print("Input directory does not exist!")
    sys.exit()

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in os.listdir(input_dir):
    print("Processing: ", i)

    if not (i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg")):
        shutil.copy(os.path.join(input_dir, i), os.path.join(output_dir, i))
        continue

    filename, file_extension = os.path.splitext(i)
    original_path = os.path.join(input_dir, i)

    img = cv2.imread(original_path, cv2.IMREAD_UNCHANGED)

    
    cv2.imwrite(os.path.join(output_dir, filename + ".webp"), img, [int(cv2.IMWRITE_WEBP_QUALITY), 85])

    if file_extension == ".png":
        cv2.imwrite(os.path.join(output_dir, filename + ".png"), img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    else:
        cv2.imwrite(os.path.join(output_dir, filename + ".jpg"), img, [int(cv2.IMWRITE_JPEG_QUALITY), 85])

    img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))

    cv2.imwrite(os.path.join(output_dir, filename + "@2x.webp"), img, [int(cv2.IMWRITE_WEBP_QUALITY), 85])

    if file_extension == ".png":
        cv2.imwrite(os.path.join(output_dir, filename + "@2x.png"), img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    else:
        cv2.imwrite(os.path.join(output_dir, filename + "@2x.jpg"), img, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
