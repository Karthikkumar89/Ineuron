
import logging

logging.basicConfig(filename='test1.log',filemode='w',level= logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%d-%m-%y  %H:%M:%S')

#A class & its methods
class A:
    logging.info('Division of two numbers')
    def divide(self,a,b):
        try:
            s=a/b
            logging.info("Division completed & result below")
            return s

        except Exception as e:
            logging.error(e)

# List class & its methods
class lists:

    def extract_list(self,*args):
        logging.info('List extraction starts')
        try:
            logging.info([i for i in args if type(i)==list])
            logging.info('List extraction complete')
        except Exception as e:
            logging.error(e,'input only list, tuples, set or Dict')

    def squares(self,list):
        try:
            logging.info('Square #s in the list')
            logging.info([i**2 for i in list])
            logging.info('Sqauare operation complete')
        except Exception as e:
            logging.error(e,'Enter only integers')

#method calling
s=A()
s.divide(5,0)

l=lists()
l.extract_list([1,2],['k'],'2',[2,9,'kart'])

sq=lists()
sq.squares([1,2,3])














