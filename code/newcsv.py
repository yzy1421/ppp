import pandas as pd
import os

#Function to produce new csv
def newcsv(path,finalpath):
    os.chdir(path)
    folder = os.walk(path)
    files = list(folder)[0][2]
    print(files)
    for file in files:
        filepath = path + '/' + file
        filename = file.split('.')[0]
        data = pd.read_csv(filepath, engine='python')
        col_name = data.columns.tolist()
        col_name.insert(col_name.index('time'), 'image_id')
        datanew = data.reindex(columns=col_name)[['image_id', 'Types']]
        datanew = datanew.rename(columns={'Types': 'label_id'})
        for i in range(len(datanew.index)):
            datanew.loc[i, 'image_id'] = '%s_time%d.jpg' % (filename, i)

        os.chdir(finalpath)
        datanew.to_csv('%s.csv' % filename, header=True, index=False)
        os.chdir(path)

#path='/home/zy3/Documents/testcsv'
path='/home/zy3/Documents/FINALDATA/CSV'
finalpath='/home/zy3/Project_SC/newcsv'
newcsv(path,finalpath)