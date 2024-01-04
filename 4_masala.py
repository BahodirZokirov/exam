def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str):
                raise ValueError("Xatolik: Argumentlar son bo'lishi kerak, str kiritilgan.")
        for key, value in kwargs.items():
            if isinstance(value, str):
                raise ValueError(f"Xatolik: {key} argumenti son bo'lishi kerak, str kiritilgan.")
        return func(*args, **kwargs)
    return wrapper

@validate_arguments
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(3, 5)
print("Natija:", result)

try:
    result_with_str = multiply_numbers(3, "5")
except ValueError as ve:
    print(f"Xatolik: {ve}")
