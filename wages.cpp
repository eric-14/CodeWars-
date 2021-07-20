#include <iostream>
using namespace std;


class wages
{
    public:
    float weekly_salary;
    float pay_per_hour;
    int no_hours;
    int overtime_hours;
    float overtime_rate;

    Wages(int weekly_salary,float pay_per_hour,int no_hours,int overtime_hours, float overtime_rate){
        this->weekly_salary = weekly_salary;
        this->pay_per_hour = pay_per_hour;
        this->no_hours =  no_hours;
        this->overtime_hours = overtime_hours;
        this->overtime_rate = overtime_rate;
    }
    float calculate(int weekly_salary,float pay_per_hour,int no_hours,int overtime_hours, float overtime_rate){
        return salary = no_hours * pay_per_hour + (overtime_hours * overtime_rate *pay_per_hour);
    }
}

int main()
{
    cout<<"Total wages per week "<<Wages()<<endl;
}