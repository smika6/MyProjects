import pandas as pd
import os

train_target = 100 # number of articles per class
test_target = 10

def put_in_folder(type_, content, article_id, subdir):
    print(1)
    f = open(f"dataset/{subdir}/{type_}/{article_id}.txt", 'w')
    f.write(content)
    f.close()

classes = ["fake", "satire", "bias", "conspiracy", "state", "junksci", "hate", "clickbait", "unreliable", "political", "reliable"]

# df = pd.read_csv('news_001.csv')
# split = int(.8 * len(df))
# df_train = fd.iloc[:split]
# df_test = fd.iloc[split:]

train_counts = [0,0,0,0,0,0,0,0,0,0,0]
test_counts = [0,0,0,0,0,0,0,0,0,0,0]

row_num = 1
train_done = all(counts >= train_target for counts in train_counts)
test_done = all(counts >= test_target for counts in test_counts)
# for index, row in fd.iterrows():
path = '/content/drive/MyDrive/fullcontextnews_chunked'
file_list = os.listdir(path)
files = iter(file_list)
df = pd.read_csv(os.join(path,next(files)))
row_iterator = df.iterrows()
while not train_done or not test_done:
    row = next(row_iterator)[1]
    if row == None:
        df = pd.read_csv(os.join(path,next(files)))
        row_iterator = df.iterrows()
        row = next(row_iterator)[1]
    # print(row['1st_type'])
    # print(row)
    # print(2)
    if not train_done:
        # print(3)
        t = row['1st_type']
        print(t)
        if t in classes:
            i = classes.index(t)
            if train_counts[i] < train_target:
                train_counts[i] += 1
                put_in_folder(t, row['content'], row_num, 'train')
        t = row['2nd_type']
        if t in classes:
            i = classes.index(t)
            if train_counts[i] < train_target:
                train_counts[i] += 1
                put_in_folder(t, row['content'], row_num, 'train')
        t = row['3rd_type']
        if t in classes:
            i = classes.index(t)
            if train_counts[i] < train_target:
                train_counts[i] += 1
                put_in_folder(t, row['content'], row_num, 'train')
        row_num += 1
        print(train_counts)
        train_done = all(counts >= train_target for counts in train_counts)
    elif not test_done:
        t = row['1st_type']
        if t in classes:
            i = classes.index(t)
            if test_counts[i] < test_target:
                test_counts[i]+=1
                put_in_folder(t, row['content'], row_num, 'test')
        t = row['2nd_type']
        if t in classes:
            i = classes.index(t)
            if test_counts[i] < test_target:
                test_counts[i]+=1
                put_in_folder(t, row['content'], row_num, 'test')

        t = row['3rd_type']
        if t in classes:
            i = classes.index(t)
            if test_counts[i] < test_target:
                test_counts[i]+=1
                put_in_folder(t, row['content'], row_num, 'test')
        row_num += 1
        print(test_counts)
        test_done = all(counts >= test_target for counts in test_counts)
    else:
        print("broken")
        break
