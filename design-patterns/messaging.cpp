#include <iostream>

//Implementor
class MessageSender {
    public:
    virtual ~MessageSender() {}
    virtual std::string send_message()const = 0;
};

//Implementor1

class EmailSender: public MessageSender {
    public:
    std::string send_message () const override{
        return "Email\n";
    }
};

//implementor2
class SlackSender: public MessageSender {
    public:
    std::string send_message () const override{
        return "Slack\n";
    }
};


//Abstraction
class Message {
    protected:
        MessageSender* sender_;
    public: 
    Message(MessageSender* message_sender): sender_(message_sender){};
    virtual ~Message() {}

    virtual std::string Operation() const {
        return "Abstraction: Base operation with: " +
        this->sender_->send_message();
    }
};

class TextMessage : public Message {
 public:
  TextMessage(MessageSender* message_sender) : Message(message_sender) {
  }
    std::string Operation() const override {
    return "TextAbstraction: Text operation with: " +
           this->sender_->send_message();
  }
};

class ImageMessage : public Message {
 public:
  ImageMessage(MessageSender* message_sender) : Message(message_sender) {
  }
  std::string Operation() const override  {
    return "ImageAbstraction: Image operation with: " +
           this->sender_->send_message();
  }
};


int main(){
    MessageSender* message_sender = new EmailSender;
    MessageSender* new_message_sender = new SlackSender;

    Message * text_message = new TextMessage(message_sender);
    std::cout << text_message->Operation();

    Message * image_message = new ImageMessage(message_sender);
     std::cout << image_message->Operation();

    text_message = new TextMessage(new_message_sender);
    image_message = new ImageMessage(new_message_sender);
    std::cout << text_message->Operation();
     std::cout << image_message->Operation();


    delete message_sender;
    delete text_message;
    delete image_message;

    return 0;
}
