#include <pthread.h>

// Version from p318, no prevention of deadlocks
int a, b;
pthread_mutex_t lock_a = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t lock_b = PTHREAD_MUTEX_INITIALIZER;

void procedure1(int arg) {
	pthread_mutex_lock(&lock_a);
	if (a == arg) {
		procedure2(arg);
	}
	pthread_mutex_unlock(&lock_a);
}

void procedure2(int arg) {
	pthread_mutex_lock(&lock_b);
	b = arg;
	pthread_mutex_unlock(&lock_b);
}

//// unacceptable version: (locks b unnecessairly)
void procedure1(int arg) {
	pthread_mutex_lock(&lock_b);
	pthread_mutex_lock(&lock_a);
	if (a == arg) {
		procedure2(arg);
	}
	pthread_mutex_unlock(&lock_a);
	pthread_mutex_unlock(&lock_b);
}

//////////////////////////////////////////////////////////////////////////////
/// Modified version ///
// Declared at beginning of code somewhere
int used_b = 0 // Track use of lock_b so it can be obtained before a

void procedure1(int arg; int used_b) {
	/* Unlike the unacceptable version, this version only gets lock_b if
	it is likely to be needed because the thread used it in the past */
	pthread_mutex_lock(&lock_a);
	if (used_b == 1) {
		pthred_mutex_lock(&lock_b);
	}
	if (a == arg) {
		procedure2(arg);
	}
	pthread_mutex_unlock(&lock_a);
	if (used_b == 1) {
		pthread_mutex_unlock(&lock_b)
		used_b = 0
	}
}

int procedure2(int arg; int used_b) {
	/* modified from void to int, and returns a value to know if b was
	locked so that the other program only gets lock_b if needed. */
	pthread_mutex_lock(&lock_b);
	b = arg;
	pthread_mutex_unlock(&lock_b);
	used_b = 1
	return used_b 
}

