# import time
# import multiprocessing

# def cpu_bound(number):
#     print(sum(i * i for i in range(number)))

# def calculate_sums(numbers):
#     with multiprocessing.Pool() as pool:
#         pool.map(cpu_bound, numbers)

# def main():
#     start_time = time.perf_counter()  
#     numbers = [10000000 + x for x in range(20)]
#     calculate_sums(numbers)
#     end_time = time.perf_counter()
#     print('Calculation takes {} seconds'.format(end_time - start_time))
    
# if __name__ == '__main__':
#     main()

# import asyncio
# import time

# async def cpu_bound(number):
#     print(sum(i * i for i in range(number)))

# async def calculate_sums(numbers):
#     tasks = []
#     for number in numbers:
#         task = asyncio.create_task(cpu_bound(number))
#         print(task.get_name())
#         tasks.append(task)
#     results = await asyncio.gather(*tasks)
#     for num, result in zip(numbers, results):
#         print(f"Sum for {num}: {result}")

# async def main():
#     start_time = time.perf_counter()  
#     numbers = [10000000 + x for x in range(20)]
#     await calculate_sums(numbers)
#     end_time = time.perf_counter()
#     print('Calculation takes {} seconds'.format(end_time - start_time))

# if __name__ == '__main__':
#     asyncio.run(main())

import time
import concurrent.futures

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate_sums(numbers_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        pool.map(cpu_bound, numbers_list)

def calculate_multi_sums(numbers_list):
    with concurrent.futures.ProcessPoolExecutor() as pool:
        pool.map(cpu_bound, numbers_list)

def main():
    start_time = time.perf_counter() 
    numbers_list = [] 
    numbers_list = [10000000 + x for x in range(20)]
    calculate_sums(numbers_list)
    # calculate_multi_sums(numbers_list)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))
    
if __name__ == '__main__':
    main()