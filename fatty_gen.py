def fatty_gen(chain_length, double_bond, orientation):
    "Generates SMILES code string for a fatty acid"
    saturated = "C"*chain_length
    unsaturated = saturated[:double_bond] + "=" + saturated[double_bond:]
    if orientation == "E" or orientation == "e":
        fatty_acid = saturated[:(double_bond-1)] + "/C=C/" + saturated[(double_bond+1):]
    elif orientation == "Z" or orientation == "z":
        fatty_acid = saturated[:(double_bond-1)] + "/C=C\\" + saturated[(double_bond+1):]
    else:
        fatty_acid = unsaturated
    return fatty_acid