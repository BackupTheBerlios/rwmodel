import pickle

#store object
def serialize(obj, filename):
  filehandler = open(filename,'w')
  pickle.dump(obj, filehandler)

#get object
def deserialize(filename):
  filehandler = open(filename,'r')
  return pickle.load(filehandler)
