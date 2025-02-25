import cv2
import os

# Load image
img = cv2.imread("Shiv.jpg")  # Ensure PNG format

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# ASCII Mapping
d = {chr(i): i for i in range(255)}

m, n, z = 0, 0, 0

# Store passcode in first few pixels
for i in range(len(password)):
    img[n, m, z] = d[password[i]]
    m += 1

# Separator pixel
img[n, m, z] = 255
m += 1

# Encode message
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    m += 1
    z = (z + 1) % 3

# **Add null terminator to mark the end of the message**
img[n, m, z] = 0

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")
