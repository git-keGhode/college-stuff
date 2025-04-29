

## Practical - 1  :  Linear Search 

#### Code :

```cpp
#include <iostream>

using namespace std;

int main() {
    int a[15] = {1, 2, 3, 4, 5, 6, 77,7, 8, 9, 10}, val, flag = 0;
    cout << "Enter a value you want to search: ";
    cin >> val;
    for (int i = 0; i < 10; i++) {
        if (a[i] == val) {
            cout << "Value is at position " << i + 1; 
            flag = 1;
            break;
        }
    }
    if (flag == 0) {
        cout << "Value is not found.";
    }
    return 0;
}
```
#### Output :
![[Pasted image 20250327224029.png]]

## Practical - 2 : Matrix Multiplication

#### Code:

```cpp
#include <iostream>

using namespace std;

int main() {
    // Define 2x2 matrices
    int matrix1[2][2] = {{1, 2}, {3, 4}};
    int matrix2[2][2] = {{1, 2}, {3, 4}};
    int resmatrix[2][2] = {{0, 0}, {0, 0}};

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                resmatrix[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
    cout << "Result of matrix multiplication: " << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << resmatrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
```

#### Output :

![[Pasted image 20250327224704.png]]


## Practical- 3: Write the logic for following 

1. From decimal to octal
2. Binary to Octal 
3. Decimal to Hexadecimal 
4. Hexadecimal to Octal 
5. Binary to Decimal

## Code :
```cpp
#include <iostream>
#include <cmath>
#include <sstream>

using namespace std;

string decimalToOctal(int decimal) {
    string octal = "";
    while (decimal > 0) {
        octal = to_string(decimal % 8) + octal;
        decimal /= 8;
    }
    return (octal == "") ? "0" : octal;
}

int binaryToDecimal(string binary) {
    int decimal = 0;
    int power = 0;
    for (int i = binary.length() - 1; i >= 0; i--) {
        if (binary[i] == '1') {
            decimal += pow(2, power);
        }
        power++;
    }
    return decimal;

}

string binaryToOctal(string binary) {
    int decimal = binaryToDecimal(binary);
    return decimalToOctal(decimal);

}

string decimalToHexadecimal(int decimal) {
    string hex = "";
    string hexDigits = "0123456789ABCDEF";
    while (decimal > 0) {
        hex = hexDigits[decimal % 16] + hex;
        decimal /= 16;
    }
    return (hex == "") ? "0" : hex;
}

int hexadecimalToDecimal(string hex) {
    int decimal = 0;
    int power = 0;

    for (int i = hex.length() - 1; i >= 0; i--) {
        if (hex[i] >= '0' && hex[i] <= '9') {
            decimal += (hex[i] - '0') * pow(16, power);
        } else if (hex[i] >= 'A' && hex[i] <= 'F') {
            decimal += (hex[i] - 'A' + 10) * pow(16, power);
        }
        power++;
    }
    return decimal;
}

string hexadecimalToOctal(string hex) {
    int decimal = hexadecimalToDecimal(hex);
    return decimalToOctal(decimal);

}

int main() {

    int decimal;
    string binary, hex;
    cout << "Enter Decimal number: ";
    cin >> decimal;
    cout << "Decimal to Octal: " << decimalToOctal(decimal) << endl;
    cout << "Enter Binary number: ";
    cin >> binary;
    cout << "Binary to Octal: " << binaryToOctal(binary) << endl;
    cout << "Enter Decimal number: ";
    cin >> decimal;
    cout << "Decimal to Hexadecimal: " << decimalToHexadecimal(decimal) <<endl;
    cout << "Enter Hexadecimal number: ";
    cin >> hex;
    cout << "Hexadecimal to Octal: " << hexadecimalToOctal(hex) << endl;
    cout << "Enter Binary number: ";
    cin >> binary;
    cout << "Binary to Decimal: " << binaryToDecimal(binary) << endl;
    return 0;

}
```

## Output :
![[Pasted image 20250327225207.png]]


## Practical 4 : Inverse Of Matrix (2 * 2) 

#### Code :
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

void inverseMatrix(float matrix[2][2]) {

    float determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] *      matrix[1][0]);

    if (determinant == 0) {
        cout << "Inverse does not exist (Determinant is zero)." << endl;
        return;
    }
    float inverse[2][2];
    inverse[0][0] = matrix[1][1] / determinant;
    inverse[0][1] = -matrix[0][1] / determinant;
    inverse[1][0] = -matrix[1][0] / determinant;
    inverse[1][1] = matrix[0][0] / determinant;
    cout << "Inverse of the matrix:" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << fixed << setprecision(2) << inverse[i][j] << " ";
        }
        cout << endl;
    }
}
int main() {
    float matrix[2][2];
    cout << "Enter elements of 2x2 matrix:" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> matrix[i][j];
        }
    }
    inverseMatrix(matrix);
    return 0;
}
```


#### Output :
![[Pasted image 20250327230322.png]]




## Practical – 5 : Caesar Cipher 

#### Code :
```cpp
#include <iostream>

