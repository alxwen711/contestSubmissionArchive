#include <iostream>
#include <vector>
using namespace std;

int ex(vector<vector<int>> ar, int x) {
  vector<vector<int>> cr;
  for (int t = 0; t < 10; t++) {
    for (int u = 0; u < ar[t].size(); u++) {
      vector<int> snth = [ar[t][u],t];
      cr.push_back(snth);
    }
  }
  cr.sort();
  cr.reverse();
  bool add = true;
  int ans = 0;
  int index = x;
  int h[10] = [0,0,0,0,0,0,0,0,0,0];
  for (int m = 0; m < cr.size(); m++) {
    vector<int> v = cr[m]
    h[v[1]] ++;
    if (count(h.begin(), h.end(), 10) != 0) {
      return ans;
    }
    if ((10 - count(h.begin(), h.end(), 0)) < max_element(h.begin(), h.end())) {
      add = false;
    }
    else {
      add = true;
    }
    if (add) {
      ans += (index - v[0]);
    }
    index = v[0];
  }
  if (add) {
    ans += index;
  }
  return ans;
}

int solve(int n, string s) {
  vector<vector<int>> ar {{},{},{},{},{},{},{},{},{},{}};
  int ans = 0;
  for (int j = 0; j < n; j++) {
    ar[int(s[j])].push_back(j);
    if (ar[int(s[j])].size() == 11) {
      ar[int(s[j])].erase(0);
    }
    ans += ex(ar,j+1);
  }
  return ans;
}

int main() {
  int t;
  int n;
  string s;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> n;
    cin >> s;
    cout << solve(n,s) << "\n";
  }
  return 0;
    
}
