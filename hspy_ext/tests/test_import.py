import numpy as np

from hspy_ext import signal, component


def test_import_signal():
    my_signal = signal.MySignal(np.arange(10))
    assert my_signal._signal_type == 'MySignal'

def test_import_components():
    my_component = component.MyComponent()
    assert my_component._id_name == 'dcbd09ee-a420-4700-b60d-3a59e07e1237'
    assert my_component.parameter_1.value == 1
    assert my_component.parameter_2.value == 2