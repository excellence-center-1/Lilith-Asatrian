try:
    products = {}
    def add_product(product_id, name, category, price):
        if product_id not in products:
            products[product_id] = {"name": name, "category": category, "price": price}
        else:
            raise Exception("Such product ID already exists.")

    def update_product(product_id, name = None, category = None, price=None):
        if product_id in products:
            if name:
                products[product_id]["name"] = name
            if category:
                products[product_id]["category"] = category
            if price:
                products[product_id]["price"] = price
        else:
            raise Exception("Product not found")

    def delete_product(product_id):
        if product_id in products:
            del products[product_id]
        else:
            raise Exception("Product not found")

    def get_product_details(product_id):
        if product_id in products:
            return products.get(product_id, "Product not found")
    def get_all_products():
        for key, value in products.items():
            print(key, value)
    add_product("1", "Smartphone", "Electronics", 250000)   
    add_product("2", "Desk", "Furniture", 114000) 
    # add_product("1", "Washing machine", "Electronics", 670000)
    add_product("7", "Oven", "Electronics", 590000)
    print(get_product_details("1"))
    update_product("1", price=300000)
    # delete_product("7")
    get_all_products()
except Exception as e:
    print("Unexpected exception occured: ", e)



    

    




