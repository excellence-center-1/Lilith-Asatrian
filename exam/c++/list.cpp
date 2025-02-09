#include <iostream>
#include <string>
template <typename T> class Node {
    protected:
        T* value;
        Node* prev;
        Node* next;
    
    public:
        Node(const T& val): value(new T(val)), prev(nullptr), next(nullptr){}
        ~Node(){
            delete value;
        }

        void set_value(const T& val){
            *value = val;
        }

        T& get_value(){
            return *value;
        }

        // Node* get_prev(Node<T>* node){
        //     return node->prev;
        // }

        //const xi?
        Node* get_prev() const{
            return prev;
        }

        Node* get_next() const{
            return next;
        }

        void set_prev(Node<T>* node){
            prev = node;
        }


        void set_next(Node<T>* node){
            next = node;
        }

};


template <typename T>
class List {
    protected:
        Node<T>* head;
    
    public: 
        List(): head(nullptr){}
        ~List(){
            Node<T>* current = head;
            while(current){
                Node<T>* next = current->get_next();
                delete current;
                current = next;
            }
        }

        void push_back(const T& val){
            Node<T>* new_node = new Node<T>(val);
            if(head == nullptr){
                head = new_node;
            }
            else {
                Node<T>* curr_el = head;
                while(curr_el->get_next()){
                    curr_el = curr_el->get_next();
                }
                curr_el->set_next(new_node);
                new_node->set_prev(curr_el);
            }
        }

        T pop(){
            if(head==nullptr){
                throw std::logic_error("Can't pop from an empty list.");
            }
            Node<T>* curr_el = head;
            while(curr_el->get_next()){
                curr_el = curr_el->get_next();
            }
            T value = curr_el->get_value();
            if(curr_el==head){
                head = nullptr;
            } else {
                curr_el->get_prev()->set_next(nullptr);
            }
            delete curr_el;
            return value;
        }

        void push_front(const T& val){
            Node<T>* new_node = new Node<T>(val);
            if(head==nullptr){
                head = new_node;
            } else {
                head->set_prev(new_node);
                new_node->set_next(head);
                head = new_node;
            }
        }

        int find(const T& value){
            int i = 0;
            Node<T>* curr_el = head;
            if(curr_el->get_value() == value){
                return i;
            } 
            else {
                while(curr_el->get_next()){
                    ++i;
                    if(curr_el->get_value() == value){
                        return i;
                    }
                    curr_el = (*curr_el).get_next();
                } 

            }
            return -1;
        }

};

int main(){
    // Node<int> a(10);
    // std::cout<<a.get_value()<<std::endl;
    // a.set_value(15);
    // std::cout<<a.get_value()<<std::endl;
    try {
        List<int> list;
        list.push_back(13);
        list.push_front(15);
        list.push_back(20);
        list.push_front(10);

        std::cout<<"Element is found at index "<<list.find(2)<<std::endl;
    }
    catch(const std::exception& E){
        std::cerr<<E.what()<<std::endl;
    }
    return 0;
}
