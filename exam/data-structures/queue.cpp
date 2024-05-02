#include <iostream>
#include <vector>
template <typename T> class Queue{
private:
    std::vector<T> vec;

public:
    void enqueue(const T& elem){
        vec.push_back(elem);
    }

    T dequeue(){
        if(empty()){
            throw std::out_of_range("NO ELEMENT");
        }
        T front_elem = vec.front();
        vec.erase(vec.begin());
        return front_elem;
    }

    T front(){
        return 
    }
    bool empty(){
        return vec.empty();
    }
};

int main(){
    Queue<int> queue;

    queue.enqueue(10);
    queue.enqueue(15);
    std::cout<<queue.dequeue();
    // while(!queue.empty()){
    //     std::cout<<queue.dequeue()<<" ";
    // }



    std::cout<<std::endl;
    return 0;
}
    

