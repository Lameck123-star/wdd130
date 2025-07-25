  # Don't forget to include formula.py in the same folder!

def make_periodic_table():
    periodic_table_dict = {
        # symbol: [name, atomic_mass]
        "H": ["Hydrogen", 1.00794],
        "C": ["Carbon", 12.0107],
        "O": ["Oxygen", 15.9994],
        "N": ["Nitrogen", 14.00674],
        "S": ["Sulfur", 32.065],
        "Cl": ["Chlorine", 35.453],
        "Na": ["Sodium", 22.98976928],
        "Fe": ["Iron", 55.845],
        # Add more elements as needed
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0.0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][1]
        total_mass += atomic_mass * quantity
    return total_mass

def main():
    # Step 1: Get user input
    formula = input("Enter the molecular formula of the sample: ")
    sample_mass = float(input("Enter the mass in grams of the sample: "))

    # Step 2: Parse formula
    symbol_quantity_list = parse_formula(formula)

    # Step 3: Get periodic table
    periodic_table = make_periodic_table()

    # Step 4: Compute molar mass
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    print(f"{molar_mass:.5f} grams/mole")

    # Step 5: Compute moles
    number_of_moles = sample_mass / molar_mass
    print(f"{number_of_moles:.5f} moles")

if __name__ == "__main__":
    main()