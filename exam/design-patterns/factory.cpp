#include <iostream>

class flower{
    public:
        virtual std::string display()const=0;
};

class rose: public flower{
    public:
        std::string display()const override{
            return std::string("Rose");
        }
};

class kakach: public flower{
    std::string display()const override{
        return std::string("Kakach");
    }
};

class Shop{
    public:
        virtual flower* createFlower()const=0;
        virtual ~Shop(){};
};

class RoseShop: public Shop{
    public:
        virtual flower* createFlower()const override{
            return new rose;
        }
};

class KakachShop: public Shop{
    public: 
        virtual flower* createFlower()const override{
            return new kakach;
        }
};

int main(){
    Shop *shop1 = new RoseShop();
    Shop *shop2 =new KakachShop();
    flower *roseobj=(*shop1).createFlower();//accessing the object it points to 
    flower *kakachobj=shop2->createFlower();//the same way of writing

    std::cout<<roseobj->display()<<std::endl;
    std::cout<<kakachobj->display()<<std::endl;

    delete shop1;
    delete shop2;
    delete roseobj;
    delete kakachobj;

    return 0;
}