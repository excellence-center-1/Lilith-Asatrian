// #include <iostream>
// using namespace std;
// struct Student{
//     string name;
//     int age;
//     float grade;
// };

// void input(Student* arr, int n){
//     for(int i = 0; i<n; ++i){
//         cout<<"Student["<<i<<"] name: "; cin>>arr->name;
//         cout<<"Student["<<i<<"] age: "; cin>>arr->age;
//         cout<<"Student["<<i<<"] grade: "; cin>>arr->grade;
//         ++arr;
//     }
// }

// void output(Student* arr, int n){
//     for(int i = 0; i<n; ++i){
//         cout<<"Student["<<i<<"] name: "<<arr->name<<endl;
//         cout<<"Student["<<i<<"] age: "<<arr->age<<endl;
//         cout<<"Student["<<i<<"] grade: "<<arr->grade<<endl;
//         ++arr;
//     }
// }
// float average(Student* arr, int n){
//     float sum = 0;
//     for(int i = 0; i<n; ++i){
//         sum+=(*arr).grade;
//         ++arr;
//     }
//     return sum/n;
// }
// int main(){
//     int n;
//     cout<<"Enter the number of students: ";
//     cin>>n;
//     Student* arr = new Student[n];
//     input(&arr[0], n);
//     cout<<"-----Output---------\n";
//     output(arr, n);
//     cout<<"-----AVERAGE------\n";
//     cout<<average(arr, n)<<endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// enum Type{Car, Bike, Truck };
// struct Car{
//     string make;
//     string model;
//     int year;
//     Car(string make, string model, int year){
//         this->make = make;
//         this->model = model;
//         this->year = year;
//     }
// };
// struct Bike{
//     string make;
//     string type;
//     int year;
//     Bike(string make, string type, int year): make(make), type(type), year(year){}
// };
// struct Truck{
//     float capacity;
//     string make;
//     int year;
//     Truck(float capacity, string make, int year){
//         this->capacity = capacity;
//         this->make = make;
//         this->year = year;
//     }
// };

// union VehicleInfo{
//     struct Car car;
//     struct Bike bike;
//     struct Truck truck;
// };

// struct Vehicle{
//     Type vehicle;
//     VehicleInfo info;
    
// };

// int main(){
//     int n;
//     cout<<"n="; cin>>n;
//     Vehicle vehicles[3];


//     return 0;
// }