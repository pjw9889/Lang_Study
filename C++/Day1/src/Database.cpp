#include <iostream>
#include <stdexcept>
#include "Database.h"

using namespace std;

namespace Records{
	Database::Database() : mNextEmployeeNumber(kFirstEmployeeNumber){

	}

	Employee& Database::addEmployee(const string& firstName, const string& lastName){
		Employee theEmployee;
		theEmployee.setFirstName(firstName);
		theEmployee.setLastName(lastName);
		theEmployee.setEmployeeNumber(mNextEmployeeNumber++);
		theEmployee.hire();
		mEmployees.push_back(theEmplyee);
		return mEmployees[mEmployees.size() - 1];
	}

	Employee& Database::getEmployee(int employeeNumber){
		for (auto&employee : mEmplyees){
			if (employee.getEmployeeNumber() == employeeNumber){
				return employee;
			}
		}
		throw runtime_error("No emplyee Found.");
	}
	
	void Database::displayAll() const{
		for (const auto& employee : mEmployess){
			employee.display();
		}
	}

	void Database::displayCurrent() const{
		for (const auto& employee : mEmployess){
			if (employee.getIsHired())
				employee.display();
		}
	}
	
}