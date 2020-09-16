if __name__ == '__main__':
    s = raw_input()
    strlen = len(s)
    if strlen>1 and strlen<=100:
        print any([char.isalnum() for char in s])
        print any([char.isalpha() for char in s])
        print any([char.isdigit() for char in s])
        print any([char.islower() for char in s])
        print any([char.isupper() for char in s])
        
