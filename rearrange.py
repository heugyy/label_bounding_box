# file = open("result.txt", "r")
# new_file = open('label.txt', 'w')
#
# for l in file:
#     new_l = l.split(',')
#     if new_l[0][0] == '/':
#         new_l0 = new_l[0].split('/')[3:]
#     else:
#         new_l0 = new_l[0].split('/')[1:]
#     new_l_0 = ''
#     for i in new_l0:
#         if "\\" in i:
#             new_ii = ''
#             for ii in i.split('\\'):
#                 new_ii += ii + '/'
#             i = new_ii[:-1]
#         new_l_0 += i + '/'
#     new_l_0 = new_l_0[:-1]
#     new_file.write(new_l_0)
#     for i in new_l[1:]:
#         new_file.write(', '+i)
#
# new_file.close()

"""
rearrange label.txt to train.txt and text.txt that fit yolo3
"""
import os

file = open("label.txt", "r")
train_file = open('train.txt', 'w')
test_file = open('test.txt', 'w')
names = []
num_per_class = {}
for l in file:
    new_l = l.split(',')
    new_l = [i.strip() for i in new_l]
    cls_name = new_l[1]
    if cls_name not in names:
        names.append(cls_name)
        num_per_class[cls_name] = 1
    else:
        num_per_class[cls_name] += 1
    if num_per_class[cls_name] > 450:
        test_file.write('E:/' + new_l[0] + '\n')
        folder_splits = new_l[0].split('/')
        folder_name = 'test/' + folder_splits[-2]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_name = '/' + folder_splits[-1].split('.')[0] + '.txt'
        test_label_file = open(folder_name + file_name, 'w')
        for i in range((len(new_l)-2)//4):
            if i:
                test_label_file.write(' ')
            x,y,w,h = (float(new_l[4+i*4]) + float(new_l[2+i*4]))/2,\
                      (float(new_l[5 + i*4]) + float(new_l[3 + i*4]))/2,\
                      float(new_l[4+i*4])-float(new_l[2+i*4]), \
                      float(new_l[5+i*4])-float(new_l[3+i*4])

            test_label_file.write(str(len(names)-1) + ' '
                                  + str(x) + ' '
                                  + str(y) + ' '
                                  + str(w) + ' '
                                  + str(h))
        test_label_file.close()

    else:
        train_file.write('E:/' + new_l[0] + '\n')
        folder_splits = new_l[0].split('/')
        folder_name = 'train/' + folder_splits[-2]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_name = '/' + folder_splits[-1].split('.')[0] + '.txt'
        train_label_file = open(folder_name + file_name, 'w')
        new_l = new_l[2:]
        for i in range(len(new_l)//4):
            if i:
                train_label_file.write(' ')
            x, y, w, h = (float(new_l[i*4]) + float(new_l[2 + i*4])) / 2, \
                         (float(new_l[1 + i*4]) + float(new_l[3 + i*4])) / 2, \
                         float(new_l[2 + i*4]) - float(new_l[i*4]), \
                         float(new_l[3 + i*4]) - float(new_l[1 + i*4])

            train_label_file.write(str(len(names) - 1) + ' '
                                  + str(x) + ' '
                                  + str(y) + ' '
                                  + str(w) + ' '
                                  + str(h))
        train_label_file.close()


train_file.close()
test_file.close()