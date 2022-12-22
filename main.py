class Patient:
  def __init__(self, id, name, ssn):
    self.__id = id
    self.__name = name
    self.__ssn = ssn
    
  def setId(self, newId):
    self.__id = newId

  def getId(self):
    return self.__id

  def setName(self, newName):
    self.__name = newName

  def getName(self):
    return self.__name

  def setSsn(self, newSsn):
    self.__ssn = newSsn

  def getSsn(self):
    return self.__ssn

obj1 = Patient(1, "Josh", 5050)
print("**using getter**")
print(obj1.getId())
print(obj1.getName())
print(obj1.getSsn())

print("")
print("**using setter**")

obj1.setId(100)
obj1.setName("JoshHerr")
obj1.setSsn(6060)

print(obj1.getId())
print(obj1.getName())
print(obj1.getSsn())

#