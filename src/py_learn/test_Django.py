results = [['goods_sku:latest:78470526'], [1]]

sku_lock_external_quantity_map = dict(zip(results[0], results[1]))
total = sum(sku_lock_external_quantity_map.values())
print(total)
