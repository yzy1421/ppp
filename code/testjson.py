import json
import os
import ast
os.chdir('/home/zy3/Project_SC/finaljson')
file='finaljson.json'
with open(file, 'r') as load_f:
    #load_dict = json.loads(load_f)
    #print(load_dict[-1])
    json_data=ast.literal_eval(load_f)
    print(json.dumps(json_data))

path='/home/zy3/Downloads/Scene-Classification-master/datao/ai_challenger_scene_train_20170904'
file='scene_train_annotations_20170904.json'
with open(file, 'r') as load_f:
    load_dict = json.loads(load_f)
    print(load_dict[-1])
    # json_data=ast.literal_eval(load_f)
    # print(json.dumps(json_data))
