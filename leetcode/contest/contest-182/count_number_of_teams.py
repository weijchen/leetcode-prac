def numTeams(rating) -> int:
  """
  :type rating: List[int]
  :rtype: int
  """
  ret = []
  for one_id, one_val in enumerate(rating):
  	for two_id, two_val in enumerate(rating[one_id:]):
  		if two_val > one_val:
  			for three_id, three_val in enumerate(rating[one_id+two_id:]):
  				if three_val > two_val:
  					ret.append((one_val, two_val, three_val))

  for one_id, one_val in enumerate(rating):
  	for two_id, two_val in enumerate(rating[one_id:]):
  		if two_val < one_val:
  			for three_id, three_val in enumerate(rating[one_id+two_id:]):
  				if three_val < two_val:
  					ret.append((one_val, two_val, three_val))
  return len(ret)

numTeams(arr)