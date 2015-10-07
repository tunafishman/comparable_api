

class Comparable(object):

        def __init__(self, cid):
        self.name = 'carl'
        self.geo = 'us-west-2'
        self.cid = 1

    def Name(self):
        return self.name

    def Cid(self):
        return self.cid

    def Json(self):
        return {
            'name': self.name,
            'geo': self.geo,
            'cid': self.cid
        }
