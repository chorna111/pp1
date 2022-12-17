class CONTACT:
    def __init__(self,name,email,telephone):
        self.name=name
        self.email=email
        self.telephone=telephone
    def __repr__(self):
        sp=20
        p=' '
        if len(self.name)<sp:
            len1=sp-len(self.name)

            len2=sp-len(self.email)
        return f'{self.name}{p*len1}{self.email}{p*len2}{self.telephone}'
