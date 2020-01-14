def add_all(t):
    total = 0
    for x in t:
      total += x
    return total
  
 def capitalize_all(t):
     res = []
     for s in t:
         res.apped(s.capitalize())
     return res
  
  
  def only_upper(t):
      res = []
      for s in t:
        if s.isupper():
          res.append(s)
      return res
