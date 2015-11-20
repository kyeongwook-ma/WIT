from psd_tools import PSDImage
import psd_tools

class PSDHelper(object):

    path = "./img/"

    def __init__(self, file_name):
        self.file_name = file_name
        self.psd = PSDImage.load(file_name)

    def save2PNG(self):
        merged = self.psd.as_PIL()
        merged.save(self.path + self.file_name)

    def save_group_2_PNG(self):
        groups = filter(lambda x : isinstanc(x, psd_tools.Group), self.psd.layers)
        for group in groups: group.save(self.path + group.name)


psdhelper = PSDHelper('perfumeInfo_ver1.2.psd')
psdhelper.save2PNG()

