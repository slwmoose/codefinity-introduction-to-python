# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]

categories = "Candy Aisle, Pasta Aisle"
category1 = "Candy Aisle"
category2 = "Pasta Aisle"

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print("We have " + candy1[0:9] + " for " + bubblegum_price[0:6] + " in the " + category1[0:11])
print("We have " + candy2[0:9] + " for " + chocolate_price[0:6] + " in the " + category1[0:11])
print("We have " + dry_goods[0:5] + " for " + pasta_price[0:6] + " in the " + category2[0:11])