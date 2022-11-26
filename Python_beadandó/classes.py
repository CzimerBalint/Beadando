class BevetData:
  def __init__(self, name, amount, category, date):
    self.name = name
    self.amount = amount
    self.category = category
    self.date = date

  def __str__(self):
    return f"{self.name} {self.amount} {self.category} {self.date}"
