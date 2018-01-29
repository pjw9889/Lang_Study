#include <iostream>
#include "Employee.h"

using namespace std;
using namespace Records;

int main(){

	cout << "Testing the Employee class." << endl;
	Employee emp;

	emp.setFirstName("Jae");
	emp.setLastName("Park");
	emp.setEmployeeNumber(14);
	emp.setSalary(5000);
	emp.promote();
	emp.promote(50);
	emp.hire();
	emp.display();
	
	return 0;
}