def NULL_not_found(object: any)-> int:
  
  obj = type(object)

  if (object == None):
    print("Nothing: ", object , obj)
  elif (object != object):
    print("Cheese: ", object, obj)
  elif(obj == False):
    print("Fake: ", object, obj)
  elif(object == 0):
    print("Zero: ", object, obj)
  elif(object == ''):
    print("Empty: ", obj)
  else:
    print("Type not Found")
    return 1
  return 0