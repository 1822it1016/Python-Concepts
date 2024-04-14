# # Decorators 


# def decorator_func(my_fuct):
#     def wrap():
#         print("Pre")
#         my_fuct()
#         print("Post")
#     return wrap    


# @decorator_func
# def print_name():
#     print("My name is akash")


# print_name()



# #Generators


# def generate_values():
#     yield 4
#     yield 3
#     yield 2
#     yield 1

# "all three ways of printing generators"
# generator_object = generate_values()
# print(generator_object.__next__())
# print(next(generator_object))
# for i in generator_object:
#     print(i)



# # Iterators
    
# class EvenNumbers:
#     def __init__(self):
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if i < 1000:
#             self.current += 2
#             return self.current
#         else:
#             raise StopIteration

# even_numbers = EvenNumbers()

# print(next(even_numbers))  # Output: 2
# print(next(even_numbers))  # Output: 4
# print(next(even_numbers))  # Output: 6
# for i in even_numbers:
#     print(i)


    

import asyncio

async def test_basic_wait():
    print("Wait started")
    await asyncio.sleep(2)  # Use asyncio.sleep() instead of time.sleep()
    print("wait Ended")

async def run_sum():
    print("Start summing")
    sum_result = 2 + 2
    print(f"Sum ended and sum is {sum_result}")

async def main():
    await asyncio.gather(test_basic_wait(), run_sum())

asyncio.run(main())
