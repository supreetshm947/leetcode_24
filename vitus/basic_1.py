def process_data(obj):
    # Write your code here
    if hasattr(obj, 'process') and callable(getattr(obj, 'process')):
        return obj.process()
    return None


class class1:
    def process(self):
        return "Something"

class class2:
    pass

print(process_data(class1()))