import lxml.etree

# Step 1: Parse the XML document
inventory = lxml.etree.parse('inventory.xml')

#############################################        Xpath Queries          ########################################################

# Get the names of all products that have variants with a quantity greater than 5:
query1 = inventory.xpath('/inventory/products/product[variants/variant/quantity > 5]/name')
for product in query1:
    print(product.text)
print("=========================================================")

# Get the names and prices of all products in the "Food" category:
query2 = inventory.xpath('/inventory/products/product[category="Food"]/name | /inventory/products/product['
                         'category="Food"]/price')
for product in query2:
    print(product.text)
print("=========================================================")

# Get the total sales for the customer id 1:
query3 = inventory.xpath('sum(//order[customer/@id="1"]/total)')
print(query3)
print("=========================================================")

# Get count of products by supplier 1
query4 = inventory.xpath('count(//product[supplier/@id="1"])')
print(query4)
print("=========================================================")

# Get the last order cost
query5 = inventory.xpath('/inventory/orders/order[last()]/total')
for product in query5:
    print(product.text)
print("=========================================================")

