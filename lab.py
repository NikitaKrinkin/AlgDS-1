class CircularDeque:
    def __init__(self, n: int, push_force: bool):
        assert type(n) is int, "Deque only supports integers"
        assert type(push_force) is bool, "push_force should be bool!"
        assert n > 0, "Invalid deque size"
        self.deq_size = n
        self.push_force = push_force
        self.vals: list[int | None] = [None for _ in range(n)]
        # front and back 'pointers'
        self.push_front_idx: int | None = None
        self.push_back_idx: int | None = None

    def update_front_index(self, step=-1):
        self.push_front_idx += step
        if self.push_front_idx >= self.deq_size:
            self.push_front_idx = 0
        elif self.push_front_idx < 0:
            self.push_front_idx = self.deq_size - 1

    def update_back_index(self, step=1):
        self.push_back_idx += step
        if self.push_back_idx >= self.deq_size:
            self.push_back_idx = 0
        elif self.push_back_idx < 0:
            self.push_back_idx = self.deq_size - 1

    def check_collision(self, atr: str):
        if atr != "front" and atr != "back":
            raise KeyError("Only front and back are available")
        if self.push_back_idx == self.push_front_idx:
            if atr == "front":
                self.update_back_index(-1)
            elif atr == "back":
                self.update_front_index(1)

    def first_push(self, x: int):
        self.vals[0] = x
        self.push_front_idx = 0
        self.push_back_idx = 0

    def push_front(self, x: int):
        assert type(x) is int, "Deque only supports integers"
        if self.push_front_idx is None:
            self.first_push(x)
        else:
            self.update_front_index()
            if self.vals[self.push_front_idx] is None:
                self.vals[self.push_front_idx] = x
            elif self.push_force:
                self.vals[self.push_front_idx] = x
            else:
                raise IndexError("Unable to push: place is busy!")
            self.check_collision("front")

    def push_back(self, x: int):
        assert type(x) is int, "Deque only supports integers"
        if self.push_back_idx is None:
            self.first_push(x)
        else:
            self.update_back_index()
            if self.vals[self.push_back_idx] is None:
                self.vals[self.push_back_idx] = x
            elif self.push_force:
                self.vals[self.push_back_idx] = x
            else:
                raise IndexError("Unable to push: place is busy!")
            self.check_collision("back")


    def pop_front(self) -> int:
        if self.empty():
            raise IndexError("Unable to pop -- deque is empty!")
        val = self.vals[self.push_front_idx]
        if val is None:
            raise KeyError
        self.vals[self.push_front_idx] = None
        self.update_front_index(1)
        if self.empty():
            self.push_front_idx: int | None = None
            self.push_back_idx: int | None = None
        return val

    def pop_back(self) -> int:
        if self.empty():
            raise IndexError("Unable to pop -- deque is empty!")
        val = self.vals[self.push_back_idx]
        if val is None:
            raise KeyError
        self.vals[self.push_back_idx] = None
        self.update_back_index(-1)
        if self.empty():
            self.push_front_idx: int | None = None
            self.push_back_idx: int | None = None
        return val

    def front(self) -> int:
        if self.empty():
            raise IndexError("Unable to front -- deque is empty!")
        val = self.vals[self.push_front_idx]
        if val is None:
            raise KeyError
        return val

    def back(self) -> int:
        if self.empty():
            raise IndexError("Unable to back -- deque is empty!")
        val = self.vals[self.push_back_idx]
        if val is None:
            raise KeyError
        return val

    def size(self) -> int:
        return self.deq_size - self.vals.count(None)

    def empty(self) -> bool:
        return self.vals.count(None) == self.deq_size

    def full(self):
        return self.vals.count(None) == 0

    def resize(self, new_cap: int):
        assert new_cap > 0, "Invalid deque size"
        assert new_cap is int, "New_cap should be integer!"
        if new_cap < 1:
            raise AttributeError("New capacity should be greater that zero!")
        new_vals: list[int | None] = [None for _ in range(new_cap)]
        new_idx = 0
        while not self.empty() and new_vals.count(None) != 0:
            new_vals[new_idx] = self.pop_front()
            new_idx += 1
        self.vals = new_vals
        self.deq_size = new_cap
        self.push_front_idx = 0
        self.push_back_idx = new_idx - 1
