#include <iostream>
#include <string.h>


// This was a challenge that my friend completed at some point. I decided to remake it because I was bored.
bool isPalindrome(std::string text);


int main() 
{
    std::cout << isPalindrome("me");

    return 0;
}


bool isPalindrome(std::string text)
{
    std::string reversed_text;

    for(int i = text.size() - 1; i >= 0; i--) 
    {
        reversed_text += text[i];
    }

    if(reversed_text == text) 
    {
        return true;
    } else 
    {
        return false;
    }
}
