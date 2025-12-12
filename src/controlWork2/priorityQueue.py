class Vertex:
    def __init__(self, degree, value, left_child, right_child):
        self.key = value
        self.child = left_child
        self.sibling = right_child
        self.deg = degree

class PriorityQueue:
    def __init__(self):
        self.head = None


    def merge(self, h1, h2):
        if h1.head is None:
            self.head = h2.head
            return
        if h2.head is None:
            self.head = h1.head
            return
        h = PriorityQueue()
        h.head = Vertex(-1, 0, None, None)
        cur_h = h.head
        cur_h1 = h1.head
        cur_h2 = h2.head
        while cur_h1 is not None and cur_h2 is not None:
            if cur_h1.deg < cur_h2.deg:
                cur_h.sibling = cur_h1
                cur_h = cur_h1
                cur_h1 = cur_h1.sibling
            else:
                cur_h.sibling = cur_h2
                cur_h = cur_h2
                cur_h2 = cur_h2.sibling
        if cur_h1 is None:
            while cur_h2 is not None:
                cur_h.sibling = cur_h2
                cur_h2 = cur_h2.sibling
        else:
            while cur_h1 is not None:
                cur_h.sibling = cur_h1
                cur_h1 = cur_h1.sibling
        cur_h = h.head
        if cur_h is None:
            self.head = h.head
            return
        while cur_h.sibling is not None:
            if cur_h.deg != cur_h.sibling.deg:
                tmp = cur_h.sibling
                cur_h.sibling = cur_h.sibling.child
                cur_h = tmp
                continue
            cur_h = cur_h.sibling
        self.head = h.head


    def insert(self, value):
        new_h = PriorityQueue()
        new_h.head = Vertex(1, value, None, None)
        self.merge(new_h)


    def extract_min(self, h):
        mn = -1e9
        x = None
        curx = self.head
        curxBefore = None
        xBefore = None
        while curx is not None:
            if curx.key < mn:
                mn = curx.key
                x = curx
                xBefore = curxBefore
            curxBefore = curx
            curx = curx.sibling
        if xBefore is None:
            self.head = x.sibling
        else:
            xBefore.sibling = x.sibling
        h_new = None
        curx = x.child
        h_new.head = x.child
        while curx is not None:
            curx = curx.sibling
        h = self.merge(h, h_new)
        return x


    def delete(self, h):
        while self.head is not None:
            self.exctract_min(h)
