lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywaniak": ["marchew", "seler", "rukola"]
}
x = 0
for shop, products in lista_zakupow.items():
    shop = shop.title ()
    products_titled = []
    for product in products:
        products_titled.append (product.title())
        x = x + 1
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products_titled}.")
print (f"W sumie kupuję {x} produktów")

# zadanie drugie
print("zadanie 2")
by_5 = []
for i in range (0,100):
    if i%5 == 0:
        by_5.append(i)
    else:
        continue
print(by_5)
