# approach 1
import a
import b

obj1 = a.Animal()
obj1.display()

obj2 = b.Bird()
obj2.display()

from a import Animal
from b import Bird

obj1 = a.Animal()
obj1.display()

obj2 = b.Bird()
obj2.display()