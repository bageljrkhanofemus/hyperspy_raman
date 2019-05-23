from hyperspy.component import Component
from traits.api import CBool
from hyperspy.ui_registry import add_gui_method


@add_gui_method(toolkey="hspy_ext.MyComponent")
class MyComponent(Component):

    """
    """

    test_gui = CBool(True)

    def __init__(self, parameter_1=1, parameter_2=2):
        # Define the parameters
        Component.__init__(self, ('parameter_1', 'parameter_2'))

        # Optionally we can set the initial values
        self.parameter_1.value = parameter_1
        self.parameter_1.value = parameter_1

        # The units (optional)
        self.parameter_1.units = 'Tesla'
        self.parameter_2.units = 'Kociak'

        # Once defined we can give default values to the attribute
        # For example we fix the attribure_1 (optional)
        self.parameter_1.free = False

        # And we set the boundaries (optional)
        self.parameter_1.bmin = 0.
        self.parameter_1.bmax = None

        # Optionally, to boost the optimization speed we can also define
        # the gradients of the function we the syntax:
        # self.parameter.grad = function
        self.parameter_1.grad = self.grad_parameter_1
        self.parameter_2.grad = self.grad_parameter_2

    # Define the function as a function of the already defined parameters,
    # x being the independent variable value
    def function(self, x):
        p1 = self.parameter_1.value
        p2 = self.parameter_2.value
        return p1 + x * p2

    # Optionally define the gradients of each parameter
    def grad_parameter_1(self, x):
        """
        Returns d(function)/d(parameter_1)
        """
        return 0

    def grad_parameter_2(self, x):
        """
        Returns d(function)/d(parameter_2)
        """
        return x

