        self._rules = []
        self.generate_rules()
    def __init__(self, doc, whitespace=True):
        GenericSyntaxHighligher.__init__(self, doc)