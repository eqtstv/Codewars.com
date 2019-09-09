def unique_in_order(iterable):
    if iterable:
        list = [iterable[i] for i in range(len(iterable)-1) if iterable[i] != iterable[i+1]]
        list.append(iterable[-1])
        return list 
    else:
        return []
