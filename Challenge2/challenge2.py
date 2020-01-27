import os
import itertools
import functools
directory =os.getcwd()

def read_input(filename):
    lines = open(directory + "/"+filename).read().split("\n")
    bids = {line.split("\t")[0]: int(line.split('\t')[1]) for line in lines}
    items = bids['Items']
    del bids['Items']

    return items,bids

def custom_compare(bid1, bid2):
    if bid1[1] == bid2[1]:
        if bid1[0]<bid2[0]:
              return 1
        else: return -1
    if bid1[1] < bid2[1]:
        return -1
    elif bid1[1] > bid2[1]:
        return 1
    return 0

def auction(bids):
    ## sort
    sorted_bids = {k: v for k, v in sorted(bids.items(), key=functools.cmp_to_key(custom_compare) , reverse=True)}
    ## shift
    sorted_bids=dict(zip(sorted_bids, itertools.islice(itertools.cycle(sorted_bids.values()), 1, None)))
#    winners = dict(itertools.islice(sorted_bids.items(), nItems))
#   print(winners)
    return sorted_bids

def main():
    nItems, bids =read_input("input.txt")
    sorted_bids =auction(bids)
 #   print(sorted_bids)
    with open("output.txt", "w+") as f:
        if len(sorted_bids)<1:
            f.write("No Winnners")
        else:
            it=iter(sorted_bids.items())
            for i in range(nItems):
                item=next(it)
                f.write(item[0])
                f.write("\t")
                f.write(str(item[1]))
                f.write("\n")
            for i in range(nItems,len(bids)):
                item=next(it)
                f.write(item[0])
                f.write("\tLost")
                f.write("\n")
    f.close()


main()