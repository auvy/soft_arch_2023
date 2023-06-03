class DAL:
  def __init__(self):
    print("ok")
  
  def connect(self, connection):
    # pretend that connection is not a list lol
    print("reconnected")
    self.db = connection
  
  def create(self, data):
    if hasattr(self, "db"):
      self.db.append(data)
    else:
      return False
  
  def get_all(self):
    if hasattr(self, "db"):
      return self.db
    return False

  def get_one(self, id):
    if id < len(self.db) - 1:
      return self.db[id]
    return False
  
  def delete(self, id):
    del self.db[-id]