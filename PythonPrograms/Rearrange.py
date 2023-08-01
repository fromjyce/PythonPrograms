# A list with negative elements at the left and positive elements at teh right and zero at the end
def rearrange(lst):
  zeroes = []
  return_lst = []
  for num in lst:
    if num<1 and num!=0:
      return_lst.append(num)
    if num==0:
      zeroes.append(num)
  for num in return_lst:
    if num in lst:
      lst.remove(num)
  for num in zeroes_lst:
    if num in lst:
      lst.remove(num)
  return_lst.extend(lst)
  if zeroes_lst:
    for num in zeroes_lst:
      return_lst.append(num)
  return return_lst
