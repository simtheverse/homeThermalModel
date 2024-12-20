def roomAir():
    # Air definition
    Air = dict()
    Air['h'] = 4/1.8  #W/((m^2)*R)
    Air['As']= 3.35*3.35*6  # m^2
    Air['r_specific_J_per_kgR'] = 287.058/1.8  # J/kgK to J/kgR
    Air['V'] = 991 * 10 / 35.315 #991 sqFt * 10 ft height -> m^3
    Air['c'] = 1*1000/1.8 # 1 kJ/kg/K -> J/kg/R

    return Air