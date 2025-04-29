# get data from kaggle dataset

import os
import kagglehub
import shutil


def download_kaggle_dataset(output_dir, dataset_name='zillow/zecon'):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Download the dataset
    path = kagglehub.dataset_download(
        dataset_name
    )
    # move the file to data/[dataset_name]
    shutil.move(path, output_dir)
    

if __name__ == "__main__":
    # Define the dataset name and output directory
    dataset_name = 'rounakbanik/the-movies-dataset'
    output_dir = 'data/the-movies-dataset'
    # Check if the dataset is already downloaded 
    if os.path.exists(output_dir):
        print(f'Dataset already exists at {output_dir}')
    else:
        # Download the dataset
        download_kaggle_dataset(output_dir, dataset_name)

    print(f'Dataset downloaded and extracted to {output_dir}')
    