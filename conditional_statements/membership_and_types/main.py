# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

#boolean variables
contains_raw = "raw" in description
contains_Imported = "Imported" in description

#Use the type function
price_is_float = type(price) == float
count_is_int = type(count) == int

#Output Requirements
print ("Contains 'raw':", contains_raw)
print ("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)