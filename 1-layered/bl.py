class BL:
  def __init__(self, dl_conn):
    print("bl created")
    self.dl = dl_conn
  
  def get_data(self):
    return self.dl.get_all()