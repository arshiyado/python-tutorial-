import numpy as np 

# casting using astype()
"""
a = np.array([1, 2, 3, 4, 5])
print("Original array:", a)
print("Original dtype:", a.dtype)
a_float = a.astype(np.float32)
print("Converted array:", a_float)
print("Converted dtype:", a_float.dtype)
a_complex = a.astype(np.complex64)
print("Converted array:", a_complex)
print("Converted dtype:", a_complex.dtype)
"""
# casting using cast
"""
d = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print("Original array:", d)
print("Original dtype:", d.dtype)
d_int = np.int32(d)
print("Converted array:", d_int)
print("Converted dtype:", d_int.dtype)
d_complex = np.complex64(d_int)
print("Converted array:", d_complex)
print("Converted dtype:", d_complex.dtype)
d_float = d_int.astype(np.float128)
print("float array:", d_float)
print("float dtype:", d_float.dtype)
"""
#valid cast of string to number
"""
str = np.array(["1", "2", "3", "4"], dtype='U20')
print(str)
ans = np.int16(str)
print(ans)
"""
#invalid cast of string to number
"""
str = np.array(["1", "two", "3", "4"], dtype='U20')
print(str)
ans = np.int16(str)
print(ans)
"""
# complex warning
"""
arr = np.array([1+2j, 2+3j, 3+4j], dtype=np.complex64)
brr = arr.astype(np.int32)
print(brr)
"""

