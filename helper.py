import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sys 
import tqdm 
import glob 
import os 
from pydub import AudioSegment

sys.path.append('/ocean/projects/cis220031p/hyd/dsta_acoustic_estimator')
import tap_filepath_local
sys.path.append('/ocean/projects/cis220031p/hyd/personality/vqfs/')
import process_formulas

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


def get_opensmile_feature(opensmilefile):
    '''
    Given opensmile feature file, 
    get 24 VQF from the 25 llfs. 
    '''
    feats = np.load(opensmilefile)
    tap_feats_avg = np.mean(feats, axis=0)
    tap_feats_dict = {name: feat for name, feat in zip(llfs, tap_feats_avg)}
    vqfs = process_formulas.get_vqf(tap_feats_avg)
    return tap_feats_dict, vqfs

def get_vqf_feature(tapfile):
    '''
    Given TAP feature file,
    get 24 VQF from the 25 llfs.
    '''

    tap_feats = pd.read_csv(tapfile)
    column_names = list(tap_feats.columns)
    tap_feats = tap_feats.drop(columns=['file', 'Unnamed: 0'])
    tap_feats_avg = np.mean(tap_feats, axis=0)
    tap_feats_dict = tap_feats_avg.to_dict()
    tap_feats_avg = np.array(tap_feats_avg[llfs])
    print(tap_feats_avg)
    vqfs = process_formulas.get_vqf(tap_feats_avg)
    return tap_feats_dict, vqfs

def get_vqf_feature_from_feats(tap_feats):
    '''
    Given TAP feature file,
    get 24 VQF from the 25 llfs.
    '''
    column_names = llfs
    tap_feats = pd.DataFrame(data=tap_feats, columns=column_names )
    # tap_feats = tap_feats.drop(columns=['file', 'Unnamed: 0'])
    tap_feats_avg = np.mean(tap_feats.astype(np.float64), axis=0)
    tap_feats_dict = tap_feats_avg.to_dict()
    tap_feats_avg = np.array(tap_feats_avg[llfs])
    vqfs_feats = process_formulas.get_vqf(tap_feats_avg)
    vqfs_list = []
    for name in vqfs: 
        vqfs_list.append(vqfs_feats[name])
    return tap_feats_dict, vqfs_list

def extract_tap_features(indir):
    '''
    Given the directory containing all audio files (in wav format), 
    extract the TAP 25 llfs features and save them into csvs. 
    '''
    all_audio_files = glob.glob(indir+'/*.wav')

    for wavfile in all_audio_files:
        outfile = wavfile.replace('Audio_clips', 'tap_feats').replace('.wav', '.csv')
        if os.path.isfile(outfile): continue
        print(f'extracting tap for {outfile}')
        try:
            df = get_tap_feature(wavfile)
            # print(df)
        except Exception as e:
            print(e)
            continue
        
        # print('Writing to file: ')
        # print(outfile)
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        df.to_csv(outfile)

def get_llf_vqf(indir_tap, indir_opensmile, use='tap'):
    '''
    Given directory for saved feature files
    return a dictionary with the llf and vqf feats
    for each file
    '''
    if use == 'tap':
        indir = indir_tap 
        all_audio_files = glob.glob(indir+'/*.csv') # tap features
        all_audio_files = all_audio_files[:1]
    else:
        indir = indir_opensmile
        all_audio_files = glob.glob(indir+'*/*.npy') # opensmile features 
    
    vqfs_dict = {}
    llfs_dict = {}
   
    for tapfile in all_audio_files:
        basename = os.path.splitext(os.path.basename(tapfile))[0]
        vq = basename.split('_')[0]
        basename = ('_').join(basename.split('_')[1:]).split('.')[0]
        # try:
        if use == 'tap':
            tap_feats, vqf_feats = get_vqf_feature(tapfile)
        else:
            tap_feats, vqf_feats = get_opensmile_feature(tapfile)
        vqfs_dict[basename] = vqf_feats
        llfs_dict[basename] = tap_feats
        # except Exception as e:
        #     print(e)
        #     print('Error in fetching vqf')
        #     continue
        print(vqf_feats)
        print(tap_feats)

    return llfs_dict, vqfs_dict