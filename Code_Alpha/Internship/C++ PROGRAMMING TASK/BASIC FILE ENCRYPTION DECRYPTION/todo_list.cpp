#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Function to encrypt the text using Caesar Cipher
void encryptFile(const string& inputFile, const string& outputFile, int key) {
    ifstream inFile(inputFile);
    ofstream outFile(outputFile);
    
    if (!inFile) {
        cerr << "Error opening input file!" << endl;
        return;
    }
    if (!outFile) {
        cerr << "Error opening output file!" << endl;
        return;
    }
    
    char ch;
    while (inFile.get(ch)) {
        if (isalpha(ch)) {  // Encrypt only alphabetic characters
            char offset = isupper(ch) ? 'A' : 'a';
            ch = (ch - offset + key) % 26 + offset;
        }
        outFile.put(ch);
    }

    cout << "Encryption successful!" << endl;
}

// Function to decrypt the text using Caesar Cipher
void decryptFile(const string& inputFile, const string& outputFile, int key) {
    ifstream inFile(inputFile);
    ofstream outFile(outputFile);
    
    if (!inFile) {
        cerr << "Error opening input file!" << endl;
        return;
    }
    if (!outFile) {
        cerr << "Error opening output file!" << endl;
        return;
    }

    char ch;
    while (inFile.get(ch)) {
        if (isalpha(ch)) {  // Decrypt only alphabetic characters
            char offset = isupper(ch) ? 'A' : 'a';
            ch = (ch - offset - key + 26) % 26 + offset;
        }
        outFile.put(ch);
    }

    cout << "Decryption successful!" << endl;
}

int main() {
    string inputFile, outputFile;
    int key;
    int choice;

    cout << "Enter the input file name: ";
    cin >> inputFile;
    cout << "Enter the output file name: ";
    cin >> outputFile;
    cout << "Enter the key (shift value): ";
    cin >> key;

    cout << "Choose operation: \n1. Encrypt\n2. Decrypt\nEnter choice: ";
    cin >> choice;

    if (choice == 1) {
        encryptFile(inputFile, outputFile, key);
    } else if (choice == 2) {
        decryptFile(inputFile, outputFile, key);
    } else {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}
