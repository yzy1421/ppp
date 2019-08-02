import csv
import json
import os
#path='/home/zy3/Documents/testcsv/newcsv'
path='/home/zy3/Project_SC/newcsv'
os.chdir(path)
#os.mkdir('testjson')

def csv_to_json(path,finalpath):
    # path='/home/zy3/Documents/testcsv/newcsv'

    folder = os.walk(path)
    files = list(folder)[0][2]
    os.chdir(path)
    for file in files:
        filepath = path + '/' + file
        csvfile = open(filepath, 'r')


        fieldnames = ('image_id', 'label_id')

        reader = csv.DictReader(csvfile, fieldnames)

        out = json.dumps([row for row in reader])
        os.chdir(finalpath) #should be changed
        jsonfile = open('%s.json' % file.split('.')[0], 'w')
        out='['+out[51:]
        jsonfile.write(out)

finalpath='/home/zy3/Project_SC/testjson'
csv_to_json(path,finalpath)