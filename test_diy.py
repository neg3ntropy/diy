from diy import *

class Interface(object):
    def imethod(self):
        raise NotImplementedError()

class Implementation(Interface):
    def __init__(self):
        self.value = 'Implementation'
    def imethod(self):
        return self.value


injector.provide(Interface, Implementation)


@inject(interface=Interface)
class Dependent(object):
    def __init__(self, interface):
        self.interface = interface


Dependent().interface.imethod()


Dependent(interface='parameter').interface


instance = Implementation()
instance.value = 'instance'
injector.provide_instance(Interface, instance, name='name')


@inject(interface=named('name', Interface))
class NamedDependent(object):
    def __init__(self, interface):
        self.interface = interface

NamedDependent().interface.imethod()


@singleton(interface=Interface)
class SomeSingleton(Dependent):
    pass

SomeSingleton() is SomeSingleton()


@inject(singleton=SomeSingleton)
class SingletonDependent(object):
    def __init__(self, singleton):
        self.singleton = singleton

SingletonDependent().singleton is SomeSingleton()
