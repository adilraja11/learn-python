value = 0

try:
    if value == 0:
        raise Exception('Not Valid Value')
except Exception as e:
    print(f'Exception: {e}')