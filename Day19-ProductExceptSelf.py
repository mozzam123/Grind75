def product_except_self(input_list):
    output_list = []
    for i in range(len(input_list)):
        product = 1

        for j in range(len(input_list)):
            if i != j:
                product *= input_list[j]
        output_list.append(product)
    print(output_list)




product_except_self([2,3,4,3])