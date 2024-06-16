"""DATA IMPORT"""

import pandas as pd
import torchaudio
import os

# Paths to metadata files
current_directory = os.path.dirname(os.path.abspath(__file__))

train_metadata_path = os.path.join(current_directory, 'it/train.tsv')
dev_metadata_path = os.path.join(current_directory, 'it/dev.tsv')
tst_metadata_path = os.path.join(current_directory, 'it/test.tsv')
validated_metadata_path = os.path.join(current_directory, 'it/validated.tsv')


# Load metadata into pandas DataFrame
train_df = pd.read_csv(train_metadata_path, sep='\t')
dev_df = pd.read_csv(dev_metadata_path, sep='\t')
tst_df = pd.read_csv(tst_metadata_path, sep='\t')
validated_df = pd.read_csv(validated_metadata_path, sep='\t')


# Example: here is the column where path to audio is stored
print("PATH IS")
print(train_df.iloc[0]['path'] )

#LOAD AUDIO
audio_path = os.path.join(current_directory, 'it/clips', train_df.iloc[0]['path'] + ".mp3")
print(f"Audio file path: {audio_path}")

waveform, sample_rate = torchaudio.load(audio_path)

print(f"Loaded audio file: {audio_path}")
print(f"Waveform shape: {waveform.shape}")
print(f"Sample rate: {sample_rate}")
