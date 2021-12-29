import os
import pandas as pd
from time_function import time_function
import combine_csvs_local  # import combine_csv_files_in_folder

classes = ["fake", "satire", "bias", "conspiracy", "state", "junksci",
           "hate", "clickbait", "unreliable", "political", "reliable"]

test_classes_count = [0,0,0,0,0,0,0,0,0,0,0]
train_classes_count = [0,0,0,0,0,0,0,0,0,0,0]
    
def put_in_folder(content, type1, type2, type3, subdir, article_id, classes_count):

    types = [type for type in classes if type in [
        type1, type2, type3] and len(type) != 0]

    for t in types:

        classes_count[classes.index(t)] += 1

        fn = f"dataset/{subdir}/{t}/{article_id}.txt"
        with open(fn, 'w', encoding="utf-8") as f:
            f.write(str(content))


@time_function
def partition_dataset_locally_from_entire_dataset():

    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
        os.mkdir('dataset/train')
        os.mkdir('dataset/test')

        for cl in classes:
            os.mkdir(os.path.join("dataset/train", cl))
            os.mkdir(os.path.join("dataset/test", cl))

    cwd = os.getcwd()

    dataset_folder = cwd + '/PreliminaryTraining/ENTIRE_CONTEXT_DATASET/'

    filename = 'news.csv'

    path_to_file = os.path.join(dataset_folder, filename)

    if not os.path.exists(path_to_file):
        combine_csvs_local.combine_csv_files_in_folder()
        print(f'Created {path_to_file}')

    print(f'Proccessing {path_to_file}')

    df = pd.read_csv(path_to_file, low_memory=False,
                     names=['domain', 'title', 'content', '1st_type', '2nd_type', '3rd_type'])

    df = df[['content', '1st_type', '2nd_type', '3rd_type']]

    df = df.sample(frac=1)

    print(f'Proccessed {path_to_file}')

    split = int(.8 * len(df))

    print(f'\nProccessing test')

    df_test = df.iloc[split:]

    df_test[:50000].apply(lambda x:
                  put_in_folder(x['content'], x['1st_type'], x['2nd_type'], x['3rd_type'], 'test', x.name, test_classes_count), axis=1)

    del(df_test)

    print(f'Proccessed test')

    print(f'\nProccessing train')

    df_train = df.iloc[:split]

    df_train[:50000].apply(lambda x:
                   put_in_folder(x['content'], x['1st_type'], x['2nd_type'], x['3rd_type'], 'train', x.name, train_classes_count), axis=1)

    del(df_train, df)

    print(f'Proccessed train')

    print(classes)
    print('test\t',test_classes_count)
    print('train\t',train_classes_count)

if __name__ == "__main__":
    partition_dataset_locally_from_entire_dataset()
