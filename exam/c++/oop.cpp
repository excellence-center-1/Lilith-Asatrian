#include <iostream>
#include <string>
class Animal{
    private:
        std::string name;
        int age;

    protected:
        void displayinfo();
    public:
        Animal(std::string name1, int age1): name(name1), age(age1){}
        ~Animal(){}
};

void Animal::displayinfo(){
    std::cout<<"Name: "<<name<<std::endl;
    std::cout<<"Age: "<<age<<std::endl;
}

class Mammal: protected Animal{
    protected:
        std::string type;
    public:
        Mammal(std::string type1, std::string name1, int age1): Animal(name1, age1), type(type1){}
        ~Mammal(){}
        void set_type(std::string type){
            this->type=type;
        }
        std::string get_type(){
            return type;
        }
};

class Bird: Animal{
    protected: 
        float wingSpan;
    public:
        Bird(float wingSpan1, std::string name1, int age1): Animal(name1, age1), wingSpan(wingSpan1){}
        void set_wing(float wingSpan){
            this->wingSpan=wingSpan;
        }
        float get_wing(){
            return wingSpan;
        }
};

class MarineMammal: protected Mammal{
    private:
        float swimSpeed;
    public:
        MarineMammal(float swimSpeed, std::string type, std::string name, int age ): 
                Mammal(type, name, age), swimSpeed(swimSpeed){}
        ~MarineMammal(){}
        void set_swimspeed(float swimspeed){
            this->swimSpeed=swimSpeed;
        }
        
        float get_swimspeed(){
            return swimSpeed;
        }

};

class Dolphin: protected MarineMammal, Bird{
    public:
        Dolphin(float swimSpeed,float wingSpan, std::string type, std::string name, int age ): 
                MarineMammal(swimSpeed, type, name, age), Bird(wingSpan, name, age){}
        ~Dolphin(){}
        void displayAllInfo(){
            MarineMammal::displayinfo();
            std::cout<<"Wing span is "<<get_wing()<<" long."<<std::endl;
            std::cout<<"Swim speed is "<<get_swimspeed()<<" fast."<<std::endl;
        }
};
int main(){
    Dolphin dolphin(13, 12.5, "crazy", "Baby", 56 );
    dolphin.displayAllInfo();
    return 0;
}