using namespace std;

string caesarCipher(string text, int shift) {
    for (char &c : text)
        if (isalpha(c))
            c = (c - (isupper(c) ? 'A' : 'a') + shift) % 26 + (isupper(c) ? 'A' : 'a');
    return text;
}

int main() {
    string message = "HELLO";
    int shift = 3;
    string encrypted = caesarCipher(message, shift);
    string decrypted = caesarCipher(encrypted, 26 - shift);
    cout << "Original: " <<endl << message <<endl<< "\nEncrypted: " <<endl << encrypted <<endl << "\nDecrypted: "<<endl << decrypted;
}
```


#### Output :
![[Pasted image 20250327231051.png]]




## Practical-6: Row Transposition Cipher 

#### Code : 
```cpp

```


#### Output :
![[Pasted image 20250327231730.png]]





## Practical-7: Rail fence Cipher :

#### Code :
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class RailFenceCipher {
public:
    static string encrypt(const string& text, int rails) {
        if (rails < 2) 
        return text;
        vector<string> railLines(rails);
        int rail = 0;
        bool goingDown = false;
        
        for (char c : text) {
            railLines[rail] += c;
            if (rail == 0 || rail == rails - 1) goingDown = !goingDown;
            rail += goingDown ? 1 : -1;
        }
        string encrypted;
        for (const auto& row : railLines) encrypted += row;
        return encrypted;
    }
    static string decrypt(const string& encrypted, int rails) {
    
        if (rails < 2) return encrypted;
        vector<string> railLines(rails, string(encrypted.length(), '\0'));
        int rail = 0;
        bool goingDown = false;

        for (size_t i = 0; i < encrypted.length(); i++) {
            railLines[rail][i] = '*';
            if (rail == 0 || rail == rails - 1) goingDown = !goingDown;
            rail += goingDown ? 1 : -1;
        }

        size_t index = 0;
        for (auto& row : railLines)
            for (char& c : row)
                if (c == '*') c = encrypted[index++];
        
        string decrypted;
        rail = 0;
        goingDown = false;

        for (size_t i = 0; i < encrypted.length(); i++) {
            decrypted += railLines[rail][i];
            if (rail == 0 || rail == rails - 1) goingDown = !goingDown;
            rail += goingDown ? 1 : -1;
        }
        return decrypted;
    }
};
int main() {
    string message = "HELLO WORLD";
    int rails = 3;
    string encrypted = RailFenceCipher::encrypt(message, rails);
    string decrypted = RailFenceCipher::decrypt(encrypted, rails);
    cout << "Original: " << message << "\nEncrypted: " << encrypted << "\nDecrypted: " << decrypted << endl;
    return 0;
}
```


#### Output :

![[Pasted image 20250327233021.png]]



## Practical-8: Hill Cipher 2 * 2  :

#### Code :

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class HillCipher {
private:
    int key[2][2];

    int modInverse(int det) {
        det %= 26;
        for (int i = 1; i < 26; i++)
            if ((det * i) % 26 == 1) return i;
        return -1; 
    }

    void computeInverseKey(int invKey[2][2]) {
        int det = key[0][0] * key[1][1] - key[0][1] * key[1][0];
        det = (det % 26 + 26) % 26; 

        int detInv = modInverse(det);
        if (detInv == -1) {
            cout << "Invalid key! No modular inverse exists.\n";
            exit(1);
        }

        invKey[0][0] = ( key[1][1] * detInv) % 26;
        invKey[0][1] = (-key[0][1] * detInv) % 26;
        invKey[1][0] = (-key[1][0] * detInv) % 26;
        invKey[1][1] = ( key[0][0] * detInv) % 26;

        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                if (invKey[i][j] < 0) invKey[i][j] += 26;
    }

    string processText(const string& text, int matrix[2][2]) {
        string result;
        string processedText = text;
        if (processedText.length() % 2 != 0) processedText += 'X'; // Pad 

        for (size_t i = 0; i < processedText.length(); i += 2) {
            int a = processedText[i] - 'A';
            int b = processedText[i + 1] - 'A';

            int c1 = (matrix[0][0] * a + matrix[0][1] * b) % 26;
            int c2 = (matrix[1][0] * a + matrix[1][1] * b) % 26;

            result += char(c1 + 'A');
            result += char(c2 + 'A');
        }
        return result;
    }

public:
    HillCipher(int k[2][2]) {
        key[0][0] = k[0][0]; key[0][1] = k[0][1];
        key[1][0] = k[1][0]; key[1][1] = k[1][1];
    }

    string encrypt(const string& text) {
        return processText(text, key);
    }

    string decrypt(const string& encrypted) {
        int invKey[2][2];
        computeInverseKey(invKey);
        return processText(encrypted, invKey);
    }
};

