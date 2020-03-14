import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import csv
import os

# data_path = 'E:/Yanyang/cycleGAN/classification/MoleMap/Micro_Macro_separate/macro'
# data_path = '/Volumes/Seagate Backup Plus Drive/Yanyang/cycleGAN/classification/Data/MoleMap_camera_7cls'
data_path = 'E:/Yanyang/cycleGAN/classification/Data/MoleMap_camera_7cls'
file_name = 'results.txt'
folder_list = os.listdir(data_path)



class TestClass():
    def __init__(self,file_name, folder,fname):
        self.fname = fname.split('/')[-1]
        self.img = mpimg.imread(fname)
        self.label = folder.split('_')[0]
        self.point = ()
        self.file = open("result.txt", "a")
        self.file.write('{}, {}'.format(fname, self.label))
        print(fname+self.label)

    def getCoord(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.imshow(self.img)
        cid = fig.canvas.mpl_connect('button_press_event', self.__onclick__)

        plt.show()

        return self.point

    def __onclick__(self,click):
        self.point = (click.xdata,click.ydata)
        numrows, numcols, _ = self.img.shape
        self.point = self.point[0]/numcols, self.point[1]/numrows
        self.file.write(', {:.4f}, {:.4f}'.format( self.point[0], self.point[1]))
        print('{:.4f}, {:.4f}'.format( self.point[0], self.point[1]))
        return self.point

    def close_file(self):
        self.file.write('\n')
        self.file.close()


# for folder in folder_list:
for folder in ['DF','MEL','NV','VASC']:
    folder_path= os.path.join(data_path,folder)
    cnt = 0
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path,img_name)
        img = TestClass(file_name, folder, img_path)
        img.getCoord()
        img.close_file()
        cnt+=1
        if cnt >= 500:
            break



