#include<iostream>
#include<pthread.h>
#include<string>
#include<unistd.h>
using namespace std;

#define NUM_THREADS 5
#define BLACK "\033[0m"
#define RED "\033[1;31m"
#define GREEN "\033[1;32m"
#define YELLOW "\033[1;33m"
#define BLUE "\033[1;34m"
#define CYAN "\033[1;36m"

static pthread_mutex_t mutex1;


void* print_id(void *id){
    string colour;
    pthread_mutex_lock(&mutex1);
    long int thread_id = (long int)id;
    switch (thread_id)
    {
    case 0:
        colour = RED;
        break;
    case 1:
        colour = GREEN;
        break;
    case 2:
        colour = YELLOW;
        break;
    case 3:
        colour = BLUE;
        break;
    case 4:
        colour = CYAN;
        break;
    default:
        colour = BLACK;
        break;
    }
    cout<<colour<<"I'm the thread of "<<thread_id<<endl;
    pthread_mutex_unlock(&mutex1);
    pthread_exit(NULL);
}

int main(){
    pthread_t threads[NUM_THREADS];
    int t;
    long int i;
    for(i=0; i<NUM_THREADS; i++){
        t = pthread_create(&threads[i], NULL, print_id, (void*)i);
        if(t != 0){
            cout << "Error in thread creation: "<<t<<endl;
        }
    }
    for(i=0;i<NUM_THREADS;i++){
        void *status;
        t = pthread_join(threads[i], &status);
        if(t != 0){
            cout << "Error in thread creation: " << t << endl;
        }
    }
    return 0;
}
