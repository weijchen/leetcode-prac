def findLucky(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    dic = {each: arr.count(each) for each in arr}
    cor = [k for k,v in dic.items() if k == v]
    ret = max(cor) if len(cor) > 0 else -1

    return ret
    
findLucky(arr)