'''
Write a decorator that wraps a function in a try-except block and print an error if error has happened
    Example
    ```python
    @catch_errors
    def some_function_with_risky_operation(data):
        print(data['key'])


    some_function_with_risky_operation({'foo': 'bar'})
    > Found 1 error during execution of your function: KeyError no such key as foo

    some_function_with_risky_operation({'key': 'bar'})
    > bar
'''

def decorator_try_except(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Found 1 error during execution of your function: {type(error).__name__} no such key as '{error.args[0]}'")
    return wrapper

@decorator_try_except
def some_function_with_risky_operation(data):
    return data.get('key', None)

result = some_function_with_risky_operation({'key': 'bar'})
if result is not None:
    print(result)
else:
    print("Key not found")


'''
Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs

    Example

    ```python
    @is_admin
    def show_customer_receipt(user_type: str):
        # some very dangerous operation

    show_customer_receipt(user_type='user')
    > ValueError: Permission denied

    show_customer_receipt(user_type='admin')
    > function pass as it should be
    ```
'''

def require_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_type = kwargs.get('user_type')
            if user_type != role:
                raise ValueError(f"Користувач повинен мати {role} роль, щоб отримати доступ до цієї функції")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@require_role('admin')
def show_customer_receipt(user_type):
    if user_type == 'user':
        return "Квитанція клієнта"
    else:
        raise ValueError("У дозволі відмовлено")

show_customer_receipt(user_type='admin')