## Notes for personal referral.

### 06-07-2026
- making an abstract base class helps to abstract the OCR engine interface, making swapping engines easy and promoting modular code
- by putting config params in a class's init attributes (TesseractEngine) we decouple env vars from the class

### 13-07-2026
- remember, when we test, we are testing for behaviour, not implementation. Behaviour is what the function does. Implementation is how the function does what it does. We don't care about how, we care about what.

### 14-07-2026
- you can pass functions as an argument. They are of type 'Callable'

### 17-07-2026
- when mocking, unittest.mock.patch patches functions internally whereas unittest.mock.Mock lets you pass patched objects into the function instead, making the mocked dependency explicit. Always use Mock() where possible.

### 18-07-2026
- pyright config in pyproject.toml: 'include' tells pyright the scope of analysis. 'extraPaths' tells it where to expect imports from

### 26-07-2026
- Mocking in unit tests carry a trade-off between cascading failures and hardcoded mocked dependency logic. PrincessLana subjectively advised to avoid mocking whenever possible, so that tests fail instead of passing inaccurately.
