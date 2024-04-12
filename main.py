import os, sys 
import numpy as np 
import pandas as pd
from helper import get_tap_feature
from process_formulas import get_vqf, get_ocean

def extract_tap_features(audio_path):
    '''
    Given the directory containing all audio files (in wav format), 
    extract the TAP 25 llfs features and save them into csvs. 
    '''
    try:
        tap_feats = get_tap_feature(audio_path)
    except Exception as e:
        print(e)
        print('Tap feats could not be extracted')
    return tap_feats 

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
    vqfs_feats = get_vqf(tap_feats_avg)
    vqfs_list = []
    for name in vqfs: 
        vqfs_list.append(vqfs_feats[name])
    return tap_feats_dict, vqfs_feats, vqfs_list


def main(audio_path):
    # get the TAP feature 
    tap_feats = extract_tap_features(audio_path)

    # get the VQFs 
    _, vqfs_dict, vqfs_list = get_vqf_feature_from_feats(tap_feats)
    # get the OCAEN traits 

    ocean_dict = get_ocean(vqfs_list)

    print(vqfs_dict)
    print(ocean_dict)
    
    return 

if __name__ == '__main__':
    llfs = ['Loudness', 'alphaRatio', 'hammarbergIndex', 'slope0-500', 'slope500-1500', 'spectralFlux', 'mfcc_coeff1', 'mfcc_coeff2', 'mfcc_coeff3', \
            'mfcc_coeff4', 'F0_semitone_From27.5Hz', 'jitter_local', 'shimmer_local_dB', 'HNRdBACF', 'logRelF0-H1-H2', 'logRelF0-H1-A3', 'F1_frequency', \
            'F1_bandwidth', 'F1_amplitudeLogRelF0', 'F2_frequency', 'F2_bandwidth', 'F2_amplitudeLogRelF0', 'F3_frequency', 'F3_bandwidth', 'F3_amplitudeLogRelF0']# llf 
        
    vqfs = ['Coveredness' ,'Aphonicity' ,'Biphonicity','Breathiness','Creakiness','Diplophonicity','Flutter','Glottalization','Hoarseness','Roughness',\
            'Nasality','Jitter','Pressed','Pulsed','Resonant','Shimmer','Strained','Strohbassness','Tremor','Twanginess','Ventricular','Wobble','Yawniness','Loudness']

    ##
    audio_path = sys.argv[1] 
    main(audio_path)