import pickle

def sav_dict(dict,path):
    with open(path,"wb") as file:
        pickle.dump(dict,file)

def load_dict(path):
    with open(path,"rb") as file:
        return pickle.load(file)
    
diction = {"a":1, "b":2, "c":3, "d":4, "e":5}
path = "SampleWrite.txt"

sav_dict(diction,path)
recovered=load_dict(path)
print(recovered)