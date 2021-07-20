#include <iostream>
using namespace std;
class invoiceItem
{
    public:
    char item_name;
    int quantity;
    float price;
    float total_cost;

    InvoiceItem(char item_name,int quantity,float price,float total_cost){
        this->item_name = item_name;
        this->quantity = quantity;
        this->price = price;
        this->total_cost =total_cost;
    }
    
    char get_itemname(){
        cout<<"item_name"<<item_name<<endl;
    }
    char set_itemname(char item_name){
        this->item_name = item_name
    }
    int get_quantity(){
        cout<<"Quantity"<<this->quantity<<endl;
    }
    int set_quantity(int quantity){
        this->quantity = quantity
    }
    float set_price(int price){
        this->price = price
    }
    float get_price()
    {
        cout<<"price"<<this->price<<endl;
    }
}
int main(){
    
}