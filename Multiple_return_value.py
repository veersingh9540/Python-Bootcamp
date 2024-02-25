def format_name(f_name, l_name):
    """Taking the first and last name as the input and making output that in a single line."""
    if f_name == "" or l_name == "":
        return "You didn't have valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first???"), input("what is your last name ?? ") ))