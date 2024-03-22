class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder(){
        
    }
    
    void addNum(int num) {
        ms.insert(num);
        if(ms.size() == 1) {
            mid= ms.begin(); 
            return;
        }
        if(num < *mid) {
            if(ms.size() % 2 == 0) mid = prev(mid);
        }
        else{//note that for duplicate values in multiset in c++, new ones always insert behind old ones, i.e., same ways as it was larger
            if(ms.size() % 2 == 1) mid = next(mid);
        }
    }
    
    double findMedian() {      
        return ms.size() % 2? (double)*mid : (double) (*mid + *next(mid))/2.0;
    }
private:
    multiset<int> ms;
    multiset<int>::iterator mid;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */