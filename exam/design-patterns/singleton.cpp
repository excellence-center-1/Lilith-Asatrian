#include <iostream>
class Singleton{
    protected:
        Singleton()=default;

    public:
        int data;
        //static keyword make this function specific to the class
        static Singleton& getinstance(){
            static Singleton instance;
            return instance;
        }
        Singleton(const Singleton&)=delete;//copy constructor
        Singleton(Singleton&&)=delete;//move constructor
        Singleton operator=(const Singleton&)=delete;//copy assignment
        Singleton operator=(Singleton&&)=delete;//move assignment
};
int main(){
    Singleton& instance1=Singleton::getinstance();
    instance1.data=50;
    std::cout<<"Instance1="<<instance1.data<<std::endl;
    Singleton& instance2=Singleton::getinstance();
    instance2.data=60;
    std::cout<<"Instance2="<<instance2.data<<std::endl;

    // Singleton instance3=instance1;
    return 0;
}