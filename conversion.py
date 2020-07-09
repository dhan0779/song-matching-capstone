import matplotlib.pyplot as plt
from microphone import record_audio
import librosa as lib
import matplotlib as mlab
import numpy as np
from pathlib import Path


def file_to_samples(song,
                    sampling_rate = 44100):
    """Converts given song file to numpy array of samples
    
    Parameters
    ----------
    song: str; .mp3 file path  

    sampling_rate: int; Sampling Rate of the song, Hz
                        Defaults to 44100 Hz

    Returns: 
    spectogram: 2D numpy array; rows - freqs, columns - times, elements - 

    """
    samples, rate = lib.load(song, sr=sampling_rate, mono=True)
    spectrogram, freqs, times = mlab.specgram(
        samples,
        NFFT=4096,
        Fs=rate,
        window=mlab.window_hanning,
        noverlap=int(4096 / 2)
    )

    return spectrogram, rate

def mic_to_samples(duration,
                   sampling_rate = 44100):
    """Records audio sample

    Parameters
    ----------
    duration: clip length; 
    sampling_rate: int; Sampling Rate of the song, Hz
                        Defaults to 44100 Hz

    Returns: samples, sampling_rate
    """
    pass

