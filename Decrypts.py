import cv2
import numpy as np

# Load encrypted image
img = cv2.imread("encryptedImage.png")

# ASCII Mapping
c = {i: chr(i) for i in range(256)}

# Extract stored passcode
stored_pass = ""
m, n, z = 0, 0, 0

while True:
    pixel_value = img[n, m, z]
    if pixel_value == 255:  # Separator pixel detected
        m += 1
        break
    stored_pass += c.get(pixel_value, "?")
    m += 1

# Ask for passcode
user_pass = input("Enter passcode for decryption: ")

# Validate passcode
if user_pass != stored_pass:
    print("Incorrect passcode! Decryption failed.")
    exit(1)

# If passcode is correct, continue decryption
decrypted_msg = ""
while True:
    pixel_value = img[n, m, z]

    # **Stop at null terminator (0)**
    if pixel_value == 0:
        break

    char = c.get(pixel_value, "?")
    if not char.isprintable():
        break

    decrypted_msg += char
    m += 1
    z = (z + 1) % 3

print("Decryption successful! Message:", decrypted_msg)
