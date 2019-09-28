def func(**kwargs):
    """
    """
    print(kwargs.get('verbose', False))


func()
func(verbose=True)
func(verbose=False)
func(verbose=True, num_events=3)
func(True)
