import numpy as np
# np.int16 Integer (-32768 to 32767)
# np.int32 Integer (-2147483648 to 2147483647)
# np.int64 Integer (-9223372036854775808 to 9223372036854775807)
#
array_a = np.array([32766, 32767, 32768], dtype=np.int32)

print(array_a)

# np.uint16 Unsigned Integer (0 to 65535)
# np.uint32 Unsigned Integer (0 to 4294967295)
# np.uint64 Unsigned Integer (0 to 18446744073709551615)

array_b = np.array([-1, 0, 1])
print(array_b)