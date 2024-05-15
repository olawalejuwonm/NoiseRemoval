"""
This module loads an audio file, applies noise reduction, and saves the result.
"""

# from fileinput import filename
import time
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import simpledialog
import librosa
import noisereduce as nr
import soundfile as sf

# create the root window
root = tk.Tk()
root.title("Tarm Noise Reduction App")
root.resizable(False, False)
root.geometry("300x150")


def select_file():
    # filetypes = (("text files", "*.txt"), ("All files", "*.*"))
    # file type should be audio files
    try:
        filetypes = (("audio files", "*.wav"), ("All files", "*.*"))

        file_name = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        reduction_strength = simpledialog.askinteger(
            "Reduction Strength",
            "Enter the reduction strength (0 to 100%): ",
            parent=root,
        )
        # freq_range = input(
        #     "Enter the frequency range to smooth the mask over in Hz (default is 500): "
        # )
        freq_range = simpledialog.askinteger(
            "Frequency Range",
            "Enter the frequency range to smooth the mask over in Hz (default is 500): ",
            parent=root,
        )

        # print(file_name)
        # print(reduction_strength)
        # print(freq_range)

        # Close previous window
        root.destroy()
        # show a loading message
        showinfo(
            title="Loading",
            message="Noise reduction will take some time, Press OK to continue.",
        )

        # Load your audio file
        y, sr = librosa.load(file_name)
        # The proportion to reduce the noise by (1.0 = 100%)
        # reduction_strength = input("Enter the reduction strength (0 to 100%): ")
        # use tkinter to get the reduction strength

        if not reduction_strength:
            reduction_strength = 50

        # Convert the reduction strength to a float
        reduction_strength = float(reduction_strength) / 100
        # start time
        # The frequency range to smooth the mask over in Hz, by default 500
        # freq_range = input(
        #     "Enter the frequency range to smooth the mask over in Hz (default is 500): "
        # )
        freq_range = int(freq_range) if freq_range else 500
        start_time = time.time()

        # Apply noise reduction
        reduced_noise = nr.reduce_noise(
            y=y,
            sr=sr,
            stationary=False,
            prop_decrease=reduction_strength,
            freq_mask_smooth_hz=freq_range,
        )

        sf.write("reduced-noise.wav", reduced_noise, sr)
        # end time
        end_time = time.time()
        # Save the result
        # Calculate the time taken in minutes
        time_taken = (end_time - start_time) / 60
        # close the previous window
        # root.destroy()
        # print(f"Time taken to reduce noise: {time_taken} minutes")
        showinfo(
            title="Noise Reduction Complete",
            message=f"Time taken to reduce noise: {time_taken} minutes."
            + "File saved as reduced-noise.wav",
        )
        # terminate the program
        sys.exit()
    except Exception as e:
        showinfo(title="Error", message=f"An error occurred: {e}")
    # showinfo(title="Selected File", message=filename)


open_button = ttk.Button(
    root, text="Open a File To Perform Noise Reduction", command=select_file
)

# open button

open_button.pack(expand=True)

# run the application
root.mainloop()

# # Save the result
# librosa.output.write_wav(
#     "conversation-in-class-room-reduced.wav", reduced_noise, sr)
