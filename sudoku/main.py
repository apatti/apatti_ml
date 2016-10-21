__author__ = 'apatti'
import model
import csp

if __name__ == '__main__':
    m = model.sModel()
    '''
    m.writerow(0, [0, 0, 9, 0, 0, 0, 0, 0, 0])
    m.writerow(1, [0, 4, 0, 0, 1, 6, 0, 0, 0])
    m.writerow(2, [0, 8, 0, 9, 0, 7, 0, 0, 0])
    m.writerow(3, [0, 3, 0, 0, 0, 0, 8, 0, 0])
    m.writerow(4, [0, 0, 2, 6, 0, 1, 0, 9, 5])
    m.writerow(5, [0, 0, 0, 3, 5, 0, 2, 6, 0])
    m.writerow(6, [1, 0, 0, 0, 0, 0, 9, 0, 0])
    m.writerow(7, [0, 0, 0, 0, 0, 0, 7, 4, 8])
    m.writerow(8, [0, 0, 7, 0, 0, 9, 0, 5, 0])
    
    m.writerow(0, [0, 3, 4, 0, 9, 0, 0, 8, 0])
    m.writerow(1, [0, 0, 0, 4, 0, 0, 0, 0, 0])
    m.writerow(2, [0, 0, 0, 0, 0, 7, 0, 0, 6])
    m.writerow(3, [1, 0, 0, 0, 0, 0, 0, 0, 0])
    m.writerow(4, [5, 6, 0, 0, 0, 0, 0, 9, 1])
    m.writerow(5, [0, 0, 9, 7, 0, 1, 2, 4, 0])
    m.writerow(6, [0, 0, 0, 0, 0, 3, 0, 2, 0])
    m.writerow(7, [0, 0, 0, 0, 0, 0, 5, 0, 4])
    m.writerow(8, [0, 5, 0, 2, 0, 0, 6, 3, 8])
    
    m.display()
    print m.solve()
    m.display()
    '''
    c = csp.csp()
    c.setup({'A':[[1,2,3,4],['A<B']],'B':[[1,2,3,4],['C<D']],'C':[[1,2,3,4],['A<B']],'D':[[1,2,3,4],['A<B']]})
    print c.getvariables()
    print c.getdomain('A')
    print c.getconstraints('B')
