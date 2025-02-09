# Առցանց խանութում ամեն օր կատարվում են տարբեր գործարքներ։ 
# Յուրաքանչյուր գործարք պարունակում է տվյալներ գնորդի անունի, ապրանքի անվան և ապրանքի գնի վերաբերյալ։ 
# Անհրաժեշտ է 
# 1)արտածել գնորդների ընդհանուր գնումների գումարը, 
# 2)ըստ գործարքների քանակի ամենաակտիվ գնորդի ազգանունը,
# 3)ամենաթանկ գնված ապրանքը։

def data_inp():
    customer = input("Enter customer name: ")
    dict = {}
    name_pr = input("Enter product name: ")
    price_pr = float(input("Enter product price: "))
    llist = (name_pr, price_pr)
    dict[customer] = llist
    return dict
try:
    q = int(input("Enter transaction quantity: "))
    if q <= 0:
        raise Exception("Quantity must be natural!")
    transactions = []
    for i in range(q):
        transactions.append(data_inp())

    overall_prices = {} #overall price for each customer dictionary
    overall_activity = {} #overall activity keeping dictionary
    expensive = float('-inf') #very small number for finding the most expensive product
    exp_prod = '' #the most expensive product name

    for i in transactions:
        for j in i:
            product = i[j]
            price = product[1]
            if price>expensive:
                expensive = price
                exp_prod = product
            if j not in overall_prices:
                overall_prices[j] = price
            else:
                overall_prices[j] += price
            if j not in overall_activity:
                overall_activity[j] = 1
            else:
                overall_activity[j]+=1
    print("Overall prices for each user are: ", overall_prices)
    print("The most expensive product bought is: ", exp_prod)

    new_l_act = []
    for i in overall_activity:
        new_l_act.append(overall_activity[i])
    max_activity = max(new_l_act)
    for i in overall_activity:
        if overall_activity[i] == max_activity:
            print("The most transactions are done by customer: ", i)
            break       
except Exception as e:
    print("Unexpected exception occured: ", e)