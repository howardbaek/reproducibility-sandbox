import os
from pathlib import Path
import pyrefinebio

# Define the directory path
data_dir: Path = Path('data/SRP070849')

# Define the data file path
data_file: Path = Path(os.path.join(data_dir, 'SRP070849.tsv'))

# Define the metadata file path
metadata_file: Path = Path(os.path.join(data_dir, 'metadata_SRP070849.tsv'))

# Try to create the directory
try:
  os.mkdir(data_dir, mode = 0o777)
except OSError as error:  # Catch the OSError exception
  print(error)

# If data or metadata files do not exist, download the data
if not data_file.exists() or not metadata_file.exists():

    print("Downloading SRP070849 from refine.bio")

    # Create a token for downloading the data
    pyrefinebio.create_token(agree_to_terms=True, save_token=False)

    # Download the dataset
    pyrefinebio.download_dataset(
      "data/dataset.zip",
      "cansav09@gmail.com",
      experiments=["SRP070849"],
      extract=True
    )
