import sys

with open('Input1.txt') as f:
    lines = f.readlines()


# Defining Function for split
def split(lines):
    import re

# Reference List
    food_list = ['chocolate', 'chocolates', 'chips', 'fish', 'chicken_breast', 'milk']
    medicine_list = ['pills', 'cough syrup', 'eye drops']

    p_total = []
    out = []
    tax = []

# Iterating basket and spliting price and product list
    for i in lines:
        product = []
        price = []
        items = i.split()
        for j in items:
            if j.isnumeric() or re.match(r'^-?\d+(?:\.\d+)$', j) is not None:
                price.append(j)
            else:
                product.append(j)

# Defining  Zero Tax, Sales tax & Import Duty tax with Rounding
# ZeroTax for products without any tax
        if (any(k in food_list for k in product) or any(k in medicine_list for k in product) or any(k == 'Book' for k in product)) and (all(k != 'imported' for k in product)):
            out.append(str(price[0])+' '+' '.join(product[:-1])+':'+str(price[1]))
            p_total.append(float(price[1]))
# Sales Tax (10%)
        elif any(k not in food_list for k in product) and any(k not in medicine_list for k in product) and any(k != 'Book' for k in product) and all(k != 'imported' for k in product):
            taxx =  ((float(price[1])*10)/100)
            taxx = round(taxx / 0.05) * 0.05
            price[1] = taxx+float(price[1])
            price[1] = float("{:.3f}".format(price[1]))
            out.append(str(price[0])+' '+' '.join(product[:-1])+':'+str(price[1]))
            tax.append(taxx)
            p_total.append(float(price[1]))
        # Products with both Sales(10%) and Import tax (5%)
        elif all(k not in food_list for k in product) and all(k not in medicine_list for k in product) and all(k != 'Book' for k in product) and any(k == 'imported' for k in product):
            taxx1 = round(0.05 * round(float((float(price[1]) * 10) / 100) / 0.05), 2)
            taxx2 = round(0.05 * round(float((float(price[1]) * 5) / 100) / 0.05), 2)
            taxx = round(taxx1+taxx2,2)
            price[1] = taxx+float(price[1])
            price[1] = round(float(price[1]),4)
            out.append(str(price[0])+' '+' '.join(product[:-1])+':'+str(price[1]))
            tax.append(taxx)
            p_total.append(float(price[1]))
# Import Duty tax (5%)
        elif (any(k in food_list for k in product) or any(k in medicine_list for k in product) or any(k == 'Book' for k in product)) and (any(k == 'imported' for k in product)):
            taxx =  ((float(price[1])*5)/100)
            taxx = round(taxx , 1)

            price[1] = taxx+float("{:.2f}".format(float(price[1])))

            price[1] = float("{:.2f}".format(price[1]))
            out.append(str(price[0])+' '+' '.join(product[:-1])+':'+str(price[1]))
            tax.append(taxx)
            p_total.append(float(price[1]))
    return p_total, out, tax

# Returning values for tax = 'sales tax per product', Out = 'initial price + tax' , Total = 'Sum of price of all producting including tax'.

total, List_of_Products, total_tax = split(lines)
# b1 is the variable, whose change makes changes with Input. If we change it to b2 or b3, it will show result for Input 2 and Input 3 respectively.
# For futher use of this code, we can use a text file or an excel file with some changes and this program can be used as daily purpose grocery tax calculator.


sys.stdout = open("TexT", "w")

print(*[i for i in List_of_Products], sep = '\n') # printing the list of products in b1 and prices after tax evaluation

print('Sales Taxes:',float("{:.2f}".format(sum(total_tax)))) # printing the total Sales tax after evaluation

print('Total:',float("{:.3f}".format(sum(total))))# printing Total for all prices including tax

sys.stdout.close()