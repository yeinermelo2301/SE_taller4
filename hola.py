import argparse
def say_hello ( yeiner = "World" ):
print ( "Hello " , yeiner, "!" )
parser = argparse.ArgumentParser( description = 'Say hello.' )
parser.add_argument( '--yeiner' , type = str , required = False ,
metavar = 'yeiner' , help = 'your yeiner' , default = 'World' )
args = parser.parse_args()
say_hello(args.yeiner)
