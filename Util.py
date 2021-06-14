#-------------------------------------------------------------------------------
# util.py
#-------------------------------------------------------------------------------

class Participant:
  def __init__(self, id, name, lptype, date, email, subject):
      self._id = id
      self._name = name
      self._date = date
      self._lptype = lptype
      self._email = email
      self._topic = subject

  def __str__(self):
      return str(self._id) + ', ' + self._email + ', ' + self._name + ', ' + self._date + \
          self._lptype + ', ' + self._topic
    
  def getId(self):
    return self._id

  def getName(self):
    return self._name

  def getDate(self):
    return self._date

  def getLPtype(self):
    return self._lptype

  def getEmail(self):
    return self._email

  def getTopic(self):
    return self._topic
