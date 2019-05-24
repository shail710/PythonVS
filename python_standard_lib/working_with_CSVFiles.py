import csv
# # writing a csv file
# with open('data.csv', 'w') as file:
#     # csv module has writer() method to create a csv writer, this takes file obj as an argument
#     writer = csv.writer(file)
#     # after creating csv writer for the file, we can write in to csv file
#     writer.writerow(['transactio_id', 'product_id', 'price'])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

# reading a csv file
with open('data.csv') as file:
    reader = csv.reader(file)
    # this will read all the data from the csv file and put it in a list
    # print(list(reader))
    #Output: [['transactio_id', 'product_id', 'price'], [], ['1000', '1', '5'], [], ['1001', '2', '15'], []]
    # for row in reader:
    #     print(row)

    # above for loop will not print any thing because,
    # this reader object has a index or a position that is set to the beginning of the file.
    # when we convert this reader, to a list, that position goes to the end of the file
    # so when we iterate over it, we are already at the end of the file

    # we should iterate over reader object directly instead

    for row in reader:
        print(row)
    # Output:
    # ['transactio_id', 'product_id', 'price']
    # []
    # ['1000', '1', '5']
    # []
    # ['1001', '2', '15']
    # []
