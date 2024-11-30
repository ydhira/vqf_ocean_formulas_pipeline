import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sys 
import tqdm 
import glob 
import os 
from pydub import AudioSegment

sys.path.append('dsta_acoustic_estimator')
import tap_filepath_local

llfs = ['Loudness', 'alphaRatio', 'hammarbergIndex', 'slope0-500', 'slope500-1500', 'spectralFlux', 'mfcc_coeff1', 'mfcc_coeff2', 'mfcc_coeff3', \
            'mfcc_coeff4', 'F0_semitone_From27.5Hz', 'jitter_local', 'shimmer_local_dB', 'HNRdBACF', 'logRelF0-H1-H2', 'logRelF0-H1-A3', 'F1_frequency', \
            'F1_bandwidth', 'F1_amplitudeLogRelF0', 'F2_frequency', 'F2_bandwidth', 'F2_amplitudeLogRelF0', 'F3_frequency', 'F3_bandwidth', 'F3_amplitudeLogRelF0']# llf 
        
vqfs = ['Coveredness' ,'Aphonicity' ,'Biphonicity','Breathiness','Creakiness','Diplophonicity','Flutter','Glottalization','Hoarseness','Roughness',\
            'Nasality','Jitter','Pressed','Pulsed','Resonant','Shimmer','Strained','Strohbassness','Tremor','Twanginess','Ventricular','Wobble','Yawniness','Loudness']

def _helper(wavfile, combined_sounds):
    wavfile_basename = os.path.basename(wavfile)
    wavfile_combined = 'del/'+wavfile_basename
    combined_sounds.export(wavfile_combined, format="wav")
    return wavfile_combined

def get_tap_feature(wavfile):
    df=pd.DataFrame()
    y , y2 = None, None
    
    try:
        y2 = tap_filepath_local.main(wavfile, normalize=True)
        filename = wavfile
    except Exception as e:
        # print(f'Couldnt process file {wavfile}')
        # print(e)
        sound1 = AudioSegment.from_wav(wavfile)
        sound2 = AudioSegment.from_wav(wavfile)
        sound3 = AudioSegment.from_wav(wavfile)

        combined_sounds = sound1 + sound2 + sound3 
        wavfile_combined = _helper(wavfile, combined_sounds)
        filename = wavfile_combined
        try:
            y2 = tap_filepath_local.main(wavfile_combined, normalize=True)
        except Exception as e:
            sound4 = AudioSegment.from_wav(wavfile)
            combined_sounds = combined_sounds + sound4
            wavfile_combined = _helper(wavfile, combined_sounds)
            filename = wavfile_combined
            try:
                y2 = tap_filepath_local.main(wavfile_combined, normalize=True)
            except Exception as e:

                sound5 = AudioSegment.from_wav(wavfile)
                combined_sounds = combined_sounds + sound5
                wavfile_combined = _helper(wavfile, combined_sounds)
                filename = wavfile_combined
                try:
                    y2 = tap_filepath_local.main(wavfile_combined, normalize=True)

                except Exception as e:
                    sound6 = AudioSegment.from_wav(wavfile)
                    combined_sounds = combined_sounds + sound6
                    wavfile_combined = _helper(wavfile, combined_sounds)
                    filename = wavfile_combined
                    try:
                        y2 = tap_filepath_local.main(wavfile_combined, normalize=True)

                    except Exception as e:
                        sound7 = AudioSegment.from_wav(wavfile)
                        combined_sounds = combined_sounds + sound7
                        wavfile_combined = _helper(wavfile, combined_sounds)
                        filename = wavfile_combined
                        try:
                            y2 = tap_filepath_local.main(wavfile_combined, normalize=True)

                        except Exception as e:
                            sound8 = AudioSegment.from_wav(wavfile)
                            combined_sounds = combined_sounds + sound8
                            wavfile_combined = _helper(wavfile, combined_sounds)
                            filename = wavfile_combined
                            try:
                                y2 = tap_filepath_local.main(wavfile_combined, normalize=True)

                            except Exception as e:
                                sound9 = AudioSegment.from_wav(wavfile)
                                combined_sounds = combined_sounds + sound9
                                wavfile_combined = _helper(wavfile, combined_sounds)
                                filename = wavfile_combined
                                try:
                                    y2 = tap_filepath_local.main(wavfile_combined, normalize=True)

                                except Exception as e:
                                    print(f'Couldnt process file {wavfile}')
                                    print(e)
            
    # print(y2)
    y2['file'] = filename
    df = pd.concat([df,y2])
    return df