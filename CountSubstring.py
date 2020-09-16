def count_substring(string, sub_string):
    start=0
    count=0
    strlen = len(string)
    if strlen>1 and strlen<=100:
        while start< strlen:
            pos = string.find(sub_string,start)
            if pos!=-1:
                start = pos+1
                count = count+1
            else:
                break
        return count
    else:
        return 0

if __name__ == '__main__':
   string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
