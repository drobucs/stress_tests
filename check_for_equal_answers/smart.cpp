#include <cstdio>
#include <cstring>

const int BUFF_SIZE = 4097;

void calculateKMP(int *pi, const char *string, size_t sizeString) {
    pi[0] = 0;
    for (size_t i = 1; i < sizeString; ++i) {
        int j = pi[i - 1];
        while (j > 0 && string[i] != string[j]) {
            j = pi[j - 1];
        }
        if (string[i] == string[j]) {
            j++;
        }
        pi[i] = j;
    }
}

bool checkKMP(const int *pi, int &prefPi, const char *string, size_t sizeString, const char *buff, size_t buffLength) {
    for (size_t i = 0; i < buffLength; ++i) {
        int curPi = prefPi;
        while (curPi > 0 && string[curPi] != buff[i]) {
            curPi = pi[curPi - 1];
        }
        if (string[curPi] == buff[i]) {
            curPi++;
        }
        prefPi = curPi;
        if (prefPi == sizeString) {
            return true;
        }
    }
    return false;
}

int main(int argc, char **argv) {

    if (argc != 3) {
        fprintf(stderr, "invalid number of arguments:\n\trequired: 2\n\tactually: %d\n", argc - 1);
        return -1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == nullptr) {
        perror("Error occurred ");
        return -1;
    }

    char buff[BUFF_SIZE];
    buff[BUFF_SIZE - 1] = '\0';

    size_t sizeString = strlen(argv[2]);

    char *string = new char[sizeString + 1];
    string[sizeString] = '\0';

    for (size_t i = 0; i < sizeString; ++i) {
        string[i] = argv[2][i];
    }

    int *pi = new int[sizeString];

    calculateKMP(pi, string, sizeString);

    size_t buffLength = fread(buff, 1, BUFF_SIZE - 1, file);

    int prefPi = 0;
    bool existString = false;
    while (buffLength != 0) {
        existString = checkKMP(pi, prefPi, string, sizeString, buff, buffLength);
        if (existString) {
            break;
        }
        buffLength = fread(buff, 1, BUFF_SIZE - 1, file);
        if (ferror(file) != 0) {
            fprintf(stderr, "Error occurred: error while reading file");
            return -1;
        }
    }

    if (existString) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    delete[] pi;
    delete[] string;
    fclose(file);
    return 0;
}
