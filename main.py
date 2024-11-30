import sys 
import numpy as np 
from helper import get_tap_feature
from process_formulas import get_vqf, get_ocean

def extract_tap_features(audio_path):
    '''
    Given the directory containing all audio files (in wav format), 
    extract the TAP 25 llfs features and save them into csvs. 
    Input: 
        audio_path: 
            Path of the audio file 
    Return: 
        tap_feats (np.array): 
            np array of shape T x 25
    '''
    try:
        tap_feats = get_tap_feature(audio_path)
    except Exception as e:
        print(e)
        print('Tap feats could not be extracted')
    tap_feats = np.array(tap_feats)[:,:25].astype(np.float64)
    return tap_feats 

def get_vqf_feature_from_feats(tap_feats, hyperparam_dataset, take_mean = True):
    '''
    Given TAP feature file,
    get 24 VQF from the 25 llfs.
    Input: 
        tap_feats (pandas dataframe): 
            list of 25 low level features of the shape of T x 25 where 
            T is the time. 
        hyparam_dataset (str):
            Dataset name from which the mean and std statistics are used for voice quality formulae. 
        take_mean (bool)
    Returns: 
        1. vqfs_feats (dict): dictionary form of the voice quality features. 
        2. vqfs_list (np.array): list form of the voice quality formulae. 24 or T x 24 , if take_mean - True or False respectively 
    '''
    # column_names = llfs
    # tap_feats = pd.DataFrame(data=tap_feats, columns=column_names )
    if take_mean: 
        tap_feats_ = np.mean(tap_feats, axis=0) # shape = 25 
        # tap_feats_avg = np.array(tap_feats_avg[llfs]) 
    else: 
        tap_feats_ = tap_feats.transpose() # 25 x T 
    #     tap_feats_avg = np.array(tap_feats) # T x 25 

    vqfs_feats = get_vqf(tap_feats_, hyperparam_dataset)
    vqfs_list = []
    for name in vqfs: 
        vqfs_list.append(vqfs_feats[name])
    vqfs_list=np.array(vqfs_list).transpose()
    return vqfs_list

def get_ocean_from_vqf(vqfs, take_mean = True):
    '''
    Given the VQF feature, gets the 5 OCEAN traits. 
    Input: 
        vqfs (np.array):
            T x 24 
        take_mean (bool):
            if True, then the mean of the vqfs is taken, otherwise not. 
    Return: 
        1. ocean (np.array):
            list of the OCEAN trait. 5 or T x 5 depending if take_mean=True or False respectively. 
    '''
    if take_mean:
        vqfs_ = np.mean(vqfs, axis=0)
    else: 
        vqfs_ = np.array(vqfs).transpose()
    ocean_dict = get_ocean(vqfs_)
    ocean = []
    for name in ocean_traits: 
        ocean.append(ocean_dict[name])
    ocean = np.array(ocean).transpose()
    return np.array(ocean)

def main(audio_path):
    # get the TAP feature 
    tap_feats = extract_tap_features(audio_path)

    # get the VQFs 
    vqfs_list = get_vqf_feature_from_feats(tap_feats, 'sre', take_mean=False)
    
    # get the OCAEN traits 
    ocean_list = get_ocean_from_vqf(vqfs_list, take_mean=False)
    
    return vqfs_list, ocean_list

if __name__ == '__main__':
    llfs = ['Loudness', 'alphaRatio', 'hammarbergIndex', 'slope0-500', 'slope500-1500', 'spectralFlux', 'mfcc_coeff1', 'mfcc_coeff2', 'mfcc_coeff3', \
            'mfcc_coeff4', 'F0_semitone_From27.5Hz', 'jitter_local', 'shimmer_local_dB', 'HNRdBACF', 'logRelF0-H1-H2', 'logRelF0-H1-A3', 'F1_frequency', \
            'F1_bandwidth', 'F1_amplitudeLogRelF0', 'F2_frequency', 'F2_bandwidth', 'F2_amplitudeLogRelF0', 'F3_frequency', 'F3_bandwidth', 'F3_amplitudeLogRelF0']# llf 
        
    vqfs = ['Coveredness' ,'Aphonicity' ,'Biphonicity','Breathiness','Creakiness','Diplophonicity','Flutter','Glottalization','Hoarseness','Roughness',\
            'Nasality','Jitter','Pressed','Pulsed','Resonant','Shimmer','Strained','Strohbassness','Tremor','Twanginess','Ventricular','Wobble','Yawniness','Loudness']

    ocean_traits = ['Openness','Conscientiousness','Extraversion','Agreeableness','Neuroticism']
    ##
    audio_path = sys.argv[1] 
    vqfs_list, ocean_list = main(audio_path)
    print("voice quality: ")
    print(vqfs_list)
    print("OCEAN Traits: ")
    print(ocean_list)