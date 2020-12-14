import array
import time
from functools import reduce
import dis
print(list(map(lambda x: {x: min(1, max((x - 40) / 10., 0))}, range(35, 55, 2))))

def builtin_join(arr: array):
    return ''.join(arr)


def reduce_join(arr: array):
    return reduce(lambda c, n: f'{c},{n}', arr)


foo_list = array.array('u', ['a'] * 100_000)

t_start = time.time()
join_result = builtin_join(foo_list)
t_end = time.time()
print('---join---')
dis.dis(builtin_join)
print(f'join -> {(t_end - t_start):8f}')

t_start = time.time()
reduce_result = reduce_join(foo_list)
t_end = time.time()
print('---reduce---')
dis.dis(reduce_join)
print(f'reduce -> {(t_end - t_start):8f}')
