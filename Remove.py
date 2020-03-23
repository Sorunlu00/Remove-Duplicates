import pandas as pd

with open("duplicates.txt", 'r+')as email:
    lines = email.read().splitlines()
    na_duplicate = []
    for x in lines:
        if x not in na_duplicate:
            na_duplicate.append(x)
    print("\tYou have had lines:", len(lines))
    print('\tDuplicates removed from the list is: ', len(lines) - len(na_duplicate), "\n")
    print(*na_duplicate, sep=" \n")
    print('\n')
    pd.DataFrame(na_duplicate).to_clipboard(excel=True, header=False, index=False)
    print(input('Press any key to exit.'))
