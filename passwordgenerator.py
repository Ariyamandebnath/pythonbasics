import string
import random
if __name__=="__main__":


    def main():
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        def randompassword():
            s = []
            s.extend(s1)
            # print(s)
            s.extend(s2)
            # print(s)
            s.extend(s3)
            # print(s)
            s.extend(s4)
            # print(s)

            random.shuffle(s)
            print('your password is :')
            print("".join(s[0:passwordlen]))

        passwordlen = (input("Enter the length of the password"))
        if passwordlen.isdigit():
            passwordlen = int(passwordlen)
            randompassword()
        else:
            print("either give a numeric input or else password wont generate")
            main()
    main()