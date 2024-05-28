#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_audio(url, save_path):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=save_path)
    status_label.config(text="Download completed!")

def on_download_button_click():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    if save_path:  # Check if a directory was selected
        download_audio(url, save_path)

# Create the main window
root = tk.Tk()
root.title("YouTube to MP3 Downloader")

# Create URL entry
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Create download button
download_button = tk.Button(root, text="Download", command=on_download_button_click)
download_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Create status label
status_label = tk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
