import openpyxl


def generate_test_products_xls(filename='test_products.xlsx', num_products=20):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    headers = ['name', 'description', 'price', 'stock', 'barcode']
    sheet.append(headers)
    for i in range(1, num_products + 1):
        product_name = f'Товар {i}'
        description = f'Опис товару {i}'
        price = i * 10.0
        stock = i * 5
        barcode = f'1234567890{i:02}'
        sheet.append([product_name, description, price, stock, barcode])
    workbook.save(filename)
    print(f'File {filename} generated successfully!')


if __name__ == '__main__':
    generate_test_products_xls()
