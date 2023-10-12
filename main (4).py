"""write a function called linear_ search_ product that takes the list of products and a target product 
Name as input. The function should perform a linear search to find the target product in the list and
return a list of indicates of all occurrences of the product if found, or an empty list if the product is not
found.
"""


def linearSearchProduct(productlist,targetProduct):
  indices = []

  for index, product in enumerate(productlist):
     if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products,target)
print (result)