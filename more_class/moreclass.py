#coding:utf-8

__metaclass__ = type #确定使用新式类

class Person:

    def setName(self,name):
        self.name = name

    def getName(self, name):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name

