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