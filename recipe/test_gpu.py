import qulacs


state = qulacs.QuantumStateGpu(2)
if state.get_device_name() != 'gpu':
    raise RuntimeError('GPU test failed')
