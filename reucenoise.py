"""
This module loads an audio file, applies noise reduction, and saves the result.
"""

import librosa
import noisereduce as nr
import soundfile as sf
import time


# Load your audio file
y, sr = librosa.load(input("Enter the audio file directory: "))
# The proportion to reduce the noise by (1.0 = 100%)
reduction_strength = input("Enter the reduction strength (0 to 100%): ")
# Convert the reduction strength to a float
reduction_strength = float(reduction_strength) / 100
# start time
# The frequency range to smooth the mask over in Hz, by default 500
freq_range = input(
    "Enter the frequency range to smooth the mask over in Hz (default is 500): "
)
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
print(f"Time taken to reduce noise: {time_taken} minutes")
# # Save the result
# librosa.output.write_wav(
#     "conversation-in-class-room-reduced.wav", reduced_noise, sr)
