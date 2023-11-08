animal(elephant,herbivore).
animal(lion,carnivore).
animal(giraffe,herbivore).
animal(zebra,herbivore).
animal(hawk,carnivore).
animal(snake,carnivore).
animal(kangaroo,herbivore).
animal(panda,herbivore).
animal(rabbit,herbivore).
animal(dog,carnivore).
eat(elephant,grass).
eat(lion,meat).
eat(giraffe,leaves).
eat(zebra,grass).
eat(hawk,small_mammals).
eat(snake,rodents).
eat(kangaroo,grass).
eat(panda,bamboo).
iscarnivore(X) :- animal(X,carnivore).
isherbivore(X) :- animal(X,herbivore).
