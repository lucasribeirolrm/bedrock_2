from classificacao.classifier import classify_product

product_description = input("Digite a descrição do produto: ")
categoria = classify_product(product_description)

print(f"O produto foi classificado como: {categoria}")