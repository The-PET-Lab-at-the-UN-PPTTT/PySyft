import numpy as np

HANDLED_FUNCTIONS = {}

def inputs2child(*args, **kwargs):
    args = [x.child if isinstance(x, PassthroughTensor) else x for x in args]
    kwargs = {x[0] : x[1].child if isinstance(x[1], PassthroughTensor) else x[1] for x in kwargs.items()}
    return args,kwargs

def is_acceptable_simple_type(obj):
    return isinstance(obj, (int,bool,float, np.ndarray))

class PassthroughTensor(np.lib.mixins.NDArrayOperatorsMixin):
    """A simple tensor class which passes method/function calls to self.child"""
    
    def __init__(self, child):
        self.child = child

    def __len__(self):
        return len(self.child)
        
    @property
    def shape(self):
        return self.child.shape        
    
    def __add__(self, other):
        return self.__class__(self.child + other.child)
    
    def __sub__(self, other):
        return self.__class__(self.child - other.child)    
    
    def __neg__(self):
        return self * -1
    
    def copy(self):
        return self.__class__(self.child.copy())
    
    def __mul__(self, other):
        
        if is_acceptable_simple_type(other):
            return self.__class__(self.child * other)
        
        return self.__class__(self.child * other.child)        
    
    def __truediv__(self, other):
        
        if is_acceptable_simple_type(other):
            return self.__class__(self.child / other)
        
        return self.__class__(self.child / other.child)        
    
    def manual_dot(self, other):
        
        expanded_self = self.repeat(other.shape[1]).reshape(self.shape[0], self.shape[1], other.shape[1])
        expanded_other = other.repeat(self.shape[0]).reshape(other.shape[0], other.shape[1], self.shape[0]).transpose(2,0,1)
        
        prod = expanded_self * expanded_other
        result = prod.sum(1)
        
        return result    
    
    def dot(self, other):
        return self.manual_dot(other)
#         if isinstance(other, self.__class__):
#             return self.__class__(self.child.dot(other.child))

#         return self.__class__(self.child.dot(other))

    def __ge__(self, other):
        return self.__class__(self.child >= other.child)    
    
    def __le__(self, other):
        return self.__class__(self.child <= other.child)
    
    def reshape(self, *dims):
        return self.__class__(self.child.reshape(*dims))
    
    def repeat(self, *args, **kwargs):
        return self.__class__(self.child.repeat(*args, **kwargs))
    
    def sum(self, dim):
        return self.__class__(self.child.sum(dim))
    
    def transpose(self, *args, **kwargs):
        return self.__class__(self.child.transpose(*args, **kwargs))
        
    def __array_function__(self, func, types, args, kwargs):
#         args, kwargs = inputs2child(*args, **kwargs)
        
        print(func)
    
        # Note: this allows subclasses that don't override
        # __array_function__ to handle PassthroughTensor objects.
        if not all(issubclass(t, self.__class__) for t in types):
            return NotImplemented
        
        if func in HANDLED_FUNCTIONS[self.__class__]:
            return HANDLED_FUNCTIONS[self.__class__][func](*args, **kwargs)
        else:
            return self.__class__(func(*args, **kwargs))        

#     def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
#         print(ufunc)
#         print(method)
#         print(inputs)
#         print(kwargs)
#         return NotImplemented
#         print()
#         if method == '__call__':
#             N = None
#             scalars = []
#             for input in inputs:
#                 if isinstance(input, Number):
#                     scalars.append(input)
#                 elif isinstance(input, self.__class__):
#                     scalars.append(input._i)
#                     if N is not None:
#                         if N != self._N:
#                             raise TypeError("inconsistent sizes")
#                     else:
#                         N = self._N
#                 else:
#                     return NotImplemented
#             return self.__class__(N, ufunc(*scalars, **kwargs))
#         else:
#             return NotImplemented
        
    def __repr__(self):
        return f"{self.__class__.__name__}(child={self.child})"

    
def implements(tensor_type, np_function):
        "Register an __array_function__ implementation for DiagonalArray objects."
        def decorator(func):
            if tensor_type not in HANDLED_FUNCTIONS:
                HANDLED_FUNCTIONS[tensor_type] = {}
                
            HANDLED_FUNCTIONS[tensor_type][np_function] = func
            return func
        return decorator
    
    
@implements(PassthroughTensor, np.square)
def square(x):
    return x*x

