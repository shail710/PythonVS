class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


# cloud = TagCloud()
# cloud.add('Python')
# cloud.add('python')
# cloud.add('PYTHON')
# cloud.add('JAVASCRIPT')
# cloud.add('JavaScript')
# cloud.__setitem__('java', 2)
# print(len(cloud))
# print(cloud.__getitem__('pyThon'))
# for tag in cloud:
#     print(tag, cloud[tag])

# Output:
# 3
# 3
# python 3
# javascript 2
# java 2
