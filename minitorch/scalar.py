from .autodiff import FunctionBase, Variable, History
from . import operators
import numpy as np


## Task 1.1
## Derivatives


def central_difference(f, *vals, arg=0, epsilon=1e-6):
    r"""
    Computes an approximation to the derivative of `f` with respect to one arg.

    See :doc:`derivative` or https://en.wikipedia.org/wiki/Finite_difference for more details.

    Args:
       f : arbitrary function from n-scalar args to one value
       *vals (floats): n-float values :math:`x_0 \ldots x_{n-1}`
       arg (int): the number :math:`i` of the arg to compute the derivative
       epsilon (float): a small constant

    Returns:
       float : An approximation of :math:`f'_i(x_0, \ldots, x_{n-1})`
    """

    vals1 = list(vals)
    vals2 = list(vals)
    vals1[arg] = vals1[arg] + epsilon
    vals2[arg] = vals2[arg] - epsilon
    if len(vals) == 1:
        return (f(vals1[0]) - f(vals[0])) / epsilon
    if len(vals) == 2:
        return (f(vals1[0], vals1[1]) - f(vals2[0], vals2[1])) / (2*epsilon)
    # TODO: Implement for Task 1.1.
    raise NotImplementedError('Need to implement for Task 1.1')

 
## Task 1.2 and 1.4
## Scalar Forward and Backward


class Scalar(Variable):
    """
    A reimplementation of scalar values for autodifferentiation
    tracking.  Scalar Variables behave as close as possible to standard
    Python numbers while also tracking the operations that led to the
    number's creation. They can only be manipulated by
    :class:`ScalarFunction`.

    Attributes:
        data (float): The wrapped scalar value.

    """

    def __init__(self, v, back=History(), name=None):
        super().__init__(back, name=name)
        self.data = float(v)

    def __repr__(self):
        return "Scalar(%f)" % self.data

    def __mul__(self, b):
        return Mul.apply(self, b)

    def __truediv__(self, b):
        return Mul.apply(self, Inv.apply(b))

    def __add__(self, b):
        # TODO: Implement for Task 1.2.
        return Add.apply(self, b)
        raise NotImplementedError('Need to implement for Task 1.2')

    def __lt__(self, b):
        # TODO: Implement for Task 1.2.
        return LT.apply(self, b)
        raise NotImplementedError('Need to implement for Task 1.2')

    def __gt__(self, b):
        # TODO: Implement for Task 1.2.
        return LT.apply(b, self)
        raise NotImplementedError('Need to implement for Task 1.2')

    def __sub__(self, b):
        # TODO: Implement for Task 1.2.
        return Add.apply(self, -b)
        raise NotImplementedError('Need to implement for Task 1.2')

    def __neg__(self):
        # TODO: Implement for Task 1.2.
        return Neg.apply(self)
        raise NotImplementedError('Need to implement for Task 1.2')

    def log(self):
        # TODO: Implement for Task 1.2.
        return Log.apply(self)
        raise NotImplementedError('Need to implement for Task 1.2')

    def exp(self):
        # TODO: Implement for Task 1.2.
        return Exp.apply(self)
        raise NotImplementedError('Need to implement for Task 1.2')

    def sigmoid(self):
        # TODO: Implement for Task 1.2.
        return Sigmoid.apply(self)
        raise NotImplementedError('Need to implement for Task 1.2')

    def relu(self):
        # TODO: Implement for Task 1.2.
        return ReLU.apply(self)
        raise NotImplementedError('Need to implement for Task 1.2')

    def get_data(self):
        return self.data


