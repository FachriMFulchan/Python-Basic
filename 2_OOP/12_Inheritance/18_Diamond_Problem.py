#inheritance jadi kaya diamond gitu

class A():
    def show(self):
        print ('ini adalah show A')

class B(A):
    def show(self):
        print ('ini adalah show B')

class C(A):
    def show(self):
        print ('ini adalah show C')

class D(B,C):
    pass


objek = D()
objek.show()
print(help(objek))

#jadi sama aja mentingin prioritas (METHOD RESOLUTION ORDER)