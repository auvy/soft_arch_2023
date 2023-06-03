class BL:
  def __init__(self):
    print("bl created")
  
  def __init__(self, dl_conn):
    print("bl created")
    self.dl = dl_conn
    
  def conn(self, dl_conn):
    self.dl = dl_conn
  
  def get_data(self):
    if hasattr(self, "dl"):
      return self.dl.get_all()
    else:
      return False