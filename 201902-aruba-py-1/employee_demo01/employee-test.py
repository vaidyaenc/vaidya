from employee import Employee


def main():
    employees=[]
    for i in range(1,11):
        name='Employee {}'.format(i)
        employees.append(Employee(name,1000))

    for e in employees:
        print(e.info())

if __name__=='__main__':
    main()