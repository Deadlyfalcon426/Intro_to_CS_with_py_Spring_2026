class RollercoasterQueue:
    def __init__(self, __ride_seats, length):
        self.__ride_seats = __ride_seats
        self.__ride_length = length
        self.__queue_length = 0
    def board_ride(self):
        if self.__queue_length>=self.__ride_seats:
            self.__queue_length -= self.__ride_seats
        else:
            self.__queue_length = 0
    def length(self):
        return self.__queue_length
    def enqueue(self):
        self.__queue_length+=1

ppl_per_ride = int(input("How many people fit in one ride? "))
ride_length = int(input("How long is the ride, in minutes? "))
rc_queue = RollercoasterQueue(ppl_per_ride, ride_length)
for iteration in range(20):
    rc_queue.enqueue()
while(rc_queue.length()!=0):
    rc_queue.board_ride()
    print(rc_queue.length())

        