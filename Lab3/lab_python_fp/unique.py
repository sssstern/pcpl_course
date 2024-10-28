import types

class generatortoiter(object):
    def __init__(self, gen):
        self.gen = gen  
    def __iter__(self):
        return self.gen()


class Unique(object):
    def __init__(self, items, **kwargs):
        if isinstance(items, types.GeneratorType):
            self.data = iter(*items)
        else :
            self.data = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.unique_items = set()

    def __next__(self):
        while True:
            item = next(self.data)
            check_item = item.lower() if self.ignore_case and isinstance(item, str) else item
            if check_item not in self.unique_items:
                self.unique_items.add(check_item)
                return item
            
    def __iter__(self):
        return self
    

if __name__ == "__main__":
    data = [1, 1, 2, 2, 3, 3, 4, 4, 'a', 'A', 'b', 'B', 'a', 'A']
    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))