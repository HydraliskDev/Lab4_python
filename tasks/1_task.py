def make_file_logger(filename):
    """Возвращает замыкание, которое дописывает значения в файл."""
    count = 0                          # счётчик записей

    def log(value):
        nonlocal count
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'{value}\n')
        count += 1
        return count

    return log
logger = make_file_logger('log.txt')
print(logger('первая запись'))   
print(logger('вторая запись'))
print(logger('вторая запись'))    
           