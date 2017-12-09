def print_models(unprinted_designs, compled_models):
    """print all models in unprinted_designs,
       After print finished,element in unprinted_designs will move into compled_models"""

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print ("Printing Model:" + current_design)
        compled_models.append(current_design)

    print ("3D Print Finished!\n")


compled_models = []
unprinted_designs = ["plane", "heart", "printer"]

print_models(unprinted_designs[:], compled_models)

for model in compled_models:
    print (model + " Printed!")
