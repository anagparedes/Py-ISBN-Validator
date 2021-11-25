import isbn_validator

def is_valid(isbn):
  length = len(isbn)
  if length ==10:
   return True

  elif length ==13:
   return True
  else:
   return False

  