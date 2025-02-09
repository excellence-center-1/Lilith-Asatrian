#include <iostream>
#include <string>
struct Rectangle {
    private:
        float length;
        float width;
    public:
        Rectangle(float length, float width){
            if(length<=0 || width<=0){
                throw std::invalid_argument("Not valid arguments are given.");
            }
            this->length = length;
            this->width = width;
        }

        Rectangle() = default;
        ~Rectangle(){};

        float getWidth() {
            return this->width;
        }

        void setWidth(float width){
            this->width = width;
        }

        float perimeter(){
            return 2*(width+length);
        }

        float area(){
            return width*length;
        }

        void isSquare(){
            if(length==width){
                std::cout<<"true" ;
            }
            else {
               std::cout<<"false" ;
            }
        }
};  

int main(){
    try{
        Rectangle r(-6,6);
        std::cout<<"The rectangle is square: ";
        r.isSquare();
        std::cout<<std::endl;
        std::cout<<"Perimeter equals: "<<r.perimeter()<<std::endl;
    }catch(std::invalid_argument& err) {
        std::cout<<err.what()<<std::endl;
    }

    return 0;
}