"""
An unordered collection of unique, immutable objects
Define it using {} - like dict but no key needed
You can use the set {} constructor to create one
"""



def main():
    """
    Test function
    :return:
    """
    p = {6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 5]
    print(data, type(data))
    # eliminate duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    for item in sdata:
        print(item)
    # Supports membership testing: in, not in
    print(5 in sdata)
    # Adding elements to sets:
    sdata.add(45)
    print(sdata)
    sdata.update([2, 99, 44, 33, 1, 2, 88])  # Adds only unique values
    print(sdata)
    # Removing elements
    # Remove() method: raises KeyError if not found
    sdata.remove(44)
    print(sdata)
    # Discard() method: does not raise any error
    sdata.discard(77)
    print(sdata)

    # Make a copy of set
    wdata = sdata.copy()
    print(wdata is sdata)
    print(wdata == sdata)

    ###### Define some sets
    blue_eyes = {"Olivia", "Harry", "Lily", "Jack"}
    blond_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry", "Lily", "Amelia", "Lola"}
    o_blood = {"Mia", "Joshua", "Lily", "Olivia"}
    b_blood = {"Amelia", "Jack", }
    a_blood = {"Harry"}
    ab_blood = {"Joshua", "Lola"}

    print(blue_eyes.union(blond_hair))
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))






if __name__ == '__main__':
    main()
    exit(0)