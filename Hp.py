import Data_Structures as ds
import random


def get_random_model(num_of_boxes):
    random.seed(47)
    boxList = [ds.Box(float(random.randint(1, 10)), float(random.randint(1, 10)), float(random.randint(1, 10))) for i in range(num_of_boxes)]
    return ds.PalletizationModel(ds.Bin(10, 10, 10), boxList)

def get_random_box_list(num_of_boxes):
    random.seed(47)
    boxList = [ds.Box(float(random.randint(1, 10)), float(random.randint(1, 10)), float(random.randint(1, 10))) for i in range(num_of_boxes)]
    return boxList

def get_fixed_model(num_of_boxes):
    random.seed(47)
    boxList = [ds.Box(70, 70, 70) for i in range(num_of_boxes)]
    return ds.PalletizationModel(ds.Bin(100.0, 100.0, 100.0), boxList)

if __name__ == '__main__':
    bin = ds.Bin(10, 10, 10)
    box_list = get_random_box_list(20)
    s = ds.Search(bin, box_list)
    res = s.backtracking_search(ds.PalletizationModel(bin, box_list))
    print "ue"
