#include <iostream>
using namespace std;

int main() {
	int testcase;
	//scanf("%d\n", &testcase);
	cout << testcase << "\n";
	for (int i = 0; i < testcase; i++) {
		int n; 
		scanf("%d\n", &n);
		int low;
		int high;
		int cost;
		scanf("%d %d %d\n", &low, &high, &cost);
		bool dual = false;
		int lc = cost;
		int hc = cost;
		printf("%d\n", cost);
		int l;
		int h;
		int c;
		for (int j = 0; j < n-1; j++) {
			scanf("%d %d %d\n", &l, &h, &c);
			if (dual) {
				if (((l < low) && (h >= high)) || ((h > high) && (l <= low))) {
					cost = c;
					low = l;
					high = h;
					dual = false;
				}
				else if ((l < low) || ((l == low) && (c < lc))) {
					low = l;
					lc = c;
					cost = hc + lc;
				}
                else if ((h > high) || ((h == high) && (c < lc))) {
					high = h;
					hc = c;
					cost = hc + lc; 
                }   
			}
			else {
				if (((l < low) && (h >= high)) || ((h > high) && (l <= low)) || ((l == low) && (h == high) && (c < cost))) {
					cost = c;
					low = l;
					high = h;
				}
				else if (l < low) {
					dual = true;
					low = l;
					hc = cost;
					lc = c;
					cost = hc + lc;
				}
				else if (h > high) {
					dual = true;
					high = h;
					lc = cost;
					hc = c;
					cost = hc + lc;
                }
			}
			printf("%d\n", cost);
		}
	}
	return 0;
}
