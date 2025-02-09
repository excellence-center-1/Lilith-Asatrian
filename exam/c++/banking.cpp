#include <iostream>
#include <map>
using namespace std;
class BankManagement {
    public:
        BankManagement(
            string name, 
            string surname, 
            string passport, 
            float dramBalance, 
            float rubliBalance
            ):
            name(name)
            ,surname(surname)
            ,passport(passport)
            // ,dramBalance(dramBalance)
            // ,rubliBalance(rubliBalance)
            {
                currency_accounts["dram"]=dramBalance;
                currency_accounts["rubli"] = rubliBalance;
                ++numOfAccounts;
            }     
        BankManagement() = default;
        ~BankManagement(){
            --numOfAccounts;
        }

        static int getNumOfAccount() {
            return numOfAccounts;
        }

        void deposit(string currency, float amount){
            currency_accounts[currency] += amount;
            if(currency=="dram") {
                dramBalance += amount;
            } else if(currency =="rubli") {
                rubliBalance += amount;
            }
        }

        float getDramBalance(){
            return dramBalance;
        }

        float getRubliBalance(){
            return rubliBalance;
        }

    private:
        string name;
        string surname;
        string passport;
        // float dramBalance;
        // float rubliBalance;
        map<string, float> currency_accounts;
        static float dramBalance;
        static float rubliBalance;
        static int numOfAccounts;
};

int BankManagement::numOfAccounts = 0;
float BankManagement::dramBalance = 0.0;
float BankManagement::rubliBalance = 0.0;

int main(){
    BankManagement myobj("Lilit", "Asatryan", "AT120568", 50, 1200 );
    myobj.deposit("dram", 15000);
    myobj.deposit("rubli", 70000);
    cout<<"Dram balance: "<<myobj.getDramBalance()<<endl;
    cout<<"Rubli balance: "<<myobj.getRubliBalance()<<endl;
    myobj.deposit("rubli", 500);
    cout<<"Rubli balance more: "<<myobj.getRubliBalance()<<endl;
    BankManagement another("Serine", "Asatryan", "AT120568", 350000, 0 );
    std::cout<<"NUMBER OF ACCOUNTS"<<myobj.getNumOfAccount()<<endl;
}


