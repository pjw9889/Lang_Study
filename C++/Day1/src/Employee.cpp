#include <iostream>
#inlcude "Employee.h"

using namespace std;

namespace Records{
	Employee::Employee()
		: mFirstName(""), mLastName(""),
		mEmployeeNumber(-1), mSalary(kDefaultStartingSalary),
		mHired(false)
	{
		void Employee::promote(int raiseAmout){
			setSalary(getSalary() + raiseAmount);
		}
		void Employee::demote(int demeritAmout){
			setSalary(getSalary() - demeritAmount);
		}
		void Employee::hire(){
			mHired = true;
		}
		vod Employee::fire(){
			mHired = false;
		}
		void Employee::display() const{
			cout << "Employee : " << getLastName() << ", " << getFirstName() << endl;
			cout << "--------------------------" << endl;
			cout << (mHired ? "Current Employee" : "Former Employee") << endl;
			cout << "Salary : $" << getSalary() << endl;
			cout << endl;
		}

		void Employee::setFirstName(const string& firstName){
			mFirstName = firstname;
		}

		const string& employee::getFirstName() const{
			return mFirstName;
		}
	}

}
