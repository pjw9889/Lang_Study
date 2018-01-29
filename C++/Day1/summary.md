# Day 1



## 1.1 C++ preview



### 1.1.1 namespace

:: scope Operator

using namespace name : How to use namespace



### 1.1.2 Enum type



enum : basically int type

enum class : can use varity type



### 1.1.3 Array



after include Array Header, can use array type

array<int, 3> arr = {9.8.7};



### 1.1.4 Auto function return type

"auto" type

auto x = 123; // it is int type

decltype(x) y = 456; // guess y type from x type

decltype (auto) y = 456;

auto result = getFoo(); // return function value 



## 1.2 Memory management



### 1.2.1 dynamic array size 



int arraysize = 8;

int *myVariable = new int[arraysize];

delete [] *myVariable;



### 1.2.2 Smart pointer



Smart pointer exist in <Memory> header



type : unique_ptr, shared_ptr, weak_ptr



make common pointer

Employee * anEmployee = new Employee;



#### unique_ptr

std::unique_ptr <Employee> anEmployee(new Emplyee);

#### shared_ptr

dont support array type

std::make_shared<>();



## 1.3 Class

Need to member, method

have a constructor, destrcutor