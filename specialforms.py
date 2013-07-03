
class DefineForm:
    def apply(self, context, args):
        name = args.head()
        value = args.tail().head()
        context.set(name, value)
        return value

