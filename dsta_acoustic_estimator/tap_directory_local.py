from tap import *

import os
from pathlib import Path
import argparse
import glob
import pandas as pd


def main(args):
    
    input_dir  = args.input_directory
    output_dir = args.output_directory
    
    if not Path(input_dir).is_dir():
        raise RuntimeError('Main Function Error: the input dir for waveform (wav) files \"' + input_dir + '\" does not exist!')
    
    if not Path(output_dir).is_dir():
        os.makedirs(output_dir)
    
    audioPathList = sorted(glob.glob(input_dir + '/*.wav'))
    acousticList = []

    for audioPath in tqdm(audioPathList):

        try:

            acoustics = get_acousticsFromAudioPath(ACOUSTIC_ESTIMATOR, audioPath)
            acoustics = acoustics.cpu().detach().numpy()
            
            acoustics = pd.DataFrame(acoustics, columns = ACOUSTIC_FEATURE_NAMES)
            acoustics.to_csv(path_or_buf = output_dir + '/' + audioPath.split('/')[-1].split('.wav')[0] + '.csv', index=False)

        except Exception as e:

            print('Main Function:\n {}'.format(e))

            continue
            
    return None

# Example Usage:
#
# get_acousticsFromAudioPathList(
#     estimator     = ACOUSTIC_ESTIMATOR,
#     audioPathList = ["/content/clean_fileid_0.wav", "/content/clean_fileid_0.wav"])

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input_directory" , 
        help = 'The input dir for the waveform (wav) file.' )

    parser.add_argument(
        "--output_directory" , 
        help = 'The output dir for the acoustic (csv) file.')

    args = parser.parse_args()

    main(args)
