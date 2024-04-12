# Temporal Acoustic Parameter Estimator

This project provides a temporal acoustic parameter estimator, including frequency, energy, amplitude, and spectral features. 

## Setup

1. Download Package Archive
```bash
wget -q https://cmu.box.com/shared/static/c0nki93s9du5rcdzpt6pjrssx26oiymt --content-disposition --show-progress
```

2. Extract Package Archive
```bash
unzip -q tap.zip
```

3. Change Directory To ./tap
```
cd tap
```

4. Install the required packages to use this code:

```python
pip install -r requirements.txt 
```


## Code and Files 

In this codebase, we provide code that can take as input paths to wav files and write as output the features in csv files.
To run the code on single files, you may use `tap_filepath_local.py` and to perform the computation on a directory comprising multiple wav files, 
you may use `tap_filepath_local.py`.


- `tap_filepath_local.py` 

```
usage:
‎
# Generate Acoustics Given Waveform Filepath
python tap_filepath_local.py \
    --input_filepath  ./example/tap_filepath_example/example_waveform_0.wav \
    --output_filepath ./example/tap_filepath_example/example_acoustic_0.csv
‎
arguments:

    --input_filepath   The input file path for the waveform (wav) file.
    --output_filepath  The output file path for the acoustic (csv) file.
```

- `tap_directory_local.py`
```
usage:
‎
# Generate Acoustics Given Waveform Directory
python tap_directory_local.py \
    --input_directory  ./example/tap_directory_example/example_waveform_directory \
    --output_directory ./example/tap_directory_example/example_acoustic_directory
‎
arguments:

    --input_directory   The input directory for the waveform (wav) files.
    --output_directory  The output directory for the acoustic (csv) files.
```
