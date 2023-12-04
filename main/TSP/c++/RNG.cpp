#include <iostream>
#include <process.h>
#include <math.h>
#include <ctime>
#include <algorithm>

int dist[100][100], c[100], n;

void world_tour() {
    for (int i = 0; i < 100; i++) {
        c[i] = i;
    }
}

class RNG {
    char asking;
    int x0, a = 48271, c = 0;
    long m = pow(2, 31) - 1;
    int x_prev = (a * Seed() + c) % m;

public:
    int Seed() {
        std::cout << "Input your seed? (y/n)";
        std::cin >> asking;
        if (asking == 'y' or asking == 'Y') {
            std::cout << "Seed: ";
            std::cin >> x0;
        }
        else {
            x0 = _getpid() + time(NULL);
            if (asking == 'n' or asking == 'N') {
                std::cout << "Well, you choose randomized then\n";
            }
            else {
                std::cout << "GO TO HELL!!!\n";
            }
            return x0;
        };
    };

    int PRNG() {
        x_prev = (a * x_prev + c) % m;
        return x_prev;
    };

    int RNG_inrange(int min, int max) {
        int values = (PRNG() / (pow(2, 31) - 2)) * (max - min) + min;
        if (values > min) { return values; }
        else { return -1 * values; }
    };

    void distance(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) { dist[i][j] = RNG_inrange(1, 100); }
        }
    }
};

void cities_dist() {
    std::cout << "Distance of cities:\n";
    for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) { std::cout << "(" << i << "," << j << "): " << dist[i][j] << "\t"; }
            std::cout << "\n";
        }
}

void tsp() {
    int s, min = 0, cities[100];
    std::copy(c, c + n, cities);
    do {
        s = 0;
        if (c[0] == 0) {
            for (int i = 1; i < n; i++) { s += dist[c[i - 1]][c[i]]; }
        };
        if (min < s or min == 0) {
            min = s;
            std::copy(c, c + n, cities);
        }
    } while (std::next_permutation(c, c + n));
    std::cout << "Shortest way to go is: ";
    for (int i = 0; i < n; i++) {
        std::cout << cities[i];
        if (i < n - 1) { std::cout << "->"; }
    }
    std::cout << " with the distance of " << min;
}

int main() {
    world_tour();
    std::cout << "Number of cities: "; std::cin >> n;
    RNG RNG;
    RNG.distance(n);
    cities_dist();
    tsp();
    
    return 0;
}