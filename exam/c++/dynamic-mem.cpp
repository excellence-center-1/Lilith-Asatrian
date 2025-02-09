#include <iostream>
// int* func(){
//     int a = 5;
//     int* ptr = &a;
//     return ptr;
// }

// int main(){
    // int* arr = new int[5];
    // *(arr+2) = 15;

    // for(int i = 0; i<5; ++i){
    //     std::cout<<*(arr+i);
    // }
    // std::cout<<*func();
    // delete[] arr;
    // int n,m;
    // std::cin>>m;
    // std::cin>>n;
    // int** ptr = new int*[m];
    // for(int i = 0; i<m; ++i){
    //     ptr[i] = new int[n];
    //     for(int j = 0; j<n; ++j){
    //         std::cin>>ptr[i][j];
    //     }
    // }

    class Geeks{
        int a;

        public:
            Geeks(int a){
                this->a = a;
            }
            Geeks(){};
            void display(){
                std::cout<<"Displayed!";
            }
        
        friend class GCG;
    };
    class GCG{
        int id;
        public:
        void display(Geeks& geeks){
            std::cout<<geeks.a<<std::endl;
        }

    };

    int main(){
        Geeks* geek = new Geeks(10);
        GCG* gcg = new GCG();
        gcg->display(*geek);
        delete geek;
        delete gcg;
        return 0;
    }
