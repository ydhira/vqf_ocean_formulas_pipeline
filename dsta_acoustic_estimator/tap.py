# -*- coding: utf-8 -*-
""" 
This file contains utility functions for our Temporal Acoustic Estimator that can be used to compute the spectrogram from raw audio and 
functions that use the Acoustic Parameter Estimator model to generate acoustic features from these spectrograms. 
"""

import numpy 
import os
import torch
import torchaudio
import typing


from tqdm.auto import tqdm


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

### Waveform Threshold Limits
MINIMUM_DURATION_IN_SECONDS = 5

### Waveform Default Parameters
DEFAULT_SAMPLE_RATE = 16000

### Spectrogram Default Parameters
DEFAULT_N_FFT       = 640
DEFAULT_HOP_LENGTH  = 160
DEFAULT_WIN_LENGTH  = 640
DEFAULT_WINDOW      = torch.hamming_window(DEFAULT_WIN_LENGTH)

ACOUSTIC_FEATURE_NAMES = [
    'Loudness',
    'alphaRatio',
    'hammarbergIndex',
    'slope0-500',
    'slope500-1500',
    'spectralFlux',
    'mfcc_coeff1',
    'mfcc_coeff2',
    'mfcc_coeff3',
    'mfcc_coeff4',
    'F0_semitone_From27.5Hz',
    'jitter_local',
    'shimmer_local_dB',
    'HNRdBACF',
    'logRelF0-H1-H2',
    'logRelF0-H1-A3',
    'F1_frequency',
    'F1_bandwidth',
    'F1_amplitudeLogRelF0',
    'F2_frequency',
    'F2_bandwidth',
    'F2_amplitudeLogRelF0',
    'F3_frequency',
    'F3_bandwidth',
    'F3_amplitudeLogRelF0'
]

## Computed over Microsoft DNS Challenge 2020 Data, which our estimator is trained on 

ACOUSTIC_MEAN = torch.tensor(
    [  2.31615782e-01, -5.02114248e+00,  7.16793156e+00,  1.40047576e-02,
      -1.44424592e-03,  1.18291244e-01,  7.16937304e+00,  5.01161051e+00,
       7.38044071e+00,  1.30544746e+00,  7.16783571e+00,  7.72617990e-03,
       3.78611624e-01,  1.80594587e+00,  2.74223471e+00,  7.16790104e+00,
       2.29371735e+02,  2.61031281e+02, -2.86713428e+01,  4.58741486e+02,
       2.72984955e+02, -2.86713428e+01,  4.58874390e+02,  2.71175812e+02,
      -2.86713428e+01], dtype=torch.float32)

ACOUSTIC_STANDARD_DEVIATION = torch.tensor(
    [ 4.24716711e-01, 1.09750290e+01, 1.51086359e+01, 2.98775751e-02,
      1.85245797e-02, 2.39421308e-01, 1.63376312e+01, 1.22261524e+01,
      1.53735695e+01, 1.42613926e+01, 1.21981163e+01, 2.58955006e-02,
      8.05543840e-01, 3.83967781e+00, 6.79308844e+00, 1.41308403e+01,
      3.49271667e+02, 6.28384338e+02, 6.05799637e+01, 6.89079407e+02,
      5.62089905e+02, 6.05799637e+01, 1.09140088e+03, 5.42341919e+02,
      6.05799637e+01], dtype=torch.float32)

class AcousticEstimator(torch.nn.Module):
    
    def __init__(self):
        
        super(AcousticEstimator, self).__init__()
        
        self.lstm = torch.nn.LSTM(642, 256, 4, bidirectional=True, batch_first=True)
        
        self.linear1 = torch.nn.Linear(512, 256)
        self.linear2 = torch.nn.Linear(256, 128)
        self.linear3 = torch.nn.Linear(128, 25)
        
        self.act = torch.nn.GELU()
        
    def forward(self, spectrogram):

        hidden, _   = self.lstm(spectrogram)
        hidden      = self.linear1(hidden)
        hidden      = self.act(hidden)
        hidden      = self.linear2(hidden)
        hidden      = self.act(hidden)
        acoustics   = self.linear3(hidden)
        
        return acoustics

MODEL_PATH = "/ocean/projects/cis220031p/hyd/dsta_acoustic_estimator/hamming_lld_estimator_13mse_13mae.pt"

CHECKPOINT = torch.load(MODEL_PATH, map_location=DEVICE)['model_state_dict']

ACOUSTIC_ESTIMATOR = AcousticEstimator()
ACOUSTIC_ESTIMATOR.load_state_dict(CHECKPOINT)
ACOUSTIC_ESTIMATOR.to(DEVICE)

