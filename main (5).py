def LinearSearchProduct(productList,targetproduct):
  indices=[]
  for index , products in enumerate(productList):
    if products == targetproduct:
      indices.append(index)
  return indices

products=["shoes","boot","loafer","shoes","sanda","shoes"]
target1="shoes"
target2="apple"
result1=LinearSearchProduct(products,target1)
result2=LinearSearchProduct(products,target2)
print(result1)
print(result2)