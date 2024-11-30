#  Objective Measurements of Voice Quality and Personality OCEAN Traits

## Description 

This project documents the code and pipeline used in the paper titled `Objective Measurements of Voice Quality and Personality OCEAN Traits'. 
The work proposes formulation for extracting voice quality features and OCEAN personality traits from a given speech sample. 
The steps required for extracting the features: 
1. Input a speech file in .wav format 
2. Extract low level speech features 
3. Extract voice quality features 
4. Extract OCEAN personality traits 

## Usage 

### Extract low level speech features: 
We narrow down low level speech features to a list of 25 features. Some of these features are alphaRatio, hammarbargIndex, F1-frequency, etc. 
We use the Temporal Acoustic Parameter (TAP) model [1]. The model is trained on speech data and is trained for predicting the opensmile features. It is shown to be robust in predicting the low level speech features. 

### Extracting voice quality features: 
We narrow down voice qualities to a list of 24 voice qualities. This list includes breathiness, nasality, coveredness, aphonicty, loudness, etc. For the full list of voice qualities, please read our paper. We then propose formulae that extract the voice qualities based on the low level speech features. These formulae can be found in the file [CITE]. Please look into function: [CITE]. 

### Extracting OCEAN traits: 
We represent personality using the OCEAN traits. These traits are Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We propose formulae for the OCEAN traits from the 24 voice qualities. These formulae are listed in [CITE] file. 

Run 
python main.py <audiopath>



## Contact

Hira Dhamyal - hyd@cs.cmu.edu

Project Link: [https://github.com/ydhira/voicequeslityformulae/tree/master](https://github.com/ydhira/voicequeslityformulae/tree/master)


[1] Y. Zeng, J. Konan, S. Han, D. Bick, M. Yang, A. Kumar, S.Watanabe, and B. Raj, “Taploss: A temporal acoustic parameter loss for speech enhancement,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5.