def get_waveformFromAudioPath(
    audioPath : str) -> typing.Tuple[torch.FloatTensor, int]:
    """
    Parameters:

        audioPath (str): 
            Path to audio file.

    Returns:

        waveform (torch.FloatTensor): 
            A 1-D time sequence.
    """

    try:

        waveform, sampleRate = torchaudio.load(audioPath)

        # Resamples the waveform if necessary at the new frequency using  
        # bandlimited interpolation. [Smith, 2020].
        waveform = torchaudio.functional.resample(
            waveform  = waveform            , 
            orig_freq = sampleRate          , 
            new_freq  = DEFAULT_SAMPLE_RATE )
        
        return waveform[0], DEFAULT_SAMPLE_RATE

    except Exception as e:

        raise RuntimeError(
            'Exception thrown in get_waveformFromAudioPath:\n {}'.format(e))

def get_spectrogramFromWaveform(
    waveform   : torch.FloatTensor,
    sampleRate: int
    ) -> torch.FloatTensor:
    
    """
    Parameters:

        waveform (torch.FloatTensor): 
            A 1-D time sequence.

    Returns:
    
        spectrogram (torch.FloatTensor): 
            Returns a wrapped complex tensor of size [2*T, 2*(N_FFT+1)], where 
            N_FFT is the number of frequencies where STFT is applied and 
            T is the total number of frames used. 
            Note: Real and imaginary alternate in sequence.
    """
    try:

        # Check if waveform is not a 1-D time sequence.
        if waveform.dim() != 1: 

            raise RuntimeError(
                'RuntimeError in getSpectrogramFromWaveform: ' +
                'waveform.dim() should be 1 but received {}'.format(
                    waveform.dim()))

        # Resamples the waveform if necessary at the new frequency using  
        # bandlimited interpolation. [Smith, 2020].
        waveform = torchaudio.functional.resample(
            waveform  = waveform            , 
            orig_freq = sampleRate          , 
            new_freq  = DEFAULT_SAMPLE_RATE )
        
        # Check if waveform duration is less than minimum limit.
        if len(waveform) < MINIMUM_DURATION_IN_SECONDS * DEFAULT_SAMPLE_RATE:
            
            raise RuntimeWarning(
                'RuntimeWarning in getSpectrogramFromWaveform: ' +
                'len(waveform) should be greater than {} but received {}'.format(
                    MINIMUM_DURATION_IN_SECONDS * DEFAULT_SAMPLE_RATE,
                    len(waveform) ) )
            
        # See: https://pytorch.org/docs/stable/generated/torch.stft.html
        spectrogram = torch.stft(
            input          = waveform           , 
            n_fft          = DEFAULT_N_FFT      , 
            hop_length     = DEFAULT_HOP_LENGTH , 
            win_length     = DEFAULT_WIN_LENGTH , 
            window         = DEFAULT_WINDOW     ,
            return_complex = False              )
        
        # Permute to make time first: (N_FFT//2+1, T, 2) -> (T, N_FFT//2+1, T)
        spectrogram = spectrogram.permute(1, 0, 2)

        # Alternate between corresponding real and imag components over time    
        spectrogram = spectrogram.reshape(-1, DEFAULT_N_FFT + 2)

        # Remove last 5 frames, whose targets were not available during training
        spectrogram = spectrogram[:-5].float()
        
        return spectrogram

    except Exception as e:

        raise RuntimeError(
            'Exception thrown in get_spectrogramFromWaveform: {}'.format(e))


def get_spectrogramFromAudioPath(
    audioPath : str) -> torch.FloatTensor:
    """
    Parameters:

        audioPath (str): 
            Path to audio file.

    Returns:

        spectrogram (torch.FloatTensor): 
            Returns a wrapped complex tensor of size [2*T, 2*(N_FFT+1)], where 
            N_FFT is the number of frequencies where STFT is applied and 
            T is the total number of frames used. 
            Note: Real and imaginary alternate in sequence.
    """

    try:

        waveform, sampleRate = get_waveformFromAudioPath(audioPath)

        spectrogram = get_spectrogramFromWaveform(waveform, sampleRate)

        return spectrogram

    except Exception as e:

        print('Exception thrown in get_spectrogramFromAudioPath: {}'.format(e))

