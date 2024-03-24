class Solution {
public:
    int dayOfYear(string date) {
        int year = stoi(date.substr(0,4));
        bool leap_year = (!(year % 4) && (year % 100)) || !(year % 400);
        int month = stoi(date.substr(5,2));
        int day_of_month = stoi(date.substr(8));
        int day = 0;
        for(int i = 1; i < month; i++){
            switch(i){
                case 1: day += 31; break;
                case 2: day += leap_year ? 29:28; break;
                case 3: day += 31; break;
                case 4: day += 30; break;
                case 5: day += 31; break;
                case 6: day += 30; break;
                case 7: day += 31; break;
                case 8: day += 31; break;
                case 9: day += 30; break;
                case 10: day += 31; break;
                case 11: day += 30; break;        
            }         
        }
        day += day_of_month;
        return day;  
    }
};