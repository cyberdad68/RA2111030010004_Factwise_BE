def max_score(points,k):
    tot_sum=sum(points)
    if k>=len(points):
        return tot_sum
    w_sum=sum(points[:k])
    max_sum=w_sum

    for i in range(1,k+1):
        w_sum=w_sum-points[k-i]+points[-i]
        max_sum=max(max_sum,w_sum)
    return max_sum
print(max_score([1,2,3,4,5,6,1],3))




        
