num=1

if __name__ == '__main__':
    while True:
        try:
            num+=1
            print(num)
            if num % 2 ==0:
                raise RuntimeError('testError')
        except Exception as e:
            print("catch error")
        finally:
            print("this is finally")