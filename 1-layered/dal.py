class DAL:
  def __init__(self):
    print("ok")
  
  def __init__(self, connection):
    print("connected idk")
    self.db = connection
  
  def connect(self, connection):
    # pretend that connection is not a list lol
    print("reconnected")
    self.db = connection
  
  def create(self, data):
    self.db.append(data)
  
  def get_all(self):
    if self.db:
      return self.db
    return False

  def get_one(self, id):
    if id < len(self.db) - 1:
      return self.db[id]
    return False
  
  def delete(self, id):
    del self.db[-id]