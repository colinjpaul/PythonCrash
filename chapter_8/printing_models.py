def print_models(designs, completed_designs):
    while designs:
        current_design = designs.pop()
        print("Printing model: " + current_design)
        completed_designs.append(current_design)


def show_completed_models(completed):
    # Display all completed models
    print("\n The following models have been printed: ")
    for model in completed:
        print(model)


# Start with designs that need to be printed
completed_models = []
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print(unprinted_designs)







