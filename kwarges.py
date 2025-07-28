def filter_info(**kwargs):
    allowed_keys = ['name', 'city']
    for keys, values in kwargs.items():
        if keys in allowed_keys:
            print(f"{keys} : {values}")

        


filter_info(name='Prakash', age=25, language='Python', city='Delhi')