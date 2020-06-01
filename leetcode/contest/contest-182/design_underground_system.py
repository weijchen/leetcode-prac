class UndergroundSystem(object):

  def __init__(self):
    self.inBook = {}
    self.outBook = {}
    self.passenger = []

  def checkIn(self, id, stationName, t):
    """
    :type id: int
    :type stationName: str
    :type t: int
    :rtype: None
    """
    if stationName not in self.inBook.keys():
      self.inBook[stationName] = dict()
    if id not in self.inBook[stationName].keys() and id not in self.passenger:
      self.inBook[stationName][id] = t
      self.passenger.append(id)
          
  def checkOut(self, id, stationName, t):
    """
    :type id: int
    :type stationName: str
    :type t: int
    :rtype: None
    """
    if stationName not in self.outBook.keys():
      self.outBook[stationName] = dict()
    if id not in self.outBook[stationName].keys():
      self.outBook[stationName][id] = t
      self.passenger.pop(self.passenger.index(id))

  def getAverageTime(self, startStation, endStation):
    """
    :type startStation: str
    :type endStation: str
    :rtype: float
    """
    start = self.inBook[startStation]
    end = self.outBook[endStation]
    id_start = list(set(list(start.keys())))
    id_end = list(set(list(end.keys())))
    tm = [(end[idx], start[idx]) for idx in id_end if idx in id_start]
    tm_diff = [float(t[0]-t[1]) for t in tm]
    return int(sum(tm_diff)/len(tm_diff))
