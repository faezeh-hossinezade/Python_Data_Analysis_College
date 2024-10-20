# coding: utf-8
def my_any(x):
  t = True
  for item in x:
    if bool(item):
      return t
    else:
        t = False
        return t
