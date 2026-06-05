#there are 3 types of error
# 1: compile error
# 2: logigal error 
# 3: runtime error
# we can't anything its compile error or logical erroe
# but we modify the runtime error

try:
    a=int(input())
    b=int(input())
    c=a+b
    print(c)
except ValueError as e:
    print('valueerror')
except TypeError as e:
    print('type error')   

except Exception:
    print('error')
finally:
    print('done')    