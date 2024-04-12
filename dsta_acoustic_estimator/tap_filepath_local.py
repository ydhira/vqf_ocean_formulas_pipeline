from tap import *

import argparse
import glob
import torch
import pandas as pd
from pathlib import Path

def main(input_filepath, normalize):

    # input_filepath  = args.input_filepath
    # output_filepath = args.output_filepath
    
    if not Path(input_filepath).is_file():
        raise RuntimeError('Main Function Error: the input path for waveform (wav) files \"' + input_filepath + '\" does not exist!')
        
    acoustics = get_acousticsFromAudioPath(
        ACOUSTIC_ESTIMATOR                        ,
        audioPath = input_filepath, normalize = normalize )
    
    acoustics = pd.DataFrame(
        data    = acoustics              ,
        columns = ACOUSTIC_FEATURE_NAMES )
    # print(acoustics)
    # acoustics.to_csv(
    #     path_or_buf = output_filepath ,
    #     index       = None        )
    return acoustics

if __name__=="__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input_filepath" , 
        help = 'The input file path for the waveform (wav) file.' )

    parser.add_argument(
        "--output_filepath" , 
        help = 'The output file path for the acoustic (csv) file.')

    args = parser.parse_args()

    main(args)
