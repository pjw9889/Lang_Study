#include <iostream>
#include "Database.h"
using namespace std;
using namespace Records;

int main(){

	Database myDB;
	Employee& emp1 = myDb.addEmployee("Park", "Jae");
	emp1.fire();
	Employee& emp2 = myDb.addEmployee("Par", "Ja");
	emp2.setSalary(1090000);
	Employee& emp3 = myDb.addEmployee("ar", "J");
	emp3.setSalary(10000);

	emp3.promote();
	cout << "all employess : " << endl << endl;
	myDB.displayAll;
	cout << endl << "current employees : " << endl << endl;
	myDB.displayCurrent();
	cout << endl << "former employees : " << endl << endl;
	myDb.displayFormer();

	return 0;
}