class ScalarFunction(FunctionBase):
    "A function that processes and produces Scalar variables."

    @staticmethod
    def forward(ctx, *inputs):
        """Args:

           ctx (:class:`Context`): A special container object to save
                                   any information that may be needed for the call to backward.
           *inputs (list of numbers): Numerical arguments.

        Returns:
            number : The computation of the function :math:`f`

        """
        pass

    @staticmethod
    def backward(ctx, d_out):
        """
        Args:
            ctx (Context): A special container object holding any information saved during in the corresponding `forward` call.
            d_out (number):
        Returns:
            numbers : The computation of the derivative function :math:`f'_{x_i}` for each input :math:`x_i` times `d_out`.
        """
        pass

    # checks.
    variable = Scalar
    data_type = float

    @staticmethod
    def data(a):
        return a


# Examples
class Add(ScalarFunction):
    "Addition function"

    @staticmethod
    def forward(ctx, a, b):
        return a + b

    @staticmethod
    def backward(ctx, d_output):
        return d_output, d_output


class Log(ScalarFunction):
    "Log function"

    @staticmethod
    def forward(ctx, a):
        ctx.save_for_backward(a)
        return operators.log(a)

    @staticmethod
    def backward(ctx, d_output):
        a = ctx.saved_values
        return operators.log_back(a, d_output)


class LT(ScalarFunction):
    "Less-than function"

    @staticmethod
    def forward(ctx, a, b):
        return 1.0 if a < b else 0.0

    @staticmethod
    def backward(ctx, d_output):
        return 0.0


# To implement.


class Mul(ScalarFunction):
    "Multiplication function"

    @staticmethod
    def forward(ctx, a, b):
        # TODO: Implement for Task 1.2.
        ctx.save_for_backward((a, b))

        return operators.mul(a, b)
        raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        # TODO: Implement for Task 1.4.
        a, b = ctx.saved_values
        df_x = b
        df_y = a
        return (df_x * d_output, df_y * d_output)
        raise NotImplementedError('Need to implement for Task 1.4')


class Inv(ScalarFunction):
    "Inverse function"

    @staticmethod
    def forward(ctx, a):
        # TODO: Implement for Task 1.2.

        ctx.save_for_backward(a)

        return operators.inv(a)
        raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        # TODO: Implement for Task 1.4.
        x = ctx.saved_values

        df_x = -1 / (x) ** 2
        return df_x * d_output
        raise NotImplementedError('Need to implement for Task 1.4')


class Neg(ScalarFunction):
    "Negation function"

    @staticmethod
    def forward(ctx, a):
        # TODO: Implement for Task 1.2.
        return operators.neg(a)
        raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        # TODO: Implement for Task 1.4.
        df_x = -1

        return -d_output
        raise NotImplementedError('Need to implement for Task 1.4')


class Sigmoid(ScalarFunction):
    "Sigmoid function"

    @staticmethod
    def forward(ctx, a):
        # TODO: Implement for Task 1.2.

        ctx.save_for_backward(a)

        return operators.sigmoid(a)
        raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        # TODO: Implement for Task 1.4.

        x = ctx.saved_values

        df_x = operators.sigmoid(x) * (1 - operators.sigmoid(x))

        return df_x * d_output 
        
        raise NotImplementedError('Need to implement for Task 1.4')


class ReLU(ScalarFunction):
    "ReLU function"

    @staticmethod
    def forward(ctx, a):
        # TODO: Implement for Task 1.2.
        ctx.save_for_backward(a)

        return operators.relu(a)
        raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        # TODO: Implement for Task 1.4.
        x = ctx.saved_values
        
        return 0 if x <= 0 else d_output

        return df_x

        raise NotImplementedError('Need to implement for Task 1.4')


class Exp(ScalarFunction):
    "Exp function"

    @staticmethod
    def forward(ctx, a):
        # TODO: Implement for Task 1.2.
        ctx.save_for_backward(a)

        return operators.exp(a)

        raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        # TODO: Implement for Task 1.4.
        x = ctx.saved_values
        
        df_x = operators.exp(x)
        return df_x * d_output
        raise NotImplementedError('Need to implement for Task 1.4')


def derivative_check(f, *scalars):

    pass
