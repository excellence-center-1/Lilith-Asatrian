#include <iostream>
//Abstract Chair
class Chair {
    public:
        virtual std::string display () const=0;
        virtual ~Chair(){};
};

//Abstract Piano
class Piano {
    public: 
        virtual std::string display()const=0;
};

class CircleChair: public Chair{
    public:
        std::string display()const override{
            return std::string("Circle chair");
        }
};

class RecChair: public Chair{
    std::string display()const override{
        return std::string("Rectangle chair");
    }
    virtual ~RecChair(){};
};

class ElectricPiano: public Piano{
    std::string display()const override
    {
        return std::string("Electric Piano");
    }
};

class ClassicPiano: public Piano{
    std::string display()const override
    {
        return std::string("Classic Piano");
    }
};

class Country{
    public:
    virtual Chair* createChair()const=0;
    virtual Piano* createPiano()const=0;
};

class Bulgary: public Country{
    public:
        Chair* createChair()const override{
            return new CircleChair;
        }
        Piano* createPiano()const override{
            return new ElectricPiano;
        }
};

class Italia: public Country{
    public: 
    Chair* createChair()const override{
        return new RecChair;
    }
    public:
    Piano* createPiano()const override{
        return new ClassicPiano;
    }
};

int main(){

    std::cout<<"Bulgarian: ";
    Country* bulgary=new Bulgary();
    Country* italia=new Italia();
    Chair* bulgcircleChair= (*bulgary).createChair();
    std::cout<<bulgcircleChair->display()<<std::endl;

    std::cout<<"Italian: ";
    Country *italia = new Italia();
    Piano* italClassPiano=(*italia).createPiano();
    std::cout<<italClassPiano->display()<<std::endl;
    
    delete bulgary;
    delete italia;
    delete bulgcircleChair;
    delete italClassPiano;
    return 0;
}



// class Italian{
//     virtual Chair* createObjectCircleChair()=0;
//     virtual Piano* createObjectElectricPiano()=0;
// };

// class ItalianFactory: public Italian{
//     Chair* createObjectCircleChair(){
//         return new CircleChair();
//     }
//     Piano* createObjectEletricPiano(){
//         return new ElectricPiano;
//     }
// };

// class Bulgarian{
//     public:
//     virtual Chair* createRecChair()const =0;
//     virtual Piano* createClassicPiano()const=0;
//     virtual ~Bulgarian(){};
// };

// class BulgarianFactory: public Bulgarian{
//     public: 

//     Chair* createRecChair()const override{
//         return new RecChair;
//     }
//     Piano* createClassicPiano()const override{
//         return new ClassicPiano;
//     }

//     virtual ~BulgarianFactory(){};
// };
