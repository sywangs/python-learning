def make_pizza(size,*toppings):
    """receive parametersof he the pizza' size,and uncetain toppings and print them"""
    print ("Ordered Pizza's size:" + str(size) + "inches")
    print ("with toppings")
    for topping in toppings:
        print (topping)

make_pizza(8,"mushrooms","green peppers","cheese")
