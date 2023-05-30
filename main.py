def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """

    f=open(file_name, mode='r')
    s=f.read()
    list1 = []
    list2 = []
    for i in s.split('\n'):
        list1.append(i.split(','))
        # print(list1)
        # list1(i)
    for k in list1:
        list2.append(k[-1])

    return list2
print(get_country_column('data.csv'))
