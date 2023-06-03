class PL:
  def __init__(self):
    print("kk")
  
  def __init__(self, bl):
    self.blayer = bl
  
  def display(self, data):
    str = ''
    for d in data:
      str += f'Data: {d}\n'
    return str

  def display_bl(self):
    data = self.blayer.get_data()
    if data:
      return self.display(data)
    return 'no data'