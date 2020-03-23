import pandas as pd

with open("duplicates.txt", 'r+')as email:
    lines = email.read().splitlines()
    na_duplicate = []
    for x in lines:
        if x not in na_duplicate:
            na_duplicate.append(x)
    print(*na_duplicate, sep=" \n")
    print('\n')
    print("\tYou have had lines:", len(lines))
    print('\tDuplicates removed from the list is: ', len(lines) - len(na_duplicate), "\n")
    print('Has been copied to your clipboard!')
    print('\n')
    pd.DataFrame(na_duplicate).to_clipboard(excel=True, header=False, index=False)
    print('\t\t\t\t\tAuthor: kxf3/Sorunlu00')
    print(input('Press Enter key to exit.'))

