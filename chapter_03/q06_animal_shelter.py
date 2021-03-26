from typing import Optional

class LinkedListNode:
    def __init__(self, value) -> None:
        self.next: Optional[LinkedListNode] = None
        self.data = value

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None

    def add(self, value):
        new_node = LinkedListNode(value)
        if self.last:
            self.last.next = new_node
        self.last = new_node

        if not self.first:
            self.first = self.last

    def remove(self):
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None

        return data

    def peek(self):
        return self.first.data

    def is_empty(self):
        return self.first is None


class OrderTaggedAnimal:
    def __init__(self, animal, order) -> None:
        self.animal = animal
        self.order = order

class Dog:
    pass

class Cat:
    pass

class AnimalQueue:
    def __init__(self):
        self.current_order = 0
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        queue = self.dogs if isinstance(animal, Dog) else self.cats
        tagged_animal = OrderTaggedAnimal(animal, self.current_order)
        self.current_order += 1
        queue.add(tagged_animal)

    def dequeueAny(self):
        first_dog = self.dogs.peek()
        first_cat = self.cats.peek()

        if first_dog.order <= first_cat.order:
            return self.dequeueDog()

        return self.dequeueCat()

    def dequeueDog(self):
        return self.dogs.remove().animal

    def dequeueCat(self):
        return self.cats.remove().animal

queue = AnimalQueue()

dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
cat1 = Cat()
cat2 = Cat()
cat3 = Cat()

queue.enqueue(dog1)
queue.enqueue(cat1)
queue.enqueue(cat2)
queue.enqueue(dog2)
queue.enqueue(dog3)
queue.enqueue(cat3)

assert queue.dequeueAny() is dog1
assert queue.dequeueDog() is dog2
assert queue.dequeueCat() is cat1
assert queue.dequeueAny() is cat2
assert queue.dequeueDog() is dog3
assert queue.dequeueCat() is cat3
