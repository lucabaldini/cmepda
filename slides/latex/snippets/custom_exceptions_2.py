class ValueTooLargeError(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__('{}: {} is too large'.format(self.__class__.__name__,
                                                      self.value))

value = 100
try:
  if value > 10:
      raise ValueTooLargeError(value)
except ValueError as e:
    print(e)
