import json
import os
# path='/home/zy3/Project_SC/a'
# file='20160211_083022_2018-03-20.json'
# os.chdir(path)
# f=open(os.path.join(path,file),'r')
# json_dic=json.load(f)

# f.close()
# print(json_dic)
# print(type(json_dic))
# #
# with open('finaljson.json', 'w') as finaljson:
#     dict = json.dumps(json_dic)
#     finaljson.write(dict)
#
# final='finaljson.json'
# ff=open(os.path.join(final),'r')
# j=json.load(ff)
# print(j)
# path='/home/zy3/Downloads/Scene-Classification-master/datao/ai_challenger_scene_train_20170904'
# file='scene_train_annotations_20170904.json'
# f=open(os.path.join(path,file),'r')
# json_lst=json.load(f)
# json_dict=json.loads(jsonm)
# print(json_dic)
# print(type(json_dic))

# final='finaljson.json'
# with open(final,'r') as fina:
#     fa=json.load(fina)
#     print(fa)
# path='/home/zy3/Project_SC/finaljson'
# file='finaljson.json'
# os.chdir(path)
# f=open(os.path.join(path,file),'r')
# json_dic=json.load(f)
# print(json)

# import json
# import os
# def json_select(path,finalpath):
#
#     #path = '/home/zy3/Documents/testcsv/newcsv/testjson/'
#     os.chdir(path)
#     folder = os.walk(path)
#     files = list(folder)[0][2]
#     lst=[]
#     for file in files:
#         #filepath = path + '/' + file
#         #filename = file.split('.')[0]
#         #filename = '20160211_083022_2018-03-20.json'
#         #print(file)
#         with open(os.path.join(path,file), 'r') as load_f:
#             load_dict = json.load(load_f)
#         n = len(load_dict)
#         #print(n,end='')
#         i = 0
#         #finalpath = '/home/zy3/Documents/testcsv/newcsv/'
#
#         while i <= n-1:
#
#             lst.append(load_dict[i])
#             i += 100
#                 #print(n,i)
#         os.chdir(finalpath)
#         with open('tfinaljson.json','w') as f:
#             out=json.dumps(lst)
#             f.write(out)
path = '/home/zy3/Project_SC/finaljson'
# finalpath = '/home/zy3/Project_SC/finaljson'
# #path = '/home/zy3/Project_SC/a'
# json_select(path,finalpath)

final='tfinaljson.json'
ff=open(os.path.join(path,final),'r')
j=json.load(ff)
print(j)