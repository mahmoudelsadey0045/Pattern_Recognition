import os
import numpy as np
from skimage import io
from sklearn.cluster import KMeans
from tkinter import Tk, filedialog, Button, Label, StringVar, Entry
from PIL import Image, ImageTk


def calculate_unique_colors(image):
    rgb_image = image.convert("RGB")
    unique_colors = set(rgb_image.getdata())
    return len(unique_colors)


def select_image():
    global selected_filename, original_image, original_label, original_colors_var, status_var
    filename = filedialog.askopenfilename(title="Select Image File",
                                          filetypes=[("Image Files", "*.png; *.jpg; *.jpeg")])
    if filename:
        try:
            original_image = Image.open(filename)
            original_image.thumbnail((400, 400))
            display_original_image(original_image)
            selected_filename = filename
            status_var.set('Image selected. Press "Compress Image" to start compression.')
            # Calculate and display the original image size in KB
            original_size_kb = os.path.getsize(filename) / 1024.0
            original_size_var.set(f"Original Image Size: {original_size_kb:.2f} KB")
            # Calculate and display the number of unique colors in the original image
            original_unique_colors = calculate_unique_colors(original_image)
            original_colors_var.set(f"Original Image Colors: {original_unique_colors}")
        except Exception as e:
            status_var.set(f'Error: {str(e)}')


def display_original_image(image):
    original_image_tk = ImageTk.PhotoImage(image)
    original_label.config(image=original_image_tk)
    original_label.image = original_image_tk


def compress_image():
    global selected_filename, compressed_label, compressed_colors_var, status_var, k_entry, compress_button, \
        original_size_var, compressed_size_var
    try:
        # Retrieve the filename of the selected image
        filename = selected_filename
        # Open the original image
        original_image = Image.open(filename)
        # Read the image using skimage
        image = io.imread(filename)
        rows, cols = image.shape[0], image.shape[1]
        # Reshape the image to a 2D array of pixels
        image = image.reshape(rows * cols, 3)
        # Get the K value from the entry field and convert it to an integer
        k_value = int(k_entry.get())
        # Perform K-means clustering
        kMeans = KMeans(n_clusters=k_value)
        kMeans.fit(image)
        # Extract the cluster centers (new colors) and labels for (each pixel)
        centers = np.asarray(kMeans.cluster_centers_, dtype=np.uint8)
        labels = np.asarray(kMeans.labels_, dtype=np.uint8)
        labels = np.reshape(labels, (rows, cols))
        # Create a new image array with the same dimensions as the original
        newImage = np.zeros((rows, cols, 3), dtype=np.uint8)
        # Assign the new colors to each pixel in the new image
        for i in range(rows):
            for j in range(cols):
                newImage[i, j, :] = centers[labels[i, j], :]
        # Convert the new image array to a PIL image
        compressed_image = Image.fromarray(newImage)
        compressed_image.thumbnail((400, 400))
        # Display the compressed image in the GUI
        display_compressed_image(compressed_image)
        # Save the compressed image to a new file
        save_filename = filename.split('.')[0] + '-compressed.png'
        io.imsave(save_filename, newImage)
        # Update the status to indicate success
        status_var.set('Image has been compressed successfully.')
        # Calculate and display the compressed image size in KB
        compressed_size_kb = os.path.getsize(save_filename) / 1024.0
        compressed_size_var.set(f"Compressed Image Size: {compressed_size_kb:.2f} KB")
        # Calculate and display the number of unique colors in the compressed image
        compressed_unique_colors = calculate_unique_colors(compressed_image)
        compressed_colors_var.set(f"Compressed Image Colors: {compressed_unique_colors}")
        # Disable the compress button to prevent re-compression
        compress_button.config(state="disabled")
    except Exception as e:
        status_var.set(f'Error: {str(e)}')


def display_compressed_image(image):
    compressed_image_tk = ImageTk.PhotoImage(image)
    compressed_label.config(image=compressed_image_tk)
    compressed_label.image = compressed_image_tk


def exit_application():
    root.destroy()


root = Tk()
root.title("Image Compression")
root.geometry("900x900")

k_label = Label(root, text="Enter K value for K-means clustering:")
k_label.pack()

k_entry = Entry(root)
k_entry.pack()

original_label = Label(root)
original_label.pack(pady=5)

compressed_label = Label(root)
compressed_label.pack(pady=5)

original_colors_var = StringVar()
original_colors_label = Label(root, textvariable=original_colors_var)
original_colors_label.pack(pady=5)

compressed_colors_var = StringVar()
compressed_colors_label = Label(root, textvariable=compressed_colors_var)
compressed_colors_label.pack(pady=5)

original_size_var = StringVar()
original_size_label = Label(root, textvariable=original_size_var)
original_size_label.pack(pady=5)

compressed_size_var = StringVar()
compressed_size_label = Label(root, textvariable=compressed_size_var)
compressed_size_label.pack(pady=5)

select_button = Button(root, text="Select Image", command=select_image)
select_button.pack(pady=10)

compress_button = Button(root, text="Compress Image", command=compress_image)
compress_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=exit_application)
exit_button.pack(pady=5)

status_var = StringVar()
status_label = Label(root, textvariable=status_var)
status_label.pack()
selected_filename = None

root.mainloop()