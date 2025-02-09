def pascalTriangle(rowIndex):
    if rowIndex==0:
        return [1]
    if rowIndex==1:
        return [1,1]

    if rowIndex>1:
        prev_list = pascalTriangle(rowIndex-1)
        i = 1
        new = [1, 1]
        while i<len(prev_list):
            new.insert(i, prev_list[i-1]+prev_list[i])
            i+=1
        return new

print(pascalTriangle(6))