#include <iostream>

using namespace std;

int sum(int n1, int n2){
    
    return n1+n2;
}

int sub(int n1, int n2){
    return n1-n2;
}

int divi(int n1, int n2){
    char okay;
    return n1 / n2;
} 

int mult(int n1, int n2){
    char m = 'a';
    return n1* n2;
}


int main(){
    cout<<"Digite sua operação (numero - operador - numero) - (2+6):";

    int n1          = getchar() - 48;
    char opr        = getchar();
    int n2          = getchar() - 48;
    float result    = 0; 


    if(opr == '+'){
        result = sum(n1,n2);
    } else if(opr == '-'){
        result = sub(n1,n2);
    }else if(opr == '*'){
        result = mult(n1,n2);
    }else if(opr == '/'){
        result = divi(n1,n2);
    }else{
        cout<<"\n Valores invalidos!\n";
    }
    
    cout<<"Resultado: "<<result<<endl;
    
    return 0;
}
