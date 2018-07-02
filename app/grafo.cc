#include <iostream>
#include <vector>

using namespace std;


using VI = vector<int>;
using VB = vector<bool>;
using VVI = vector<VI>;


VI sol(9), data(7);
VB used(10, false);
int cont = 0;
VVI connect = {
  {0, 1, 2},
  {0, 2, 3, 5},
  {1, 2, 4, 6},
  {2, 5, 6},
  {3, 5, 7},
  {4, 6, 8},
  {5, 6, 7, 8},
};


void start() {
  system("clear");
  cout << "\t" << "\t";
  cout << "PROGRAMA PARA RESOLVER GRAFOS -- DAVID ÁLVAREZ";
  cout << endl << endl << endl;
  cout << "El grafo debe introducirse fila por fila comenzando por arriba." << endl;
  cout << "Introduzca grafo: ";
}


void print() {
  cout << endl << endl;
  cout << "\t" << "\t" << "\t" << sol[0] << "\t" << "\t" << sol[1] << endl << endl;
  cout << "\t" << "\t" << "\t" << "\t" << data[0] << endl << endl;
  cout << "\t" << "\t" << "\t" << "\t" << sol[2] << endl << endl;
  cout << "\t" << "\t" << data[1] << "\t" << "\t" << "\t" << "\t" << data[2] << endl << endl;
  cout << "\t" << sol[3] << "\t" << "\t" << "\t" << data[3] << "\t" << "\t" << "\t" << sol[4] << endl << endl;
  cout << "\t" << "\t" << "\t" << sol[5] << "\t" << "\t" << sol[6] << endl << endl;
  cout << "\t" << "\t" << data[4] << "\t" << "\t" << "\t" << "\t" << data[5] << endl << endl;
  cout << "\t" << "\t" << "\t" << "\t" << data[6] << endl << endl;
  cout << "\t" << "\t" << sol[7] << "\t" << "\t" << "\t" << "\t" << sol[8] << endl << endl << endl;
}


void read() {
  for (int i = 0; i < 7; ++i) {
    int x;
    cin >> x;
    data[i] = x;
  }
  
  bool understand = false;
  while (not understand) {
    print();
    cout << "¿El tablero es correcto? (s/n): ";
    string res;
    cin >> res;
    if (res == "s" or res == "S" or res == "Si"
  	or res == "Sí" or res == "si" or res == "sí")
      understand = true;
    else if (res == "n" or res == "N"
  	     or res == "No" or res == "no") {
      cout << endl << "Vuelva a introducir el tablero: ";
      for (int i = 0; i < 7; ++i) {
  	int x;
  	cin >> x;
  	data[i] = x;
      }
    }
  }
}


bool check() {
  for (int i = 0; i < 7; ++i) {
    bool filled = true;
    int value = 0;
    for (int j = 0; j < int(connect[i].size()); ++j) {
      if (sol[connect[i][j]] == 0) filled = false;
      value += sol[connect[i][j]];
    }
    if (filled and value != data[i]) return false;
  }
  
  return true;
}


void solve(int i) {
  if (i == 9) {
    ++cont;
    cout << endl << "Solución número " << cont << ":";
    return print();
  }

  for (int j = 1; j < 10; ++j)
    if (not used[j]) {
      sol[i] = j;
      used[j] = true;
      if (check()) solve(i + 1);
      sol[i] = 0;
      used[j] = false;
    }
}


int main() {
  start();
  read();

  solve(0);

  if (cont == 0)
    cout << "No se ha encontrado ninguna solución." << endl;
}
