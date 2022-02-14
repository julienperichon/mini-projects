from math import ceil
import cv2 as cv
import curses

console = curses.initscr()
console.nodelay(True)
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # resize the image
    height, width = gray.shape
    aspect_ratio = height / width
    new_width = 150
    new_height = aspect_ratio * new_width * 0.55
    gray = cv.resize(gray, (new_width, int(new_height)))
    # _, gray = cv.threshold(gray, 70, 255, cv.THRESH_TOZERO)
    # gray = cv.normalize(gray, None, 0, 255, cv.NORM_MINMAX)

    # replace each pixel with a character from array
    chars = " .:!*%$@&#SB"
    # chars = " _.,-=+:;cba!?0123456789$W#@Ñ"
    step = ceil(255 / len(chars))
    new_pixels = [chars[pixel // step] for pixel in gray.flatten()]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    console.clear()
    console.addstr(ascii_image)
    console.refresh()

    if console.getch() == ord('q'):
        break

# When everything done, release the capture
cap.release()
curses.endwin()
