#include <iostream>
//Product
class Shaurma{
    private:
        bool _onion;
        std::string _sauce;
        std::string _meat;
    public:
        void setOnion(const bool presence){
            _onion=presence;
        }
        void setMeat(const std::string& meat){
            _meat=meat;
        }

        void setSauce(const std::string& sauce){
            _sauce=sauce;
        }

        void print(){
            std::cout<<"Shaurma with"<<std::endl<<"Meat: "<<_meat<<std::endl<<"Sauce: "<<_sauce<<std::endl<<(_onion)? "With onion": "Without Onion";
            
        }
};

//Builder Abstract class
class ShaurmaBuilder{
    public: 
        virtual void BuildOnion()const=0;
        virtual void BuildMeat()const=0;
        virtual void BuildSauce()const=0;
        virtual Shaurma getresult()const=0;
    private:
        Shaurma _shaurma;
};


//Concrete Buildera
class XoziShaurma: public ShaurmaBuilder{

    private:
        Shaurma *xoziShaurma;
    public:
        void BuildOnion()const override{
            xoziShaurma->setOnion(true);
        }
        void BuildMeat()const override{
            xoziShaurma->setMeat("xoz");
        }

        void BuildSauce()const override{
            xoziShaurma->setSauce("Smetan");
        }

        Shaurma getresult() const override{
            return (*xoziShaurma);
        }
};

//Director

class ShaurmaDirector{
    public:
        Shaurma buildShaurma(ShaurmaBuilder& builder){
            builder.BuildMeat();
            builder.BuildSauce();
            builder.BuildOnion();
            return builder.getresult();
        }
};

int main(){
    ShaurmaDirector director;
    XoziShaurma XoziShaurmaBuilder;
    Shaurma shaurma=director.buildShaurma(XoziShaurmaBuilder);
}