int main() {
    int keyMatrix[2][2];
    string message;

    // Input the 2x2 key matrix
    cout << "Enter 2x2 key matrix:" << endl;
    cout << "Enter first row (two integers): ";
    cin >> keyMatrix[0][0] >> keyMatrix[0][1];
    cout << "Enter second row (two integers): ";
    cin >> keyMatrix[1][0] >> keyMatrix[1][1];

    HillCipher cipher(keyMatrix);

    // Input the message to be encrypted
    cout << "Enter message (only uppercase letters): ";
    cin >> message;

    // Encrypt the message
    string encrypted = cipher.encrypt(message);
    // Decrypt the message
    string decrypted = cipher.decrypt(encrypted);

    // Output the results
    cout << "Original:   " << message << endl;
    cout << "Encrypted:  " << encrypted << endl;
    cout << "Decrypted:  " << decrypted << endl;

    return 0;
}


```




#### Output :

![[Pasted image 20250327234450.png]]




## Practical-9: Vernam Cipher

#### Code :
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    string message;
    string key;
    
    
    cout << "Enter Message: ";
    getline(cin, message);
    
    cout << "Enter Key: ";
    getline(cin, key);
    
    
    while (key.length() < message.length()) {
        key += key;
    }
    key = key.substr(0, message.length());
    
    
    string encrypted = message;
    string decrypted = message;
    
    
    for (size_t i = 0; i < message.size(); i++) {
        if (isalpha(message[i])) {
            if (isupper(message[i])) {
                
                encrypted[i] = ((message[i] - 'A') ^ (key[i] % 26)) + 'A';
            } else if (islower(message[i])) {
                
                encrypted[i] = ((message[i] - 'a') ^ (key[i] % 26)) + 'a';
            }
        }
        
    }
    
   
    for (size_t i = 0; i < encrypted.size(); i++) {
        if (isalpha(encrypted[i])) {
            if (isupper(encrypted[i])) {
                decrypted[i] = ((encrypted[i] - 'A') ^ (key[i] % 26)) + 'A';
            } else if (islower(encrypted[i])) {
                decrypted[i] = ((encrypted[i] - 'a') ^ (key[i] % 26)) + 'a';
            }
        }
       
    }
    
    cout << "Original:   " << message << "\n";
    cout << "Key:        " << key << "\n";
    cout << "Encrypted:  " << encrypted << "\n";
    cout << "Decrypted:  " << decrypted << "\n";
    
    return 0;
}
---------------------------------------------------------------------------------
#include <iostream>
#include <string>

using namespace std;


const string base64_chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

string base64Encode(const string& input) {
    string output;
    int val = 0, valb = -6;
    for (size_t i = 0; i < input.length(); i++) {
        unsigned char c = input[i];
        val = (val << 8) + c;
        valb += 8;
        while (valb >= 0) {
            output.push_back(base64_chars[(val >> valb) & 0x3F]);
            valb -= 6;
        }
    }
    if (valb > -6)
        output.push_back(base64_chars[((val << 8) >> (valb + 8)) & 0x3F]);
    while (output.size() % 4)
        output.push_back('=');
    return output;
}


string vernamCipher(const string& text, int key) {
    string result = "";
    unsigned char byteKey = key % 256;  // Ensure key is in byte range
    for (size_t i = 0; i < text.length(); i++) {
        result += text[i] ^ byteKey;  
    }
    return result;
}


string vernamCipher(const string& text, const string& key) {
    string result = "";
    if (key.empty()) return text;  // Handle empty key case
    
    for (size_t i = 0; i < text.length(); i++) {
        result += text[i] ^ key[i % key.length()]; 
    }
    return result;
}

int main() {
    string message;
    int choice;

    cout << "Enter the message: ";
    getline(cin, message);

    cout << "Choose key type:\n";
    cout << "1. String key (e.g., MyKey123)\n";
    cout << "2. Numeric key (e.g., 2000)\n";
    cout << "Enter choice (1 or 2): ";
    cin >> choice;
    cin.ignore();  

    string encrypted;

    if (choice == 1) {
        string strKey;
        cout << "Enter string key: ";
        getline(cin, strKey);
        
        encrypted = vernamCipher(message, strKey);
       
        string decrypted = vernamCipher(encrypted, strKey);
        
        cout << "\nOriginal: " << message
             << "\nCipher Text (Base64): " << base64Encode(encrypted)
             << "\nDecrypted: " << decrypted << endl;
    } 
    else if (choice == 2) {
        int numKey;
        cout << "Enter numeric key: ";
        cin >> numKey;
        
        encrypted = vernamCipher(message, numKey);
      
        string decrypted = vernamCipher(encrypted, numKey);
        
        cout << "\nOriginal: " << message
             << "\nCipher Text (Base64): " << base64Encode(encrypted)
             << "\nDecrypted: " << decrypted << endl;
    } 
    else {
        cout << "Invalid choice!" << endl;
        return 1;
    }

    return 0;
}

```

