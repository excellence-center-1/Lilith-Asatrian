#  Առկա են  2 ֆակուլտատիվ կուրսեր՝ մաթեմատիկա և ինֆորմատիկա, որոնց գրանցվել են ուսանողներ։
#  Անհրաժեշտ է գտնել․
#  1)այն ուսանողների քանակը, որոնք գրանցվել են 2 կուրսին էլ,
#  2)գտնել այն ուսանողների քանակը, որոնք գրանցվել են գոնե մեկ կուրսի, 
#  3)գտնել միայն մաթեմատիկա և միայն ինֆորմատիկա կուրսերին գրանցված ուսանողներին,
#  4)Արտածել այն ուսանողների անունները, որոնք գրանցվել են 2 կուրսերին էլ, 
#  5)Արտածել այն ուսանողների անունները, որոնք գրանցվել են միայն մեկ կուրսի, կուրսի նշումը կողքին

def student(n):
    st = []
    for _ in range(n):
        surname = input("Enter surname: ")
        st.append(surname)
    return set(st)
try:
    n = int(input("Students' quantity who applied for Mathematics: "))
    if n<=0:  
        raise Exception("n must be natural!")
    st_math = student(n)
    m = int(input("Students' quantity who applied for Informatics: "))
    if m<=0:
        raise Exception("m must be natural!")
    st_inform = student(m)

    print()
    inter = st_math & st_inform
    print("Both maths and informatics courses applied students' count: ", len(inter))
    print("Both maths and inform students surnames:")
    for i in inter:
        print(i, end=' ')
    print()
    at_least_one = st_math | st_inform
    print("At least one course applied students' count: ", len(at_least_one))
   
    only_math = st_math - st_inform
    only_inform = st_inform - st_math
    union_of_all = only_math | only_inform
    print("Only math course applied students' count: ", len(only_math))
    print("Only math course applied students' surnames: ")
    for i in only_math:
        print(i, end=" ")
    print()

    print("Only informatics course applied students' count: ", len(only_inform))
    print("Only informatics course applied students' surnames: ")
    for i in only_inform:
        print(i, end=" ")
    print()
    print("Only one course applied students' surnames: ", len(union_of_all))
except Exception as e:
    print("Unexpected exception occured: ", e)
except ValueError as e:
    print("Convertation failed: ", e)