def get_acousticsFromSpectrogram(
    estimator   : torch.nn.Module   ,
    spectrogram : torch.FloatTensor,
    normalize: bool = False
    ) -> torch.FloatTensor:
    """
    Parameters:

        estimator (torch.nn.Module):
            See our ICASSP paper: [Yunyang, et al. 2023].

        spectrogram (torch.FloatTensor): 
            A wrapped complex tensor of size [2*T, 2*(N_FFT+1)], where 
            N_FFT is the number of frequencies where STFT is applied and 
            T is the total number of frames used. 
            Note: Real and imaginary alternate in sequence.

    Returns:

        acoustics (torch.FloatTensor): 
            25 time series for each audio. Each time series represents an 
            acoustic. Our ICASSP paper: [Yunyang, et al. 2023].
    """

    try:

        # Check if spectrogram is not a 2-D time sequence.
        if spectrogram.dim() != 2:

            raise RuntimeError(
                'RuntimeError in get_acousticsFromSpectrogram:\n ' +
                'waveform.dim() should be 2 but received {}'.format(
                    spectrogram.dim()))
            
        # Check default frequency requirements are met
        if spectrogram.shape[1] != 642:
            raise RuntimeError(
                'RuntimeError in get_acousticsFromSpectrogram:\n ' +
                'spectrogram.shape[1] should be 642 but received {}'.format(
                    spectrogram.shape[1]))

        # Check default duration requirement is met
        if spectrogram.shape[0] < 125: 
            raise RuntimeError(
                'RuntimeError in get_acousticsFromSpectrogram:\n ' +
                'spectrogram.shape[0] should be 125 but received {}'.format(
                    spectrogram.shape[0]))

        # Calculate acoustics using our estimator. [Yunyang, et al. 2023]
        acoustics = estimator(spectrogram.to(DEVICE)).detach()

        return acoustics

    except Exception as e:
        
        raise RuntimeError(
            'Exception thrown in get_acousticsFromSpectrogram:\n {}'.format(e))
        
def get_denormalizedAcoustics(
   acoustics : numpy.ndarray ) -> numpy.ndarray:
   """
   Parameters:


       acoustics (torch.FloatTensor):
           Standard normalized acoustics directly output from the
           AcousticEstimator neural network module.


   Returns:


       denormalizedAcoustics (torch.FloatTensor):
           Acoustics denormalized to restore their original scale.
   """

    
   denormalizedAcoustics = (ACOUSTIC_STANDARD_DEVIATION * acoustics) + ACOUSTIC_MEAN


   return denormalizedAcoustics
        
        
def get_acousticsFromWaveform(
    estimator  : torch.nn.Module   ,
    waveform   : torch.FloatTensor ,
    sampleRate : int ,
    normalize: bool = False) -> numpy.ndarray:
    """
    Parameters:

        estimator (torch.nn.Module): 
            See our ICASSP paper: [Yunyang, et al. 2023].

        waveform (torch.FloatTensor): 
            A 1-D time sequence.
        
        sampleRate (int):
            Sampling Rate of the Audio signal
            
         normalize (bool):
            Whether to return normalized features
         

    Returns:

        acoustics (torch.FloatTensor): 
            25 time series for each audio. Each time series represents an 
            acoustic. 
    """

    try:

        spectrogram = get_spectrogramFromWaveform(waveform, sampleRate)

        acoustics = get_acousticsFromSpectrogram(estimator, spectrogram.to(DEVICE))
        
        acoustics = acoustics.cpu().numpy()
        
        if not normalize:
            
            acoustics = get_denormalizedAcoustics(acoustics)

        return acoustics
        
    except Exception as e:

        raise RuntimeError(
            'Exception thrown in get_acousticsFromWaveform:\n {}'.format(e))

            
  
def get_acousticsFromAudioPath(
    estimator : torch.nn.Module ,
    audioPath : str,
    normalize: bool = False
    ) -> numpy.ndarray:
    """
    Parameters:

        estimator (torch.nn.Module): 
            See our ICASSP paper: [Yunyang, et al. 2023].
        
        audioPath (str): 
            Path to audio file.
        
        normalize (bool):
            Whether to return normalized features

    Returns:

        acoustics (torch.FloatTensor): 
            25 time series for each audio. Each time series represents an 
            acoustic. Our ICASSP paper: [Yunyang, et al. 2023].
    """

    try:

        waveform, sampleRate = get_waveformFromAudioPath(audioPath)

        acoustics = get_acousticsFromWaveform(estimator, waveform, sampleRate,normalize)
        

        return acoustics

    except Exception as e:

        raise RuntimeError(
            'Exception thrown in get_acousticsFromAudioPath:\n {}'.format(e))

def get_acousticsFromAudioPathList(
    estimator     : torch.nn.Module  ,
    audioPathList : typing.List[str],
    normalize: bool = False,
) -> typing.List[numpy.ndarray]:
    """
    Parameters:

        estimator (torch.nn.Module): 
            See our ICASSP paper: [Yunyang, et al. 2023].
        
        audioPath (str): 
            List of paths, each to an audio file.
        
        normalize (bool):
            Whether to return normalized features

    Returns:

        acoustics (list[torch.FloatTensor]): 
            A list of 25 time series for each audio. Each time series 
            represents an acoustic. Our ICASSP paper: [Yunyang, et al. 2023].
    """

    acousticList = []

    for audioPath in tqdm(audioPathList):

        try:

            acoustics = get_acousticsFromAudioPath(estimator, audioPath,normalize)

            acousticList.append(acoustics)

        except Exception as e:

            print('Warning in get_acousticsFromAudioPathList:\n {}'.format(e))

            continue

    return acousticList

# Example Usage:
#
# get_acousticsFromAudioPathList(
#     estimator     = ACOUSTIC_ESTIMATOR,
#     audioPathList = ["/content/clean_fileid_0.wav", "/content/clean_fileid_0.wav"])

