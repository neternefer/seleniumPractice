'''
Decorator Design Pattern
- dynamically add a new feature to an object (only that particular object,
not the entire subclass)
- all decorators wrapped around the object must have the same basic interface
- build-in in Python
'''
class TextTag:

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

class BoldWrapper(TextTag):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())

class ItalicWrapper(TextTag):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())

if __name__ == "__main__":
    simple_text = TextTag('Hello, world!')
    special_text = ItalicWrapper(BoldWrapper(simple_text))
    print("Before: {}".format(simple_text.render()))
    print("After: {}".format(special_text.render()))
    
                          
