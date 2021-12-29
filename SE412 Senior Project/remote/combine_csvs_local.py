
import os
import pandas as pd
from time_function import time_function

@time_function
def combine_csv_files_in_folder(input_folder='/PreliminaryTraining/CONTEXT_DATASET/', 
                                output_folder='/PreliminaryTraining/ENTIRE_CONTEXT_DATASET/',
                                output_filename='news.csv'):
    cwd = os.getcwd()
    dataset_folder = cwd + input_folder
    output_dataset_folder = cwd + output_folder
    output_filepath = output_dataset_folder + output_filename

    if not os.path.isdir(dataset_folder):
        os.mkdir(dataset_folder)
        print(f'Created {dataset_folder}.\n')

    if not os.path.isdir(output_dataset_folder):
        os.mkdir(output_dataset_folder)
        print(f'Created {output_dataset_folder}.\n')
    
    print(f'Creating {output_filename}.\n')

    with open(output_filepath,'w',encoding='utf-8') as output_file:

        for filename in os.listdir(dataset_folder):

            print(f'Processing {filename}.')

            path_to_file = os.path.join(dataset_folder,filename)   

            with open(path_to_file,'r', encoding='utf-8', errors='ignore') as f:

                lines = f.readlines()

                data = lines[1:]

                for r in data:
                    output_file.write(r)
                
            print(f'Processed {filename}.\n')
    
    print(f'Finished creating {output_filename}.\n')
    
if __name__ == '__main__':
    combine_csv_files_in_folder()


