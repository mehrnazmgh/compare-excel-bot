import pandas as pd



main_df = pd.read_excel(r'C:\Users\p30-1\Desktop\pythonProject\compare-excel-bot\file1.xlsx')
main_phones=main_df['phone']
# print (main_phones)
input_df = pd.read_excel(r'C:\Users\p30-1\Desktop\pythonProject\compare-excel-bot\file2.xlsx')
input_phones=input_df['phone']
# print(input_phones)

def same_values(main_phones, input_phones):
  count = 0
  for index in range(len(main_phones)):
    main_item = main_phones[index]
    # print(main_item)
    for i in range(len(input_phones)):
      if main_item == input_phones[i]:
        print('{0} in file1 with {1} in file2  {2} is Same.'.format(index , i , main_item))
        count += 1
        
      
      
  print("count is : " + str(count))
  
            
same_values(main_phones , input_phones)