#### Output ;
![[Pasted image 20250327235105.png]]




## Practical-10: Polyalphabetic Cipher

#### Code :

```cpp
#include <iostream>

using namespace std;

string extendKey(const string& message, const string& key) {
    string newKey = key;
    while (newKey.length() < message.length()) {
        newKey += key;  
    }
    return newKey.substr(0, message.length());  
}

string encrypt(const string& message, const string& key) {
    string encrypted = message;
    string extendedKey = extendKey(message, key);

    for (size_t i = 0; i < message.size(); i++) {
        if (isalpha(message[i])) {
            char base = isupper(message[i]) ? 'A' : 'a';
            encrypted[i] = ((message[i] - base + (extendedKey[i] - base)) % 26) + base;
        }
    }
    return encrypted;
}

string decrypt(const string& encrypted, const string& key) {
    string decrypted = encrypted;
    string extendedKey = extendKey(encrypted, key);

    for (size_t i = 0; i < encrypted.size(); i++) {
        if (isalpha(encrypted[i])) {
            char base = isupper(encrypted[i]) ? 'A' : 'a';
            decrypted[i] = ((encrypted[i] - base - (extendedKey[i] - base) + 26) % 26) + base;
        }
    }
    return decrypted;
}

int main() {
    string message = "HELLO WORLD";
    string key = "KEY";  

    string encrypted = encrypt(message, key);
    string decrypted = decrypt(encrypted, key);

    cout << "Original:   " << message << "\n";
    cout << "Key:        " << key << "\n";
    cout << "Encrypted:  " << encrypted << "\n";
    cout << "Decrypted:  " << decrypted << "\n";
    return 0;
}

```

#### Output :

![[Pasted image 20250328000242.png]]

## Practical-11: Mono-alphabetic Cipher :

#### Code :

```cpp
#include <iostream>
using namespace std;

string monoalphabeticEncrypt(string text, string key) {
    string encryptedText = "";
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (char c : text) {
        if (isalpha(c)) {
            char upperChar = toupper(c);
            int index = alphabet.find(upperChar);
            encryptedText += key[index];
        } else {
            encryptedText += c;
        }
    }
    return encryptedText;
}

string monoalphabeticDecrypt(string text, string key) {
    string decryptedText = "";
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (char c : text) {
        if (isalpha(c)) {
            int index = key.find(c);
            decryptedText += alphabet[index];
        } else {
            decryptedText += c;
        }
    }
    return decryptedText;
}

int main() {
    string text, key;

    cout << "Enter plaintext (UPPERCASE only): ";
    cin >> text;

    cout << "Enter 26-letter substitution key: ";
    cin >> key;

    string encrypted = monoalphabeticEncrypt(text, key);
    cout << "Encrypted: " << encrypted << endl;
    
    string decrypted = monoalphabeticDecrypt(encrypted, key);
    cout << "Decrypted: " << decrypted << endl;
    return 0;
}

```

#### Output :

![[Pasted image 20250328001017.png]]




| Cipher                    | Type                           | Key          | Strength         | Security                                   | Notes                               |
| ------------------------- | ------------------------------ | ------------ | ---------------- | ------------------------------------------ | ----------------------------------- |
| **Caesar Cipher**         | Substitution                   | Shift value  | Weak             | Easily broken (brute-force)                | Simple, fast, but insecure          |
| **Vernam Cipher**         | Stream Cipher                  | Random key   | Perfect secrecy  | Unbreakable if key is random & used once   | Requires secure key management      |
| **Playfair Cipher**       | Substitution (Bigram)          | Matrix key   | Moderate         | Vulnerable to frequency analysis           | Uses digraphs for added complexity  |
| **Transposition Cipher**  | Transposition                  | Permutation  | Moderate to Weak | Vulnerable to pattern recognition          | Rearranges letters                  |
| **Substitution Cipher**   | Substitution                   | Alphabet key | Moderate         | Vulnerable to frequency analysis           | Replaces letters randomly           |
| **Polyalphabetic Cipher** | Substitution (multiple shifts) | Keyword      | Strong           | Vulnerable to cryptanalysis with short key | Multiple shifts for security        |
| **Hill Cipher**           | Polygraphic (Matrix)           | Matrix key   | Strong           | Vulnerable to known-plaintext attacks      | Uses matrix multiplication          |
| **Rail Fence Cipher**     | Transposition                  | Rail count   | Very weak        | Easily broken with simple techniques       | Simple transposition, poor security |